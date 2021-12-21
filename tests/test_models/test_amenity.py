#!/usr/bin/python3
"""
Unittest class for models/city.py
"""
from models.amenity import Amenity
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestAmenity(unittest.TestCase):
    """unittest for Amenity class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(Amenity().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_if_name_is_public(self):
        """test that if name is public string"""
        self.assertEqual(str, type(Amenity().name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", Amenity().__dict__)

    def test_with_two_unique_users_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_with_different_created_at(self):
        am1 = Amenity()
        sleep(0.5)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_with_different_updated_at(self):
        am1 = Amenity()
        sleep(0.5)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_repr(self):
        am = Amenity()
        am.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        am.created_at = am.updated_at = date
        am_str = am.__str__()
        self.assertIn("[Amenity] (123456)", am_str)
        self.assertIn("'id': '123456'", am_str)
        self.assertIn("'created_at': " + date_repr, am_str)
        self.assertIn("'updated_at': " + date_repr, am_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, Amenity(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        am = Amenity(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(am.id, "123")
        self.assertEqual(am.created_at, date)
        self.assertEqual(am.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class TestAmenitySave(unittest.TestCase):
    """Testing save method in the City class"""

    @classmethod
    def SetUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def RenameRemove(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.5)
        up_at = am.updated_at
        am.save()
        self.assertLess(up_at, am.updated_at)

    def test_two_save(self):
        am = Amenity()
        sleep(0.5)
        up_at1 = am.updated_at
        am.save()
        self.assertLess(up_at1, am.updated_at)
        up_at2 = am.updated_at
        sleep(0.5)
        am.save()
        self.assertLess(up_at2, am.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            Amenity().save(None)

    def test_save_if_updates(self):
        am = Amenity()
        am.save()
        am_id = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(am_id, f.read())

class TestAmenityDict(unittest.TestCase):
    """unittest for testing to_dict mothod of City class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_dict_with_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_dict_with_added_attr(self):
        am = Amenity()
        am.middle_name = "ALX"
        am.my_number = 88
        self.assertEqual("ALX", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_if_datetime_attr(self):
        am_dict = Amenity().to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(Amenity().to_dict(), Amenity().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            Amenity().to_dict(None)

if __name__ == '__main__':
    unittest.main()

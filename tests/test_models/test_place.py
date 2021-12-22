#!/usr/bin/python3
"""
Unittest class for models/city.py
"""
from models.place import Place
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestPlace(unittest.TestCase):
    """unittest for City class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(Place, type(Place()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(Place(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(Place().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_if_city_id_is_public(self):
        """tests that if city_id is public string"""
        pl = Place()
        self.assertEqual(str, type(Place().city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_if_user_id_is_public(self):
        """test that if name is public string"""
        pl = Place()
        self.assertEqual(str, type(Place().user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_if_name_is_public(self):
        pl = Place()
        self.assertEqual(str, type(pl.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_if_description_is_public(self):
        pl = Place()
        self.assertEqual(str, type(pl.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("description", pl.__dict__)

    def test_if_number_room_is_public(self):
        pl = Place()
        self.assertEqual(int, type(pl.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_if_number_bathrooms_is_public(self):
        pl = Place()
        self.assertEqual(int, type(pl.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_if_max_guest_is_public(self):
        pl = Place()
        self.assertEqual(int, type(pl.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_if_price_by_night_is_public(self):
        pl = Place()
        self.assertEqual(int, type(pl.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_if_latitude_is_public(self):
        pl = Place()
        self.assertEqual(float, type(pl.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_if_longitude_is_public(self):
        pl = Place()
        self.assertEqual(float, type(pl.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_if_amenity_ids_is_public(self):
        pl = Place()
        self.assertEqual(list, type(pl.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_with_two_unique_users_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_with_different_created_at(self):
        pl1 = Place()
        sleep(0.5)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_with_different_updated_at(self):
        pl1 = Place()
        sleep(0.5)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_repr(self):
        pl = Place()
        pl.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        pl.created_at = pl.updated_at = date
        pl_str = pl.__str__()
        self.assertIn("[Place] (123456)", pl_str)
        self.assertIn("'id': '123456'", pl_str)
        self.assertIn("'created_at': " + date_repr, pl_str)
        self.assertIn("'updated_at': " + date_repr, pl_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, Place(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        pl = Place(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(pl.id, "123")
        self.assertEqual(pl.created_at, date)
        self.assertEqual(pl.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

class TestPlaceSave(unittest.TestCase):
    """Testing save method in the Place class"""

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
        pl = Place()
        sleep(0.5)
        up_at = pl.updated_at
        pl.save()
        self.assertLess(up_at, pl.updated_at)

    def test_two_save(self):
        pl = Place()
        sleep(0.5)
        up_at1 = pl.updated_at
        pl.save()
        self.assertLess(up_at1, pl.updated_at)
        up_at2 = pl.updated_at
        sleep(0.5)
        pl.save()
        self.assertLess(up_at2, pl.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            Place().save(None)

    def test_save_if_updates(self):
        pl = Place()
        pl.save()
        pl_id = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(pl_id, f.read())

class TestPlaceDict(unittest.TestCase):
    """unittest for testing to_dict mothod of Place class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_dict_with_correct_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_dict_with_added_attr(self):
        pl = Place()
        pl.middle_name = "ALX"
        pl.my_number = 88
        self.assertEqual("ALX", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_if_datetime_attr(self):
        pl_dict = Place().to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(Place().to_dict(), Place().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            Place().to_dict(None)

if __name__ == '__main__':
    unittest.main()

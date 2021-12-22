#!/usr/bin/python3
"""
Unittest class for models/city.py
"""
from models.city import City
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestCity(unittest.TestCase):
    """unittest for City class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(City, type(City()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(City(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(City().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(City().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_if_state_id_is_public(self):
        """tests that if state_id is public string"""
        city = City()
        self.assertEqual(str, type(City().state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_if_name_is_public(self):
        """test that if name is public string"""
        city = City()
        self.assertEqual(str, type(city.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_with_two_unique_users_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_with_different_created_at(self):
        city1 = City()
        sleep(0.5)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_with_different_updated_at(self):
        city1 = City()
        sleep(0.5)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_repr(self):
        city = City()
        city.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        city.created_at = city.updated_at = date
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + date_repr, city_str)
        self.assertIn("'updated_at': " + date_repr, city_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, City(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        city = City(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city.id, "123")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

class TestCitySave(unittest.TestCase):
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
        city = City()
        sleep(0.5)
        up_at = city.updated_at
        city.save()
        self.assertLess(up_at, city.updated_at)

    def test_two_save(self):
        city = City()
        sleep(0.5)
        up_at1 = city.updated_at
        city.save()
        self.assertLess(up_at1, city.updated_at)
        up_at2 = city.updated_at
        sleep(0.5)
        city.save()
        self.assertLess(up_at2, city.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            City().save(None)

    def test_save_if_updates(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())

class TestCityDict(unittest.TestCase):
    """unittest for testing to_dict mothod of City class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_with_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_dict_with_added_attr(self):
        city = City()
        city.middle_name = "ALX"
        city.my_number = 88
        self.assertEqual("ALX", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_if_datetime_attr(self):
        city_dict = City().to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(City().to_dict(), City().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            City().to_dict(None)

if __name__ == '__main__':
    unittest.main()

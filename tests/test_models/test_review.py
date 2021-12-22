#!/usr/bin/python3
"""
Unittest class for models/city.py
"""
from models.review import Review
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestReview(unittest.TestCase):
    """unittest for Review class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(Review, type(Review()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(Review(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(Review().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_if_place_id_is_public(self):
        """tests that if place_id is public string"""
        rv = Review()
        self.assertEqual(str, type(rv.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_if_user_id_is_public(self):
        """test that if user_id is public string"""
        rv = Review()
        self.assertEqual(str, type(rv.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_if_text_is_public(self):
        rv = Review()
        self.assertEqual(str, type(rv.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_with_two_unique_users_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_with_different_created_at(self):
        rv1 = Review()
        sleep(0.5)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_with_different_updated_at(self):
        rv1 = Review()
        sleep(0.5)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_repr(self):
        rv = Review()
        rv.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        rv.created_at = rv.updated_at = date
        rv_str = rv.__str__()
        self.assertIn("[Review] (123456)", rv_str)
        self.assertIn("'id': '123456'", rv_str)
        self.assertIn("'created_at': " + date_repr, rv_str)
        self.assertIn("'updated_at': " + date_repr, rv_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, Review(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        rv = Review(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(rv.id, "123")
        self.assertEqual(rv.created_at, date)
        self.assertEqual(rv.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

class TestReviewSave(unittest.TestCase):
    """Testing save method in the Review class"""

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
        rv = Review()
        sleep(0.5)
        up_at = rv.updated_at
        rv.save()
        self.assertLess(up_at, rv.updated_at)

    def test_two_save(self):
        rv = Review()
        sleep(0.5)
        up_at1 = rv.updated_at
        rv.save()
        self.assertLess(up_at1, rv.updated_at)
        up_at2 = rv.updated_at
        sleep(0.5)
        rv.save()
        self.assertLess(up_at2, rv.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            Review().save(None)

    def test_save_if_updates(self):
        rv = Review()
        rv.save()
        rv_id = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rv_id, f.read())

class TestReviewDict(unittest.TestCase):
    """unittest for testing to_dict mothod of Review class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_dict_with_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_dict_with_added_attr(self):
        rv = Review()
        rv.middle_name = "ALX"
        rv.my_number = 88
        self.assertEqual("ALX", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_if_datetime_attr(self):
        rv_dict = Review().to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(Review().to_dict(), Review().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            Review().to_dict(None)

if __name__ == '__main__':
    unittest.main()

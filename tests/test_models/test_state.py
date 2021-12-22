#!/usr/bin/python3
"""
Unittest class for models/state.py
"""
from models.state import State
import unittest
from datetime import datetime
from time import sleep
import os
import models


class TestUser(unittest.TestCase):
    """unittest for State class instantiation"""

    def test_with_no_args_instatiates(self):
        """tests with no argument"""
        self.assertEqual(State, type(State()))

    def test_with_new_stored_instances(self):
        """tests with new stored instances"""
        self.assertIn(State(), models.storage.all().values())

    def test_if_id_is_public(self):
        """tests that if id is public string"""
        self.assertEqual(str, type(State().id))

    def test_if_created_at_is_public(self):
        """tests that if created_at is public datetime"""
        self.assertEqual(datetime, type(State().created_at))

    def test_if_updated_at_is_public(self):
        """tests that if updated_at is public datetime"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_if_name_is_public(self):
        """tests that if email is public string"""
        state = State()
        self.assertEqual(str, type(state.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_with_two_unique_users_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_with_different_created_at(self):
        state1 = State()
        sleep(0.5)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_with_different_updated_at(self):
        state1 = State()
        sleep(0.5)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_repr(self):
        state = State()
        state.id = "123456"
        date = datetime.today()
        date_repr = repr(date)
        state.created_at = state.updated_at = date
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + date_repr, state_str)
        self.assertIn("'updated_at': " + date_repr, state_str)

    def test_with_unsed_args(self):
        self.assertNotIn(None, State(None).__dict__.values())

    def test_with_kwargs_instatiation(self):
        date = datetime.today()
        date_iso = date.isoformat()
        state = State(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

class TestStateSave(unittest.TestCase):
    """Testing save method in the State class"""

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
        state = State()
        sleep(0.5)
        up_at = state.updated_at
        state.save()
        self.assertLess(up_at, state.updated_at)

    def test_two_save(self):
        state = State()
        sleep(0.5)
        up_at1 = state.updated_at
        state.save()
        self.assertLess(up_at1, state.updated_at)
        up_at2 = state.updated_at
        sleep(0.5)
        state.save()
        self.assertLess(up_at2, state.updated_at)

    def test_with_none_arg(self):
        with self.assertRaises(TypeError):
            State().save(None)

    def test_save_if_updates(self):
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())

class TestStateDict(unittest.TestCase):
    """unittest for testing to_dict mothod of User class"""

    def test_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_dict_with_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_dict_with_added_attr(self):
        state = State()
        state.middle_name = "ALX"
        state.my_number = 88
        self.assertEqual("ALX", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_if_datetime_attr(self):
        state_dict = State().to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = date
        dict_t = {
            'id': '123456',
            '__class__': 'State',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), dict_t)

    def test_with_dict(self):
        self.assertNotEqual(State().to_dict(), State().__dict__)

    def test_with_none_args(self):
        with self.assertRaises(TypeError):
            State().to_dict(None)

if __name__ == '__main__':
    unittest.main()

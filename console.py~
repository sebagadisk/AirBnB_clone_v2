#!/usr/bin/python3

"""
This module implements the HBnB console
"""

import cmd
from typing import final
from models import storage
from models.base_model import BaseModel

from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    This implements the HBnB console

    Args:
        classnames: this contains all classes
        dict_cache: this caches the kwarg passed in shell
    """

    classnames = [
        'BaseModel',
        'User',
        'Amenity',
        'Place',
        'Review',
        'State',
        'City'
    ]

    dict_cache = None

    prompt = "(hbnb) "

    def emptyline(self):
        """
        This does nothing on empty line
        """
        pass

    def do_count(self, args):
        """This counts the number of class instance indicated
        or all the instances saved
        """
        count = 0
        parsed_args = args.split()
        cache_store = storage.all()
        if len(parsed_args) > 0:
            for i in cache_store.values():
                    if i.__class__.__name__ == parsed_args[0]:
                        count += 1
        else:
            count = len(cache_store)
        print(count)

    def extract_dict(self, args):
        """
        This function caches the kwargs passed in
        <class_name>.update(id, kwarg)
        """
        self.dict_cache = None
        firstval = args.split('{')
        if len(firstval) == 2:
            secondval = firstval[1].split('}')
            if len(secondval) == 2:
                finalval = '{' + secondval[0] + '}'
                self.dict_cache = finalval
                args = args.replace(finalval, '', 1)
        return args

    def default(self, line):
        """
        This implements unknown commands
        """
        cmd_pair = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        ch = {'(': [' ', 1], ')': [' ', 1], ',': ['', 2]}
        test_for_func = self.extract_dict(line).split('.')
        if len(test_for_func) == 2:
            class_name = test_for_func[0]
            s_args = test_for_func[1]
            for i in ch:
                s_args = s_args.replace(i, ch[i][0], ch[i][1])
            finalargs = s_args.split()
            if len(finalargs) >= 0 and finalargs[0] in cmd_pair:
                cmdcache = finalargs[0]
                finalstr = ''
                finalstr += '{}'.format(class_name)
                dict_arr = []
                if self.dict_cache is not None:
                    dict_arr.append(class_name)
                for i in finalargs:
                    if self.dict_cache is not None:
                        if i != cmdcache:
                            i = i.replace('"', '', 2)
                            dict_arr.append(i)
                    else:
                        if i != cmdcache:
                            i = i.replace('"', '', 2)
                            finalstr += ' {}'.format(i)
                if self.dict_cache is not None:
                    dict_arr.append(self.dict_cache)
                    cmd_pair[cmdcache](dict_arr)
                else:
                    cmd_pair[cmdcache](finalstr)
        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_quit(self, args):
        """Quit command to exit program
        """
        return True

    def do_EOF(self):
        """ Executes EOF signal to quit program
        """
        print("")
        return True

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name.
        Usage: all Classname or all
        """
        filtered_obj = []
        all_instance = storage.all()
        parsed_args = args.split()
        if len(parsed_args) == 0:
            for i in all_instance.values():
                filtered_obj.append(i.__str__())
        elif len(parsed_args) == 1:
            if parsed_args[0] in self.classnames:
                for i in all_instance.values():
                    if i.__class__.__name__ == parsed_args[0]:
                        filtered_obj.append(i.__str__())
            else:
                print("** class doesn't exist **")
                return
        print(filtered_obj)

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on the class name and id
        Example : show classname id
        """
        parsedargs = args.split()
        all_instance = storage.all()
        class_name = ""
        arg_len = len(parsedargs)
        if arg_len > 1:
            if arg_len == 2:
                class_name, class_id = parsedargs
            else:
                class_name, class_id, *tmp = parsedargs
            id_formatted = '{}.{}'.format(class_name, class_id)
            if class_name in self.classnames:
                if id_formatted not in all_instance:
                    print("** no instance found **")
                else:
                    print(all_instance[id_formatted])
            elif class_name not in self.classnames:
                print("** class doesn't exist **")
        elif arg_len == 1 and parsedargs[0] not in self.classnames:
            print("** class doesn't exist **")
        elif arg_len == 1 and parsedargs[0] in self.classnames:
            print("** instance id missing **")
        if arg_len == 0:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
        and id (save the change into the JSON file)
        Usage : destroy classname id
        """
        parsedargs = args.split()
        all_instance = storage.all()
        class_name = ""
        arg_len = len(parsedargs)
        if arg_len == 2:
            class_name, class_id = parsedargs
            id_formatted = '{}.{}'.format(class_name, class_id)
            if class_name in self.classnames:
                if id_formatted not in all_instance:
                    print("** no instance found **")
                else:
                    del all_instance[id_formatted]
                    storage.save()
            elif class_name not in self.classnames:
                print("** class doesn't exist **")
        elif arg_len == 1 and parsedargs[0] not in self.classnames:
            print("** class doesn't exist **")
        elif arg_len == 1 and parsedargs[0] in self.classnames:
            print("** instance id missing **")
        if arg_len == 0:
            print("** class name missing **")

    def handle_update_errors(self, parsed_args, arg_len):
        """
        Handles Errors for update
        """
        if len(parsed_args) == 0:
            print("** class name missing **")
        elif len(parsed_args) >= 1:
            if parsed_args[0] in self.classnames:
                if arg_len == 1:
                    print("** instance id missing **")
                elif arg_len >= 2:
                    a, b, *t = parsed_args
                    id_formated = id_formated = "{}.{}".format(a, b)
                    id_exist = id_formated in storage.all()
                    if arg_len == 2 and id_exist:
                        print("** attribute name missing **")
                    else:
                        if arg_len == 3:
                            if self.dict_cache is not None:
                                if id_exist:
                                    return True
                                else:
                                    print("** no instance found **")
                                    return
                            print("** value missing **")
                        else:
                            if arg_len == 4 and id_exist:
                                return True
                            else:
                                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        return False

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if self.dict_cache is None:
            parsed_args = args.split()
        else:
            parsed_args = args
        arg_len = len(parsed_args)
        no_err = self.handle_update_errors(parsed_args, arg_len)
        dict_right = self.dict_cache is not None
        if no_err and dict_right and type(eval(parsed_args[2]) == dict):
            class_name, class_id, dict_val = parsed_args
            dict_ = eval(dict_val)
            id_formated = "{}.{}".format(class_name, class_id)
            all_instance = storage.all()
            if id_formated in all_instance:
                obj = all_instance[id_formated]
                for k, v in dict_.items():
                    if k in obj.__class__.__dict__.keys() and type(
                            obj.__class__.__dict__[k]) in [float, int, str]:
                        attr_t = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = attr_t(v)
                    else:
                        obj.__dict__[k] = v
                storage.save()
        elif no_err and len(parsed_args) >= 4:
            class_name, class_id, attr_name, attr_val, *tmp = parsed_args
            all_instance = storage.all()
            id_formated = "{}.{}".format(class_name, class_id)
            obj_trgt = all_instance[id_formated]
            if attr_name in obj_trgt.__class__.__dict__.keys():
                attr_t = type(obj_trgt.__class__.__dict__[attr_name])
                obj_trgt.__dict__[attr_name] = attr_t(attr_val)
            else:
                obj_trgt.__dict__[attr_name] = attr_val
            storage.save()

    def do_create(self, args):
        """ Creates a new instance of BaseModel and saves it to JSON file
        Usage: create classname
        """
        parsed_args = args.split()
        if len(parsed_args) == 0:
            print("** class name missing **")
        elif parsed_args[0] in self.classnames:
                new_obj = eval(parsed_args[0])()
                print(new_obj.id)
                storage.new(new_obj)
                storage.save()
        elif args not in self.classnames:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

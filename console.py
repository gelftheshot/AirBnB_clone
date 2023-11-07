#!/usr/bin/python3
import cmd
import re

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    __cl = ("Amenity", "BaseModel", "City", "Place", "Review", "State", "User")

    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        args = line.split()
        err_str = self.__handle_err(args, 1)
        if err_str:
            print(err_str)
        else:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, line):
        args = line.split()
        obj = models.storage.all()
        err_str = self.__handle_err(args, 0, obj.keys())
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            print(obj[id])

    def do_destroy(self, line):
        args = line.split()
        obj = models.storage.all()
        err_str = self.__handle_err(args, 0, obj.keys())
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            del obj[id]
            models.storage.save()

    def do_all(self, line):
        args = line.split()
        err_str = self.__handle_err(args, 1)
        if err_str:
            print(err_str)
        else:
            cls_strs = [
                x.__str__()
                for x in models.storage.all().values()
                if x.__class__.__name__ == args[0]
            ]
            print(cls_strs)

    def do_update(self, line):
        args = line.split()
        obj = models.storage.all()
        err_str = self.__handle_err(args, 4, obj.keys())
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            key = args[2]
            val = self.__handle_quote(" ".join(args[3:]))
            print(val)
            if key in obj[id].__dict__.keys():
                try:
                    val = type(obj[id].__dict__[key])(val)
                    setattr(obj[id], key, val)
                    models.storage.save()
                except ValueError:
                    print("Invalid value for {}".format(key))

    def __handle_err(self, args, ac, ins_list=None):
        if not args:
            return "** class name missing **"
        if args[0] not in self.__cl:
            return "** class doesn't exist **"

        if ac == 1:
            return ""

        if len(args) == 1:
            return "** instance id missing **"

        id = "{}.{}".format(args[0], args[1])
        if id not in ins_list:
            return "** no instance found **"

        if ac == 4:
            if len(args) == 2:
                return "** attribute name missing **"
            if len(args) == 3:
                return "** value missing **"

        return ""

    def __handle_quote(self, string):
        res = re.search(r'"(.*?)"', string)
        if res:
            return res.group(1)
        else:
            return string.split()[0]


if __name__ == "__main__":
    HBNBCommand().cmdloop()

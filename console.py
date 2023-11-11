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
        """
        Quits the console.

        Args:
            line: Any arguments passed to the quit command. Not used in this method.
        """
        return True

    def do_EOF(self, line):
        """
        Handles the EOF (End of File) signal to quit the console.

        Args:
            line: Any arguments passed to the EOF command. Not used in this method.
        """
        return True

    def emptyline(self):
        """
        Handles the event when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty command entered.
        However, if overridden, it performs a specific action. In this case, it does nothing.
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of a given class, saves it to the JSON file, and prints its id.

        Args:
            line (str): The input line from the console. It should contain the class name.
        """
        args = line.split()
        err_str = self.__handle_err(args, 1)
        if err_str:
            print(err_str)
        else:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.

        Args:
            line (str): The input line from the console, should contain the class name and id.
        """
        args = line.split()
        obj = models.storage.all()
        err_str = self.__handle_err(args, 0, obj.keys())
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            print(obj[id])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.

        Args:
            line (str): The input line from the console, should contain the class name and id.
        """
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
        """
        Prints all instances of a class.

        Args:
            line (str): The input line from the console, should contain the class name.
        """
        args = line.split()
        if not args:
            for obj in models.storage.all().values():
                print(obj.__str__())
        else:
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

    def __is_float(self, input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute.

        Args:
            line (str): The input line from the console, should contain the class name, id, attribute name, and attribute value.
        """
        args = line.split()
        obj = models.storage.all()
        err_str = self.__handle_err(args, 4, obj.keys())
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            key = args[2]
            val = " ".join(args[3:])
            try:
                if key in obj[id].__dict__.keys():
                    val = type(obj[id].__dict__[key])(val)
                elif val.isdigit():
                    val = int(val)
                elif self.__is_float(val):
                    val = float(val)
                if isinstance(val, str):  # only handle quotes if val is a string
                    val = self.__handle_quote(val)
                setattr(obj[id], key, val)
            except ValueError:
                print("Invalid value for {}".format(key))

    def do_count(self, line):
        """
        Counts the number of instances of a class.

        Args:
            line (str): The input line from the console, should contain the class name.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            count = 0
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    count += 1
            print(count)
        except KeyError:
            print("** class doesn't exist **")

    def default(self, line: str):
        """Default method for command line. Handles the commands in the format <class name>.<command>(<parameters>).

        Args:
            line (str): The input line from the console.
        """
        args = re.match(r"^(\w*)\.(\w+)\((.*)\)", line)
        if args :
            args = args.groups()
        if args is not None:
            if args[0] not in self.__cl and args[0] != "":
                print("** class doesn't exist **")
                return
            
        if args is not None and len(args) > 1:
            if args[1] == "all":
                self.do_all(args[0])
            elif args[1] == "count":
                self.do_count(args[0])
            elif args[1] == "show":
                self.do_show(args[0] + " " + args[2])
            elif args[1] == "destroy":
                self.do_destroy(args[0] + " " + args[2])
            elif args[1] == "update":
                res = re.search(r"{(.*?)}", args[2])
                if res:
                    obj = eval("{}{}{}".format("{", res.group(1), "}"))
                    for k, v in obj.items():
                        self.do_update(
                            "{} {} {} {}".format(args[0], args[2].split(",")[0], k, v)
                        )
                else:
                    update_args = " ".join(args[2].split(","))
                    self.do_update(args[0] + " " + update_args)
        else:
            print("*** Unknown syntax: {}".format(line))

    def __handle_err(self, args, ac, ins_list=None):
        """
        Handles errors for commands that require a class name and an instance id.

        Args:
            args (list): The arguments from the console command.
            ac (int): The number of arguments required for the command.
            ins_list (list, optional): The list of instance ids. Defaults to None.

        Returns:
            str: An error message if there is an error, or an empty string if there are no errors.
        """
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

    def __handle_quote(self, val):
        if val[0] == val[-1] == "'":
            return val[1:-1]  
        return val


if __name__ == "__main__":
    HBNBCommand().cmdloop()

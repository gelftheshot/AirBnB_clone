#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    __cl = "BaseModel"

    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        args = line.split()
        err_str, _ = self.__handle_err(args, 1)
        if err_str:
            print(err_str)
        else:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, line):
        args = line.split()
        err_str, obj = self.__handle_err(args, 0)
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            print(obj[id])

    def do_destroy(self, line):
        args = line.split()
        err_str, obj = self.__handle_err(args, 0)
        if err_str:
            print(err_str)
        else:
            id = "{}.{}".format(args[0], args[1])
            del obj[id]
            models.storage.save()

    def do_all(self, line):
        args = line.split()
        err_str, _ = self.__handle_err(args, 1)
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
        err_str, obj = self.__handle_err(args, 0)
        if err_str:
            print(err_str)
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            id = "{}.{}".format(args[0], args[1])
            key = args[2]
            val = args[3].strip('"')
            if key in obj[id].__dict__.keys():
                try:
                    val = type(obj[id].__dict__[key])(val)
                    setattr(obj[id], key, val)
                    models.storage.save()
                except ValueError:
                    print("Invalid value for {}".format(key))

    def __handle_err(self, args, ac):
        if not args:
            return ("** class name missing **", None)
        if args[0] not in self.__cl:
            return ("** class doesn't exist **", None)

        if ac == 1:
            return ("", None)

        if len(args) == 1:
            return ("** instance id missing **", None)

        id = "{}.{}".format(args[0], args[1])
        obj = models.storage.all()
        if id not in obj.keys():
            return ("** no instance found **", None)

        return ("", obj)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

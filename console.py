#!/usr/bin/python3
"""This a  Console module for AirBnB """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """This a Class for the console AirBnB"""
    prompt = "(hbnb) "

    g_Classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    g_Strings = ["name", "amenity_id", "place_id", "state_id",
                 "user_id", "city_id", "description", "text",
                 "email", "password", "first_name", "last_name"]
    g_Integers = ["number_rooms", "number_bathrooms",
                 "max_guest", "price_by_night"]

    g_Floats = ["latitude", "longitude"]

    def do_EOF(self, arg):
        """Ctrl-D to exit the program\n"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything\n"""
        pass

    def do_create(self, arg):
        """it Creates a new instance """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_clear(self, arg):
        """it Clear data storage """
        storage.all().clear()
        storage.save()
        print("** All data has been cleared! **")

    def valid(self, arg, id_flag=False, att_flag=False):
        """validation of arguments that pass to commands"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.g_Classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and id_flag:
            print("** instance id missing **")
            return False
        if id_flag and args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
            return False
        if len(args) == 2 and att_flag:
            print("** attribute name missing **")
            return False
        if len(args) == 3 and att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        """it Prints the string representation of an instance"""
        if self.valid(arg, True):
            args = arg.split()
            instance_key = args[0]+"."+args[1]
            print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """it Deletes an instance"""
        if self.valid(arg, True):
            args = arg.split()
            instance_key = args[0]+"."+args[1]
            del storage.all()[instance_key]
            storage.save()

    def do_all(self, arg):
        """it Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if len(args) >= 1:
            if args[0] not in self.g_Classes:
                print("** class doesn't exist **")
                return
            instance_list = [str(value) for key, value in storage.all().items() if args[0] in key]
        else:
            instance_list = [str(value) for value in storage.all().values()]
        print(instance_list)

    def casting(self, arg):
        """it cast string to float or int if possible"""
        try:
            if "." in arg:
                return float(arg)
            else:
                return int(arg)
        except ValueError:
            return arg

    def do_update(self, arg):
        """it Updates an instance by adding or updating attribute"""
        if self.valid(arg, True, True):
            args = arg.split()
            instance_key = args[0]+"."+args[1]
            value = re.search(r'"([^"]+)"', arg).group(1)
            setattr(storage.all()[instance_key], args[2], self.casting(value))
            storage.save()

    def count(self, arg):
        """the number of instances of a class"""
        instance_count = 0
        for key in storage.all():
            if arg[:-1] in key:
                instance_count += 1
        print(instance_count)

    def _exec(self, arg):
        """this helper function parsing filtering replacing"""
        methods = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }
        excu = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        args = excu[0][0]+" "+excu[0][2]
        args_list = args.split(", ")
        args_list[0] = args_list[0].replace('"', "").replace("'", "")
        if len(args_list) > 1:
            args_list[1] = args_list[1].replace('"', "").replace("'", "")
        args = " ".join(args_list)
        if excu[0][1] in methods:
            methods[excu[0][1]](args)

    def default(self, arg):
        """if no command found"""
        excu = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(excu) != 0 and excu[0][1] == "update" and "{" in arg:
            arg_dict = re.search(r'{([^}]+)}', arg).group()
            arg_dict = json.loads(arg_dict.replace("'", '"'))
            for key, value in arg_dict.items():
                arg = arg.split("{")[0] + key + ", " + str(value) + ")"
                self._exec(arg)
        elif len(excu) != 0:
            self._exec(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

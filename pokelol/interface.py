import sys
from typing import Callable, Iterable
import os

class Interface:
    """
    This class configure the basic output
    """

    def __init__(self, interface_type: str = "terminal"):
        self._type = interface_type

    def __call__(self, *args, **kwargs):
        sys.stdout.write("* " + "".join(map(str, *args)) + "\n")

    def interaction(self, question):
        self(question)
        return sys.stdin.readline()

    def display_single_string(self, string):
        self(string)

    def multiple_choices_no_back(self, choices: dict, question: str = ""):
        """
        returns the associeated var of the choice

        Parameters
        ----------
        question : str
            string to display before printing possible choices

        choices : dict
            {"string to display": var_to_return}

        Returns
        -------
        var_to_return
        """
        rt_ = {}
        if question != "":
            self(question)
        for k, i in enumerate(choices.keys()):
            self(f"{k} : {i}")
            rt_[k] = choices[i]
        while True:
            number = int(self.interaction(f'choose a number in {0} - {len(choices) - 1}'))
            if number not in range(len(choices)):
                print(f"Number {number} not in " + "{" + f"0 - {len(choices) - 1}" + "}")
            else:
                break
        return rt_[number]

    def multiple_choices(self, choices: dict, question: str = "", back_callable: Callable = None):
        """
        returns the associeated var of the choice

        Parameters
        ----------
        back_callable : Callable to go back to last menu

        question : str
            string to display before printing possible choices

        choices : dict
            {"string to display": var_to_return}

        Returns
        -------
        var_to_return
        """
        if back_callable is None:
            return multiple_choices_no_back(choices, question)
        rt_ = {}
        choices["Back"] = back_callable
        if question != "":
            self(question)
        for k, i in enumerate(choices.keys()):
            self(f"{k} : {i}")
            rt_[k] = choices[i]
        while True:
            number = int(self.interaction(f'choose a number in {0} - {len(choices) - 1}'))
            if number not in range(len(choices)):
                print(f"Number {number} not in " + "{" + f"0 - {len(choices) - 1}" + "}")
            else:
                break
        return rt_[number]



my_print = Interface()


def print(*args, **kwargs):
    my_print(args)


def multiple_choices_no_back(choices: dict, question: str = ""):
    return my_print.multiple_choices_no_back(choices, question)


def input(question):
    return my_print.interaction(question)


def multiple_choices(choices: dict, question: str = "", back_callable: Callable = None):
    return my_print.multiple_choices(choices, question, back_callable)


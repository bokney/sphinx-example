
"""
example.py

This is an example module for purpose of
testing sphinx documentation generation 🆗
"""


class ExampleClass:
    """
    An example class. It takes the users name then
    greets the user when the greet() method is called.

    :param name: Name of individual to be greeted.
    :type name: str

    Attributes:
        name (str): instance name
    """

    def __init__(self, name: str):
        """
        Constructor method.
        """
        self.name = name

    def greet(self):
        """
        Prints message greeting name provided.
        """
        print(f"Hello {self.name}! 🙋‍♂️")

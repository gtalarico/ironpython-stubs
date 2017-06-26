class PropertyPath(object):
    """
    Implements a data structure for describing a property as a path below another property, or below an owning type. Property paths are used in data binding to objects, and in storyboards and timelines for animations.
    
    PropertyPath(path: str, *pathParameters: Array[object])
    PropertyPath(parameter: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, path: str, *pathParameters: Array[object])
        __new__(cls: type, parameter: object)
        """
        pass

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string that describes the path.

Get: Path(self: PropertyPath) -> str

Set: Path(self: PropertyPath) = value
"""

    PathParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of parameters to use when the path refers to indexed parameters.

Get: PathParameters(self: PropertyPath) -> Collection[object]

"""



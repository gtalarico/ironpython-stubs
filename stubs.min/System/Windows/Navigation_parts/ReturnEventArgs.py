class ReturnEventArgs(EventArgs):
    """
    ReturnEventArgs[T]()
    ReturnEventArgs[T](result: T)
    """
    @staticmethod # known case of __new__
    def __new__(self, result=None):
        """
        __new__(cls: type)
        __new__(cls: type, result: T)
        """
        pass

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that is returned by the page function.

Get: Result(self: ReturnEventArgs[T]) -> T

Set: Result(self: ReturnEventArgs[T]) = value
"""



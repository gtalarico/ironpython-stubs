class DataErrorsChangedEventArgs(EventArgs):
    """ DataErrorsChangedEventArgs(propertyName: str) """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: DataErrorsChangedEventArgs) -> str

"""



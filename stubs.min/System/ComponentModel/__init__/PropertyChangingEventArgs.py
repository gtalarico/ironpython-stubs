class PropertyChangingEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.INotifyPropertyChanging.PropertyChanging event.
    
    PropertyChangingEventArgs(propertyName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property whose value is changing.

Get: PropertyName(self: PropertyChangingEventArgs) -> str

"""



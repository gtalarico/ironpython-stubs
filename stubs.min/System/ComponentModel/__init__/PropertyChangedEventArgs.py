class PropertyChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event.
    
    PropertyChangedEventArgs(propertyName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property that changed.

Get: PropertyName(self: PropertyChangedEventArgs) -> str

"""



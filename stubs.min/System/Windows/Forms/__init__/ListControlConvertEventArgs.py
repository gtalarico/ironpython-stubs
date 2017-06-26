class ListControlConvertEventArgs(ConvertEventArgs):
    """
    Provides data for the System.Windows.Forms.ListControl.Format event.
    
    ListControlConvertEventArgs(value: object, desiredType: Type, listItem: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, value, desiredType, listItem):
        """ __new__(cls: type, value: object, desiredType: Type, listItem: object) """
        pass

    ListItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a data source item.

Get: ListItem(self: ListControlConvertEventArgs) -> object

"""



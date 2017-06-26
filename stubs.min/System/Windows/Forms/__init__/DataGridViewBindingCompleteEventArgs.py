class DataGridViewBindingCompleteEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.DataGridView.DataBindingComplete event.
    
    DataGridViewBindingCompleteEventArgs(listChangedType: ListChangedType)
    """
    @staticmethod # known case of __new__
    def __new__(self, listChangedType):
        """ __new__(cls: type, listChangedType: ListChangedType) """
        pass

    ListChangedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value specifying how the list changed.

Get: ListChangedType(self: DataGridViewBindingCompleteEventArgs) -> ListChangedType

"""



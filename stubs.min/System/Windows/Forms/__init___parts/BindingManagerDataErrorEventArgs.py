class BindingManagerDataErrorEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.BindingManagerBase.DataError event.
    
    BindingManagerDataErrorEventArgs(exception: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, exception):
        """ __new__(cls: type, exception: Exception) """
        pass

    Exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Exception caught in the binding process that caused the System.Windows.Forms.BindingManagerBase.DataError event to be raised.

Get: Exception(self: BindingManagerDataErrorEventArgs) -> Exception

"""



class VScrollProperties(ScrollProperties):
    """
    Provides basic properties for the System.Windows.Forms.VScrollBar class.
    
    VScrollProperties(container: ScrollableControl)
    """
    @staticmethod # known case of __new__
    def __new__(self, container):
        """ __new__(cls: type, container: ScrollableControl) """
        pass

    ParentControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the control to which this scroll information applies.

"""



class DispatchWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_DISPATCH.
    
    DispatchWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object wrapped by the System.Runtime.InteropServices.DispatchWrapper.

Get: WrappedObject(self: DispatchWrapper) -> object

"""



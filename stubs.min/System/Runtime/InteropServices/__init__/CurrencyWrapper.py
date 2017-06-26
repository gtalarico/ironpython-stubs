class CurrencyWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_CY.
    
    CurrencyWrapper(obj: Decimal)
    CurrencyWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """
        __new__(cls: type, obj: Decimal)
        __new__(cls: type, obj: object)
        """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the wrapped object to be marshaled as type VT_CY.

Get: WrappedObject(self: CurrencyWrapper) -> Decimal

"""



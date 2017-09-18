# encoding: utf-8
# module System.Windows.Markup calls itself Markup
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ValueSerializerAttribute(Attribute, _Attribute):
    """
    ValueSerializerAttribute(valueSerializerType: Type)
    ValueSerializerAttribute(valueSerializerTypeName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, valueSerializerType: Type)
        __new__(cls: type, valueSerializerTypeName: str)
        """
        pass

    ValueSerializerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueSerializerType(self: ValueSerializerAttribute) -> Type

"""

    ValueSerializerTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueSerializerTypeName(self: ValueSerializerAttribute) -> str

"""




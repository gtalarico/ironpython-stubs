class LicenseProviderAttribute(Attribute, _Attribute):
    """
    Specifies the System.ComponentModel.LicenseProvider to use with a class. This class cannot be inherited.
    
    LicenseProviderAttribute()
    LicenseProviderAttribute(typeName: str)
    LicenseProviderAttribute(type: Type)
    """
    def Equals(self, value):
        """
        Equals(self: LicenseProviderAttribute, value: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            value: Another object to compare to.
            Returns: true if value is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LicenseProviderAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.LicenseProviderAttribute.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    LicenseProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the license provider that must be used with the associated class.

Get: LicenseProvider(self: LicenseProviderAttribute) -> Type

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates a unique ID for this attribute type.

Get: TypeId(self: LicenseProviderAttribute) -> object

"""


    Default = None


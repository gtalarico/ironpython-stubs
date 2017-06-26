class DataObjectFieldAttribute(Attribute, _Attribute):
    """
    Provides metadata for a property representing a data field. This class cannot be inherited.
    
    DataObjectFieldAttribute(primaryKey: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
    """
    def Equals(self, obj):
        """
        Equals(self: DataObjectFieldAttribute, obj: object) -> bool
        
            Returns a value indicating whether this instance is equal to a specified object.
        
            obj: An object to compare with this instance of System.ComponentModel.DataObjectFieldAttribute.
            Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DataObjectFieldAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, primaryKey, isIdentity=None, isNullable=None, length=None):
        """
        __new__(cls: type, primaryKey: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property represents an identity field in the underlying data.

Get: IsIdentity(self: DataObjectFieldAttribute) -> bool

"""

    IsNullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property represents a field that can be null in the underlying data store.

Get: IsNullable(self: DataObjectFieldAttribute) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the property in bytes.

Get: Length(self: DataObjectFieldAttribute) -> int

"""

    PrimaryKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property is in the primary key in the underlying data.

Get: PrimaryKey(self: DataObjectFieldAttribute) -> bool

"""



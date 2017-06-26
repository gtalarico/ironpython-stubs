class AttachedPropertyBrowsableForChildrenAttribute(AttachedPropertyBrowsableAttribute, _Attribute):
    """
    Specifies that an attached property has a browsable scope that extends to child elements in the logical tree.
    
    AttachedPropertyBrowsableForChildrenAttribute()
    """
    def Equals(self, obj):
        """
        Equals(self: AttachedPropertyBrowsableForChildrenAttribute, obj: object) -> bool
        
            Determines whether the current System.Windows.AttachedPropertyBrowsableForChildrenAttribute�.NET Framework attribute is equal to a specified object.
        
            obj: The System.Windows.AttachedPropertyBrowsableForChildrenAttribute to compare to the current System.Windows.AttachedPropertyBrowsableForChildrenAttribute.
            Returns: true if the specified System.Windows.AttachedPropertyBrowsableForChildrenAttribute is equal to the current System.Windows.AttachedPropertyBrowsableForChildrenAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: AttachedPropertyBrowsableForChildrenAttribute) -> int
        
            Returns the hash code for this System.Windows.AttachedPropertyBrowsableForChildrenAttribute�.NET Framework attribute.
            Returns: An unsigned 32-bit integer value.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IncludeDescendants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that declares whether to use the deep mode for detection of parent elements on the attached property where this �.NET Framework attribute is applied.

Get: IncludeDescendants(self: AttachedPropertyBrowsableForChildrenAttribute) -> bool

Set: IncludeDescendants(self: AttachedPropertyBrowsableForChildrenAttribute) = value
"""



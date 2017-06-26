class StyleTypedPropertyAttribute(Attribute, _Attribute):
    """
    Represents an attribute that is applied to the class definition and determines the System.Windows.Style.TargetTypes of the properties that are of type System.Windows.Style.
    
    StyleTypedPropertyAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the property that is of type System.Windows.Style.

Get: Property(self: StyleTypedPropertyAttribute) -> str

Set: Property(self: StyleTypedPropertyAttribute) = value
"""

    StyleTargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Style.TargetType of the System.Windows.StyleTypedPropertyAttribute.Property this attribute is specifying.

Get: StyleTargetType(self: StyleTypedPropertyAttribute) -> Type

Set: StyleTargetType(self: StyleTypedPropertyAttribute) = value
"""



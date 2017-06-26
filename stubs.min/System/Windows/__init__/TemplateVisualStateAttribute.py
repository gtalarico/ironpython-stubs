class TemplateVisualStateAttribute(Attribute, _Attribute):
    """
    Specifies that a control can be in a certain state and that a System.Windows.VisualState is expected in the control's System.Windows.Controls.ControlTemplate.
    
    TemplateVisualStateAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the group that the state belongs to.

Get: GroupName(self: TemplateVisualStateAttribute) -> str

Set: GroupName(self: TemplateVisualStateAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the state that the control can be in.

Get: Name(self: TemplateVisualStateAttribute) -> str

Set: Name(self: TemplateVisualStateAttribute) = value
"""



class LayoutEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.Control.Layout event. This class cannot be inherited.
    
    LayoutEventArgs(affectedComponent: IComponent, affectedProperty: str)
    LayoutEventArgs(affectedControl: Control, affectedProperty: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, affectedComponent: IComponent, affectedProperty: str)
        __new__(cls: type, affectedControl: Control, affectedProperty: str)
        """
        pass

    AffectedComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.Component affected by the layout change.

Get: AffectedComponent(self: LayoutEventArgs) -> IComponent

"""

    AffectedControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the child control affected by the change.

Get: AffectedControl(self: LayoutEventArgs) -> Control

"""

    AffectedProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property affected by the change.

Get: AffectedProperty(self: LayoutEventArgs) -> str

"""



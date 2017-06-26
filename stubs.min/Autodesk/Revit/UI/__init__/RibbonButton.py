class RibbonButton(RibbonItem):
    """ This class is the base class of PushButton and PulldownButton. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, item: RibbonButton, parentId: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the button.

Get: Image(self: RibbonButton) -> ImageSource

Set: Image(self: RibbonButton) = value
"""

    IsEnabledByContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this button can be executed. True if the pushbutton is permitted to be executed based on the 
current Revit context (active document, active view and active tool). False if the pushbutton is disabled because 
of the active context.

Get: IsEnabledByContext(self: RibbonButton) -> bool

"""

    LargeImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The large image shown on the button.

Get: LargeImage(self: RibbonButton) -> ImageSource

Set: LargeImage(self: RibbonButton) = value
"""


    m_ItemType = None


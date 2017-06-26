class TextCompositionEventArgs(InputEventArgs):
    """
    Contains arguments associated with changes to a System.Windows.Input.TextComposition.
    
    TextCompositionEventArgs(inputDevice: InputDevice, composition: TextComposition)
    """
    @staticmethod # known case of __new__
    def __new__(self, inputDevice, composition):
        """ __new__(cls: type, inputDevice: InputDevice, composition: TextComposition) """
        pass

    ControlText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets control text associated with a System.Windows.Input.TextComposition event.

Get: ControlText(self: TextCompositionEventArgs) -> str

"""

    SystemText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets system text associated with a System.Windows.Input.TextComposition event.

Get: SystemText(self: TextCompositionEventArgs) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets input text associated with a System.Windows.Input.TextComposition event.

Get: Text(self: TextCompositionEventArgs) -> str

"""

    TextComposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.TextComposition associated with a System.Windows.Input.TextComposition event.

Get: TextComposition(self: TextCompositionEventArgs) -> TextComposition

"""



class TextComposition(DispatcherObject):
    """
    Represents a composition related to text input which includes the composition text itself, any related control or system text, and a state of completion for the composition.
    
    TextComposition(inputManager: InputManager, source: IInputElement, resultText: str)
    TextComposition(inputManager: InputManager, source: IInputElement, resultText: str, autoComplete: TextCompositionAutoComplete)
    """
    def Complete(self):
        """
        Complete(self: TextComposition)
            Completes this text composition.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inputManager, source, resultText, autoComplete=None):
        """
        __new__(cls: type, inputManager: InputManager, source: IInputElement, resultText: str)
        __new__(cls: type, inputManager: InputManager, source: IInputElement, resultText: str, autoComplete: TextCompositionAutoComplete)
        """
        pass

    AutoComplete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the auto-complete setting for this text composition.

Get: AutoComplete(self: TextComposition) -> TextCompositionAutoComplete

"""

    CompositionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the composition text for this text composition.

Get: CompositionText(self: TextComposition) -> str

"""

    ControlText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets any control text associated with this text composition.

Get: ControlText(self: TextComposition) -> str

"""

    SystemCompositionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the system composition text for this text composition.

Get: SystemCompositionText(self: TextComposition) -> str

"""

    SystemText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the system text for this text composition.

Get: SystemText(self: TextComposition) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current text for this text composition.

Get: Text(self: TextComposition) -> str

"""



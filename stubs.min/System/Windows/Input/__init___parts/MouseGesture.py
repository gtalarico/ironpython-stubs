class MouseGesture(InputGesture):
    """
    Defines a mouse input gesture that can be used to invoke a command.
    
    MouseGesture()
    MouseGesture(mouseAction: MouseAction)
    MouseGesture(mouseAction: MouseAction, modifiers: ModifierKeys)
    """
    def Matches(self, targetElement, inputEventArgs):
        """
        Matches(self: MouseGesture, targetElement: object, inputEventArgs: InputEventArgs) -> bool
        
            Determines whether System.Windows.Input.MouseGesture matches the input associated with the specified System.Windows.Input.InputEventArgs object.
        
            targetElement: The target.
            inputEventArgs: The input event data to compare with this gesture.
            Returns: true if the event data matches this System.Windows.Input.MouseGesture; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mouseAction=None, modifiers=None):
        """
        __new__(cls: type)
        __new__(cls: type, mouseAction: MouseAction)
        __new__(cls: type, mouseAction: MouseAction, modifiers: ModifierKeys)
        """
        pass

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the modifier keys associated with this System.Windows.Input.MouseGesture.

Get: Modifiers(self: MouseGesture) -> ModifierKeys

Set: Modifiers(self: MouseGesture) = value
"""

    MouseAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.MouseAction associated with this gesture.

Get: MouseAction(self: MouseGesture) -> MouseAction

Set: MouseAction(self: MouseGesture) = value
"""



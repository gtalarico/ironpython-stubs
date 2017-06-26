class KeyboardFocusChangedEventArgs(KeyboardEventArgs):
    """
    Provides data for System.Windows.UIElement.LostKeyboardFocus and System.Windows.UIElement.GotKeyboardFocus�routed events, as well as related attached and Preview events.
    
    KeyboardFocusChangedEventArgs(keyboard: KeyboardDevice, timestamp: int, oldFocus: IInputElement, newFocus: IInputElement)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, timestamp, oldFocus, newFocus):
        """ __new__(cls: type, keyboard: KeyboardDevice, timestamp: int, oldFocus: IInputElement, newFocus: IInputElement) """
        pass

    NewFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that focus has moved to.

Get: NewFocus(self: KeyboardFocusChangedEventArgs) -> IInputElement

"""

    OldFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that previously had focus.

Get: OldFocus(self: KeyboardFocusChangedEventArgs) -> IInputElement

"""



class KeyboardDevice(InputDevice):
    """ Abstract class that represents a keyboard device. """
    def ClearFocus(self):
        """
        ClearFocus(self: KeyboardDevice)
            Clears focus.
        """
        pass

    def Focus(self, element):
        """
        Focus(self: KeyboardDevice, element: IInputElement) -> IInputElement
        
            Sets keyboard focus on the specified System.Windows.IInputElement.
        
            element: The element to move focus to.
            Returns: The element that has keyboard focus.
        """
        pass

    def GetKeyStates(self, key):
        """
        GetKeyStates(self: KeyboardDevice, key: Key) -> KeyStates
        
            Gets the set of key states for the specified System.Windows.Input.Key.
        
            key: The key to check.
            Returns: The set of key states for the specified key.
        """
        pass

    def GetKeyStatesFromSystem(self, *args): #cannot find CLR method
        """
        GetKeyStatesFromSystem(self: KeyboardDevice, key: Key) -> KeyStates
        
            When overridden in a derived class, obtains the System.Windows.Input.KeyStates for the specified System.Windows.Input.Key.
        
            key: The key to check.
            Returns: The set of key states for the specified key.
        """
        pass

    def IsKeyDown(self, key):
        """
        IsKeyDown(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the down state.
        
            key: The key to check.
            Returns: true if key is in the down state; otherwise, false.
        """
        pass

    def IsKeyToggled(self, key):
        """
        IsKeyToggled(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the toggled state.
        
            key: The key to check.
            Returns: true if key is in the toggled state; otherwise, false.
        """
        pass

    def IsKeyUp(self, key):
        """
        IsKeyUp(self: KeyboardDevice, key: Key) -> bool
        
            Determines whether the specified System.Windows.Input.Key is in the up state.
        
            key: The key to check.
            Returns: true if key is in the up state; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, inputManager: InputManager) """
        pass

    ActiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: KeyboardDevice) -> PresentationSource

"""

    DefaultRestoreFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the behavior of Windows Presentation Foundation (WPF) when restoring focus.

Get: DefaultRestoreFocusMode(self: KeyboardDevice) -> RestoreFocusMode

Set: DefaultRestoreFocusMode(self: KeyboardDevice) = value
"""

    FocusedElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that has keyboard focus.

Get: FocusedElement(self: KeyboardDevice) -> IInputElement

"""

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of System.Windows.Input.ModifierKeys which are currently pressed.

Get: Modifiers(self: KeyboardDevice) -> ModifierKeys

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the specified System.Windows.IInputElement that input from this device is sent to.

Get: Target(self: KeyboardDevice) -> IInputElement

"""



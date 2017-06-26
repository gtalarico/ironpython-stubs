class RoutedCommand(object, ICommand):
    """
    Defines a command that implements System.Windows.Input.ICommand and is routed through the element tree.
    
    RoutedCommand()
    RoutedCommand(name: str, ownerType: Type)
    RoutedCommand(name: str, ownerType: Type, inputGestures: InputGestureCollection)
    """
    def CanExecute(self, parameter, target):
        """
        CanExecute(self: RoutedCommand, parameter: object, target: IInputElement) -> bool
        
            Determines whether this System.Windows.Input.RoutedCommand can execute in its current state.
        
            parameter: A user defined data type.
            target: The command target.
            Returns: true if the command can execute on the current command target; otherwise, false.
        """
        pass

    def Execute(self, parameter, target):
        """
        Execute(self: RoutedCommand, parameter: object, target: IInputElement)
            Executes the System.Windows.Input.RoutedCommand on the current command target.
        
            parameter: User defined parameter to be passed to the handler.
            target: Element at which to begin looking for command handlers.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, ownerType=None, inputGestures=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, ownerType: Type)
        __new__(cls: type, name: str, ownerType: Type, inputGestures: InputGestureCollection)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    InputGestures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Input.InputGesture objects that are associated with this command.

Get: InputGestures(self: RoutedCommand) -> InputGestureCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the command.

Get: Name(self: RoutedCommand) -> str

"""

    OwnerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that is registered with the command.

Get: OwnerType(self: RoutedCommand) -> Type

"""


    CanExecuteChanged = None


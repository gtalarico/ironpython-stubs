class ManipulationStartingEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationStarting, event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationStartingEventArgs) -> bool
        
            Cancels the manipulation and promotes touch to mouse events.
            Returns: true if touch was successfully promoted to mouse events, otherwise, false.
        """
        pass

    def SetManipulationParameter(self, parameter):
        """
        SetManipulationParameter(self: ManipulationStartingEventArgs, parameter: ManipulationParameters2D)
            Adds parameters to the current manipulation of the specified element.
        
            parameter: The parameter to add.
        """
        pass

    IsSingleTouchEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether one finger can start a manipulation.

Get: IsSingleTouchEnabled(self: ManipulationStartingEventArgs) -> bool

Set: IsSingleTouchEnabled(self: ManipulationStartingEventArgs) = value
"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the container that all manipulation events and calculations are relative to.

Get: ManipulationContainer(self: ManipulationStartingEventArgs) -> IInputElement

Set: ManipulationContainer(self: ManipulationStartingEventArgs) = value
"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationStartingEventArgs) -> IEnumerable[IManipulator]

"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets which types of manipulations are possible.

Get: Mode(self: ManipulationStartingEventArgs) -> ManipulationModes

Set: Mode(self: ManipulationStartingEventArgs) = value
"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object that describes the pivot for a single-point manipulation.

Get: Pivot(self: ManipulationStartingEventArgs) -> ManipulationPivot

Set: Pivot(self: ManipulationStartingEventArgs) = value
"""



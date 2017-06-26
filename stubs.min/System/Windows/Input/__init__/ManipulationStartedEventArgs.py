class ManipulationStartedEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationStarted event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationStartedEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if manipulation was successfully, otherwise, false.
        """
        pass

    def Complete(self):
        """
        Complete(self: ManipulationStartedEventArgs)
            Completes the manipulation without inertia.
        """
        pass

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that the System.Windows.Input.ManipulationStartedEventArgs.ManipulationOrigin property is relative to.

Get: ManipulationContainer(self: ManipulationStartedEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationStartedEventArgs) -> Point

"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationStartedEventArgs) -> IEnumerable[IManipulator]

"""



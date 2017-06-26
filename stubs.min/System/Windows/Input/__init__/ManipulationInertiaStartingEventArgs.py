class ManipulationInertiaStartingEventArgs(InputEventArgs):
    """ Provides data for the System.Windows.UIElement.ManipulationInertiaStarting event. """
    def Cancel(self):
        """
        Cancel(self: ManipulationInertiaStartingEventArgs) -> bool
        
            Cancels the manipulation.
            Returns: true if the manipulation was successfully canceled; otherwise, false.
        """
        pass

    def SetInertiaParameter(self, parameter):
        """
        SetInertiaParameter(self: ManipulationInertiaStartingEventArgs, parameter: InertiaParameters2D)
            Specifies the behavior of a manipulation during inertia.
        
            parameter: The object that specifies the behavior of a manipulation during inertia.
        """
        pass

    ExpansionBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or sets the rate of slowdown of expansion inertial movement.

Get: ExpansionBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaExpansionBehavior

Set: ExpansionBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""

    InitialVelocities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rates of changes to the manipulation that occur before inertia starts.

Get: InitialVelocities(self: ManipulationInertiaStartingEventArgs) -> ManipulationVelocities

"""

    ManipulationContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container that the System.Windows.Input.ManipulationStartedEventArgs.ManipulationOrigin property is relative to.

Get: ManipulationContainer(self: ManipulationInertiaStartingEventArgs) -> IInputElement

"""

    ManipulationOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationInertiaStartingEventArgs) -> Point

Set: ManipulationOrigin(self: ManipulationInertiaStartingEventArgs) = value
"""

    Manipulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationInertiaStartingEventArgs) -> IEnumerable[IManipulator]

"""

    RotationBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate of slowdown of rotational inertial movement.

Get: RotationBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaRotationBehavior

Set: RotationBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""

    TranslationBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the rate of slowdown of linear inertial movement.

Get: TranslationBehavior(self: ManipulationInertiaStartingEventArgs) -> InertiaTranslationBehavior

Set: TranslationBehavior(self: ManipulationInertiaStartingEventArgs) = value
"""



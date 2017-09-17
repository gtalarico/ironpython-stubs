class ManipulationCompletedEventArgs(InputEventArgs):
 """ Provides data for the System.Windows.UIElement.ManipulationCompleted event. """
 def Cancel(self):
  """
  Cancel(self: ManipulationCompletedEventArgs) -> bool
  
   Cancels the manipulation.
   Returns: true if the manipulation was successfully canceled; otherwise,false.
  """
  pass
 FinalVelocities=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the velocities that are used for the manipulation.

Get: FinalVelocities(self: ManipulationCompletedEventArgs) -> ManipulationVelocities

"""

 IsInertial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.UIElement.ManipulationCompleted event occurs during inertia.

Get: IsInertial(self: ManipulationCompletedEventArgs) -> bool

"""

 ManipulationContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the container that defines the coordinates for the manipulation.

Get: ManipulationContainer(self: ManipulationCompletedEventArgs) -> IInputElement

"""

 ManipulationOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationCompletedEventArgs) -> Point

"""

 Manipulators=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationCompletedEventArgs) -> IEnumerable[IManipulator]

"""

 TotalManipulation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total transformation that occurs during the current manipulation.

Get: TotalManipulation(self: ManipulationCompletedEventArgs) -> ManipulationDelta

"""



class ManipulationDeltaEventArgs(InputEventArgs):
 """ Provides data for the System.Windows.UIElement.ManipulationDelta event. """
 def Cancel(self):
  """
  Cancel(self: ManipulationDeltaEventArgs) -> bool
  
   Cancels the manipulation.
   Returns: true if the manipulation was successfully canceled; otherwise,false.
  """
  pass
 def Complete(self):
  """
  Complete(self: ManipulationDeltaEventArgs)
   Completes the manipulation without inertia.
  """
  pass
 def ReportBoundaryFeedback(self,unusedManipulation):
  """
  ReportBoundaryFeedback(self: ManipulationDeltaEventArgs,unusedManipulation: ManipulationDelta)
   Specifies that the manipulation has gone beyond certain boundaries.
  
   unusedManipulation: The portion of the manipulation that represents moving beyond the boundary.
  """
  pass
 def StartInertia(self):
  """
  StartInertia(self: ManipulationDeltaEventArgs)
   Starts inertia on the manipulation by ignoring subsequent contact movements and 
    raising the System.Windows.UIElement.ManipulationInertiaStarting event.
  """
  pass
 CumulativeManipulation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cumulated changes of the current manipulation.

Get: CumulativeManipulation(self: ManipulationDeltaEventArgs) -> ManipulationDelta

"""

 DeltaManipulation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the most recent changes of the current manipulation.

Get: DeltaManipulation(self: ManipulationDeltaEventArgs) -> ManipulationDelta

"""

 IsInertial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.UIElement.ManipulationDelta event occurs during inertia.

Get: IsInertial(self: ManipulationDeltaEventArgs) -> bool

"""

 ManipulationContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the container that defines the coordinates for the manipulation.

Get: ManipulationContainer(self: ManipulationDeltaEventArgs) -> IInputElement

"""

 ManipulationOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point from which the manipulation originated.

Get: ManipulationOrigin(self: ManipulationDeltaEventArgs) -> Point

"""

 Manipulators=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationDeltaEventArgs) -> IEnumerable[IManipulator]

"""

 Velocities=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rates of the most recent changes to the manipulation.

Get: Velocities(self: ManipulationDeltaEventArgs) -> ManipulationVelocities

"""



class ManipulationBoundaryFeedbackEventArgs(InputEventArgs):
 """ Provides data for the System.Windows.UIElement.ManipulationBoundaryFeedback event. """
 BoundaryFeedback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unused portion of the direct manipulation.

Get: BoundaryFeedback(self: ManipulationBoundaryFeedbackEventArgs) -> ManipulationDelta

"""

 ManipulationContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the container that the System.Windows.Input.ManipulationBoundaryFeedbackEventArgs.BoundaryFeedback property is relative to.

Get: ManipulationContainer(self: ManipulationBoundaryFeedbackEventArgs) -> IInputElement

"""

 Manipulators=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of objects that represents the touch contacts for the manipulation.

Get: Manipulators(self: ManipulationBoundaryFeedbackEventArgs) -> IEnumerable[IManipulator]

"""



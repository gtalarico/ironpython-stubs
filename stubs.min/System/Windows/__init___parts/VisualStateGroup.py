class VisualStateGroup(DependencyObject):
 """
 Contains mutually exclusive System.Windows.VisualState objects and System.Windows.VisualTransition objects that are used to move from one state to another.
 
 VisualStateGroup()
 """
 CurrentState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.VisualState that is currently applied to the control.

Get: CurrentState(self: VisualStateGroup) -> VisualState

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the System.Windows.VisualStateGroup.

Get: Name(self: VisualStateGroup) -> str

Set: Name(self: VisualStateGroup)=value
"""

 States=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of mutually exclusive System.Windows.VisualState objects.

Get: States(self: VisualStateGroup) -> IList

"""

 Transitions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.VisualTransition objects.

Get: Transitions(self: VisualStateGroup) -> IList

"""


 CurrentStateChanged=None
 CurrentStateChanging=None


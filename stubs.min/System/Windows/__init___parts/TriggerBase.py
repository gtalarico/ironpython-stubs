class TriggerBase(DependencyObject):
 """ Represents the base class for specifying a conditional value within a System.Windows.Style object. """
 EnterActions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.TriggerAction objects to apply when the trigger object becomes active. This property does not apply to the System.Windows.EventTrigger class.

Get: EnterActions(self: TriggerBase) -> TriggerActionCollection

"""

 ExitActions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.TriggerAction objects to apply when the trigger object becomes inactive. This property does not apply to the System.Windows.EventTrigger class.

Get: ExitActions(self: TriggerBase) -> TriggerActionCollection

"""



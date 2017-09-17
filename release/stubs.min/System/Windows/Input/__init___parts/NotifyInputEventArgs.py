class NotifyInputEventArgs(EventArgs):
 """ Provides data for raw input being processed by the System.Windows.Input.NotifyInputEventArgs.InputManager. """
 InputManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the input manager processing the input event.

Get: InputManager(self: NotifyInputEventArgs) -> InputManager

"""

 StagingItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the staging area input item being processed by the input manager.

Get: StagingItem(self: NotifyInputEventArgs) -> StagingAreaInputItem

"""



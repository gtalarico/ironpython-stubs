class TabbedDialogExtension(object):
 """
 Contains the information required to create and implement the behavior for the new tab inside 
 the Revit options dialog.
 
 TabbedDialogExtension(userControl: UserControl,onOK: TabbedDialogAction)
 """
 def GetContextualHelp(self):
  """
  GetContextualHelp(self: TabbedDialogExtension) -> ContextualHelp
  
   Gets the contextual help.
   Returns: The contextual help assigned to the help button of the Revit options dialog,or 
    ll if there is no binding assigned.
  """
  pass
 def SetContextualHelp(self,contextualHelp):
  """
  SetContextualHelp(self: TabbedDialogExtension,contextualHelp: ContextualHelp)
   Sets the contextual help.
  
   contextualHelp: The contextual help.
  """
  pass
 @staticmethod
 def __new__(self,userControl,onOK):
  """ __new__(cls: type,userControl: UserControl,onOK: TabbedDialogAction) """
  pass
 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The control.

Get: Control(self: TabbedDialogExtension) -> UserControl

"""

 OnCancelAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cancel handler.

Get: OnCancelAction(self: TabbedDialogExtension) -> TabbedDialogAction

Set: OnCancelAction(self: TabbedDialogExtension)=value
"""

 OnOKAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ok handler.

Get: OnOKAction(self: TabbedDialogExtension) -> TabbedDialogAction

"""

 OnRestoreDefaultsAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The restore defaults handler.

Get: OnRestoreDefaultsAction(self: TabbedDialogExtension) -> TabbedDialogAction

Set: OnRestoreDefaultsAction(self: TabbedDialogExtension)=value
"""



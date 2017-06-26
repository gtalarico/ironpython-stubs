class RibbonItemData(object):
 """ Base class used to contain information necessary to construct a RibbonItem in the Ribbon. """
 def GetContextualHelp(self):
  """
  GetContextualHelp(self: RibbonItemData) -> ContextualHelp
  
   Gets the contextual help bound with this control.
   Returns: The contextual help assigned to the item,or ll if there is no binding assigned.
  """
  pass
 def SetContextualHelp(self,contextualHelp):
  """
  SetContextualHelp(self: RibbonItemData,contextualHelp: ContextualHelp)
   Sets the contextual help bound with this button data.
  
   contextualHelp: The contextual help.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,name: str) """
  pass
 LongDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Long description of the command tooltip

Get: LongDescription(self: RibbonItemData) -> str

Set: LongDescription(self: RibbonItemData)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the item.

Get: Name(self: RibbonItemData) -> str

Set: Name(self: RibbonItemData)=value
"""

 ToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description that appears as a ToolTip for the item.

Get: ToolTip(self: RibbonItemData) -> str

Set: ToolTip(self: RibbonItemData)=value
"""

 ToolTipImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image to show as a part of the button extended tooltip

Get: ToolTipImage(self: RibbonItemData) -> ImageSource

Set: ToolTipImage(self: RibbonItemData)=value
"""



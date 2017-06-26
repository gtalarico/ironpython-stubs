class RibbonItem(object):
 """
 The RibbonItem object represents an item on RibbonPanel,can be a push-button or a pull-down 
 which should contain the information for creating one RibbonItem.
 """
 def Equals(self,obj):
  """
  Equals(self: RibbonItem,obj: object) -> bool
  
   Determines whether the specified System.Object is equal to the current 
    System.Object.
  
  
   obj: Another panel object.
  """
  pass
 def GetContextualHelp(self):
  """
  GetContextualHelp(self: RibbonItem) -> ContextualHelp
  
   Gets the contextual help bound with this control.
   Returns: The contextual help assigned to the item,or ll if there is no binding assigned.
  """
  pass
 def SetContextualHelp(self,contextualHelp):
  """
  SetContextualHelp(self: RibbonItem,contextualHelp: ContextualHelp)
   Sets the contextual help bound with this button.
  
   contextualHelp: The contextual help.
  """
  pass
 def setItemText(self,*args):
  """ setItemText(self: RibbonItem,text: str) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is enabled.

Get: Enabled(self: RibbonItem) -> bool

Set: Enabled(self: RibbonItem)=value
"""

 ItemText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text displayed on the item.

Get: ItemText(self: RibbonItem) -> str

Set: ItemText(self: RibbonItem)=value
"""

 ItemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item type.

Get: ItemType(self: RibbonItem) -> RibbonItemType

"""

 LongDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Long description of the command tooltip

Get: LongDescription(self: RibbonItem) -> str

Set: LongDescription(self: RibbonItem)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the item.

Get: Name(self: RibbonItem) -> str

"""

 ToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description that appears as a ToolTip for the item.

Get: ToolTip(self: RibbonItem) -> str

Set: ToolTip(self: RibbonItem)=value
"""

 ToolTipImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image to show as a part of the button extended tooltip

Get: ToolTipImage(self: RibbonItem) -> ImageSource

Set: ToolTipImage(self: RibbonItem)=value
"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is visible.

Get: Visible(self: RibbonItem) -> bool

Set: Visible(self: RibbonItem)=value
"""


 m_ItemType=None


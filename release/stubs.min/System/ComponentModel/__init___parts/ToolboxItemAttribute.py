class ToolboxItemAttribute(Attribute,_Attribute):
 """
 Represents an attribute of a toolbox item.

 

 ToolboxItemAttribute(defaultType: bool)

 ToolboxItemAttribute(toolboxItemTypeName: str)

 ToolboxItemAttribute(toolboxItemType: Type)
 """
 def Equals(self,obj):
  """
  Equals(self: ToolboxItemAttribute,obj: object) -> bool

  

   obj: The object to compare.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: ToolboxItemAttribute) -> int """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ToolboxItemAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,defaultType: bool)

  __new__(cls: type,toolboxItemTypeName: str)

  __new__(cls: type,toolboxItemType: Type)
  """
  pass
 def __ne__(self,*args):
  pass
 ToolboxItemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of the toolbox item.



Get: ToolboxItemType(self: ToolboxItemAttribute) -> Type



"""

 ToolboxItemTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the type of the current System.Drawing.Design.ToolboxItem.



Get: ToolboxItemTypeName(self: ToolboxItemAttribute) -> str



"""


 Default=None
 None=None


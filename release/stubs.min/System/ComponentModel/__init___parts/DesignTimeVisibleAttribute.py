class DesignTimeVisibleAttribute(Attribute,_Attribute):
 """
 System.ComponentModel.DesignTimeVisibleAttribute marks a component's visibility. If System.ComponentModel.DesignTimeVisibleAttribute.Yes is present,a visual designer can show this component on a designer.

 

 DesignTimeVisibleAttribute(visible: bool)

 DesignTimeVisibleAttribute()
 """
 def Equals(self,obj):
  """
  Equals(self: DesignTimeVisibleAttribute,obj: object) -> bool

  

   obj: The object to compare.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DesignTimeVisibleAttribute) -> int """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DesignTimeVisibleAttribute) -> bool

  

   Gets a value indicating if this instance is equal to the 

    System.ComponentModel.DesignTimeVisibleAttribute.Default value.

  

   Returns: true,if this instance is equal to the System.ComponentModel.DesignTimeVisibleAttribute.Default 

    value; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,visible=None):
  """
  __new__(cls: type,visible: bool)

  __new__(cls: type)
  """
  pass
 def __ne__(self,*args):
  pass
 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the component should be shown at design time.



Get: Visible(self: DesignTimeVisibleAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None


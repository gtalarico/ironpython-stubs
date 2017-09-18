class DockingAttribute(Attribute,_Attribute):
 """
 Specifies the default docking behavior for a control.

 

 DockingAttribute()

 DockingAttribute(dockingBehavior: DockingBehavior)
 """
 def Equals(self,obj):
  """
  Equals(self: DockingAttribute,obj: object) -> bool

  

   Compares an arbitrary object with the System.Windows.Forms.DockingAttribute object for equality.

  

   obj: The System.Object against which to compare this System.Windows.Forms.DockingAttribute.

   Returns: true is obj is equal to this System.Windows.Forms.DockingAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DockingAttribute) -> int

  

   The hash code for this object.

   Returns: An System.Int32 representing an in-memory hash of this object.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DockingAttribute) -> bool

  

   Specifies whether this System.Windows.Forms.DockingAttribute is the default docking attribute.

   Returns: true is the current System.Windows.Forms.DockingAttribute is the default; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dockingBehavior=None):
  """
  __new__(cls: type)

  __new__(cls: type,dockingBehavior: DockingBehavior)
  """
  pass
 def __ne__(self,*args):
  pass
 DockingBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the docking behavior supplied to this attribute.



Get: DockingBehavior(self: DockingAttribute) -> DockingBehavior



"""


 Default=None


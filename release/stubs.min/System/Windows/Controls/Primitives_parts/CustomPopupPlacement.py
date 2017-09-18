class CustomPopupPlacement(object):
 """
 Defines custom placement parameters for a System.Windows.Controls.Primitives.Popup control.

 

 CustomPopupPlacement(point: Point,primaryAxis: PopupPrimaryAxis)
 """
 def Equals(self,o):
  """
  Equals(self: CustomPopupPlacement,o: object) -> bool

  

   Compares this structure with another System.Windows.Controls.Primitives.CustomPopupPlacement 

    structure to determine whether they are equal.

  

  

   o: The System.Windows.Controls.Primitives.CustomPopupPlacement structure to compare.

   Returns: true if the structures have the same values; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CustomPopupPlacement) -> int

  

   Gets the hash code for this structure.

   Returns: The hash code for this structure.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,point,primaryAxis):
  """
  __new__(cls: type,point: Point,primaryAxis: PopupPrimaryAxis)

  __new__[CustomPopupPlacement]() -> CustomPopupPlacement
  """
  pass
 def __ne__(self,*args):
  pass
 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the point that is relative to the target object where the upper-left corner of the System.Windows.Controls.Primitives.Popup control is placedl.



Get: Point(self: CustomPopupPlacement) -> Point



Set: Point(self: CustomPopupPlacement)=value

"""

 PrimaryAxis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the direction in which to move a System.Windows.Controls.Primitives.Popup control when the System.Windows.Controls.Primitives.Popup is obscured by screen boundaries.



Get: PrimaryAxis(self: CustomPopupPlacement) -> PopupPrimaryAxis



Set: PrimaryAxis(self: CustomPopupPlacement)=value

"""



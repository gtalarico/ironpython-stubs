class ManipulationPivot(object):
 """
 Specifies how a rotation occurs with one point of user input.
 
 ManipulationPivot()
 ManipulationPivot(center: Point,radius: float)
 """
 @staticmethod
 def __new__(self,center=None,radius=None):
  """
  __new__(cls: type)
  __new__(cls: type,center: Point,radius: float)
  """
  pass
 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the center of a single-point manipulation.

Get: Center(self: ManipulationPivot) -> Point

Set: Center(self: ManipulationPivot)=value
"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the area around the pivot that is used to determine how much rotation and translation occurs when a single point of contact initiates the manipulation.

Get: Radius(self: ManipulationPivot) -> float

Set: Radius(self: ManipulationPivot)=value
"""



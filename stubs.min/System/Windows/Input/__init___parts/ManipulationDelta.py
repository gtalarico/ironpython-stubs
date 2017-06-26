class ManipulationDelta(object):
 """
 Contains transformation data that is accumulated when manipulation events occur.
 
 ManipulationDelta(translation: Vector,rotation: float,scale: Vector,expansion: Vector)
 """
 @staticmethod
 def __new__(self,translation,rotation,scale,expansion):
  """ __new__(cls: type,translation: Vector,rotation: float,scale: Vector,expansion: Vector) """
  pass
 Expansion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the amount the manipulation has resized in device-independent units (1/96th inch per unit).

Get: Expansion(self: ManipulationDelta) -> Vector

"""

 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rotation of the manipulation in degrees.

Get: Rotation(self: ManipulationDelta) -> float

"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the amount the manipulation has resized as a multiplier.

Get: Scale(self: ManipulationDelta) -> Vector

"""

 Translation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the linear motion of the manipulation.

Get: Translation(self: ManipulationDelta) -> Vector

"""



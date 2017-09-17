class ManipulationVelocities(object):
 """
 Describes the speed at which manipulations occurs.
 
 ManipulationVelocities(linearVelocity: Vector,angularVelocity: float,expansionVelocity: Vector)
 """
 @staticmethod
 def __new__(self,linearVelocity,angularVelocity,expansionVelocity):
  """ __new__(cls: type,linearVelocity: Vector,angularVelocity: float,expansionVelocity: Vector) """
  pass
 AngularVelocity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the speed of rotation.

Get: AngularVelocity(self: ManipulationVelocities) -> float

"""

 ExpansionVelocity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rate at which the manipulation is resized.

Get: ExpansionVelocity(self: ManipulationVelocities) -> Vector

"""

 LinearVelocity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the speed of linear motion.

Get: LinearVelocity(self: ManipulationVelocities) -> Vector

"""



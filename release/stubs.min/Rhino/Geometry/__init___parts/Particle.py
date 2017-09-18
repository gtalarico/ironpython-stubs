class Particle(object):
 """
 Represents a simple particle.

    This base class only defines position and display properties (size,color,bitmap id).

    You will most likely create a class that derives from this particle class to perform some

    sort of physical simulation (movement over time or frames).

 

 Particle()
 """
 def Update(self):
  """
  Update(self: Particle)

   Base class implementation does nothing.
  """
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Color(self: Particle) -> Color



Set: Color(self: Particle)=value

"""

 DisplayBitmapIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisplayBitmapIndex(self: Particle) -> int



Set: DisplayBitmapIndex(self: Particle)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index in ParentSystem for this Particle. Can change when the particle

   system is modified.



Get: Index(self: Particle) -> int



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """3d Location of the Particle.



Get: Location(self: Particle) -> Point3d



Set: Location(self: Particle)=value

"""

 ParentSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent particle system of this particle.



Get: ParentSystem(self: Particle) -> ParticleSystem



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Size(self: Particle) -> Single



Set: Size(self: Particle)=value

"""



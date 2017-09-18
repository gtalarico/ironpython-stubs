class ParticleSystem(object,IEnumerable[Particle],IEnumerable):
 """ ParticleSystem() """
 def Add(self,particle):
  """
  Add(self: ParticleSystem,particle: Particle) -> bool

  

   Adds a particle to this ParticleSystem. A Particle can only be in one system

     at a 

    time.  If the Particle already exists in a different system,this function

     will 

    return false. You should remove the particle from the other system first

     before 

    adding it.

  

  

   particle: A particle to be added.

   Returns: true if this particle was added to the system or if is already in the system.

     false 

    if the particle already exists in a different system.
  """
  pass
 def Clear(self):
  """
  Clear(self: ParticleSystem)

   Remove all Particles from this system.
  """
  pass
 def GetEnumerator(self):
  """ GetEnumerator(self: ParticleSystem) -> IEnumerator[Particle] """
  pass
 def Remove(self,particle):
  """
  Remove(self: ParticleSystem,particle: Particle)

   Removes a single particle from this system.

  

   particle: The particle to be removed.
  """
  pass
 def Update(self):
  """
  Update(self: ParticleSystem)

   Calls Update on every particle in the system.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[Particle](enumerable: IEnumerable[Particle],value: Particle) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BoundingBox(self: ParticleSystem) -> BoundingBox



"""

 DisplaySizesInWorldUnits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisplaySizesInWorldUnits(self: ParticleSystem) -> bool



Set: DisplaySizesInWorldUnits(self: ParticleSystem)=value

"""

 DrawRequiresDepthSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DrawRequiresDepthSorting(self: ParticleSystem) -> bool



Set: DrawRequiresDepthSorting(self: ParticleSystem)=value

"""



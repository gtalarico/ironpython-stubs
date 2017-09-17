class ConicalSurface(Surface,IDisposable):
 """ A Conical Surface. """
 @staticmethod
 def Create(frameOfReference,halfAngle):
  """
  Create(frameOfReference: Frame,halfAngle: float) -> ConicalSurface
  
   Creates a conical surface defined by a local reference frame and a half angle.
  
   frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 
    for the cone.
     Frame.Origin is a point on the cylinder's axis.Frame.BasisZ 
    points along the axis,while Frame.BasisX and Frame.BasisY are orthogonal to 
    the axis. The frame may be either left-handed or right-handed (see 
    Frame.IsRightHanded). Note that
     the "handedness" of the frame does not,by 
    itself,determine the surface's orientation.
  
   halfAngle: Cone angle. Must be not 0,lesser than PI/2 and greater than -PI/2.
   Returns: The created ConicalSurface.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Surface,A_0: bool) """
  pass
 def GetFrameOfReference(self):
  """
  GetFrameOfReference(self: ConicalSurface) -> Frame
  
   Returns frame of reference associated with this ConicalSurface.
   Returns: Frame of reference associated with this ConicalSurface.
  """
  pass
 @staticmethod
 def IsValidConeAngle(halfAngle):
  """
  IsValidConeAngle(halfAngle: float) -> bool
  
   Checks whether the input value lies is not 0,greater than -PI/2 and lesser 
    than PI/2.
  
  
   halfAngle: Cone half-angle parameter.
   Returns: True if input is not 0,lesser than PI/2 and greater than -PI/2,false 
    otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Surface,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Axis of the cone. This is the Z axis of the local coordinate system associated with this cone.

Get: Axis(self: ConicalSurface) -> XYZ

"""

 HalfAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cone angle.

Get: HalfAngle(self: ConicalSurface) -> float

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Apex of the cone. This is the origin of the local coordinate system associated with this cone.

Get: Origin(self: ConicalSurface) -> XYZ

"""

 XDir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """X axis of the local coordinate system associated with this cone.

Get: XDir(self: ConicalSurface) -> XYZ

"""

 YDir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """X axis of the local coordinate system associated with this cone.

Get: YDir(self: ConicalSurface) -> XYZ

"""



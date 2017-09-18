class ProjectPosition(APIObject,IDisposable):
 """
 An object that is used to represent a geographical offset and rotation.

 

 ProjectPosition(ew: float,ns: float,elevation: float,angle: float)
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 @staticmethod
 def __new__(self,ew,ns,elevation,angle):
  """ __new__(cls: type,ew: float,ns: float,elevation: float,angle: float) """
  pass
 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Angle from True North



Get: Angle(self: ProjectPosition) -> float



Set: Angle(self: ProjectPosition)=value

"""

 EastWest=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """East/West offset



Get: EastWest(self: ProjectPosition) -> float



Set: EastWest(self: ProjectPosition)=value

"""

 Elevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Elevation above ground level.



Get: Elevation(self: ProjectPosition) -> float



Set: Elevation(self: ProjectPosition)=value

"""

 NorthSouth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """North/South offset



Get: NorthSouth(self: ProjectPosition) -> float



Set: NorthSouth(self: ProjectPosition)=value

"""



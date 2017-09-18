class WallSweepInfo(object,IDisposable):
 """
 Represents a wall sweep or reveal of a vertically compound structure.

 

 WallSweepInfo(type: WallSweepType,vertical: bool)

 WallSweepInfo(fixed: bool,type: WallSweepType)
 """
 def Dispose(self):
  """ Dispose(self: WallSweepInfo) """
  pass
 def IsEqual(self,toCompare):
  """
  IsEqual(self: WallSweepInfo,toCompare: WallSweepInfo) -> bool

  

   Determines if the input object is equivalent to this WallSweepInfo.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WallSweepInfo,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,type: WallSweepType,vertical: bool)

  __new__(cls: type,fixed: bool,type: WallSweepType)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CutsWall=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if you want the sweep to cut geometry out of the host wall.



Get: CutsWall(self: WallSweepInfo) -> bool



Set: CutsWall(self: WallSweepInfo)=value

"""

 DefaultSetback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sweep setback distance from inserts,such as windows and doors.



Get: DefaultSetback(self: WallSweepInfo) -> float



Set: DefaultSetback(self: WallSweepInfo)=value

"""

 Distance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance from either the top or base of the wall.



Get: Distance(self: WallSweepInfo) -> float



Set: Distance(self: WallSweepInfo)=value

"""

 DistanceMeasuredFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if Distance is measured from the top or bottom of the wall.



Get: DistanceMeasuredFrom(self: WallSweepInfo) -> DistanceMeasuredFrom



Set: DistanceMeasuredFrom(self: WallSweepInfo)=value

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the sweep or reveal.



Get: Id(self: WallSweepInfo) -> int



Set: Id(self: WallSweepInfo)=value

"""

 IsCutByInserts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the sweep is cut by wall inserts.



Get: IsCutByInserts(self: WallSweepInfo) -> bool



Set: IsCutByInserts(self: WallSweepInfo)=value

"""

 IsFixed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the described wall sweep is fixed.  A sweep is fixed if it is a part of a vertical compound structure.



Get: IsFixed(self: WallSweepInfo) -> bool



"""

 IsProfileFlipped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the profile is applied upside-down.



Get: IsProfileFlipped(self: WallSweepInfo) -> bool



Set: IsProfileFlipped(self: WallSweepInfo)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: WallSweepInfo) -> bool



"""

 IsVertical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the sweep or reveal is swept vertically or horizontally.



Get: IsVertical(self: WallSweepInfo) -> bool



"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the material used to create the sweep or reveal.



Get: MaterialId(self: WallSweepInfo) -> ElementId



Set: MaterialId(self: WallSweepInfo)=value

"""

 ProfileId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the profile family used to create the sweep or reveal.



Get: ProfileId(self: WallSweepInfo) -> ElementId



Set: ProfileId(self: WallSweepInfo)=value

"""

 WallOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset from the sweep or reveal to the wall.



Get: WallOffset(self: WallSweepInfo) -> float



Set: WallOffset(self: WallSweepInfo)=value

"""

 WallSide=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The side of the wall to which the sweep or reveal is attached.



Get: WallSide(self: WallSweepInfo) -> WallSide



Set: WallSide(self: WallSweepInfo)=value

"""

 WallSweepType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type (either a wall sweep or a reveal).



Get: WallSweepType(self: WallSweepInfo) -> WallSweepType



Set: WallSweepType(self: WallSweepInfo)=value

"""



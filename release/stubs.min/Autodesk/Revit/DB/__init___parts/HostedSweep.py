class HostedSweep(HostObject,IDisposable):
 """ An object that represents an object hosted by an edge of a roof or floor within the Autodesk Revit project. """
 def AddSegment(self,targetRef):
  """
  AddSegment(self: HostedSweep,targetRef: Reference)

   Add segments to the hosted sweep object.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetEndPointParameter(self,targetRef,endIdx):
  """
  GetEndPointParameter(self: HostedSweep,targetRef: Reference,endIdx: int) -> float

  

   Retrieve segment's start point or end point parameter.

  

   targetRef: Segment's reference whose parameter want to be get.

   endIdx: Start point (=0) or end point (=1).

   Returns: Start point or end point parameter.
  """
  pass
 def HorizontalFlip(self):
  """
  HorizontalFlip(self: HostedSweep)

   Flip the hosted sweep object along horizontal line.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveSegment(self,targetRef):
  """
  RemoveSegment(self: HostedSweep,targetRef: Reference)

   Remove segments from the  hosted sweep object.

  

   targetRef: Segment's reference which want to be removed.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetEndPointParameter(self,targetRef,endIdx,param):
  """
  SetEndPointParameter(self: HostedSweep,targetRef: Reference,endIdx: int,param: float) -> bool

  

   Set segment's start point or end point parameter.

  

   targetRef: Segment's reference whose parameter want to be set.

   endIdx: Start point (=0) or end point (=1).

   param: Value of parameter.

   Returns: true if operation success.
  """
  pass
 def VerticalFlip(self):
  """
  VerticalFlip(self: HostedSweep)

   Flip the hosted sweep object along vertical line.
  """
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
 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve/set the angle of the  hosted sweep object relative its references (Unit : Radian).



Get: Angle(self: HostedSweep) -> float



Set: Angle(self: HostedSweep)=value

"""

 HorizontalFlipped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the horizontal flip status of the hosted sweep object.



Get: HorizontalFlipped(self: HostedSweep) -> bool



"""

 HorizontalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve/set the horizontal offset of the hosted sweep object.



Get: HorizontalOffset(self: HostedSweep) -> float



Set: HorizontalOffset(self: HostedSweep)=value

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the length of the hosted sweep object.



Get: Length(self: HostedSweep) -> float



"""

 VerticalFlipped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the vertical flip status of the hosted sweep object.



Get: VerticalFlipped(self: HostedSweep) -> bool



"""

 VerticalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve/set the vertical offset of the hosted sweep object.



Get: VerticalOffset(self: HostedSweep) -> float



Set: VerticalOffset(self: HostedSweep)=value

"""



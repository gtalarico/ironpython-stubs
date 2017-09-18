class HomeCamera(object,IDisposable):
 """
 A structure that contains information about the camera and view for the Home view orientation stored in the model.

 

 HomeCamera(other: HomeCamera)
 """
 def Dispose(self):
  """ Dispose(self: HomeCamera) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: HomeCamera,disposing: bool) """
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
 def __new__(self,other):
  """ __new__(cls: type,other: HomeCamera) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BottomAngleOfFieldOfView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom angle of the field of view.



Get: BottomAngleOfFieldOfView(self: HomeCamera) -> float



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The zoom or orbit center.



Get: Center(self: HomeCamera) -> XYZ



"""

 EyePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The eye position point.



Get: EyePosition(self: HomeCamera) -> XYZ



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: HomeCamera) -> bool



"""

 LeftAngleOfFieldOfView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The left angle of the field of view.



Get: LeftAngleOfFieldOfView(self: HomeCamera) -> float



"""

 OrthogonalProjectionHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height of orthogonal projection view volume.



Get: OrthogonalProjectionHeight(self: HomeCamera) -> float



"""

 OrthogonalProjectionWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of orthogonal projection view volume.



Get: OrthogonalProjectionWidth(self: HomeCamera) -> float



"""

 Pivot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pivot point.



Get: Pivot(self: HomeCamera) -> XYZ



"""

 RightAngleOfFieldOfView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The right angle of the field of view.



Get: RightAngleOfFieldOfView(self: HomeCamera) -> float



"""

 TopAngleOfFieldOfView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top angle of the field of view.



Get: TopAngleOfFieldOfView(self: HomeCamera) -> float



"""

 UpDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The up direction vector.



Get: UpDirection(self: HomeCamera) -> XYZ



"""

 ViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the view which is associated to this document's Home view orientation.



Get: ViewId(self: HomeCamera) -> ElementId



"""



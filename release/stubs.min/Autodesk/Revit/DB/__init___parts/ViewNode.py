class ViewNode(RenderNode,IDisposable):
 """ A render node that represents a view. """
 def Dispose(self):
  """ Dispose(self: RenderNode,A_0: bool) """
  pass
 def GetCameraInfo(self):
  """
  GetCameraInfo(self: ViewNode) -> CameraInfo

  

   Information about the observation point (the camera) of the view.

   Returns: An instance of CameraInfo or ll if there is no info associated with the view
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RenderNode,disposing: bool) """
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
 LevelOfDetail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The level of detail the view is going to be rendered at.



Get: LevelOfDetail(self: ViewNode) -> int



Set: LevelOfDetail(self: ViewNode)=value

"""

 ViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the view element.



Get: ViewId(self: ViewNode) -> ElementId



"""



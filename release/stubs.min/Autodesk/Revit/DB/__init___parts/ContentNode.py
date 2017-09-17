class ContentNode(RenderNode,IDisposable):
 """ This is a class representing a generic content node in a model-exporting process. """
 def Dispose(self):
  """ Dispose(self: RenderNode,A_0: bool) """
  pass
 def GetAsset(self):
  """
  GetAsset(self: ContentNode) -> Asset
  
   Returns an an instance of an Asset object,which contains definitions of the 
    content node.
  """
  pass
 def GetTransform(self):
  """
  GetTransform(self: ContentNode) -> Transform
  
   A transformation matrix associated with the node.
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

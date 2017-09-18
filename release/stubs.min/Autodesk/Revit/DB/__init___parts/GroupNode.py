class GroupNode(RenderNode,IDisposable):
 """
 A node that represents set of individual elements grouped together

    in some form,such as an instance of a family or linked Revit file.
 """
 def Dispose(self):
  """ Dispose(self: RenderNode,A_0: bool) """
  pass
 def GetSymbolId(self):
  """
  GetSymbolId(self: GroupNode) -> ElementId

  

   The Id of the symbol associated with the node.
  """
  pass
 def GetTransform(self):
  """
  GetTransform(self: GroupNode) -> Transform

  

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

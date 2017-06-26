class ExclusionFilter(ElementQuickFilter,IDisposable):
 """
 A filter used to exclude a set of elements automatically.
 
 ExclusionFilter(idsToExclude: ICollection[ElementId])
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def GetIdsToExclude(self):
  """
  GetIdsToExclude(self: ExclusionFilter) -> ICollection[ElementId]
  
   Returns the ids to be excluded by this filter.
   Returns: The collection of ids to exclude.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementFilter,disposing: bool) """
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
 def __new__(self,idsToExclude):
  """ __new__(cls: type,idsToExclude: ICollection[ElementId]) """
  pass

class RevitLinkLoadResult(object,IDisposable):
 """
 This class stores the results of trying to load a single linked model.
 
 RevitLinkLoadResult(other: RevitLinkLoadResult)
 """
 def Dispose(self):
  """ Dispose(self: RevitLinkLoadResult) """
  pass
 def GetCentralModelName(self):
  """
  GetCentralModelName(self: RevitLinkLoadResult) -> ModelPath
  
   Gets the central model's name.
     If the link is not workshared,this returns 
    an empty FilePath.
     If the link is itself a central model,this returns the 
    link's name.
  """
  pass
 def GetExternalResourceReference(self):
  """
  GetExternalResourceReference(self: RevitLinkLoadResult) -> ExternalResourceReference
  
   Gets a copy of the ExternalResourceReference corresponding
     to the link.
   Returns: A copy of the ExternalResourceReference corresponding
     to the link.
  """
  pass
 def GetExternalResourceReferencesFromFailedLoads(self):
  """
  GetExternalResourceReferencesFromFailedLoads(self: RevitLinkLoadResult) -> IList[ExternalResourceReference]
  
   Searches this and all nested LinkLoadResults,and returns a list
     of 
    ExternalResourceReferences for the links that failed to load.
  
   Returns: A collection of link ExternalResourceReferences which failed to load.
  """
  pass
 def GetLinkLoadResult(self,matchExtResRef):
  """
  GetLinkLoadResult(self: RevitLinkLoadResult,matchExtResRef: ExternalResourceReference) -> RevitLinkLoadResult
  
   Searches this LinkLoadResult and all nested LinkLoadResults for the
     load 
    operation results of a specified ExternalResourceReference.
  
  
   matchExtResRef: An ExternalResourceReference whose LinkLoadResults are contained in this object.
   Returns: A LinkLoadResult object with the load results for the specified 
    ExternalResourceReference.
  """
  pass
 def GetModelName(self):
  """
  GetModelName(self: RevitLinkLoadResult) -> ModelPath
  
   Gets the name of the model.
  """
  pass
 def GetNestedLinkLoadResults(self):
  """
  GetNestedLinkLoadResults(self: RevitLinkLoadResult) -> IDictionary[str,RevitLinkLoadResult]
  
   Gets the results for this link's nested links.
   Returns: A map from nested link paths to the load results for
     that nested link.For 
    links from external servers,the "path" will be
     the display name of the 
    link.
  """
  pass
 def GetParentModelName(self):
  """
  GetParentModelName(self: RevitLinkLoadResult) -> ModelPath
  
   Returns the name of the parent of the linked model,or an empty FilePath
     if 
    the link is a top-level link.
  """
  pass
 @staticmethod
 def IsCodeSuccess(code):
  """
  IsCodeSuccess(code: RevitLinkLoadResultType) -> bool
  
   Check if load result code signifies success.
  
   code: Load result code to be verified.
   Returns: True if LinkLoadResultType argument is success,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RevitLinkLoadResult,disposing: bool) """
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
  """ __new__(cls: type,other: RevitLinkLoadResult) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the created or loaded linked model.

Get: ElementId(self: RevitLinkLoadResult) -> ElementId

"""

 IsCircularLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if these results are part of a link cycle.

Get: IsCircularLink(self: RevitLinkLoadResult) -> bool

"""

 IsNested=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if these results represent a nested link; false otherwise.

Get: IsNested(self: RevitLinkLoadResult) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RevitLinkLoadResult) -> bool

"""

 LoadResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Holds the results of creating or loading a link. Results can be LinkLoadResultType.LinkLoaded
   for success,or a variety of errors. See LinkLoadResultType for the full list.

Get: LoadResult(self: RevitLinkLoadResult) -> RevitLinkLoadResultType

"""



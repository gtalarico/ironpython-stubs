class LoadCombination(Element,IDisposable):
 """ An object that represents a load combination. """
 @staticmethod
 def Create(document,name,type=None,state=None):
  """
  Create(document: Document,name: str) -> LoadCombination
  
   Creates a new default LoadCombination.
  
   document: The Document to which new load combination element will be added.
   name: The name of the load combination.
   Returns: The newly created load combination element if successful,ll otherwise.
  Create(document: Document,name: str,type: LoadCombinationType,state: LoadCombinationState) -> LoadCombination
  
   Creates a new LoadCombination.
  
   document: The Document to which new load combination element will be added.
   name: The name of the load combination.
   type: The type of the load combination.
   state: The state of the load combination.
   Returns: The newly created load combination element if successful,ll otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCaseAndCombinationIds(self):
  """
  GetCaseAndCombinationIds(self: LoadCombination) -> IList[ElementId]
  
   Returns collection of the load combination case and combination IDs.
   Returns: A collection of the load combination case and combination IDs.
  """
  pass
 def GetComponents(self):
  """
  GetComponents(self: LoadCombination) -> IList[LoadComponent]
  
   Returns collection of the load combination components.
   Returns: A collection of the load combination components.
  """
  pass
 def GetUsageIds(self):
  """
  GetUsageIds(self: LoadCombination) -> IList[ElementId]
  
   Returns collection of the load combination usage IDs.
   Returns: A collection of the load combination usage IDs.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetComponents(self,components):
  """ SetComponents(self: LoadCombination,components: IList[LoadComponent]) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetUsageIds(self,usageIds):
  """ SetUsageIds(self: LoadCombination,usageIds: IList[ElementId]) """
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
 IsThirdPartyGenerated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the load combination was created by API.

Get: IsThirdPartyGenerated(self: LoadCombination) -> bool

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The state of the load combination.

Get: State(self: LoadCombination) -> LoadCombinationState

Set: State(self: LoadCombination)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the load combination.

Get: Type(self: LoadCombination) -> LoadCombinationType

Set: Type(self: LoadCombination)=value
"""



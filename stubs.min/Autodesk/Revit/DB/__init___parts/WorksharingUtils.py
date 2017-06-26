class WorksharingUtils(object,IDisposable):
 """ A static class that contains utility functions related to worksharing. """
 @staticmethod
 def CheckoutElements(document,elementsToCheckout,options=None):
  """
  CheckoutElements(document: Document,elementsToCheckout: ICollection[ElementId]) -> ICollection[ElementId]
  CheckoutElements(document: Document,elementsToCheckout: ISet[ElementId],options: TransactWithCentralOptions) -> ISet[ElementId]
  """
  pass
 @staticmethod
 def CheckoutWorksets(document,worksetsToCheckout,options=None):
  """
  CheckoutWorksets(document: Document,worksetsToCheckout: ICollection[WorksetId]) -> ICollection[WorksetId]
  CheckoutWorksets(document: Document,worksetsToCheckout: ISet[WorksetId],options: TransactWithCentralOptions) -> ISet[WorksetId]
  """
  pass
 @staticmethod
 def CreateNewLocal(sourcePath,targetPath):
  """
  CreateNewLocal(sourcePath: ModelPath,targetPath: ModelPath)
   Takes a path to a central model and copies the model into a new local file for 
    the current user.
  
  
   sourcePath: The path to the central model.
   targetPath: The path to put the new local file.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WorksharingUtils) """
  pass
 @staticmethod
 def GetCheckoutStatus(document,elementId,owner=None):
  """
  GetCheckoutStatus(document: Document,elementId: ElementId) -> (CheckoutStatus,str)
  
   Gets the ownership status and outputs the owner of an element.
  
   document: The document containing the element.
   elementId: The id of the element.
   Returns: An indication of whether the element is unowned,owned by the current user,or 
    owned by another user.
  
  GetCheckoutStatus(document: Document,elementId: ElementId) -> CheckoutStatus
  
   Gets the ownership status of an element.
  
   document: The document containing the element.
   elementId: The id of the element.
   Returns: A summary of whether the element is unowned,owned by the current user,or 
    owned by another user.
  """
  pass
 @staticmethod
 def GetModelUpdatesStatus(document,elementId):
  """
  GetModelUpdatesStatus(document: Document,elementId: ElementId) -> ModelUpdatesStatus
  
   Gets the status of a single element in the central model.
  
   document: The document containing the element.
   elementId: The id of the element.
   Returns: The status of the element in the local session versus the central model.
  """
  pass
 @staticmethod
 def GetUserWorksetInfo(path):
  """
  GetUserWorksetInfo(path: ModelPath) -> IList[WorksetPreview]
  
   Gets information about user worksets in a workshared model file,without fully 
    opening the file.
  
  
   path: The path to the workshared model.
   Returns: Information about all the user worksets in the model.
     The list is sorted by 
    workset id.
  """
  pass
 @staticmethod
 def GetWorksharingTooltipInfo(document,elementId):
  """
  GetWorksharingTooltipInfo(document: Document,elementId: ElementId) -> WorksharingTooltipInfo
  
   Gets worksharing information about an element to display in an in-canvas 
    tooltip.
  
  
   document: The document containing the element
   elementId: The id of the element in question
   Returns: Worksharing information about the specified element.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WorksharingUtils,disposing: bool) """
  pass
 @staticmethod
 def RelinquishOwnership(document,generalCategories,options):
  """
  RelinquishOwnership(document: Document,generalCategories: RelinquishOptions,options: TransactWithCentralOptions) -> RelinquishedItems
  
   Relinquishes ownership by the current user of as many specified elements and 
    worksets as possible,
     and grants element ownership requested by other users 
    on a first-come,first-served basis.
  
  
   document: The document containing the elements and worksets.
   generalCategories: General categories of items to relinquish.  See RelinquishOptions for details.
   options: Options to customize access to the central model.
     ll is allowed and means 
    no customization.
  
   Returns: The elements and worksets that were relinquished.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksharingUtils) -> bool

"""



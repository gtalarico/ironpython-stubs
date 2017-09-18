class BrowserOrganization(ElementType,IDisposable):
 """ The organization settings for grouping,sorting,and filtering of items in the project browser. """
 def AreFiltersSatisfied(self,elementId):
  """
  AreFiltersSatisfied(self: BrowserOrganization,elementId: ElementId) -> bool

  

   Determines if the given element satisfies the filters defined by the browser 

    organization.

  

  

   elementId: The element to check.

   Returns: True if the given element satisfies the filter.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetCurrentBrowserOrganizationForSheets(document):
  """
  GetCurrentBrowserOrganizationForSheets(document: Document) -> BrowserOrganization

  

   Gets the Autodesk.Revit.DB.BrowserOrganization that applies to the Sheets 

    section of the project browser.

  

  

   document: Revit document from which to get the organization data.

   Returns: The BrowserOrganization for sheets,or null if no sheets exist.
  """
  pass
 @staticmethod
 def GetCurrentBrowserOrganizationForViews(document):
  """
  GetCurrentBrowserOrganizationForViews(document: Document) -> BrowserOrganization

  

   Gets the Autodesk.Revit.DB.BrowserOrganization  that applies to the Views 

    section of the project browser.

  

  

   document: Revit document from which to get the organization data.

   Returns: The BrowserOrganization for views,or null if no view sections exist
  """
  pass
 def GetFolderItems(self,elementId):
  """
  GetFolderItems(self: BrowserOrganization,elementId: ElementId) -> IList[FolderItemInfo]

  

   Returns a collection of leaf Autodesk.Revit.DB.FolderItemInfo objects each 

    containing the given element Id.

  

  

   elementId: Element id located at a leaf position in the project browser.

   Returns: An array of FolderItemInfo objects.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 SortingOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sorting order if sorting of items is applicable in the browser.



Get: SortingOrder(self: BrowserOrganization) -> SortingOrder



"""

 SortingParameterId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the parameter used to determine the sorting order of items in the browser.



Get: SortingParameterId(self: BrowserOrganization) -> ElementId



"""



class PhaseFilter(Element,IDisposable):
 """ Represents an phase filter within Autodesk Revit. """
 @staticmethod
 def Create(document,name):
  """
  Create(document: Document,name: str) -> PhaseFilter
  
   Creates a new phase filter with default status presentation.
  
   document: The document.
   name: The name.
   Returns: The newly created phase filter.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPhaseStatusPresentation(self,status):
  """
  GetPhaseStatusPresentation(self: PhaseFilter,status: ElementOnPhaseStatus) -> PhaseStatusPresentation
  
   Gets the phase status presentation.
  
   status: The element phase status.
   Returns: The phase status presentation.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetPhaseStatusPresentation(self,status,presentation):
  """
  SetPhaseStatusPresentation(self: PhaseFilter,status: ElementOnPhaseStatus,presentation: PhaseStatusPresentation)
   Sets the phase status presentation.
  
   status: The element phase status.
   presentation: The phase status presentation.
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
 IsDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this filter is the default one.

Get: IsDefault(self: PhaseFilter) -> bool

"""



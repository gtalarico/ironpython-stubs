class AngularDimension(Dimension,IDisposable):
 """ An object that represents an Angular Dimension within the Revit project. """
 @staticmethod
 def Create(document,dbView,arc,references,dimensionStyle):
  """ Create(document: Document,dbView: View,arc: Arc,references: IList[Reference],dimensionStyle: DimensionType) -> AngularDimension """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetRadius(self,radius):
  """
  SetRadius(self: AngularDimension,radius: float)

   Set radius of an Angular Dimension arc.

     The new radius of the arc.
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

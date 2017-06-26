class MultiReferenceAnnotation(Element,IDisposable):
 """ Multi-reference annotations are annotations pointing to more than one reference,consisting of a dimension and associated tag. """
 @staticmethod
 def AreReferencesValidForLinearDimension(document,ownerViewId,options):
  """
  AreReferencesValidForLinearDimension(document: Document,ownerViewId: ElementId,options: MultiReferenceAnnotationOptions) -> bool
  
   If the DimensionStyleType is Linear,validates that the references are valid
    
     for an aligned multi-reference annotation.
  
  
   document: The document for the multi-reference annotation.
   ownerViewId: The view in which the multi-reference annotation will appear.
   options: Options containing the references which the dimension will witness.
   Returns: True DimensionStyleType does not equal Linear or
     if an aligned 
    multi-reference annotation can be created from the references.
  """
  pass
 @staticmethod
 def AreReferencesValidForLinearFixedDimension(document,ownerViewId,options):
  """
  AreReferencesValidForLinearFixedDimension(document: Document,ownerViewId: ElementId,options: MultiReferenceAnnotationOptions) -> bool
  
   If the DimensionStyleType is LinearFixed,validates that the references are 
    valid
     for an aligned multi-reference annotation.
  
  
   document: The document for the multi-reference annotation.
   ownerViewId: The view in which the multi-reference annotation will appear.
   options: Options containing the references which the dimension will witness.
   Returns: True DimensionStyleType does not equal LinearFixed or
     if an aligned 
    multi-reference annotation can be created from the references.
  """
  pass
 @staticmethod
 def Create(document,ownerViewId,options):
  """
  Create(document: Document,ownerViewId: ElementId,options: MultiReferenceAnnotationOptions) -> MultiReferenceAnnotation
  
   Creates a new MultiReferenceAnnotation.
  
   document: The document to which the new MultiReferenceAnnotation will be added.
   ownerViewId: The view in which the multi-reference annotation will appear.
   options: The creation options for the new MultiReferenceAnnotation.
   Returns: The new MultiReferenceAnnotation.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def IsLinearFixedDimensionDirectionValid(document,viewId,options):
  """
  IsLinearFixedDimensionDirectionValid(document: Document,viewId: ElementId,options: MultiReferenceAnnotationOptions) -> bool
  
   If the DimensionStyleType is LinearFixed,this function verifies that the 
    dimension line direction
     matches either the view's vertical or horizontal 
    direction.
  
  
   document: The document for the view.
   viewId: The view in which the dimension line direction will be tested.
   options: Options containing the DimensionStyleType and dimension line direction to test.
   Returns: True if the DimensionStyleType is LinearFixed and the dimension line direction 
    can be used in the view.
     True if the DimensionStyleType is not LinearFixed.
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
 DimensionId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The child dimension owned by this multi-reference annotation.

Get: DimensionId(self: MultiReferenceAnnotation) -> ElementId

"""

 TagId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The child IndependentTag owned by this multi-reference annotation.

Get: TagId(self: MultiReferenceAnnotation) -> ElementId

"""



class DisplacementPath(Element,IDisposable):
 """ A view-specific annotation related to a DisplacementElement. """
 @staticmethod
 def Create(aDoc,displacementElement,reference,param):
  """
  Create(aDoc: Document,displacementElement: DisplacementElement,reference: Reference,param: float) -> ElementId

  

   Creates a new DisplacementPath referencing a DisplacementElement and edge or 

    curve and adds it to the document.

  

  

   aDoc: The document.

   displacementElement: Element id of a DisplacementElement

   reference: A reference that refers to an edge or curve of one of the elements displaced by 

    the displacementElement.

  

   param: A value in the range [0,1]. It will be interpreted as a parameter for the 

    specified edge.

  

   Returns: The element id of the newly created DisplacementPath.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def IsValidParam(param):
  """
  IsValidParam(param: float) -> bool

  

   Is the specified value a valid edge or curve parameter.

  

   param: proposed edge parameter.
  """
  pass
 @staticmethod
 def IsValidReference(displacementElement,reference):
  """
  IsValidReference(displacementElement: DisplacementElement,reference: Reference) -> bool

  

   Does the specified pick represent an edge or a curve belonging to one of the 

    displaced elements.

  

  

   displacementElement: A DisplacementElement.

   reference: A pick.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetAnchorPoint(self,displacementElement,reference,param):
  """
  SetAnchorPoint(self: DisplacementPath,displacementElement: DisplacementElement,reference: Reference,param: float)

   Sets the reference that determines the origin of this DisplacementPath.

  

   displacementElement: The element id of a DisplacementElement.

   reference: A reference of an edge or a curve in the GRep of the element corresponding to 

    elemId.

  

   param: An parameter used to specify a point on the edge.
  """
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
 AncestorIdx=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the end point of the path.



Get: AncestorIdx(self: DisplacementPath) -> int



Set: AncestorIdx(self: DisplacementPath)=value

"""

 PathStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the style of the path.



Get: PathStyle(self: DisplacementPath) -> DisplacementPathStyle



Set: PathStyle(self: DisplacementPath)=value

"""



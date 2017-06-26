class ElementTransformUtils(object):
 """ A collection of utilities allowing transformation of elements (e.g. move,rotate,mirror and copy). """
 @staticmethod
 def CanMirrorElement(ADoc,elemId):
  """
  CanMirrorElement(ADoc: Document,elemId: ElementId) -> bool
  
   Determines whether element can be mirrored.
  
   ADoc: The document where the element reside.
   elemId: The element identified by id.
   Returns: True if the element can be mirrored.
  """
  pass
 @staticmethod
 def CanMirrorElements(ADoc,elemIds):
  """ CanMirrorElements(ADoc: Document,elemIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def CopyElement(document,elementToCopy,translation):
  """
  CopyElement(document: Document,elementToCopy: ElementId,translation: XYZ) -> ICollection[ElementId]
  
   Copies an element and places the copy at a location indicated by a given 
    transformation.
  
  
   document: The document that owns the element.
   elementToCopy: The id of the element to copy.
   translation: The translation vector for the new element.
   Returns: The ids of the newly created copied elements.  More than one element may be 
    created due to dependencies.
  """
  pass
 @staticmethod
 def CopyElements(*__args):
  """
  CopyElements(document: Document,elementsToCopy: ICollection[ElementId],translation: XYZ) -> ICollection[ElementId]
  CopyElements(sourceDocument: Document,elementsToCopy: ICollection[ElementId],destinationDocument: Document,transform: Transform,options: CopyPasteOptions) -> ICollection[ElementId]
  CopyElements(sourceView: View,elementsToCopy: ICollection[ElementId],destinationView: View,additionalTransform: Transform,options: CopyPasteOptions) -> ICollection[ElementId]
  """
  pass
 @staticmethod
 def GetTransformFromViewToView(sourceView,destinationView):
  """
  GetTransformFromViewToView(sourceView: View,destinationView: View) -> Transform
  
   Returns a transformation that is applied to elements when copying from one view 
    to another view.
  
  
   sourceView: The source view
   destinationView: The destination view
   Returns: The transformation from source view to destination view.
  """
  pass
 @staticmethod
 def MirrorElement(document,elementToMirror,plane):
  """
  MirrorElement(document: Document,elementToMirror: ElementId,plane: Plane)
   Creates a mirrored copy of an element about a given plane.
  
   document: The document that owns the element.
   elementToMirror: The element to mirror.
   plane: The mirror plane.
  """
  pass
 @staticmethod
 def MirrorElements(document,elementsToMirror,plane,mirrorCopies):
  """ MirrorElements(document: Document,elementsToMirror: ICollection[ElementId],plane: Plane,mirrorCopies: bool) -> IList[ElementId] """
  pass
 @staticmethod
 def MoveElement(document,elementToMove,translation):
  """
  MoveElement(document: Document,elementToMove: ElementId,translation: XYZ)
   Moves one element by a given transformation.
  
   document: The document that owns the elements.
   elementToMove: The id of the element to move.
   translation: The translation vector for the elements.
  """
  pass
 @staticmethod
 def MoveElements(document,elementsToMove,translation):
  """ MoveElements(document: Document,elementsToMove: ICollection[ElementId],translation: XYZ) """
  pass
 @staticmethod
 def RotateElement(document,elementToRotate,axis,angle):
  """
  RotateElement(document: Document,elementToRotate: ElementId,axis: Line,angle: float)
   Rotates an element about the given axis and angle.
  
   document: The document that owns the elements.
   elementToRotate: The element to rotate.
   axis: The axis of rotation.
   angle: The angle of rotation in radians.
  """
  pass
 @staticmethod
 def RotateElements(document,elementsToRotate,axis,angle):
  """ RotateElements(document: Document,elementsToRotate: ICollection[ElementId],axis: Line,angle: float) """
  pass
 __all__=[
  'CanMirrorElement',
  'CanMirrorElements',
  'CopyElement',
  'CopyElements',
  'GetTransformFromViewToView',
  'MirrorElement',
  'MirrorElements',
  'MoveElement',
  'MoveElements',
  'RotateElement',
  'RotateElements',
 ]


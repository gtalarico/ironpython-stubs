class FaceWall(HostObject,IDisposable):
 """ A wall attached to a non-vertical massing face. """
 @staticmethod
 def Create(document,wallType,locationLine,faceReference):
  """
  Create(document: Document,wallType: ElementId,locationLine: WallLocationLine,faceReference: Reference) -> FaceWall
  
   Creates a new instance of a wall attached to a non-vertical massing face.
  
   document: The document.
   wallType: The wall type.  This must be a wall type accepted by 
    IsWallTypeValidForFaceWall()
  
   locationLine: The alignment of the wall location line.
   faceReference: The reference from the massing face.  This must pass 
    IsValidFaceReferenceForFaceWall()
  
   Returns: The newly created face wall.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def IsValidFaceReferenceForFaceWall(document,faceReference):
  """
  IsValidFaceReferenceForFaceWall(document: Document,faceReference: Reference) -> bool
  
   Identifies if a reference may be used as the parent of a face wall.
  
   document: The document.
   faceReference: The reference.
   Returns: True if the reference is valid as a parent to a face wall,false otherwise.
  """
  pass
 @staticmethod
 def IsWallTypeValidForFaceWall(document,wallType):
  """
  IsWallTypeValidForFaceWall(document: Document,wallType: ElementId) -> bool
  
   Identifies if a wall type may be applied to a face wall.
  
   document: The document.
   wallType: The wall type.
   Returns: True if the wall type is valid for face wall,false otherwise.
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

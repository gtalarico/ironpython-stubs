class Truss(Element,IDisposable):
 """ Represents all kinds of Trusses. """
 def AttachChord(self,attachToElement,location,forceRemoveSketch):
  """
  AttachChord(self: Truss,attachToElement: Element,location: TrussChordLocation,forceRemoveSketch: bool)
   Attach a truss's specific chord to a specified element,the element should be a 
    roof or floor.
  
  
   attachToElement: The element to which the truss's chord will attach. The element should be a 
    roof or floor.
  
   location: The chord need to be attached.
   forceRemoveSketch: Whether to detach the original sketch if there is one.
  """
  pass
 @staticmethod
 def Create(document,trussTypeId,sketchPlaneId,curve):
  """
  Create(document: Document,trussTypeId: ElementId,sketchPlaneId: ElementId,curve: Curve) -> Truss
  
   Creates a new Truss.
  
   document: The document in which the new Truss is created.
   trussTypeId: Element id of the truss type.
   sketchPlaneId: Element id of a SketchPlane.
   curve: The curve of the truss element.
     It must be a line,must not be a vertical 
    line,and must be within the sketch plane.
  """
  pass
 def DetachChord(self,location):
  """
  DetachChord(self: Truss,location: TrussChordLocation)
   Detach a truss's specific chord from the element to which it is attached.
  
   location: The chord.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def DropTruss(truss):
  """
  DropTruss(truss: Truss)
   Drop truss Family,it will disassociate all members from the truss and delete 
    the truss.
  
  
   truss: The truss to be dropped.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetTrussMemberInfo(self,elemId):
  """
  GetTrussMemberInfo(self: Truss,elemId: ElementId) -> TrussMemberInfo
  
   Query if a given element is a member of a truss,its lock status and its usage,
    etc.
  
  
   elemId: The querying element.
   Returns: A struct TrussMemberInfo that contains the querying element's host truss,
    whether to lock to the truss,usage type,etc.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveProfile(self):
  """
  RemoveProfile(self: Truss)
   Remove the profile of a truss.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetProfile(self,topChords,bottomChords):
  """
  SetProfile(self: Truss,topChords: CurveArray,bottomChords: CurveArray)
   Add or modify the profile of a truss.
  
   topChords: The curves serving as top chords of the truss.
   bottomChords: The curves serving as bottom chords of the truss.
  """
  pass
 def TogglePinMember(self,elemId):
  """
  TogglePinMember(self: Truss,elemId: ElementId)
   Pin/Unpin a truss member.
  
   elemId: The member element is going to pin/unpin.
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
 Curves=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all the truss curves.

Get: Curves(self: Truss) -> CurveArray

"""

 Members=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all the members of truss.

Get: Members(self: Truss) -> ICollection[ElementId]

"""

 TrussType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve/set an object that represents the type of the truss.

Get: TrussType(self: Truss) -> TrussType

Set: TrussType(self: Truss)=value
"""



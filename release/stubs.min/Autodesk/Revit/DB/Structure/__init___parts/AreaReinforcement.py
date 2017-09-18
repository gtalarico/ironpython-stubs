class AreaReinforcement(Element,IDisposable):
 """ An object that represents an Area Reinforcement within the Autodesk Revit project. """
 @staticmethod
 def Create(document,hostElement,*__args):
  """
  Create(document: Document,hostElement: Element,curveArray: IList[Curve],majorDirection: XYZ,areaReinforcementTypeId: ElementId,rebarBarTypeId: ElementId,rebarHookTypeId: ElementId) -> AreaReinforcement
  Create(document: Document,hostElement: Element,majorDirection: XYZ,areaReinforcementTypeId: ElementId,rebarBarTypeId: ElementId,rebarHookTypeId: ElementId) -> AreaReinforcement
  
   Creates a new AreaReinforcement object based on a host boundary.
  
   document: The document.
   hostElement: The element that will host the AreaReinforcement. The host can be a Structural 
    Floor,Structural Wall,Structural Slab,or a Part created from a structural 
    layer belonging to one of those element types.
  
   majorDirection: A vector to define the major direction of the AreaReinforcement.
   areaReinforcementTypeId: The id of the AreaReinforcementType.
   rebarBarTypeId: The id of the RebarBarType.
   rebarHookTypeId: The id of the RebarHookType.
     If this parameter is InvalidElementId,it 
    means to create a rebar with no hooks.
  
   Returns: The newly created AreaReinforcement.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetBoundaryCurveIds(self):
  """
  GetBoundaryCurveIds(self: AreaReinforcement) -> IList[ElementId]
  
   Retrieves the set of curves forming the boundary of the Area Reinforcement.
   Returns: A collection of ElementIds of AreaReinforcementCurve elements.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetHostId(self):
  """
  GetHostId(self: AreaReinforcement) -> ElementId
  
   The element that contains the Area Reinforcement.
   Returns: The element that the Area Reinforcement object belongs to,such as a structural
    
     wall,floor or foundation.
  """
  pass
 def GetRebarInSystemIds(self):
  """
  GetRebarInSystemIds(self: AreaReinforcement) -> IList[ElementId]
  
   Returns the ids of the RebarInSystem elements owned by the AreaReinforcement
    
     element.
  """
  pass
 def IsSolidInView(self,view):
  """
  IsSolidInView(self: AreaReinforcement,view: View3D) -> bool
  
   Checks if this Area Reinforcement is shown solidly in a 3D view.
  
   view: The 3D view element
   Returns: True if Area Reinforcement is shown solidly,false otherwise.
  """
  pass
 def IsUnobscuredInView(self,view):
  """
  IsUnobscuredInView(self: AreaReinforcement,view: View) -> bool
  
   Checks if Area Reinforcement is shown unobscured in a view.
  
   view: The view element
   Returns: True if Area Reinforcement is shown unobscured,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 @staticmethod
 def RemoveAreaReinforcementSystem(doc,system):
  """
  RemoveAreaReinforcementSystem(doc: Document,system: AreaReinforcement) -> IList[ElementId]
  
   Deletes the specified AreaReinforcement,and converts its RebarInSystem
     
    elements to equivalent Rebar elements.
  
  
   doc: The document.
   system: An AreaReinforcement element in the document.
   Returns: The ids of the newly created Rebar elements.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetSolidInView(self,view,solid):
  """
  SetSolidInView(self: AreaReinforcement,view: View3D,solid: bool)
   Sets this Area Reinforcement to be shown solidly in a 3D view.
  
   view: The 3D view element
   solid: True if Area Reinforcement is shown solidly,false otherwise.
  """
  pass
 def SetUnobscuredInView(self,view,unobscured):
  """
  SetUnobscuredInView(self: AreaReinforcement,view: View,unobscured: bool)
   Sets Area Reinforcement to be shown unobscured in a view.
  
   view: The view element
   unobscured: True if Area Reinforcement is shown unobscured,false otherwise.
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
 AdditionalBottomCoverOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Additional offset from the bottom or interior cover reference.

Get: AdditionalBottomCoverOffset(self: AreaReinforcement) -> float

Set: AdditionalBottomCoverOffset(self: AreaReinforcement)=value
"""

 AdditionalTopCoverOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Additional offset from the top or exterior cover reference.

Get: AdditionalTopCoverOffset(self: AreaReinforcement) -> float

Set: AdditionalTopCoverOffset(self: AreaReinforcement)=value
"""

 AreaReinforcementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the type of the Area Reinforcement.

Get: AreaReinforcementType(self: AreaReinforcement) -> AreaReinforcementType

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the Major Direction of the Area Reinforcement.

Get: Direction(self: AreaReinforcement) -> XYZ

"""



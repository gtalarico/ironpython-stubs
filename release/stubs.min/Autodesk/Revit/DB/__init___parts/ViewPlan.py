class ViewPlan(View,IDisposable):
 """ Class for plan views """
 def CheckPlanViewRangeValidity(self,planViewRange):
  """
  CheckPlanViewRangeValidity(self: ViewPlan,planViewRange: PlanViewRange) -> IList[PlanViewRangeError]
  
   Checks if the plan view range is valid.
  
   planViewRange: The view range to validate.
   Returns: List of enums describing any errors in the plan view range.
  """
  pass
 @staticmethod
 def Create(document,viewFamilyTypeId,levelId):
  """
  Create(document: Document,viewFamilyTypeId: ElementId,levelId: ElementId) -> ViewPlan
  
   Creates a new ViewPlan.
  
   document: The document to which the ViewPlan will be added.
   viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new ViewPlan.  The type 
    needs to be a FloorPlan,CeilingPlan,AreaPlan,or StructuralPlan ViewType.
  
   levelId: The id of the Level to associate with the new plan view.
   Returns: The new ViewPlan.
  """
  pass
 @staticmethod
 def CreateAreaPlan(document,areaSchemeId,levelId):
  """
  CreateAreaPlan(document: Document,areaSchemeId: ElementId,levelId: ElementId) -> ViewPlan
  
   Creates a new area plan ViewPlan.
  
   document: The document to which the area plan will be added.
   areaSchemeId: The id of the AreaScheme which will be used by the area plan.
   levelId: The id of the Level to associate with the area plan.
   Returns: The new area plan ViewPlan.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetUnderlayBaseLevel(self):
  """
  GetUnderlayBaseLevel(self: ViewPlan) -> ElementId
  
   Returns the element id of the level that defines the bottom of the underlay 
    range.
  
   Returns: If InvalidElementId is returned,then the underlay base level is not set and no 
    elements will be displayed as underlay.
  """
  pass
 def GetUnderlayOrientation(self):
  """
  GetUnderlayOrientation(self: ViewPlan) -> UnderlayOrientation
  
   Returns the underlay orientation of this view.
   Returns: The underlay orientation for this view.
  """
  pass
 def GetUnderlayTopLevel(self):
  """
  GetUnderlayTopLevel(self: ViewPlan) -> ElementId
  
   Returns the element id of the level that defines the top of the underlay range.
   Returns: If the underlay base level is a valid level,and this method returns 
    InvalidElementId,then the underlay range is unbounded,
     and consists of 
    everything above the underlay base level.
  """
  pass
 def GetViewRange(self):
  """
  GetViewRange(self: ViewPlan) -> PlanViewRange
  
   Gets the view range.
   Returns: The view range.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetUnderlayBaseLevel(self,levelId):
  """
  SetUnderlayBaseLevel(self: ViewPlan,levelId: ElementId)
   Sets the level whose elevation will determine the bottom of the underlay range.
    
     The elevation of the next highest level will be used to determine the top 
    of the underlay range.
  
  
   levelId: The element id of a level in the project or else InvalidElementId.
  """
  pass
 def SetUnderlayOrientation(self,uo):
  """
  SetUnderlayOrientation(self: ViewPlan,uo: UnderlayOrientation)
   Sets the underlay orientation for this view.
  
   uo: The underlay orientation for this view.
  """
  pass
 def SetUnderlayRange(self,baseLevelId,topLevelId):
  """
  SetUnderlayRange(self: ViewPlan,baseLevelId: ElementId,topLevelId: ElementId)
   Sets the underlay base and underlay top to the specified levels.
  
   baseLevelId: The element id of a level in the project or InvalidElementId. If 
    InvalidElementId,
     then the underlay base level is not set and no elements 
    will be displayed as underlay.
  
   topLevelId: The element id of a level in the project or InvalidElementId. If 
    InvalidElementId,
     then the underlay range is unbounded.
  """
  pass
 def SetViewRange(self,planViewRange):
  """
  SetViewRange(self: ViewPlan,planViewRange: PlanViewRange)
   Sets the view range.
  
   planViewRange: The view range.
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
 AreaScheme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The area scheme.

Get: AreaScheme(self: ViewPlan) -> AreaScheme

"""



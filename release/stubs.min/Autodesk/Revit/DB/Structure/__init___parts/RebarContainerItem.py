class RebarContainerItem(object,IDisposable):
 """ Provides implementation for Rebar stored in RebarContainer. """
 def CanApplyPresentationMode(self,dBView):
  """
  CanApplyPresentationMode(self: RebarContainerItem,dBView: View) -> bool

  

   Checks if a presentation mode can be applied for this rebar in the given view.

  

   dBView: The view in which presentation mode will be applied.

   Returns: True if presentation mode can be applied for this view,false otherwise.
  """
  pass
 def CanUseHookType(self,proposedHookId):
  """
  CanUseHookType(self: RebarContainerItem,proposedHookId: ElementId) -> bool

  

   Checks if the specified RebarHookType id is of a valid RebarHookType for the 

    Rebar's RebarBarType

  

  

   proposedHookId: The Id of the RebarHookType

   Returns: Returns true if the id is of a valid RebarHookType for the Rebar element.
  """
  pass
 def ClearPresentationMode(self,dBView):
  """
  ClearPresentationMode(self: RebarContainerItem,dBView: View)

   Sets the presentation mode for this rebar set to the default (either for a 

    single view,or for all views).

  

  

   dBView: The view where the presentation mode will be cleared. NULL for all views
  """
  pass
 def ComputeDrivingCurves(self):
  """
  ComputeDrivingCurves(self: RebarContainerItem) -> IList[Curve]

  

   Compute the driving curves.

   Returns: Returns an empty array if an error is encountered.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RebarContainerItem) """
  pass
 def DoesBarExistAtPosition(self,barPosition):
  """
  DoesBarExistAtPosition(self: RebarContainerItem,barPosition: int) -> bool

  

   Checks whether a bar exists at the specified position.

  

   barPosition: A bar position index between 0 and NumberOfBarPositions-1.
  """
  pass
 def FindMatchingPredefinedPresentationMode(self,dBView):
  """
  FindMatchingPredefinedPresentationMode(self: RebarContainerItem,dBView: View) -> RebarPresentationMode

  

   Determines if there is a matching RebarPresentationMode for the current set of 

    selected hidden and unhidden bars assigned to the given view.

  

  

   dBView: The view.

   Returns: The presentation mode that matches the current set of selected hidden and 

    unhidden bars.

     If there is no better match,this returns 

    RebarPresentationMode.Select.
  """
  pass
 def GetBarPositionTransform(self,barPositionIndex):
  """
  GetBarPositionTransform(self: RebarContainerItem,barPositionIndex: int) -> Transform

  

   Return a transform representing the relative position of any

     individual bar 

    in the set.

  

  

   barPositionIndex: An index between 0 and (NumberOfBarPositions-1).

   Returns: The position of a bar in the set relative to the first position.
  """
  pass
 def GetBendData(self):
  """
  GetBendData(self: RebarContainerItem) -> RebarBendData

  

   Gets the RebarBendData,containing bar and hook information,of the instance.
  """
  pass
 def GetCenterlineCurves(self,adjustForSelfIntersection,suppressHooks,suppressBendRadius,multiplanarOption=None):
  """
  GetCenterlineCurves(self: RebarContainerItem,adjustForSelfIntersection: bool,suppressHooks: bool,suppressBendRadius: bool) -> IList[Curve]

  

   A chain of curves representing the centerline of the rebar.

  

   adjustForSelfIntersection: If the curves overlap,as in a planar stirrup,this parameter controls

     

    whether they should be adjusted to avoid intersection (as in fine views),

     

    or kept in a single plane for simplicity (as in coarse views).

  

   suppressHooks: Identifies if the chain will include hooks curves.

   suppressBendRadius: Identifies if the connected chain will include unfilleted curves.

   Returns: The centerline curves or empty array if the curves cannot be computed because

   

      the parameters values are inconsistent

     with the constraints of the 

    RebarShape definition.

  

  GetCenterlineCurves(self: RebarContainerItem,adjustForSelfIntersection: bool,suppressHooks: bool,suppressBendRadius: bool,multiplanarOption: MultiplanarOption) -> IList[Curve]

  

   A chain of curves representing the centerline of the rebar.

  

   adjustForSelfIntersection: If the curves overlap,as in a planar stirrup,this parameter controls

     

    whether they should be adjusted to avoid intersection (as in fine views),

     

    or kept in a single plane for simplicity (as in coarse views).

  

   suppressHooks: Identifies if the chain will include hooks curves.

   suppressBendRadius: Identifies if the connected chain will include unfilleted curves.

   multiplanarOption: If the Rebar is a multi-planar shape,this parameter controls whether to 

    generate only

     the curves in the primary plane (IncludeOnlyPlanarCurves),or 

    to generate all curves,

     (IncludeAllMultiplanarCurves) including the 

    out-of-plane connector segments as well as

     multi-planar copies of the 

    primary plane curves.

     This argument is ignored for planar shapes.

  

   Returns: The centerline curves or empty array if the curves cannot be computed because

   

      the parameters values are inconsistent

     with the constraints of the 

    RebarShape definition.
  """
  pass
 def GetDistributionPath(self):
  """
  GetDistributionPath(self: RebarContainerItem) -> Line

  

   The distribution path of a rebar set.

   Returns: A line beginning at (0,0,0) and representing the direction and

     length of 

    the set.
  """
  pass
 def GetHookOrientation(self,iEnd):
  """
  GetHookOrientation(self: RebarContainerItem,iEnd: int) -> RebarHookOrientation

  

   Returns the orientation of the hook plane at the start or at the end of the 

    rebar with respect to the orientation of the first or the last curve and the 

    plane normal.

  

  

   iEnd: 0 for the start hook,1 for the end hook.

   Returns: Value=Right: The hook is on your right as you stand at the end of the bar,

    

     with the bar behind you,taking the bar's normal as "up."

     Value=Left: 

    The hook is on your left as you stand at the end of the bar,

     with the bar 

    behind you,taking the bar's normal as "up."
  """
  pass
 def GetHookTypeId(self,end):
  """
  GetHookTypeId(self: RebarContainerItem,end: int) -> ElementId

  

   Get the id of the RebarHookType to be applied to the rebar.

  

   end: 0 for the start hook,1 for the end hook.

   Returns: The id of a RebarHookType,or invalidElementId if the rebar has

     no hook at 

    the specified end.
  """
  pass
 def GetPresentationMode(self,dBView):
  """
  GetPresentationMode(self: RebarContainerItem,dBView: View) -> RebarPresentationMode

  

   Gets the presentaion mode for this rebar set when displayed in the given view.

  

   dBView: The view.

   Returns: The presentation mode.
  """
  pass
 def HasPresentationOverrides(self,dBView):
  """
  HasPresentationOverrides(self: RebarContainerItem,dBView: View) -> bool

  

   Identifies if this rebar set has overridden default presentation settings for 

    the given view.

  

  

   dBView: The view.

   Returns: True if this rebar set has overriden default presentation settings,false 

    otherwise.
  """
  pass
 def IsBarHidden(self,view,barIndex):
  """
  IsBarHidden(self: RebarContainerItem,view: View,barIndex: int) -> bool

  

   Identifies if a given bar in this rebar set is hidden in this view.

  

   view: The view.

   barIndex: The index of the bar from this rebar set.

   Returns: True if the bar is hidden in this view,false otherwise.
  """
  pass
 def IsRebarInSection(self,dBView):
  """
  IsRebarInSection(self: RebarContainerItem,dBView: View) -> bool

  

   Identifies if this rebar set is shown as a cross-section in the given view.

  

   dBView: The view.

   Returns: True if this rebar set is shown as a cross-section,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarContainerItem,disposing: bool) """
  pass
 def SetBarHiddenStatus(self,view,barIndex,hide):
  """
  SetBarHiddenStatus(self: RebarContainerItem,view: View,barIndex: int,hide: bool)

   Sets the bar in this rebar set to be hidden or unhidden in the given view.

  

   view: The view.

   barIndex: The index of the bar from this set.

   hide: True to hide this bar in the view,false to unhide the bar.
  """
  pass
 def SetFromCurves(self,style,barType,startHook,endHook,norm,curves,startHookOrient,endHookOrient,useExistingShapeIfPossible,createNewShape):
  """ SetFromCurves(self: RebarContainerItem,style: RebarStyle,barType: RebarBarType,startHook: RebarHookType,endHook: RebarHookType,norm: XYZ,curves: IList[Curve],startHookOrient: RebarHookOrientation,endHookOrient: RebarHookOrientation,useExistingShapeIfPossible: bool,createNewShape: bool) """
  pass
 def SetFromCurvesAndShape(self,rebarShape,barType,startHook,endHook,norm,curves,startHookOrient,endHookOrient):
  """ SetFromCurvesAndShape(self: RebarContainerItem,rebarShape: RebarShape,barType: RebarBarType,startHook: RebarHookType,endHook: RebarHookType,norm: XYZ,curves: IList[Curve],startHookOrient: RebarHookOrientation,endHookOrient: RebarHookOrientation) """
  pass
 def SetFromRebar(self,rebar):
  """
  SetFromRebar(self: RebarContainerItem,rebar: Rebar)

   Set an instance of a RebarContainerItem element according to a Rebar parameters.

  

   rebar: The Rebar.
  """
  pass
 def SetFromRebarShape(self,rebarShape,barType,origin,xVec,yVec):
  """
  SetFromRebarShape(self: RebarContainerItem,rebarShape: RebarShape,barType: RebarBarType,origin: XYZ,xVec: XYZ,yVec: XYZ)

   Set an instance of a RebarContainerItem element,as an instance of a 

    RebarShape.

     The instance will have the default shape parameters from the 

    RebarShape,

     and its location is based on the bounding box of the shape in 

    the shape definition.

     Hooks are removed from the shape before computing its 

    bounding box.

     If appropriate hooks can be found in the document,they will 

    be assigned arbitrarily.

  

  

   rebarShape: A RebarShape element that defines the shape of the rebar.

   barType: A RebarBarType element that defines bar diameter,bend radius and material of 

    the rebar.

  

   origin: The lower-left corner of the shape's bounding box will be placed at this point 

    in the project.

  

   xVec: The x-axis in the shape definition will be mapped to this direction in the 

    project.

  

   yVec: The y-axis in the shape definition will be mapped to this direction in the 

    project.
  """
  pass
 def SetHookOrientation(self,iEnd,hookOrientation):
  """
  SetHookOrientation(self: RebarContainerItem,iEnd: int,hookOrientation: RebarHookOrientation)

   Defines the orientation of the hook plane at the start or at the end of the 

    rebar with respect to the orientation of the first or the last curve and the 

    plane normal.

  

  

   iEnd: 0 for the start hook,1 for the end hook.

   hookOrientation: Only two values are permitted:

     Value=Right: The hook is on your right as 

    you stand at the end of the bar,

     with the bar behind you,taking the bar's 

    normal as "up."

     Value=Left: The hook is on your left as you stand at the 

    end of the bar,

     with the bar behind you,taking the bar's normal as "up."
  """
  pass
 def SetHookTypeId(self,end,hookTypeId):
  """
  SetHookTypeId(self: RebarContainerItem,end: int,hookTypeId: ElementId)

   Set the id of the RebarHookType to be applied to the rebar.

  

   end: 0 for the start hook,1 for the end hook.

   hookTypeId: The id of a RebarHookType element,or invalidElementId if

     the rebar should 

    have no hook at the specified end.
  """
  pass
 def SetLayoutAsFixedNumber(self,numberOfBarPositions,arrayLength,barsOnNormalSide,includeFirstBar,includeLastBar):
  """
  SetLayoutAsFixedNumber(self: RebarContainerItem,numberOfBarPositions: int,arrayLength: float,barsOnNormalSide: bool,includeFirstBar: bool,includeLastBar: bool)

   Sets the Layout Rule property of rebar set to FixedNumber.

  

   numberOfBarPositions: The number of bar positions in rebar set

   arrayLength: The distribution length of rebar set

   barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 

    indicated by the normal

  

   includeFirstBar: Identifies if the first bar in rebar set is shown

   includeLastBar: Identifies if the last bar in rebar set is shown
  """
  pass
 def SetLayoutAsMaximumSpacing(self,spacing,arrayLength,barsOnNormalSide,includeFirstBar,includeLastBar):
  """
  SetLayoutAsMaximumSpacing(self: RebarContainerItem,spacing: float,arrayLength: float,barsOnNormalSide: bool,includeFirstBar: bool,includeLastBar: bool)

   Sets the Layout Rule property of rebar set to MaximumSpacing

  

   spacing: The maximum spacing between rebar in rebar set

   arrayLength: The distribution length of rebar set

   barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 

    indicated by the normal

  

   includeFirstBar: Identifies if the first bar in rebar set is shown

   includeLastBar: Identifies if the last bar in rebar set is shown
  """
  pass
 def SetLayoutAsMinimumClearSpacing(self,spacing,arrayLength,barsOnNormalSide,includeFirstBar,includeLastBar):
  """
  SetLayoutAsMinimumClearSpacing(self: RebarContainerItem,spacing: float,arrayLength: float,barsOnNormalSide: bool,includeFirstBar: bool,includeLastBar: bool)

   Sets the Layout Rule property of rebar set to MinimumClearSpacing

  

   spacing: The maximum spacing between rebar in rebar set

   arrayLength: The distribution length of rebar set

   barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 

    indicated by the normal

  

   includeFirstBar: Identifies if the first bar in rebar set is shown

   includeLastBar: Identifies if the last bar in rebar set is shown
  """
  pass
 def SetLayoutAsNumberWithSpacing(self,numberOfBarPositions,spacing,barsOnNormalSide,includeFirstBar,includeLastBar):
  """
  SetLayoutAsNumberWithSpacing(self: RebarContainerItem,numberOfBarPositions: int,spacing: float,barsOnNormalSide: bool,includeFirstBar: bool,includeLastBar: bool)

   Sets the Layout Rule property of rebar set to NumberWithSpacing

  

   numberOfBarPositions: The number of bar positions in rebar set

   spacing: The maximum spacing between rebar in rebar set

   barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 

    indicated by the normal

  

   includeFirstBar: Identifies if the first bar in rebar set is shown

   includeLastBar: Identifies if the last bar in rebar set is shown
  """
  pass
 def SetLayoutAsSingle(self):
  """
  SetLayoutAsSingle(self: RebarContainerItem)

   Sets the Layout Rule property of rebar set to Single.
  """
  pass
 def SetPresentationMode(self,dBView,presentationMode):
  """
  SetPresentationMode(self: RebarContainerItem,dBView: View,presentationMode: RebarPresentationMode)

   Sets the presentation mode for this rebar set when displayed in the given view.

  

   dBView: The view.

   presentationMode: The presentation mode.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ArrayLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the distribution path length of rebar set.



Get: ArrayLength(self: RebarContainerItem) -> float



Set: ArrayLength(self: RebarContainerItem)=value

"""

 BarsOnNormalSide=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.



Get: BarsOnNormalSide(self: RebarContainerItem) -> bool



Set: BarsOnNormalSide(self: RebarContainerItem)=value

"""

 BarTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The identifier of the rebar bar type.



Get: BarTypeId(self: RebarContainerItem) -> ElementId



"""

 BaseFinishingTurns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For a spiral,the number of finishing turns at the lower end of the spiral.



Get: BaseFinishingTurns(self: RebarContainerItem) -> int



Set: BaseFinishingTurns(self: RebarContainerItem)=value

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For a spiral,the overall height.



Get: Height(self: RebarContainerItem) -> float



Set: Height(self: RebarContainerItem)=value

"""

 IncludeFirstBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the first bar in rebar set is shown.



Get: IncludeFirstBar(self: RebarContainerItem) -> bool



Set: IncludeFirstBar(self: RebarContainerItem)=value

"""

 IncludeLastBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the last bar in rebar set is shown.



Get: IncludeLastBar(self: RebarContainerItem) -> bool



Set: IncludeLastBar(self: RebarContainerItem)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RebarContainerItem) -> bool



"""

 ItemIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of this item in its associated RebarContainer.



Get: ItemIndex(self: RebarContainerItem) -> int



"""

 LayoutRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the layout rule of rebar set.



Get: LayoutRule(self: RebarContainerItem) -> RebarLayoutRule



"""

 MaxSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the maximum spacing between rebar in rebar set.



Get: MaxSpacing(self: RebarContainerItem) -> float



Set: MaxSpacing(self: RebarContainerItem)=value

"""

 MultiplanarDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For a multiplanar rebar,the depth of the instance.



Get: MultiplanarDepth(self: RebarContainerItem) -> float



Set: MultiplanarDepth(self: RebarContainerItem)=value

"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A unit-length vector normal to the plane of the rebar



Get: Normal(self: RebarContainerItem) -> XYZ



"""

 NumberOfBarPositions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of potential bars in the set.



Get: NumberOfBarPositions(self: RebarContainerItem) -> int



Set: NumberOfBarPositions(self: RebarContainerItem)=value

"""

 Pitch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For a spiral,the pitch,or vertical distance traveled in one rotation.



Get: Pitch(self: RebarContainerItem) -> float



Set: Pitch(self: RebarContainerItem)=value

"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the number of bars in rebar set.



Get: Quantity(self: RebarContainerItem) -> int



"""

 RebarShapeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The RebarShape element that defines the shape of the rebar.



Get: RebarShapeId(self: RebarContainerItem) -> ElementId



Set: RebarShapeId(self: RebarContainerItem)=value

"""

 TopFinishingTurns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For a spiral,the number of finishing turns at the upper end of the spiral.



Get: TopFinishingTurns(self: RebarContainerItem) -> int



Set: TopFinishingTurns(self: RebarContainerItem)=value

"""

 TotalLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length of an individual bar multiplied by Quantity.



Get: TotalLength(self: RebarContainerItem) -> float



"""

 Volume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The volume of an individual bar multiplied by Quantity.



Get: Volume(self: RebarContainerItem) -> float



"""



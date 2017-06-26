class RebarInSystem(Element, IDisposable):
    """ Represents a rebar element that is part of a system. """
    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: RebarInSystem, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this rebar in the given view.
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if a presentation mode can be applied for the given view, false otherwise.
        """
        pass

    def ClearPresentationMode(self, dBView):
        """
        ClearPresentationMode(self: RebarInSystem, dBView: View)
            Sets the presentation mode for this rebar set to the default (either for a 
             single view, or for all views).
        
        
            dBView: The view where the presentation mode will be cleared. NULL for all views
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def DoesBarExistAtPosition(self, barPosition):
        """
        DoesBarExistAtPosition(self: RebarInSystem, barPosition: int) -> bool
        
            Checks whether a bar exists at the specified position.
        
            barPosition: A bar position index between 0 and NumberOfBarPositions-1.
            Returns: Always returns true, since it is not possible to de-activate the first or last 
             bars
           in a Rebar set that is part of Area or Path Reinforcement.
           (see 
             includeFirstBar and includeLastBar methods for Rebar)
        """
        pass

    def FindMatchingPredefinedPresentationMode(self, dBView):
        """
        FindMatchingPredefinedPresentationMode(self: RebarInSystem, dBView: View) -> RebarPresentationMode
        
            Determines if there is a matching RebarPresentationMode for the current set of 
             selected hidden and unhidden bars assigned to the given view.
        
        
            dBView: The view.
            Returns: The presentation mode that matches the current set of selected hidden and 
             unhidden bars.
           If there is no better match, this returns 
             RebarPresentationMode.Select.
        """
        pass

    def GetBarPositionTransform(self, barPositionIndex):
        """
        GetBarPositionTransform(self: RebarInSystem, barPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of any
           individual bar 
             in the set.
        
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
            Returns: The position of a bar in the set relative to the first position.
        """
        pass

    def GetBendData(self):
        """
        GetBendData(self: RebarInSystem) -> RebarBendData
        
            Gets the RebarBendData, containing bar and hook information, of the instance.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCenterlineCurves(self, adjustForSelfIntersection, suppressHooks, suppressBendRadius):
        """
        GetCenterlineCurves(self: RebarInSystem, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        """
        pass

    def GetDistributionPath(self):
        """
        GetDistributionPath(self: RebarInSystem) -> Line
        
            The distribution path of a rebar set.
            Returns: A line beginning at (0, 0, 0) and representing the direction and
           length of 
             the set.
        """
        pass

    def GetHookTypeId(self, end):
        """
        GetHookTypeId(self: RebarInSystem, end: int) -> ElementId
        
            Get the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            Returns: The id of a RebarHookType, or invalidElementId if the rebar has
           no hook at 
             the specified end.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: RebarInSystem) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetPresentationMode(self, dBView):
        """
        GetPresentationMode(self: RebarInSystem, dBView: View) -> RebarPresentationMode
        
            Gets the presentaion mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            Returns: The presentation mode.
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: RebarInSystem) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: RebarInSystem, dBView: View) -> bool
        
            Identifies if this RebarInSystem has overridden default presentation settings 
             for the given view.
        
        
            dBView: The view.
            Returns: True if this RebarInSystem has overriden default presentation settings, false 
             otherwise.
        """
        pass

    def IsBarHidden(self, view, barIndex):
        """
        IsBarHidden(self: RebarInSystem, view: View, barIndex: int) -> bool
        
            Identifies if a given bar in this rebar set is hidden in this view.
        
            view: The view.
            barIndex: The index of the bar from this rebar set.
            Returns: True if the bar is hidden in this view, false otherwise.
        """
        pass

    def IsRebarInSection(self, dBView):
        """
        IsRebarInSection(self: RebarInSystem, dBView: View) -> bool
        
            Identifies if this RebarInSystem is shown as a cross-section in the given view.
        
            dBView: The view.
            Returns: True if this RebarInSystem is shown as a cross-section, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: RebarInSystem, view: View3D) -> bool
        
            Checks if this rebar element is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if rebar is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: RebarInSystem, view: View) -> bool
        
            Checks if this rebar element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetBarHiddenStatus(self, view, barIndex, hide):
        """
        SetBarHiddenStatus(self: RebarInSystem, view: View, barIndex: int, hide: bool)
            Sets the bar in this rebar set to be hidden or unhidden in the given view.
        
            view: The view.
            barIndex: The index of the bar from this set.
            hide: True to hide this bar in the view, false to unhide the bar.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPresentationMode(self, dBView, presentationMode):
        """
        SetPresentationMode(self: RebarInSystem, dBView: View, presentationMode: RebarPresentationMode)
            Sets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            presentationMode: The presentation mode.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: RebarInSystem, view: View3D, solid: bool)
            Sets this rebar element to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if rebar element is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: RebarInSystem, view: View, unobscured: bool)
            Sets  RebarInSystem element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if  RebarInSystem element is shown unobscured, false otherwise.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the distribution path length of rebar set.

Get: ArrayLength(self: RebarInSystem) -> float

"""

    BarsOnNormalSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.
   For the current implementation of RebarInSystem, this property will always return true,
   but it is included in the RebarInSystem interface for consistency with the Rebar class.

Get: BarsOnNormalSide(self: RebarInSystem) -> bool

"""

    LayoutRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the layout rule of rebar set.

Get: LayoutRule(self: RebarInSystem) -> RebarLayoutRule

"""

    MaxSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the maximum spacing between rebar in rebar set.

Get: MaxSpacing(self: RebarInSystem) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unit-length vector normal to the plane of the rebar

Get: Normal(self: RebarInSystem) -> XYZ

"""

    NumberOfBarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bar positions available in the rebar.

Get: NumberOfBarPositions(self: RebarInSystem) -> int

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the number of bars in rebar set.
   For the current implementation of RebarInSystem, this property will always return the same number as NumberOfBarPositions,
   since the first and last bars of a RebarInSystem set cannot be suppressed.
   However, it is included in the RebarInSystem interface for consistency with the Rebar class.

Get: Quantity(self: RebarInSystem) -> int

"""

    RebarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the rebar.

Get: RebarShapeId(self: RebarInSystem) -> ElementId

"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: RebarInSystem) -> str

Set: ScheduleMark(self: RebarInSystem) = value
"""

    SystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of an AreaReinforcement or PathReinforcement element that owns
   this element.

Get: SystemId(self: RebarInSystem) -> ElementId

"""

    TotalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of an individual bar multiplied by Quantity.

Get: TotalLength(self: RebarInSystem) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of an individual bar multiplied by Quantity.

Get: Volume(self: RebarInSystem) -> float

"""



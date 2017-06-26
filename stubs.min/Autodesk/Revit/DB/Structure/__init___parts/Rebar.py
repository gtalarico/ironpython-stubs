class Rebar(Element, IDisposable):
    """ Represents a rebar element in Autodesk Revit. """
    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: Rebar, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this rebar in the given view.
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if presentation mode can be applied for this view, false otherwise.
        """
        pass

    def CanSuppressFirstOrLastBar(self, dBView, end):
        """
        CanSuppressFirstOrLastBar(self: Rebar, dBView: View, end: int) -> bool
        
            Checks if the first or last bar in rebar set can be hidden in the given view.
        
            dBView: The view in which presentation mode will be applied.
            end: 0 for the first bar in rebar set, 1 for the last bar.
            Returns: True the first or last bar in rebar set can be hidden for this view, false 
             otherwise.
        """
        pass

    def CanUseHookType(self, proposedHookId):
        """
        CanUseHookType(self: Rebar, proposedHookId: ElementId) -> bool
        
            Checks if the specified RebarHookType id is of a valid RebarHookType for the 
             Rebar's RebarBarType
        
        
            proposedHookId: The Id of the RebarHookType
            Returns: Returns true if the id is of a valid RebarHookType for the Rebar element.
        """
        pass

    def ClearPresentationMode(self, dBView):
        """
        ClearPresentationMode(self: Rebar, dBView: View)
            Sets the presentation mode for this rebar set to the default (either for a 
             single view, or for all views).
        
        
            dBView: The view where the presentation mode will be cleared. NULL for all views
        """
        pass

    def ComputeDrivingCurves(self):
        """
        ComputeDrivingCurves(self: Rebar) -> IList[Curve]
        
            Compute the driving curves.
            Returns: Returns an empty array if an error is encountered.
        """
        pass

    def ConstraintsCanBeEdited(self):
        """
        ConstraintsCanBeEdited(self: Rebar) -> bool
        
            Returns true, if the Rebar element's external constraints are available for 
             editing using the
           RebarConstraintsManager class.  Examples of where this 
             method would return false are:
           Rebar in Groups (which do not have 
             constraints), or legacy, sketch-based Rebar elements
           created before the 
             introduction of RebarShape families in version 2009.
        """
        pass

    @staticmethod
    def ContainsValidArcRadiiForStyleAndBarType(curves, style, barType):
        """ ContainsValidArcRadiiForStyleAndBarType(curves: IList[Curve], style: RebarStyle, barType: RebarBarType) -> bool """
        pass

    @staticmethod
    def CreateFromCurves(doc, style, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape):
        """ CreateFromCurves(doc: Document, style: RebarStyle, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, host: Element, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation, useExistingShapeIfPossible: bool, createNewShape: bool) -> Rebar """
        pass

    @staticmethod
    def CreateFromCurvesAndShape(doc, rebarShape, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient):
        """ CreateFromCurvesAndShape(doc: Document, rebarShape: RebarShape, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, host: Element, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> Rebar """
        pass

    @staticmethod
    def CreateFromRebarShape(doc, rebarShape, barType, host, origin, xVec, yVec):
        """
        CreateFromRebarShape(doc: Document, rebarShape: RebarShape, barType: RebarBarType, host: Element, origin: XYZ, xVec: XYZ, yVec: XYZ) -> Rebar
        
            Creates a new Rebar, as an instance of a RebarShape.
           The instance will have 
             the default shape parameters from the RebarShape,
           and its location is based 
             on the bounding box of the shape in the shape definition.
           Hooks are removed 
             from the shape before computing its bounding box.
           If appropriate hooks can 
             be found in the document, they will be assigned arbitrarily.
        
        
            doc: A document.
            rebarShape: A RebarShape element that defines the shape of the rebar.
            barType: A RebarBarType element that defines bar diameter, bend radius and material of 
             the rebar.
        
            host: The element to which the rebar belongs. The element must support rebar hosting;
             
           see Autodesk.Revit.DB.Structure.RebarHostData.
        
            origin: The lower-left corner of the shape's bounding box will be placed at this point 
             in the project.
        
            xVec: The x-axis in the shape definition will be mapped to this direction in the 
             project.
        
            yVec: The y-axis in the shape definition will be mapped to this direction in the 
             project.
        
            Returns: The newly created Rebar instance, or ll if the operation fails.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def DoesBarExistAtPosition(self, barPosition):
        """
        DoesBarExistAtPosition(self: Rebar, barPosition: int) -> bool
        
            Checks whether a bar exists at the specified position.
        
            barPosition: A bar position index between 0 and NumberOfBarPositions-1.
        """
        pass

    def FindMatchingPredefinedPresentationMode(self, dBView):
        """
        FindMatchingPredefinedPresentationMode(self: Rebar, dBView: View) -> RebarPresentationMode
        
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
        GetBarPositionTransform(self: Rebar, barPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of any
           individual bar 
             in the set.
        
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
            Returns: The position of a bar in the set relative to the first position.
        """
        pass

    def GetBendData(self):
        """
        GetBendData(self: Rebar) -> RebarBendData
        
            Gets the RebarBendData, containing bar and hook information, of the instance.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCenterlineCurves(self, adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption=None, barPositionIndex=None):
        """
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool) -> IList[Curve]
        
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
        
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool, multiplanarOption: MultiplanarOption) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            multiplanarOption: If the Rebar is a multi-planar shape, this parameter controls whether to 
             generate only
           the curves in the primary plane (IncludeOnlyPlanarCurves), or 
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
        
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool, multiplanarOption: MultiplanarOption, barPositionIndex: int) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            multiplanarOption: If the Rebar is a multi-planar shape, this parameter controls whether to 
             generate only
           the curves in the primary plane (IncludeOnlyPlanarCurves), or 
             to generate all curves,
           (IncludeAllMultiplanarCurves) including the 
             out-of-plane connector segments as well as
           multi-planar copies of the 
             primary plane curves.
           This argument is ignored for planar shapes.
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
           Use the barPositionIndex 
             to obtain all the curves at a specific index in the distribution.
           You can 
             use GetNumberOfBarPositions() to verify if a specific rebar has more than one 
             bar positions.
           Use GetDistributionType() to probe if the bars in a specific 
             rebar have a varying shape. If so, you can retrieve the centerline curve 
             geometry of that particular bar, by passing the appropriate index.
           When the 
             distribution type of a rebar set is uniform, the form of the bars does not vary 
             from one index to another.
        
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        """
        pass

    def GetCouplerId(self, end):
        """
        GetCouplerId(self: Rebar, end: int) -> ElementId
        
            Get the id of the Rebar Coupler that is applied to the rebar at the specified 
             end.
        
        
            end: 0 for the start Rebar Coupler, 1 for the end Rebar Coupler.
            Returns: The id of a Rebar Coupler, or invalidElementId if the rebar has
           no Rebar 
             Coupler at the specified end.
        """
        pass

    def GetDistributionPath(self):
        """
        GetDistributionPath(self: Rebar) -> Line
        
            The distribution path of a rebar set.
            Returns: A line beginning at (0, 0, 0) and representing the direction and
           length of 
             the set.
        """
        pass

    def GetEndTreatmentTypeId(self, end):
        """
        GetEndTreatmentTypeId(self: Rebar, end: int) -> ElementId
        
            Get the id of the EndTreatmentType to be applied to the rebar.
        
            end: 0 for the start end treatment, 1 for the end end treatment.
            Returns: The id of a EndTreatmentType, or invalidElementId if the rebar has
           no end 
             treatment at the specified end.
        """
        pass

    def GetFullGeometryForView(self, view):
        """
        GetFullGeometryForView(self: Rebar, view: View) -> GeometryElement
        
            Generates full geometry for the Rebar for a specific view.
        
            view: The view in which the geometry is generated.
            Returns: The generated geometry of the Rebar before cutting is applied.
        """
        pass

    def GetHookOrientation(self, iEnd):
        """
        GetHookOrientation(self: Rebar, iEnd: int) -> RebarHookOrientation
        
            Returns the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            Returns: Value = Right: The hook is on your right as you stand at the end of the bar,
          
              with the bar behind you, taking the bar's normal as "up."
           Value = Left: 
             The hook is on your left as you stand at the end of the bar,
           with the bar 
             behind you, taking the bar's normal as "up."
        """
        pass

    def GetHookTypeId(self, end):
        """
        GetHookTypeId(self: Rebar, end: int) -> ElementId
        
            Get the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            Returns: The id of a RebarHookType, or invalidElementId if the rebar has
           no hook at 
             the specified end.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: Rebar) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetParameterValueAtIndex(self, paramId, barPositionIndex):
        """
        GetParameterValueAtIndex(self: Rebar, paramId: ElementId, barPositionIndex: int) -> ParameterValue
        
            Get the parameter value for a bar at the specified index.
           The parameter Id.
             
           The bar index in the rebar distribution. Accepts only values between 0 and 
             NumberOfBarPositions-1.
           The ParameterValue for given parameterId and 
             barPositionIndex.
           Throws exception if barPositionIndex is outside 
             boundaries.
        """
        pass

    def GetPresentationMode(self, dBView):
        """
        GetPresentationMode(self: Rebar, dBView: View) -> RebarPresentationMode
        
            Gets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            Returns: The presentation mode.
        """
        pass

    def GetRebarConstraintsManager(self):
        """
        GetRebarConstraintsManager(self: Rebar) -> RebarConstraintsManager
        
            Returns an object for managing the external constraints on the Rebar element
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: Rebar) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: Rebar, dBView: View) -> bool
        
            Identifies if this Rebar has overridden default presentation settings for the 
             given view.
        
        
            dBView: The view.
            Returns: True if this Rebar has overriden default presentation settings, false otherwise.
        """
        pass

    def HookAngleMatchesRebarShapeDefinition(self, iEnd, proposedHookId):
        """
        HookAngleMatchesRebarShapeDefinition(self: Rebar, iEnd: int, proposedHookId: ElementId) -> bool
        
            Checks that the hook angle of the specified RebarHookType matches the hook 
             angle used in the Rebar's RebarShape at the specified end of the bar.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            proposedHookId: The Id of the RebarHookType
            Returns: Returns true if the hook angle of the RebarHookType matches the angle used in 
             the RebarShape at the specified end of the bar.
        """
        pass

    def IsBarHidden(self, view, barIndex):
        """
        IsBarHidden(self: Rebar, view: View, barIndex: int) -> bool
        
            Identifies if a given bar in this rebar set is hidden in this view.
        
            view: The view.
            barIndex: The index of the bar from this rebar set.
            Returns: True if the bar is hidden in this view, false otherwise.
        """
        pass

    def IsRebarInSection(self, dBView):
        """
        IsRebarInSection(self: Rebar, dBView: View) -> bool
        
            Identifies if this Rebar is shown as a cross-section in the given view.
        
            dBView: The view.
            Returns: True if this Rebar is shown as a cross-section, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: Rebar, view: View3D) -> bool
        
            Checks if this rebar element is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if rebar is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: Rebar, view: View) -> bool
        
            Checks if this rebar element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    @staticmethod
    def RebarShapeMatchesCurvesAndHooks(rebarShape, barType, norm, curves, startHook, endHook, startHookOrient, endHookOrient):
        """ RebarShapeMatchesCurvesAndHooks(rebarShape: RebarShape, barType: RebarBarType, norm: XYZ, curves: IList[Curve], startHook: RebarHookType, endHook: RebarHookType, startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> bool """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def ScaleToBox(self, origin, xVec, yVec):
        """
        ScaleToBox(self: Rebar, origin: XYZ, xVec: XYZ, yVec: XYZ)
            Move and resize the bar to fit within a specified box.
           The arguments are 
             interpreted as an arbitrary
           rectangle in 3D with vertices: origin, 
             origin+xVec,
           origin+xVec+yVec, origin+yVec. The algorithm then
           proceeds 
             as follows. First the bar is given the
           default values of the shape 
             parameters from the shape
           definition. Then, if it is possible to do so 
             without
           violating the shape definition, the parameter values
           are scaled 
             so that the width and height of the shape
           (including bar thickness) match 
             the lengths of xVec and yVec.
           If there is no way to do this within the 
             shape definition
           due to overconstraining, a compromise is attempted, such 
             as
           scaling the whole shape until either the width or the
           height is 
             correct. Finally the shape is rotated to
           match the coordinate system of the 
             box. The algorithm
           is the same one used in one-click placement.
        
        
            origin: One corner of the rectangle.
            xVec: Vector representing the first edge of the rectangle. The length
           must be 
             positive.
        
            yVec: Vector representing the second edge of the rectangle. Must
           be perpendicular 
             to xVec.
        """
        pass

    def ScaleToBoxFor3D(self, origin, xVec, yVec, height):
        """
        ScaleToBoxFor3D(self: Rebar, origin: XYZ, xVec: XYZ, yVec: XYZ, height: float)
            Move and resize a spiral or multiplanar instance to fit within a specified box.
             
           The arguments are interpreted as an arbitrary rectangle in 3D with
           
             vertices: origin, origin+xVec, origin+xVec+yVec, origin+yVec. One end of the
          
              rebar shape is inscribed in this rectangle following the procedure described
         
               for the ScaleToBox method. The other end is placed in the parallel plane at
         
               distance (center-to-center) given by the height argument, in the
           
             direction of (xVec x yVec).
           Note that spiral shapes interpret the input 
             arguments using a different convention
           than multiplanar shapes.  For spiral 
             shapes, the spiral start will be placed in
           the rectangle defined by origin, 
             xVec, yVec, and the end of the spiral will be
           placed in the parallel plane. 
              For multiplanar shapes, the rebar is placed with
           its primary shape 
             definition located in the parallel plane defined by the height
           argument, 
             and its connector segments extending in the direction opposite (xVec x yVec).
         
               This method replaces ScaleToBoxForSpiral() from prior releases.
        
        
            origin: One corner of the rectangle.
            xVec: Vector representing the first edge of the rectangle. The length
           must be 
             positive.
        
            yVec: Vector representing the second edge of the rectangle. Must
           be perpendicular 
             to xVec.
        
            height: New value for the Height or MultiplanarDepth property.
        """
        pass

    def SetBarHiddenStatus(self, view, barIndex, hide):
        """
        SetBarHiddenStatus(self: Rebar, view: View, barIndex: int, hide: bool)
            Sets the bar in this rebar set to be hidden or unhidden in the given view.
        
            view: The view.
            barIndex: The index of the bar from this set.
            hide: True to hide this bar in the view, false to unhide the bar.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetHookOrientation(self, iEnd, hookOrientation):
        """
        SetHookOrientation(self: Rebar, iEnd: int, hookOrientation: RebarHookOrientation)
            Defines the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            hookOrientation: Only two values are permitted:
           Value = Right: The hook is on your right as 
             you stand at the end of the bar,
           with the bar behind you, taking the bar's 
             normal as "up."
           Value = Left: The hook is on your left as you stand at the 
             end of the bar,
           with the bar behind you, taking the bar's normal as "up."
        """
        pass

    def SetHookTypeId(self, end, hookTypeId):
        """
        SetHookTypeId(self: Rebar, end: int, hookTypeId: ElementId)
            Set the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            hookTypeId: The id of a RebarHookType element, or invalidElementId if
           the rebar should 
             have no hook at the specified end.
        """
        pass

    def SetHostId(self, doc, hostId):
        """
        SetHostId(self: Rebar, doc: Document, hostId: ElementId)
            The element that contains the rebar.
        
            doc: The document containing both this element and the host element.
            hostId: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column. The rebar does not need
           to be 
             strictly inside the host, but it must be assigned to one host
           element.
        """
        pass

    def SetLayoutAsFixedNumber(self, numberOfBarPositions, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsFixedNumber(self: Rebar, numberOfBarPositions: int, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to FixedNumber.
        
            numberOfBarPositions: The number of bar positions in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMaximumSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMaximumSpacing(self: Rebar, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MaximumSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMinimumClearSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMinimumClearSpacing(self: Rebar, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MinimumClearSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsNumberWithSpacing(self, numberOfBarPositions, spacing, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsNumberWithSpacing(self: Rebar, numberOfBarPositions: int, spacing: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
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
        SetLayoutAsSingle(self: Rebar)
            Sets the Layout Rule property of rebar set to Single.
        """
        pass

    def SetPresentationMode(self, dBView, presentationMode):
        """
        SetPresentationMode(self: Rebar, dBView: View, presentationMode: RebarPresentationMode)
            Sets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            presentationMode: The presentation mode.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: Rebar, view: View3D, solid: bool)
            Sets this rebar element to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if rebar is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: Rebar, view: View, unobscured: bool)
            Sets this rebar element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if rebar is shown unobscured, false otherwise.
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

Get: ArrayLength(self: Rebar) -> float

Set: ArrayLength(self: Rebar) = value
"""

    BarsOnNormalSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.

Get: BarsOnNormalSide(self: Rebar) -> bool

Set: BarsOnNormalSide(self: Rebar) = value
"""

    BaseFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the lower end of the spiral.

Get: BaseFinishingTurns(self: Rebar) -> int

Set: BaseFinishingTurns(self: Rebar) = value
"""

    DistributionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of rebar distribution(also known as Rebar Set Type).

Get: DistributionType(self: Rebar) -> DistributionType

Set: DistributionType(self: Rebar) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the overall height.

Get: Height(self: Rebar) -> float

Set: Height(self: Rebar) = value
"""

    IncludeFirstBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the first bar in rebar set is shown.

Get: IncludeFirstBar(self: Rebar) -> bool

Set: IncludeFirstBar(self: Rebar) = value
"""

    IncludeLastBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the last bar in rebar set is shown.

Get: IncludeLastBar(self: Rebar) -> bool

Set: IncludeLastBar(self: Rebar) = value
"""

    LayoutRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the layout rule of rebar set.

Get: LayoutRule(self: Rebar) -> RebarLayoutRule

"""

    MaxSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the maximum spacing between rebar in rebar set.

Get: MaxSpacing(self: Rebar) -> float

Set: MaxSpacing(self: Rebar) = value
"""

    MultiplanarDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a multiplanar rebar, the depth of the instance.

Get: MultiplanarDepth(self: Rebar) -> float

Set: MultiplanarDepth(self: Rebar) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unit-length vector normal to the plane of the rebar

Get: Normal(self: Rebar) -> XYZ

"""

    NumberOfBarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of potential bars in the set.

Get: NumberOfBarPositions(self: Rebar) -> int

Set: NumberOfBarPositions(self: Rebar) = value
"""

    Pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the pitch, or vertical distance traveled in one rotation.

Get: Pitch(self: Rebar) -> float

Set: Pitch(self: Rebar) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the number of bars in rebar set.

Get: Quantity(self: Rebar) -> int

"""

    RebarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the rebar.

Get: RebarShapeId(self: Rebar) -> ElementId

Set: RebarShapeId(self: Rebar) = value
"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: Rebar) -> str

Set: ScheduleMark(self: Rebar) = value
"""

    TopFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the upper end of the spiral.

Get: TopFinishingTurns(self: Rebar) -> int

Set: TopFinishingTurns(self: Rebar) = value
"""

    TotalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of an individual bar multiplied by Quantity.

Get: TotalLength(self: Rebar) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of an individual bar multiplied by Quantity.

Get: Volume(self: Rebar) -> float

"""



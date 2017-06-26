class DatumPlane(Element, IDisposable):
    """ A base class representing a datum surface (level, grid or reference plane) in Autodesk Revit. """
    def AddLeader(self, datumEnd, view):
        """
        AddLeader(self: DatumPlane, datumEnd: DatumEnds, view: View) -> Leader
        
            Adds a default Leader for the indicated end of the datum plane. This method 
             does not apply to Reference planes (which do not support leaders).
        
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            Returns: The Leader of the datum plane. Null will return if the view is null.
        """
        pass

    def CanBeVisibleInView(self, view):
        """
        CanBeVisibleInView(self: DatumPlane, view: View) -> bool
        
            Checks if the datum plane can be visible in the view.
        
            view: The view.
            Returns: True if visible, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurvesInView(self, extentMode, view):
        """
        GetCurvesInView(self: DatumPlane, extentMode: DatumExtentType, view: View) -> IList[Curve]
        
            Gets a collection of curves representing the DatumPlane element in the given 
             view.
        
        
            extentMode: The extent type.
            view: The view.
            Returns: The curves.
        """
        pass

    def GetDatumExtentTypeInView(self, datumEnd, view):
        """
        GetDatumExtentTypeInView(self: DatumPlane, datumEnd: DatumEnds, view: View) -> DatumExtentType
        
            Identifies if the end of the datum plane is aligned with 3D extents or is set 
             to vary specifically in the indicated view.
        
        
            datumEnd: The end of the datum plane.
            view: The view in which to evaluate the datum extent settings.
            Returns: The extent type.
        """
        pass

    def GetLeader(self, datumEnd, view):
        """
        GetLeader(self: DatumPlane, datumEnd: DatumEnds, view: View) -> Leader
        
            Gets a copy of the leader applied to the indicated end of the datum plane. This 
             method does not apply to Reference planes (which do not support leaders).
        
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            Returns: The Leader of the datum plane. Null will return if no leader applied.
        """
        pass

    def GetPropagationViews(self, view):
        """
        GetPropagationViews(self: DatumPlane, view: View) -> ISet[ElementId]
        
            Gets a list of candidate views which are parallel to the current view and to 
             which the extents of the datum may be propagated.
        
        
            view: The view on which the DatumPlane shows.
            Returns: A set of ElementIds of the parallel views for extent propagation.
        """
        pass

    def HasBubbleInView(self, datumEnd, view):
        """
        HasBubbleInView(self: DatumPlane, datumEnd: DatumEnds, view: View) -> bool
        
            Identifies if the DatumPlane has bubble or not.
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            Returns: True if the DatumPlane has bubble, false otherwise.
        """
        pass

    def HideBubbleInView(self, datumEnd, view):
        """
        HideBubbleInView(self: DatumPlane, datumEnd: DatumEnds, view: View)
            Hides the bubble in a view. This method does not apply to Reference planes.
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
        """
        pass

    def IsBubbleVisibleInView(self, datumEnd, view):
        """
        IsBubbleVisibleInView(self: DatumPlane, datumEnd: DatumEnds, view: View) -> bool
        
            Identifies if the bubble is visible or not in a view.
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            Returns: True if the bubble is visible, false otherwise.
        """
        pass

    def IsCurveValidInView(self, extentMode, view, curve):
        """
        IsCurveValidInView(self: DatumPlane, extentMode: DatumExtentType, view: View, curve: Curve) -> bool
        
            Checks if the curve is valid to be as the extents for the datum plane in a 
             view.
           The curve must be bound and coincident with the original one of the 
             datum plane.
        
        
            extentMode: The extent type.
            view: The view.
            curve: The curve.
            Returns: True if it is valid, false otherwise.
        """
        pass

    def IsLeaderValid(self, datumEnd, view, leader):
        """
        IsLeaderValid(self: DatumPlane, datumEnd: DatumEnds, view: View, leader: Leader) -> bool
        
            Identifies if the leader valid or not for this DatumPlane. This method does not 
             apply to Reference planes (which do not support leaders).
        
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            leader: The Leader for setting the datum plane.
            Returns: True if the leader is valid for set leader, false otherwise.
        """
        pass

    def Maximize3DExtents(self):
        """
        Maximize3DExtents(self: DatumPlane)
            Maximizes the 3d extents of the datum plane in all possible views.
        """
        pass

    def PropagateToViews(self, view, parallelViews):
        """ PropagateToViews(self: DatumPlane, view: View, parallelViews: ISet[ElementId]) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetCurveInView(self, extentMode, view, curve):
        """
        SetCurveInView(self: DatumPlane, extentMode: DatumExtentType, view: View, curve: Curve)
            Sets the extents to match the curve.
        
            extentMode: The extent type.
            view: The view.
            curve: The curve.
        """
        pass

    def SetDatumExtentType(self, datumEnd, view, extentMode):
        """
        SetDatumExtentType(self: DatumPlane, datumEnd: DatumEnds, view: View, extentMode: DatumExtentType)
            Sets whether or not the end of the datum plane is aligned with 3D extents or is 
             set to vary specifically in the indicated view.
        
        
            datumEnd: Specifies one end of the datum plane in the view.
            view: The view in which to evaluate the datum extent settings.
            extentMode: The DatumExtentType.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetLeader(self, datumEnd, view, pLeader):
        """
        SetLeader(self: DatumPlane, datumEnd: DatumEnds, view: View, pLeader: Leader)
            Sets the leader to the indicated end of the datum plane. This method does not 
             apply to Reference planes (which do not support leaders).
        
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
            pLeader: The Leader for setting the datum plane.
        """
        pass

    def ShowBubbleInView(self, datumEnd, view):
        """
        ShowBubbleInView(self: DatumPlane, datumEnd: DatumEnds, view: View)
            Shows the bubble in a view. This method does not apply to Reference planes.
        
            datumEnd: The end of the datum plane.
            view: The view on which the DatumPlane shows.
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


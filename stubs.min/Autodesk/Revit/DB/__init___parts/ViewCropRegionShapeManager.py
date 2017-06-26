class ViewCropRegionShapeManager(object, IDisposable):
    """ A class that provides access to settings related to the crop assigned to a view or a reference callout. """
    def Dispose(self):
        """ Dispose(self: ViewCropRegionShapeManager) """
        pass

    def GetAnnotationCropShape(self):
        """
        GetAnnotationCropShape(self: ViewCropRegionShapeManager) -> CurveLoop
        
            Gets the annotation crop box assigned to the view.
            Returns: The annotation crop boundary.
        """
        pass

    def GetCropShape(self):
        """
        GetCropShape(self: ViewCropRegionShapeManager) -> IList[CurveLoop]
        
            Gets the crop boundaries that are curently active.
            Returns: The crop boundaries.
        """
        pass

    def GetSplitRegionMaximum(self, regionIndex):
        """
        GetSplitRegionMaximum(self: ViewCropRegionShapeManager, regionIndex: int) -> float
        
            Returns the proportional location of the maximum boundary of the specified 
             split crop region.
        
        
            regionIndex: Index of region to be split horizontally (numbering starts with 0).
            Returns: A value from 0 to 1 representing the maximum location for the regions split 
             boundary.
           This number represents the location as a ratio along the 
             non-split rectangular crop.
        """
        pass

    def GetSplitRegionMinimum(self, regionIndex):
        """
        GetSplitRegionMinimum(self: ViewCropRegionShapeManager, regionIndex: int) -> float
        
            Returns the proportional location of the minimum boundary of the specified 
             split crop region.
        
        
            regionIndex: Index of region to be split horizontally (numbering starts with 0).
            Returns: A value from 0 to 1 representing the minimum location for the regions split 
             boundary.
           This number represents the location as a ratio along the 
             non-split rectangular crop.
        """
        pass

    def IsCropRegionShapeValid(self, boundary):
        """
        IsCropRegionShapeValid(self: ViewCropRegionShapeManager, boundary: CurveLoop) -> bool
        
            Verifies that boundary represents one closed curve loop without 
             self-intersections,
           consisting of non-zero length straight lines in a plane 
             parallel to the view plane.
        
        
            boundary: The crop boundary.
            Returns: True if the passed crop boundary represents one closed curve loop without 
             self-intersections,
           consisting of non-zero length straight lines in a plane 
             parallel to the view plane.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ViewCropRegionShapeManager, disposing: bool) """
        pass

    def RemoveCropRegionShape(self):
        """
        RemoveCropRegionShape(self: ViewCropRegionShapeManager)
            Removes any non-rectangular boundary of the view's crop.
        """
        pass

    def RemoveSplit(self):
        """
        RemoveSplit(self: ViewCropRegionShapeManager)
            Removes any split applied to the view's crop.
        """
        pass

    def RemoveSplitRegion(self, regionIndex):
        """
        RemoveSplitRegion(self: ViewCropRegionShapeManager, regionIndex: int)
            Removes one region in split crop.
        
            regionIndex: Index of region to be deleted (numbering starts with 0).
        """
        pass

    def SetCropShape(self, boundary):
        """
        SetCropShape(self: ViewCropRegionShapeManager, boundary: CurveLoop)
            Sets the boundary of the view's crop to the specified shape.
        
            boundary: The crop boundary.
        """
        pass

    def SplitRegionHorizontally(self, regionIndex, leftPart, rightPart):
        """
        SplitRegionHorizontally(self: ViewCropRegionShapeManager, regionIndex: int, leftPart: float, rightPart: float)
            Splits horizontally one region in split crop.
        
            regionIndex: Index of region to be split horizontally (numbering starts with 0).
            leftPart: Relative portion of the original region to become the new left region (0 to 1).
            rightPart: Relative portion of the original region to become the new right region (0 to 1).
        """
        pass

    def SplitRegionVertically(self, regionIndex, topPart, bottomPart):
        """
        SplitRegionVertically(self: ViewCropRegionShapeManager, regionIndex: int, topPart: float, bottomPart: float)
            Splits vertically one region in split crop.
        
            regionIndex: Index of region to be split vertically (numbering starts with 0).
            topPart: Relative portion of the original region to become the new top region (0 to 1).
            bottomPart: Relative portion of the original region to become the new bottom region (0 to 
             1).
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BottomAnnotationCropOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset from the bottom of the view crop that determines the location of the annotation crop bottom boundary.

Get: BottomAnnotationCropOffset(self: ViewCropRegionShapeManager) -> float

Set: BottomAnnotationCropOffset(self: ViewCropRegionShapeManager) = value
"""

    CanBeSplit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Verifies that the crop of the associated view is permitted to have multiple regions.

Get: CanBeSplit(self: ViewCropRegionShapeManager) -> bool

"""

    CanHaveAnnotationCrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Verifies that the view is allowed to have an annotation crop.

Get: CanHaveAnnotationCrop(self: ViewCropRegionShapeManager) -> bool

"""

    CanHaveShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Verifies that the crop of the associated view is permitted to have a non-rectangular shape.

Get: CanHaveShape(self: ViewCropRegionShapeManager) -> bool

"""

    IsSplitHorizontally = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the view's crop is split (and the split is horizontal).

Get: IsSplitHorizontally(self: ViewCropRegionShapeManager) -> bool

"""

    IsSplitVertically = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the view's crop is split (and the split is vertical).

Get: IsSplitVertically(self: ViewCropRegionShapeManager) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ViewCropRegionShapeManager) -> bool

"""

    LeftAnnotationCropOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset from the left of the view crop that determines the location of the annotation crop left boundary.

Get: LeftAnnotationCropOffset(self: ViewCropRegionShapeManager) -> float

Set: LeftAnnotationCropOffset(self: ViewCropRegionShapeManager) = value
"""

    NumberOfSplitRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of split crop regions (1 if the crop is not currently split).

Get: NumberOfSplitRegions(self: ViewCropRegionShapeManager) -> int

"""

    RightAnnotationCropOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset from the right of the view crop that determines the location of the annotation crop right boundary.

Get: RightAnnotationCropOffset(self: ViewCropRegionShapeManager) -> float

Set: RightAnnotationCropOffset(self: ViewCropRegionShapeManager) = value
"""

    ShapeSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the view crop has a non-rectangular shape set.

Get: ShapeSet(self: ViewCropRegionShapeManager) -> bool

"""

    Split = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the view crop is split.

Get: Split(self: ViewCropRegionShapeManager) -> bool

"""

    TopAnnotationCropOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset from the top of the view crop that determines the location of the annotation crop top boundary.

Get: TopAnnotationCropOffset(self: ViewCropRegionShapeManager) -> float

Set: TopAnnotationCropOffset(self: ViewCropRegionShapeManager) = value
"""



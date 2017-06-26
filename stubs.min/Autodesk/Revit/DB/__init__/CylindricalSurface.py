class CylindricalSurface(Surface, IDisposable):
    """ A cylindrical surface. """
    @staticmethod
    def Create(frameOfReference, radius):
        """
        Create(frameOfReference: Frame, radius: float) -> CylindricalSurface
        
            Construct a cylindrical surface defined by a local coordinate system and a 
             radius.
        
        
            frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 
             for the cylinder.
           Frame.Origin is a point on the cylinder's axis. 
             Frame.BasisZ points along the axis, while Frame.BasisX and Frame.BasisY are 
             orthogonal to the axis. The frame may be either left-handed or right-handed 
             (see Frame.IsRightHanded). Note that
           the "handedness" of the frame does 
             not, by itself, determine the surface's orientation.
        
            radius: Radius of the circle that defines the base of the cylindrical surface.
            Returns: The created CylindricalSurface.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Surface, A_0: bool) """
        pass

    def GetFrameOfReference(self):
        """
        GetFrameOfReference(self: CylindricalSurface) -> Frame
        
            Returns frame of reference associated with this CylindricalSurface.
            Returns: Frame of reference associated with this CylindricalSurface.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Surface, disposing: bool) """
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

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Axis of the cylinder. This is the Z axis of the local coordinate system associated with this cylinder.

Get: Axis(self: CylindricalSurface) -> XYZ

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Center of the circle that defines the base of the cylinder. This is the origin of the local coordinate system associated with this cylinder.

Get: Origin(self: CylindricalSurface) -> XYZ

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radius of the circle that defines the base of this cylinder.

Get: Radius(self: CylindricalSurface) -> float

"""

    XDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X axis of the local coordinate system associated with this cylinder.

Get: XDir(self: CylindricalSurface) -> XYZ

"""

    YDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X axis of the local coordinate system associated with this cylinder.

Get: YDir(self: CylindricalSurface) -> XYZ

"""



class Frame(object, IDisposable):
    """
    A Frame comprises three vectors at a base point in 3D space.
    
    Frame(origin: XYZ, vec1: XYZ, vec2: XYZ, vec3: XYZ)
    Frame()
    """
    @staticmethod
    def CanDefineRevitGeometry(frameOfReference):
        """
        CanDefineRevitGeometry(frameOfReference: Frame) -> bool
        
            Tests whether the supplied Frame object may be used to define a Revit curve or 
             surface.
           In order to satisfy the requirements the Frame must be orthonormal
             
           and its origin is expected to lie within the Revit design limits 
             Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).
        
        
            frameOfReference: Frame to be validated.
            Returns: True if this Frame may be used as a local frame of reference, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Frame) """
        pass

    def IsOrthogonal(self):
        """
        IsOrthogonal(self: Frame) -> bool
        
            Determines if this frame's basis vectors are orthogonal.
            Returns: True if this frame's basis vectors are orthogonal, false if not.
        """
        pass

    def IsOrthonormal(self):
        """
        IsOrthonormal(self: Frame) -> bool
        
            Determines if this frame's basis vectors are orthonormal.
            Returns: True if this frame's basis vectors are orthonormal, false if not.
        """
        pass

    def IsRightHanded(self):
        """
        IsRightHanded(self: Frame) -> bool
        
            Determine if this frame's basis is right-handed.
            Returns: True if this frame's basis is right-handed, false if not.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Frame, disposing: bool) """
        pass

    def Transform(self, trf):
        """
        Transform(self: Frame, trf: Transform)
            Applies the input transform to this frame.
        
            trf: The transform to apply to the frame.
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

    @staticmethod # known case of __new__
    def __new__(self, origin=None, vec1=None, vec2=None, vec3=None):
        """
        __new__(cls: type, origin: XYZ, vec1: XYZ, vec2: XYZ, vec3: XYZ)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BasisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The first basis vector of the frame.

Get: BasisX(self: Frame) -> XYZ

Set: BasisX(self: Frame) = value
"""

    BasisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The second basis vector of the frame.

Get: BasisY(self: Frame) -> XYZ

Set: BasisY(self: Frame) = value
"""

    BasisZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The third basis vector of the frame.

Get: BasisZ(self: Frame) -> XYZ

Set: BasisZ(self: Frame) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Frame) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The frame's base point.

Get: Origin(self: Frame) -> XYZ

Set: Origin(self: Frame) = value
"""



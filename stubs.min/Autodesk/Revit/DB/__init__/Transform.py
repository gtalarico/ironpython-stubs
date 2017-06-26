class Transform(APIObject, IDisposable):
    """
    A transformation of the affine 3-space.
    
    Transform(source: Transform)
    """
    def AlmostEqual(self, right):
        """
        AlmostEqual(self: Transform, right: Transform) -> bool
        
            Determines whether this transformation and the specified transformation are the 
             same within the tolerance (1.0e-09).
        
        
            right: The transformation to compare with this transformation.
            Returns: True if the two transformations are equal; otherwise, false.
        """
        pass

    @staticmethod
    def CreateReflection(plane):
        """
        CreateReflection(plane: Plane) -> Transform
        
            Creates a transform that represents a reflection across the given plane.
        
            plane: The plane.
            Returns: The new transform.
        """
        pass

    @staticmethod
    def CreateRotation(axis, angle):
        """
        CreateRotation(axis: XYZ, angle: float) -> Transform
        
            Creates a transform that represents a rotation about the given axis at (0, 0, 
             0).
        
        
            axis: The rotation axis.
            angle: The angle.
            Returns: The new transform.
        """
        pass

    @staticmethod
    def CreateRotationAtPoint(axis, angle, origin):
        """
        CreateRotationAtPoint(axis: XYZ, angle: float, origin: XYZ) -> Transform
        
            Creates a transform that represents a rotation about the given axis at the 
             specified point.
        
        
            axis: The rotation axis.
            angle: The angle.
            origin: The origin point.
            Returns: The new transform.
        """
        pass

    @staticmethod
    def CreateTranslation(vector):
        """
        CreateTranslation(vector: XYZ) -> Transform
        
            Creates a transform that represents a translation via the specified vector.
        
            vector: The translation vector.
            Returns: The new transform.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def Multiply(self, right):
        """
        Multiply(self: Transform, right: Transform) -> Transform
        
            Multiplies this transformation by the specified transformation and returns the 
             result.
        
        
            right: The specified transformation.
            Returns: The transformation equal to the composition of the two transformations.
        """
        pass

    def OfPoint(self, point):
        """
        OfPoint(self: Transform, point: XYZ) -> XYZ
        
            Applies the transformation to the point and returns the result.
        
            point: The point to transform.
            Returns: The transformed point.
        """
        pass

    def OfVector(self, vec):
        """
        OfVector(self: Transform, vec: XYZ) -> XYZ
        
            Applies the transform to the vector
        
            vec: The vector to be transformed
            Returns: The new vector after transform
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Transform) """
        pass

    def ScaleBasis(self, scale):
        """
        ScaleBasis(self: Transform, scale: float) -> Transform
        
            Scales the basis vectors of this transformation and returns the result.
        
            scale: The scale value.
            Returns: The transformation equal to the composition of the two transformations.
        """
        pass

    def ScaleBasisAndOrigin(self, scale):
        """
        ScaleBasisAndOrigin(self: Transform, scale: float) -> Transform
        
            Scales the basis vectors and the origin of this transformation and returns the 
             result.
        
        
            scale: The scale value.
            Returns: The transformation equal to the composition of the two transformations.
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

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source):
        """ __new__(cls: type, source: Transform) """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(left: Transform, right: Transform) -> Transform
        
            Multiplies the two specified transforms.
        
            left: The first transformation.
            right: The second transformation.
            Returns: The transformation equal to the composition of the two transformations.
        """
        pass

    BasisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The basis of the X axis of this transformation.

Get: BasisX(self: Transform) -> XYZ

Set: BasisX(self: Transform) = value
"""

    BasisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The basis of the Y axis of this transformation.

Get: BasisY(self: Transform) -> XYZ

Set: BasisY(self: Transform) = value
"""

    BasisZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The basis of the Z axis of this transformation.

Get: BasisZ(self: Transform) -> XYZ

Set: BasisZ(self: Transform) = value
"""

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The determinant of this transformation.

Get: Determinant(self: Transform) -> float

"""

    HasReflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boolean value that indicates whether this transformation produces reflection.

Get: HasReflection(self: Transform) -> bool

"""

    Inverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The inverse transformation of this transformation.

Get: Inverse(self: Transform) -> Transform

"""

    IsConformal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boolean value that indicates whether this transformation is conformal.

Get: IsConformal(self: Transform) -> bool

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boolean value that indicates whether this transformation is an identity.

Get: IsIdentity(self: Transform) -> bool

"""

    IsTranslation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boolean value that indicates whether this transformation is a translation.

Get: IsTranslation(self: Transform) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the origin of the old coordinate system in the new coordinate system.

Get: Origin(self: Transform) -> XYZ

Set: Origin(self: Transform) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The real number that represents the scale of the transformation.

Get: Scale(self: Transform) -> float

"""


    Identity = None


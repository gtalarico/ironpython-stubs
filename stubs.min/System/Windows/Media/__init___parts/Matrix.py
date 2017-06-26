class Matrix(object, IFormattable):
    """
    Represents a 3x3 affine transformation matrix used for transformations in 2-D space.
    
    Matrix(m11: float, m12: float, m21: float, m22: float, offsetX: float, offsetY: float)
    """
    def Append(self, matrix):
        """
        Append(self: Matrix, matrix: Matrix)
            Appends the specified System.Windows.Media.Matrix structure to this System.Windows.Media.Matrix structure.
        
            matrix: The System.Windows.Media.Matrix structure to append to this System.Windows.Media.Matrix structure.
        """
        pass

    @staticmethod
    def Equals(*__args):
        """
        Equals(self: Matrix, value: Matrix) -> bool
        
            Determines whether the specified System.Windows.Media.Matrix structure is identical to this instance.
        
            value: The instance of System.Windows.Media.Matrix to compare to this instance.
            Returns: true if instances are equal; otherwise, false.
        Equals(self: Matrix, o: object) -> bool
        
            Determines whether the specified System.Object is a System.Windows.Media.Matrix structure that is identical to this System.Windows.Media.Matrix.
        
            o: The System.Object to compare.
            Returns: true if o is a System.Windows.Media.Matrix structure that is identical to this System.Windows.Media.Matrix structure; otherwise, false.
        Equals(matrix1: Matrix, matrix2: Matrix) -> bool
        
            Determines whether the two specified System.Windows.Media.Matrix structures are identical.
        
            matrix1: The first System.Windows.Media.Matrix structure to compare.
            matrix2: The second System.Windows.Media.Matrix structure to compare.
            Returns: true if matrix1 and matrix2 are identical; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Matrix) -> int
        
            Returns the hash code for this System.Windows.Media.Matrix structure.
            Returns: The hash code for this instance.
        """
        pass

    def Invert(self):
        """
        Invert(self: Matrix)
            Inverts this System.Windows.Media.Matrix structure.
        """
        pass

    @staticmethod
    def Multiply(trans1, trans2):
        """
        Multiply(trans1: Matrix, trans2: Matrix) -> Matrix
        
            Multiplies a System.Windows.Media.Matrix structure by another System.Windows.Media.Matrix structure.
        
            trans1: The first System.Windows.Media.Matrix structure to multiply.
            trans2: The second System.Windows.Media.Matrix structure to multiply.
            Returns: The result of multiplying trans1 by trans2.
        """
        pass

    @staticmethod
    def Parse(source):
        """
        Parse(source: str) -> Matrix
        
            Converts a System.String representation of a matrix into the equivalent System.Windows.Media.Matrix structure.
        
            source: The System.String representation of the matrix.
            Returns: The equivalent System.Windows.Media.Matrix structure.
        """
        pass

    def Prepend(self, matrix):
        """
        Prepend(self: Matrix, matrix: Matrix)
            Prepends the specified System.Windows.Media.Matrix structure onto this System.Windows.Media.Matrix structure.
        
            matrix: The System.Windows.Media.Matrix structure to prepend to this System.Windows.Media.Matrix structure.
        """
        pass

    def Rotate(self, angle):
        """
        Rotate(self: Matrix, angle: float)
            Applies a rotation of the specified angle about the origin of this System.Windows.Media.Matrix structure.
        
            angle: The angle of rotation.
        """
        pass

    def RotateAt(self, angle, centerX, centerY):
        """
        RotateAt(self: Matrix, angle: float, centerX: float, centerY: float)
            Rotates this matrix about the specified point.
        
            angle: The angle, in degrees, by which to rotate this matrix.
            centerX: The x-coordinate of the point about which to rotate this matrix.
            centerY: The y-coordinate of the point about which to rotate this matrix.
        """
        pass

    def RotateAtPrepend(self, angle, centerX, centerY):
        """
        RotateAtPrepend(self: Matrix, angle: float, centerX: float, centerY: float)
            Prepends a rotation of the specified angle at the specified point to this System.Windows.Media.Matrix structure.
        
            angle: The rotation angle, in degrees.
            centerX: The x-coordinate of the rotation center.
            centerY: The y-coordinate of the rotation center.
        """
        pass

    def RotatePrepend(self, angle):
        """
        RotatePrepend(self: Matrix, angle: float)
            Prepends a rotation of the specified angle to this System.Windows.Media.Matrix structure.
        
            angle: The angle of rotation to prepend.
        """
        pass

    def Scale(self, scaleX, scaleY):
        """
        Scale(self: Matrix, scaleX: float, scaleY: float)
            Appends the specified scale vector to this System.Windows.Media.Matrix structure.
        
            scaleX: The value by which to scale this System.Windows.Media.Matrix along the x-axis.
            scaleY: The value by which to scale this System.Windows.Media.Matrix along the y-axis.
        """
        pass

    def ScaleAt(self, scaleX, scaleY, centerX, centerY):
        """
        ScaleAt(self: Matrix, scaleX: float, scaleY: float, centerX: float, centerY: float)
            Scales this System.Windows.Media.Matrix by the specified amount about the specified point.
        
            scaleX: The amount by which to scale this System.Windows.Media.Matrix along the x-axis.
            scaleY: The amount by which to scale this System.Windows.Media.Matrix along the y-axis.
            centerX: The x-coordinate of the scale operation's center point.
            centerY: The y-coordinate of the scale operation's center point.
        """
        pass

    def ScaleAtPrepend(self, scaleX, scaleY, centerX, centerY):
        """
        ScaleAtPrepend(self: Matrix, scaleX: float, scaleY: float, centerX: float, centerY: float)
            Prepends the specified scale about the specified point of this System.Windows.Media.Matrix.
        
            scaleX: The x-axis scale factor.
            scaleY: The y-axis scale factor.
            centerX: The x-coordinate of the point about which the scale operation is performed.
            centerY: The y-coordinate of the point about which the scale operation is performed.
        """
        pass

    def ScalePrepend(self, scaleX, scaleY):
        """
        ScalePrepend(self: Matrix, scaleX: float, scaleY: float)
            Prepends the specified scale vector to this System.Windows.Media.Matrix structure.
        
            scaleX: The value by which to scale this System.Windows.Media.Matrix structure along the x-axis.
            scaleY: The value by which to scale this System.Windows.Media.Matrix structure along the y-axis.
        """
        pass

    def SetIdentity(self):
        """
        SetIdentity(self: Matrix)
            Changes this System.Windows.Media.Matrix structure into an identity matrix.
        """
        pass

    def Skew(self, skewX, skewY):
        """
        Skew(self: Matrix, skewX: float, skewY: float)
            Appends a skew of the specified degrees in the x and y dimensions to this System.Windows.Media.Matrix structure.
        
            skewX: The angle in the x dimension by which to skew this System.Windows.Media.Matrix.
            skewY: The angle in the y dimension by which to skew this System.Windows.Media.Matrix.
        """
        pass

    def SkewPrepend(self, skewX, skewY):
        """
        SkewPrepend(self: Matrix, skewX: float, skewY: float)
            Prepends a skew of the specified degrees in the x and y dimensions to this System.Windows.Media.Matrix structure.
        
            skewX: The angle in the x dimension by which to skew this System.Windows.Media.Matrix.
            skewY: The angle in the y dimension by which to skew this System.Windows.Media.Matrix.
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: Matrix, provider: IFormatProvider) -> str
        
            Creates a System.String representation of this System.Windows.Media.Matrix structure with culture-specific formatting information.
        
            provider: The culture-specific formatting information.
            Returns: A System.String containing the System.Windows.Media.Matrix.M11, System.Windows.Media.Matrix.M12, System.Windows.Media.Matrix.M21, System.Windows.Media.Matrix.M22, System.Windows.Media.Matrix.OffsetX, and 
             System.Windows.Media.Matrix.OffsetY values of this System.Windows.Media.Matrix.
        
        ToString(self: Matrix) -> str
        
            Creates a System.String representation of this System.Windows.Media.Matrix structure.
            Returns: A System.String containing the System.Windows.Media.Matrix.M11, System.Windows.Media.Matrix.M12, System.Windows.Media.Matrix.M21, System.Windows.Media.Matrix.M22, System.Windows.Media.Matrix.OffsetX, and 
             System.Windows.Media.Matrix.OffsetY values of this System.Windows.Media.Matrix.
        """
        pass

    def Transform(self, *__args):
        """
        Transform(self: Matrix, vector: Vector) -> Vector
        
            Transforms the specified vector by this System.Windows.Media.Matrix.
        
            vector: The vector to transform.
            Returns: The result of transforming vector by this System.Windows.Media.Matrix.
        Transform(self: Matrix, vectors: Array[Vector])
            Transforms the specified vectors by this System.Windows.Media.Matrix.
        
            vectors: The vectors to transform. The original vectors in the array are replaced by their transformed values.
        Transform(self: Matrix, point: Point) -> Point
        
            Transforms the specified point by the System.Windows.Media.Matrix and returns the result.
        
            point: The point to transform.
            Returns: The result of transforming point by this System.Windows.Media.Matrix.
        Transform(self: Matrix, points: Array[Point])
            Transforms the specified points by this System.Windows.Media.Matrix.
        
            points: The points to transform. The original points in the array are replaced by their transformed values.
        """
        pass

    def Translate(self, offsetX, offsetY):
        """
        Translate(self: Matrix, offsetX: float, offsetY: float)
            Appends a translation of the specified offsets to this System.Windows.Media.Matrix structure.
        
            offsetX: The amount to offset this System.Windows.Media.Matrix along the x-axis.
            offsetY: The amount to offset this System.Windows.Media.Matrix along the y-axis.
        """
        pass

    def TranslatePrepend(self, offsetX, offsetY):
        """
        TranslatePrepend(self: Matrix, offsetX: float, offsetY: float)
            Prepends a translation of the specified offsets to this System.Windows.Media.Matrix structure.
        
            offsetX: The amount to offset this System.Windows.Media.Matrix along the x-axis.
            offsetY: The amount to offset this System.Windows.Media.Matrix along the y-axis.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, m11, m12, m21, m22, offsetX, offsetY):
        """
        __new__(cls: type, m11: float, m12: float, m21: float, m22: float, offsetX: float, offsetY: float)
        __new__[Matrix]() -> Matrix
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(trans1: Matrix, trans2: Matrix) -> Matrix
        
            Multiplies a System.Windows.Media.Matrix structure by another System.Windows.Media.Matrix structure.
        
            trans1: The first System.Windows.Media.Matrix structure to multiply.
            trans2: The second System.Windows.Media.Matrix structure to multiply.
            Returns: The result of multiplying trans1 by trans2.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the determinant of this System.Windows.Media.Matrix structure.

Get: Determinant(self: Matrix) -> float

"""

    HasInverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Media.Matrix structure is invertible.

Get: HasInverse(self: Matrix) -> bool

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Media.Matrix structure is an identity matrix.

Get: IsIdentity(self: Matrix) -> bool

"""

    M11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the first row and first column of this System.Windows.Media.Matrix structure.

Get: M11(self: Matrix) -> float

Set: M11(self: Matrix) = value
"""

    M12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the first row and second column of this System.Windows.Media.Matrix structure.

Get: M12(self: Matrix) -> float

Set: M12(self: Matrix) = value
"""

    M21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the second row and first column of this System.Windows.Media.Matrix structure.

Get: M21(self: Matrix) -> float

Set: M21(self: Matrix) = value
"""

    M22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the second row and second column of this System.Windows.Media.Matrix structure.

Get: M22(self: Matrix) -> float

Set: M22(self: Matrix) = value
"""

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the third row and first column of this System.Windows.Media.Matrix structure.

Get: OffsetX(self: Matrix) -> float

Set: OffsetX(self: Matrix) = value
"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the third row and second column of this System.Windows.Media.Matrix structure.

Get: OffsetY(self: Matrix) -> float

Set: OffsetY(self: Matrix) = value
"""


    Identity = None


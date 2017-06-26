class Rect(object, IFormattable):
    """
    Describes the width, height, and location of a rectangle.
    
    Rect(location: Point, size: Size)
    Rect(x: float, y: float, width: float, height: float)
    Rect(point1: Point, point2: Point)
    Rect(point: Point, vector: Vector)
    Rect(size: Size)
    """
    def Contains(self, *__args):
        """
        Contains(self: Rect, rect: Rect) -> bool
        
            Indicates whether the rectangle contains the specified rectangle.
        
            rect: The rectangle to check.
            Returns: true if rect is entirely contained by the rectangle; otherwise, false.
        Contains(self: Rect, x: float, y: float) -> bool
        
            Indicates whether the rectangle contains the specified x-coordinate and y-coordinate.
        
            x: The x-coordinate of the point to check.
            y: The y-coordinate of the point to check.
            Returns: true if (x, y) is contained by the rectangle; otherwise, false.
        Contains(self: Rect, point: Point) -> bool
        
            Indicates whether the rectangle contains the specified point.
        
            point: The point to check.
            Returns: true if the rectangle contains the specified point; otherwise, false.
        """
        pass

    @staticmethod
    def Equals(*__args):
        """
        Equals(self: Rect, value: Rect) -> bool
        
            Indicates whether the specified rectangle is equal to the current rectangle.
        
            value: The rectangle to compare to the current rectangle.
            Returns: true if the specified rectangle has the same System.Windows.Rect.Location and System.Windows.Rect.Size values as the current rectangle; otherwise, false.
        Equals(self: Rect, o: object) -> bool
        
            Indicates whether the specified object is equal to the current rectangle.
        
            o: The object to compare to the current rectangle.
            Returns: true if o is a System.Windows.Rect and has the same System.Windows.Rect.Location and System.Windows.Rect.Size values as the current rectangle; otherwise, false.
        Equals(rect1: Rect, rect2: Rect) -> bool
        
            Indicates whether the specified rectangles are equal.
        
            rect1: The first rectangle to compare.
            rect2: The second rectangle to compare.
            Returns: true if the rectangles have the same System.Windows.Rect.Location and System.Windows.Rect.Size values; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Rect) -> int
        
            Creates a hash code for the rectangle.
            Returns: A hash code for the current System.Windows.Rect structure.
        """
        pass

    def Inflate(self, *__args):
        """
        Inflate(rect: Rect, size: Size) -> Rect
        
            Returns the rectangle that results from expanding the specified rectangle by the specified System.Windows.Size, in all directions.
        
            rect: The System.Windows.Rect structure to modify.
            size: Specifies the amount to expand the rectangle. The System.Windows.Size structure's System.Windows.Size.Width property specifies the amount to increase the rectangle's System.Windows.Rect.Left and 
             System.Windows.Rect.Right properties. The System.Windows.Size structure's System.Windows.Size.Height property specifies the amount to increase the rectangle's System.Windows.Rect.Top and 
             System.Windows.Rect.Bottom properties.
        
            Returns: The resulting rectangle.
        Inflate(rect: Rect, width: float, height: float) -> Rect
        
            Creates a rectangle that results from expanding or shrinking the specified rectangle by the specified width and height amounts, in all directions.
        
            rect: The System.Windows.Rect structure to modify.
            width: The amount by which to expand or shrink the left and right sides of the rectangle.
            height: The amount by which to expand or shrink the top and bottom sides of the rectangle.
            Returns: The resulting rectangle.
        Inflate(self: Rect, size: Size)
            Expands the rectangle by using the specified System.Windows.Size, in all directions.
        
            size: Specifies the amount to expand the rectangle. The System.Windows.Size structure's System.Windows.Size.Width property specifies the amount to increase the rectangle's System.Windows.Rect.Left and 
             System.Windows.Rect.Right properties. The System.Windows.Size structure's System.Windows.Size.Height property specifies the amount to increase the rectangle's System.Windows.Rect.Top and 
             System.Windows.Rect.Bottom properties.
        
        Inflate(self: Rect, width: float, height: float)
            Expands or shrinks the rectangle by using the specified width and height amounts, in all directions.
        
            width: The amount by which to expand or shrink the left and right sides of the rectangle.
            height: The amount by which to expand or shrink the top and bottom sides of the rectangle.
        """
        pass

    def Intersect(self, *__args):
        """
        Intersect(rect1: Rect, rect2: Rect) -> Rect
        
            Returns the intersection of the specified rectangles.
        
            rect1: The first rectangle to compare.
            rect2: The second rectangle to compare.
            Returns: The intersection of the two rectangles, or System.Windows.Rect.Empty if no intersection exists.
        Intersect(self: Rect, rect: Rect)
            Finds the intersection of the current rectangle and the specified rectangle, and stores the result as the current rectangle.
        
            rect: The rectangle to intersect with the current rectangle.
        """
        pass

    def IntersectsWith(self, rect):
        """
        IntersectsWith(self: Rect, rect: Rect) -> bool
        
            Indicates whether the specified rectangle intersects with the current rectangle.
        
            rect: The rectangle to check.
            Returns: true if the specified rectangle intersects with the current rectangle; otherwise, false.
        """
        pass

    def Offset(self, *__args):
        """
        Offset(rect: Rect, offsetVector: Vector) -> Rect
        
            Returns a rectangle that is offset from the specified rectangle by using the specified vector.
        
            rect: The original rectangle.
            offsetVector: A vector that specifies the horizontal and vertical offsets for the new rectangle.
            Returns: The resulting rectangle.
        Offset(rect: Rect, offsetX: float, offsetY: float) -> Rect
        
            Returns a rectangle that is offset from the specified rectangle by using the specified horizontal and vertical amounts.
        
            rect: The rectangle to move.
            offsetX: The horizontal offset for the new rectangle.
            offsetY: The vertical offset for the new rectangle.
            Returns: The resulting rectangle.
        Offset(self: Rect, offsetVector: Vector)
            Moves the rectangle by the specified vector.
        
            offsetVector: A vector that specifies the horizontal and vertical amounts to move the rectangle.
        Offset(self: Rect, offsetX: float, offsetY: float)
            Moves the rectangle by the specified horizontal and vertical amounts.
        
            offsetX: The amount to move the rectangle horizontally.
            offsetY: The amount to move the rectangle vertically.
        """
        pass

    @staticmethod
    def Parse(source):
        """
        Parse(source: str) -> Rect
        
            Creates a new rectangle from the specified string representation.
        
            source: The string representation of the rectangle, in the form "x, y, width, height".
            Returns: The resulting rectangle.
        """
        pass

    def Scale(self, scaleX, scaleY):
        """
        Scale(self: Rect, scaleX: float, scaleY: float)
            Multiplies the size of the current rectangle by the specified x and y values.
        
            scaleX: The scale factor in the x-direction.
            scaleY: The scale factor in the y-direction.
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: Rect, provider: IFormatProvider) -> str
        
            Returns a string representation of the rectangle by using the specified format provider.
        
            provider: Culture-specific formatting information.
            Returns: A string representation of the current rectangle that is determined by the specified format provider.
        ToString(self: Rect) -> str
        
            Returns a string representation of the rectangle.
            Returns: A string representation of the current rectangle. The string has the following form: "System.Windows.Rect.X,System.Windows.Rect.Y,System.Windows.Rect.Width,System.Windows.Rect.Height".
        """
        pass

    @staticmethod
    def Transform(*__args):
        """
        Transform(self: Rect, matrix: Matrix)
            Transforms the rectangle by applying the specified matrix.
        
            matrix: A matrix that specifies the transformation to apply.
        Transform(rect: Rect, matrix: Matrix) -> Rect
        
            Returns the rectangle that results from applying the specified matrix to the specified rectangle.
        
            rect: A rectangle that is the basis for the transformation.
            matrix: A matrix that specifies the transformation to apply.
            Returns: The rectangle that results from the operation.
        """
        pass

    def Union(self, *__args):
        """
        Union(self: Rect, point: Point)
            Expands the current rectangle exactly enough to contain the specified point.
        
            point: The point to include.
        Union(rect: Rect, point: Point) -> Rect
        
            Creates a rectangle that is exactly large enough to include the specified rectangle and the specified point.
        
            rect: The rectangle to include.
            point: The point to include.
            Returns: A rectangle that is exactly large enough to contain the specified rectangle and the specified point.
        Union(self: Rect, rect: Rect)
            Expands the current rectangle exactly enough to contain the specified rectangle.
        
            rect: The rectangle to include.
        Union(rect1: Rect, rect2: Rect) -> Rect
        
            Creates a rectangle that is exactly large enough to contain the two specified rectangles.
        
            rect1: The first rectangle to include.
            rect2: The second rectangle to include.
            Returns: The resulting rectangle.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, location: Point, size: Size)
        __new__(cls: type, x: float, y: float, width: float, height: float)
        __new__(cls: type, point1: Point, point2: Point)
        __new__(cls: type, point: Point, vector: Vector)
        __new__(cls: type, size: Size)
        __new__[Rect]() -> Rect
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-axis value of the bottom of the rectangle.

Get: Bottom(self: Rect) -> float

"""

    BottomLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the bottom-left corner of the rectangle

Get: BottomLeft(self: Rect) -> Point

"""

    BottomRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the bottom-right corner of the rectangle.

Get: BottomRight(self: Rect) -> Point

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the rectangle.

Get: Height(self: Rect) -> float

Set: Height(self: Rect) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the rectangle is the System.Windows.Rect.Empty rectangle.

Get: IsEmpty(self: Rect) -> bool

"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-axis value of the left side of the rectangle.

Get: Left(self: Rect) -> float

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the top-left corner of the rectangle.

Get: Location(self: Rect) -> Point

Set: Location(self: Rect) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-axis value of the right side of the rectangle.

Get: Right(self: Rect) -> float

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width and height of the rectangle.

Get: Size(self: Rect) -> Size

Set: Size(self: Rect) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-axis position of the top of the rectangle.

Get: Top(self: Rect) -> float

"""

    TopLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the top-left corner of the rectangle.

Get: TopLeft(self: Rect) -> Point

"""

    TopRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the top-right corner of the rectangle.

Get: TopRight(self: Rect) -> Point

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the rectangle.

Get: Width(self: Rect) -> float

Set: Width(self: Rect) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-axis value of the left side of the rectangle.

Get: X(self: Rect) -> float

Set: X(self: Rect) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-axis value of the top side of the rectangle.

Get: Y(self: Rect) -> float

Set: Y(self: Rect) = value
"""


    Empty = None


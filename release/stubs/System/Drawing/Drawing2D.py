# encoding: utf-8
# module System.Drawing.Drawing2D calls itself Drawing2D
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CustomLineCap(MarshalByRefObject, ICloneable, IDisposable):
    """
    Encapsulates a custom user-defined line cap.
    
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath)
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap)
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: Single)
    """
    def Clone(self):
        """
        Clone(self: CustomLineCap) -> object
        
            Creates an exact copy of this System.Drawing.Drawing2D.CustomLineCap.
            Returns: The System.Drawing.Drawing2D.CustomLineCap this method creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CustomLineCap)
            Releases all resources used by this System.Drawing.Drawing2D.CustomLineCap object.
        """
        pass

    def GetStrokeCaps(self, startCap, endCap):
        """
        GetStrokeCaps(self: CustomLineCap) -> (LineCap, LineCap)
        
            Gets the caps used to start and end lines that make up this custom cap.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetStrokeCaps(self, startCap, endCap):
        """
        SetStrokeCaps(self: CustomLineCap, startCap: LineCap, endCap: LineCap)
            Sets the caps used to start and end lines that make up this custom cap.
        
            startCap: The System.Drawing.Drawing2D.LineCap enumeration used at the beginning of a line within this cap.
            endCap: The System.Drawing.Drawing2D.LineCap enumeration used at the end of a line within this cap.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fillPath, strokePath, baseCap=None, baseInset=None):
        """
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath)
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap)
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: Single)
        """
        pass

    BaseCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Drawing2D.LineCap enumeration on which this System.Drawing.Drawing2D.CustomLineCap is based.

Get: BaseCap(self: CustomLineCap) -> LineCap

Set: BaseCap(self: CustomLineCap) = value
"""

    BaseInset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance between the cap and the line.

Get: BaseInset(self: CustomLineCap) -> Single

Set: BaseInset(self: CustomLineCap) = value
"""

    StrokeJoin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Drawing2D.LineJoin enumeration that determines how lines that compose this System.Drawing.Drawing2D.CustomLineCap object are joined.

Get: StrokeJoin(self: CustomLineCap) -> LineJoin

Set: StrokeJoin(self: CustomLineCap) = value
"""

    WidthScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount by which to scale this System.Drawing.Drawing2D.CustomLineCap Class object with respect to the width of the System.Drawing.Pen object.

Get: WidthScale(self: CustomLineCap) -> Single

Set: WidthScale(self: CustomLineCap) = value
"""



class AdjustableArrowCap(CustomLineCap, ICloneable, IDisposable):
    """
    Represents an adjustable arrow-shaped line cap. This class cannot be inherited.
    
    AdjustableArrowCap(width: Single, height: Single)
    AdjustableArrowCap(width: Single, height: Single, isFilled: bool)
    """
    def Dispose(self):
        """
        Dispose(self: CustomLineCap, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Drawing2D.CustomLineCap and 
             optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, isFilled=None):
        """
        __new__(cls: type, width: Single, height: Single)
        __new__(cls: type, width: Single, height: Single, isFilled: bool)
        """
        pass

    Filled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the arrow cap is filled.

Get: Filled(self: AdjustableArrowCap) -> bool

Set: Filled(self: AdjustableArrowCap) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the arrow cap.

Get: Height(self: AdjustableArrowCap) -> Single

Set: Height(self: AdjustableArrowCap) = value
"""

    MiddleInset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of units between the outline of the arrow cap and the fill.

Get: MiddleInset(self: AdjustableArrowCap) -> Single

Set: MiddleInset(self: AdjustableArrowCap) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the arrow cap.

Get: Width(self: AdjustableArrowCap) -> Single

Set: Width(self: AdjustableArrowCap) = value
"""



class Blend(object):
    """
    Defines a blend pattern for a System.Drawing.Drawing2D.LinearGradientBrush object. This class cannot be inherited.
    
    Blend()
    Blend(count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, count=None):
        """
        __new__(cls: type)
        __new__(cls: type, count: int)
        """
        pass

    Factors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of blend factors for the gradient.

Get: Factors(self: Blend) -> Array[Single]

Set: Factors(self: Blend) = value
"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of blend positions for the gradient.

Get: Positions(self: Blend) -> Array[Single]

Set: Positions(self: Blend) = value
"""



class ColorBlend(object):
    """
    Defines arrays of colors and positions used for interpolating color blending in a multicolor gradient. This class cannot be inherited.
    
    ColorBlend()
    ColorBlend(count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, count=None):
        """
        __new__(cls: type)
        __new__(cls: type, count: int)
        """
        pass

    Colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of colors that represents the colors to use at corresponding positions along a gradient.

Get: Colors(self: ColorBlend) -> Array[Color]

Set: Colors(self: ColorBlend) = value
"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the positions along a gradient line.

Get: Positions(self: ColorBlend) -> Array[Single]

Set: Positions(self: ColorBlend) = value
"""



class CombineMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how different clipping regions can be combined.
    
    enum CombineMode, values: Complement (5), Exclude (4), Intersect (1), Replace (0), Union (2), Xor (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Complement = None
    Exclude = None
    Intersect = None
    Replace = None
    Union = None
    value__ = None
    Xor = None


class CompositingMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the source colors are combined with the background colors.
    
    enum CompositingMode, values: SourceCopy (1), SourceOver (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SourceCopy = None
    SourceOver = None
    value__ = None


class CompositingQuality(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the quality level to use during compositing.
    
    enum CompositingQuality, values: AssumeLinear (4), Default (0), GammaCorrected (3), HighQuality (2), HighSpeed (1), Invalid (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AssumeLinear = None
    Default = None
    GammaCorrected = None
    HighQuality = None
    HighSpeed = None
    Invalid = None
    value__ = None


class CoordinateSpace(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the system to use when evaluating coordinates.
    
    enum CoordinateSpace, values: Device (2), Page (1), World (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Device = None
    Page = None
    value__ = None
    World = None


class DashCap(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of graphic shape to use on both ends of each dash in a dashed line.
    
    enum DashCap, values: Flat (0), Round (2), Triangle (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flat = None
    Round = None
    Triangle = None
    value__ = None


class DashStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the style of dashed lines drawn with a System.Drawing.Pen object.
    
    enum DashStyle, values: Custom (5), Dash (1), DashDot (3), DashDotDot (4), Dot (2), Solid (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Custom = None
    Dash = None
    DashDot = None
    DashDotDot = None
    Dot = None
    Solid = None
    value__ = None


class FillMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the interior of a closed path is filled.
    
    enum FillMode, values: Alternate (0), Winding (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Alternate = None
    value__ = None
    Winding = None


class FlushIntention(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether commands in the graphics stack are terminated (flushed) immediately or executed as soon as possible.
    
    enum FlushIntention, values: Flush (0), Sync (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Flush = None
    Sync = None
    value__ = None


class GraphicsContainer(MarshalByRefObject):
    """ Represents the internal data of a graphics container. This class is used when saving the state of a System.Drawing.Graphics object using the System.Drawing.Graphics.BeginContainer and System.Drawing.Graphics.EndContainer(System.Drawing.Drawing2D.GraphicsContainer) methods. This class cannot be inherited. """

class GraphicsPath(MarshalByRefObject, ICloneable, IDisposable):
    """
    Represents a series of connected lines and curves. This class cannot be inherited.
    
    GraphicsPath()
    GraphicsPath(fillMode: FillMode)
    GraphicsPath(pts: Array[PointF], types: Array[Byte])
    GraphicsPath(pts: Array[PointF], types: Array[Byte], fillMode: FillMode)
    GraphicsPath(pts: Array[Point], types: Array[Byte])
    GraphicsPath(pts: Array[Point], types: Array[Byte], fillMode: FillMode)
    """
    def AddArc(self, *__args):
        """
        AddArc(self: GraphicsPath, rect: Rectangle, startAngle: Single, sweepAngle: Single)
            Appends an elliptical arc to the current figure.
        
            rect: A System.Drawing.Rectangle that represents the rectangular bounds of the ellipse from which the 
             arc is taken.
        
            startAngle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the arc.
        AddArc(self: GraphicsPath, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single)
            Appends an elliptical arc to the current figure.
        
            x: The x-coordinate of the upper-left corner of the rectangular region that defines the ellipse 
             from which the arc is drawn.
        
            y: The y-coordinate of the upper-left corner of the rectangular region that defines the ellipse 
             from which the arc is drawn.
        
            width: The width of the rectangular region that defines the ellipse from which the arc is drawn.
            height: The height of the rectangular region that defines the ellipse from which the arc is drawn.
            startAngle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the arc.
        AddArc(self: GraphicsPath, rect: RectangleF, startAngle: Single, sweepAngle: Single)
            Appends an elliptical arc to the current figure.
        
            rect: A System.Drawing.RectangleF that represents the rectangular bounds of the ellipse from which the 
             arc is taken.
        
            startAngle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the arc.
        AddArc(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)
            Appends an elliptical arc to the current figure.
        
            x: The x-coordinate of the upper-left corner of the rectangular region that defines the ellipse 
             from which the arc is drawn.
        
            y: The y-coordinate of the upper-left corner of the rectangular region that defines the ellipse 
             from which the arc is drawn.
        
            width: The width of the rectangular region that defines the ellipse from which the arc is drawn.
            height: The height of the rectangular region that defines the ellipse from which the arc is drawn.
            startAngle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the arc.
        """
        pass

    def AddBezier(self, *__args):
        """
        AddBezier(self: GraphicsPath, pt1: Point, pt2: Point, pt3: Point, pt4: Point)
            Adds a cubic B�zier curve to the current figure.
        
            pt1: A System.Drawing.Point that represents the starting point of the curve.
            pt2: A System.Drawing.Point that represents the first control point for the curve.
            pt3: A System.Drawing.Point that represents the second control point for the curve.
            pt4: A System.Drawing.Point that represents the endpoint of the curve.
        AddBezier(self: GraphicsPath, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int)
            Adds a cubic B�zier curve to the current figure.
        
            x1: The x-coordinate of the starting point of the curve.
            y1: The y-coordinate of the starting point of the curve.
            x2: The x-coordinate of the first control point for the curve.
            y2: The y-coordinate of the first control point for the curve.
            x3: The x-coordinate of the second control point for the curve.
            y3: The y-coordinate of the second control point for the curve.
            x4: The x-coordinate of the endpoint of the curve.
            y4: The y-coordinate of the endpoint of the curve.
        AddBezier(self: GraphicsPath, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF)
            Adds a cubic B�zier curve to the current figure.
        
            pt1: A System.Drawing.PointF that represents the starting point of the curve.
            pt2: A System.Drawing.PointF that represents the first control point for the curve.
            pt3: A System.Drawing.PointF that represents the second control point for the curve.
            pt4: A System.Drawing.PointF that represents the endpoint of the curve.
        AddBezier(self: GraphicsPath, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single)
            Adds a cubic B�zier curve to the current figure.
        
            x1: The x-coordinate of the starting point of the curve.
            y1: The y-coordinate of the starting point of the curve.
            x2: The x-coordinate of the first control point for the curve.
            y2: The y-coordinate of the first control point for the curve.
            x3: The x-coordinate of the second control point for the curve.
            y3: The y-coordinate of the second control point for the curve.
            x4: The x-coordinate of the endpoint of the curve.
            y4: The y-coordinate of the endpoint of the curve.
        """
        pass

    def AddBeziers(self, points):
        """
        AddBeziers(self: GraphicsPath, *points: Array[Point])
            Adds a sequence of connected cubic B�zier curves to the current figure.
        
            points: An array of System.Drawing.Point structures that represents the points that define the curves.
        AddBeziers(self: GraphicsPath, points: Array[PointF])
            Adds a sequence of connected cubic B�zier curves to the current figure.
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curves.
        """
        pass

    def AddClosedCurve(self, points, tension=None):
        """
        AddClosedCurve(self: GraphicsPath, points: Array[Point])
            Adds a closed curve to this path. A cardinal spline curve is used because the curve travels 
             through each of the points in the array.
        
        
            points: An array of System.Drawing.Point structures that represents the points that define the curve.
        AddClosedCurve(self: GraphicsPath, points: Array[Point], tension: Single)
            Adds a closed curve to this path. A cardinal spline curve is used because the curve travels 
             through each of the points in the array.
        
        
            points: An array of System.Drawing.Point structures that represents the points that define the curve.
            tension: A value between from 0 through 1 that specifies the amount that the curve bends between points, 
             with 0 being the smallest curve (sharpest corner) and 1 being the smoothest curve.
        
        AddClosedCurve(self: GraphicsPath, points: Array[PointF])
            Adds a closed curve to this path. A cardinal spline curve is used because the curve travels 
             through each of the points in the array.
        
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curve.
        AddClosedCurve(self: GraphicsPath, points: Array[PointF], tension: Single)
            Adds a closed curve to this path. A cardinal spline curve is used because the curve travels 
             through each of the points in the array.
        
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curve.
            tension: A value between from 0 through 1 that specifies the amount that the curve bends between points, 
             with 0 being the smallest curve (sharpest corner) and 1 being the smoothest curve.
        """
        pass

    def AddCurve(self, points, *__args):
        """
        AddCurve(self: GraphicsPath, points: Array[Point])
            Adds a spline curve to the current figure. A cardinal spline curve is used because the curve 
             travels through each of the points in the array.
        
        
            points: An array of System.Drawing.Point structures that represents the points that define the curve.
        AddCurve(self: GraphicsPath, points: Array[Point], tension: Single)
            Adds a spline curve to the current figure.
        
            points: An array of System.Drawing.Point structures that represents the points that define the curve.
            tension: A value that specifies the amount that the curve bends between control points. Values greater 
             than 1 produce unpredictable results.
        
        AddCurve(self: GraphicsPath, points: Array[Point], offset: int, numberOfSegments: int, tension: Single)
            Adds a spline curve to the current figure.
        
            points: An array of System.Drawing.Point structures that represents the points that define the curve.
            offset: The index of the element in the points array that is used as the first point in the curve.
            numberOfSegments: A value that specifies the amount that the curve bends between control points. Values greater 
             than 1 produce unpredictable results.
        
            tension: A value that specifies the amount that the curve bends between control points. Values greater 
             than 1 produce unpredictable results.
        
        AddCurve(self: GraphicsPath, points: Array[PointF])
            Adds a spline curve to the current figure. A cardinal spline curve is used because the curve 
             travels through each of the points in the array.
        
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curve.
        AddCurve(self: GraphicsPath, points: Array[PointF], tension: Single)
            Adds a spline curve to the current figure.
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curve.
            tension: A value that specifies the amount that the curve bends between control points. Values greater 
             than 1 produce unpredictable results.
        
        AddCurve(self: GraphicsPath, points: Array[PointF], offset: int, numberOfSegments: int, tension: Single)
            Adds a spline curve to the current figure.
        
            points: An array of System.Drawing.PointF structures that represents the points that define the curve.
            offset: The index of the element in the points array that is used as the first point in the curve.
            numberOfSegments: The number of segments used to draw the curve. A segment can be thought of as a line connecting 
             two points.
        
            tension: A value that specifies the amount that the curve bends between control points. Values greater 
             than 1 produce unpredictable results.
        """
        pass

    def AddEllipse(self, *__args):
        """
        AddEllipse(self: GraphicsPath, rect: Rectangle)
            Adds an ellipse to the current path.
        
            rect: A System.Drawing.Rectangle that represents the bounding rectangle that defines the ellipse.
        AddEllipse(self: GraphicsPath, x: int, y: int, width: int, height: int)
            Adds an ellipse to the current path.
        
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            width: The width of the bounding rectangle that defines the ellipse.
            height: The height of the bounding rectangle that defines the ellipse.
        AddEllipse(self: GraphicsPath, rect: RectangleF)
            Adds an ellipse to the current path.
        
            rect: A System.Drawing.RectangleF that represents the bounding rectangle that defines the ellipse.
        AddEllipse(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single)
            Adds an ellipse to the current path.
        
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper left corner of the bounding rectangle that defines the ellipse.
            width: The width of the bounding rectangle that defines the ellipse.
            height: The height of the bounding rectangle that defines the ellipse.
        """
        pass

    def AddLine(self, *__args):
        """
        AddLine(self: GraphicsPath, pt1: Point, pt2: Point)
            Appends a line segment to this System.Drawing.Drawing2D.GraphicsPath.
        
            pt1: A System.Drawing.Point that represents the starting point of the line.
            pt2: A System.Drawing.Point that represents the endpoint of the line.
        AddLine(self: GraphicsPath, x1: int, y1: int, x2: int, y2: int)
            Appends a line segment to the current figure.
        
            x1: The x-coordinate of the starting point of the line.
            y1: The y-coordinate of the starting point of the line.
            x2: The x-coordinate of the endpoint of the line.
            y2: The y-coordinate of the endpoint of the line.
        AddLine(self: GraphicsPath, pt1: PointF, pt2: PointF)
            Appends a line segment to this System.Drawing.Drawing2D.GraphicsPath.
        
            pt1: A System.Drawing.PointF that represents the starting point of the line.
            pt2: A System.Drawing.PointF that represents the endpoint of the line.
        AddLine(self: GraphicsPath, x1: Single, y1: Single, x2: Single, y2: Single)
            Appends a line segment to this System.Drawing.Drawing2D.GraphicsPath.
        
            x1: The x-coordinate of the starting point of the line.
            y1: The y-coordinate of the starting point of the line.
            x2: The x-coordinate of the endpoint of the line.
            y2: The y-coordinate of the endpoint of the line.
        """
        pass

    def AddLines(self, points):
        """
        AddLines(self: GraphicsPath, points: Array[Point])
            Appends a series of connected line segments to the end of this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            points: An array of System.Drawing.Point structures that represents the points that define the line 
             segments to add.
        
        AddLines(self: GraphicsPath, points: Array[PointF])
            Appends a series of connected line segments to the end of this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            points: An array of System.Drawing.PointF structures that represents the points that define the line 
             segments to add.
        """
        pass

    def AddPath(self, addingPath, connect):
        """
        AddPath(self: GraphicsPath, addingPath: GraphicsPath, connect: bool)
            Appends the specified System.Drawing.Drawing2D.GraphicsPath to this path.
        
            addingPath: The System.Drawing.Drawing2D.GraphicsPath to add.
            connect: A Boolean value that specifies whether the first figure in the added path is part of the last 
             figure in this path. A value of true specifies that (if possible) the first figure in the added 
             path is part of the last figure in this path. A value of false specifies that the first figure 
             in the added path is separate from the last figure in this path.
        """
        pass

    def AddPie(self, *__args):
        """
        AddPie(self: GraphicsPath, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single)
            Adds the outline of a pie shape to this path.
        
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie is drawn.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie is drawn.
        
            width: The width of the bounding rectangle that defines the ellipse from which the pie is drawn.
            height: The height of the bounding rectangle that defines the ellipse from which the pie is drawn.
            startAngle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the pie section, measured in degrees clockwise from 
             startAngle.
        
        AddPie(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)
            Adds the outline of a pie shape to this path.
        
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie is drawn.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie is drawn.
        
            width: The width of the bounding rectangle that defines the ellipse from which the pie is drawn.
            height: The height of the bounding rectangle that defines the ellipse from which the pie is drawn.
            startAngle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the pie section, measured in degrees clockwise from 
             startAngle.
        
        AddPie(self: GraphicsPath, rect: Rectangle, startAngle: Single, sweepAngle: Single)
            Adds the outline of a pie shape to this path.
        
            rect: A System.Drawing.Rectangle that represents the bounding rectangle that defines the ellipse from 
             which the pie is drawn.
        
            startAngle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
            sweepAngle: The angle between startAngle and the end of the pie section, measured in degrees clockwise from 
             startAngle.
        """
        pass

    def AddPolygon(self, points):
        """
        AddPolygon(self: GraphicsPath, points: Array[Point])
            Adds a polygon to this path.
        
            points: An array of System.Drawing.Point structures that defines the polygon to add.
        AddPolygon(self: GraphicsPath, points: Array[PointF])
            Adds a polygon to this path.
        
            points: An array of System.Drawing.PointF structures that defines the polygon to add.
        """
        pass

    def AddRectangle(self, rect):
        """
        AddRectangle(self: GraphicsPath, rect: RectangleF)
            Adds a rectangle to this path.
        
            rect: A System.Drawing.RectangleF that represents the rectangle to add.
        AddRectangle(self: GraphicsPath, rect: Rectangle)
            Adds a rectangle to this path.
        
            rect: A System.Drawing.Rectangle that represents the rectangle to add.
        """
        pass

    def AddRectangles(self, rects):
        """
        AddRectangles(self: GraphicsPath, rects: Array[Rectangle])
            Adds a series of rectangles to this path.
        
            rects: An array of System.Drawing.Rectangle structures that represents the rectangles to add.
        AddRectangles(self: GraphicsPath, rects: Array[RectangleF])
            Adds a series of rectangles to this path.
        
            rects: An array of System.Drawing.RectangleF structures that represents the rectangles to add.
        """
        pass

    def AddString(self, s, family, style, emSize, *__args):
        """
        AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: RectangleF, format: StringFormat)
            Adds a text string to this path.
        
            s: The System.String to add.
            family: A System.Drawing.FontFamily that represents the name of the font with which the test is drawn.
            style: A System.Drawing.FontStyle enumeration that represents style information about the text (bold, 
             italic, and so on). This must be cast as an integer (see the example code later in this 
             section).
        
            emSize: The height of the em square box that bounds the character.
            layoutRect: A System.Drawing.RectangleF that represents the rectangle that bounds the text.
            format: A System.Drawing.StringFormat that specifies text formatting information, such as line spacing 
             and alignment.
        
        AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: Rectangle, format: StringFormat)
            Adds a text string to this path.
        
            s: The System.String to add.
            family: A System.Drawing.FontFamily that represents the name of the font with which the test is drawn.
            style: A System.Drawing.FontStyle enumeration that represents style information about the text (bold, 
             italic, and so on). This must be cast as an integer (see the example code later in this 
             section).
        
            emSize: The height of the em square box that bounds the character.
            layoutRect: A System.Drawing.Rectangle that represents the rectangle that bounds the text.
            format: A System.Drawing.StringFormat that specifies text formatting information, such as line spacing 
             and alignment.
        
        AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, origin: PointF, format: StringFormat)
            Adds a text string to this path.
        
            s: The System.String to add.
            family: A System.Drawing.FontFamily that represents the name of the font with which the test is drawn.
            style: A System.Drawing.FontStyle enumeration that represents style information about the text (bold, 
             italic, and so on). This must be cast as an integer (see the example code later in this 
             section).
        
            emSize: The height of the em square box that bounds the character.
            origin: A System.Drawing.PointF that represents the point where the text starts.
            format: A System.Drawing.StringFormat that specifies text formatting information, such as line spacing 
             and alignment.
        
        AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, origin: Point, format: StringFormat)
            Adds a text string to this path.
        
            s: The System.String to add.
            family: A System.Drawing.FontFamily that represents the name of the font with which the test is drawn.
            style: A System.Drawing.FontStyle enumeration that represents style information about the text (bold, 
             italic, and so on). This must be cast as an integer (see the example code later in this 
             section).
        
            emSize: The height of the em square box that bounds the character.
            origin: A System.Drawing.Point that represents the point where the text starts.
            format: A System.Drawing.StringFormat that specifies text formatting information, such as line spacing 
             and alignment.
        """
        pass

    def ClearMarkers(self):
        """
        ClearMarkers(self: GraphicsPath)
            Clears all markers from this path.
        """
        pass

    def Clone(self):
        """
        Clone(self: GraphicsPath) -> object
        
            Creates an exact copy of this path.
            Returns: The System.Drawing.Drawing2D.GraphicsPath this method creates, cast as an object.
        """
        pass

    def CloseAllFigures(self):
        """
        CloseAllFigures(self: GraphicsPath)
            Closes all open figures in this path and starts a new figure. It closes each open figure by 
             connecting a line from its endpoint to its starting point.
        """
        pass

    def CloseFigure(self):
        """
        CloseFigure(self: GraphicsPath)
            Closes the current figure and starts a new figure. If the current figure contains a sequence of 
             connected lines and curves, the method closes the loop by connecting a line from the endpoint to 
             the starting point.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: GraphicsPath)
            Releases all resources used by this System.Drawing.Drawing2D.GraphicsPath.
        """
        pass

    def Flatten(self, matrix=None, flatness=None):
        """
        Flatten(self: GraphicsPath, matrix: Matrix, flatness: Single)
            Converts each curve in this System.Drawing.Drawing2D.GraphicsPath into a sequence of connected 
             line segments.
        
        
            matrix: A System.Drawing.Drawing2D.Matrix by which to transform this 
             System.Drawing.Drawing2D.GraphicsPath before flattening.
        
            flatness: Specifies the maximum permitted error between the curve and its flattened approximation. A value 
             of 0.25 is the default. Reducing the flatness value will increase the number of line segments in 
             the approximation.
        
        Flatten(self: GraphicsPath, matrix: Matrix)
            Applies the specified transform and then converts each curve in this 
             System.Drawing.Drawing2D.GraphicsPath into a sequence of connected line segments.
        
        
            matrix: A System.Drawing.Drawing2D.Matrix by which to transform this 
             System.Drawing.Drawing2D.GraphicsPath before flattening.
        
        Flatten(self: GraphicsPath)
            Converts each curve in this path into a sequence of connected line segments.
        """
        pass

    def GetBounds(self, matrix=None, pen=None):
        """
        GetBounds(self: GraphicsPath, matrix: Matrix, pen: Pen) -> RectangleF
        
            Returns a rectangle that bounds this System.Drawing.Drawing2D.GraphicsPath when the current path 
             is transformed by the specified System.Drawing.Drawing2D.Matrix and drawn with the specified 
             System.Drawing.Pen.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix that specifies a transformation to be applied to this path 
             before the bounding rectangle is calculated. This path is not permanently transformed; the 
             transformation is used only during the process of calculating the bounding rectangle.
        
            pen: The System.Drawing.Pen with which to draw the System.Drawing.Drawing2D.GraphicsPath.
            Returns: A System.Drawing.RectangleF that represents a rectangle that bounds this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        GetBounds(self: GraphicsPath, matrix: Matrix) -> RectangleF
        
            Returns a rectangle that bounds this System.Drawing.Drawing2D.GraphicsPath when this path is 
             transformed by the specified System.Drawing.Drawing2D.Matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix that specifies a transformation to be applied to this path 
             before the bounding rectangle is calculated. This path is not permanently transformed; the 
             transformation is used only during the process of calculating the bounding rectangle.
        
            Returns: A System.Drawing.RectangleF that represents a rectangle that bounds this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        GetBounds(self: GraphicsPath) -> RectangleF
        
            Returns a rectangle that bounds this System.Drawing.Drawing2D.GraphicsPath.
            Returns: A System.Drawing.RectangleF that represents a rectangle that bounds this 
             System.Drawing.Drawing2D.GraphicsPath.
        """
        pass

    def GetLastPoint(self):
        """
        GetLastPoint(self: GraphicsPath) -> PointF
        
            Gets the last point in the System.Drawing.Drawing2D.GraphicsPath.PathPoints array of this 
             System.Drawing.Drawing2D.GraphicsPath.
        
            Returns: A System.Drawing.PointF that represents the last point in this 
             System.Drawing.Drawing2D.GraphicsPath.
        """
        pass

    def IsOutlineVisible(self, *__args):
        """
        IsOutlineVisible(self: GraphicsPath, point: Point, pen: Pen) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen.
        
        
            point: A System.Drawing.Point that specifies the location to test.
            pen: The System.Drawing.Pen to test.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen; 
             otherwise, false.
        
        IsOutlineVisible(self: GraphicsPath, x: int, y: int, pen: Pen) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            pen: The System.Drawing.Pen to test.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen; 
             otherwise, false.
        
        IsOutlineVisible(self: GraphicsPath, pt: Point, pen: Pen, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen and using 
             the specified System.Drawing.Graphics.
        
        
            pt: A System.Drawing.Point that specifies the location to test.
            pen: The System.Drawing.Pen to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath as drawn with the specified System.Drawing.Pen; otherwise, 
             false.
        
        IsOutlineVisible(self: GraphicsPath, x: int, y: int, pen: Pen, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen and using 
             the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            pen: The System.Drawing.Pen to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath as drawn with the specified System.Drawing.Pen; otherwise, 
             false.
        
        IsOutlineVisible(self: GraphicsPath, point: PointF, pen: Pen) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen.
        
        
            point: A System.Drawing.PointF that specifies the location to test.
            pen: The System.Drawing.Pen to test.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen; 
             otherwise, false.
        
        IsOutlineVisible(self: GraphicsPath, x: Single, y: Single, pen: Pen) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            pen: The System.Drawing.Pen to test.
            Returns: This method returns true if the specified point is contained within the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen; 
             otherwise, false.
        
        IsOutlineVisible(self: GraphicsPath, pt: PointF, pen: Pen, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen and using 
             the specified System.Drawing.Graphics.
        
        
            pt: A System.Drawing.PointF that specifies the location to test.
            pen: The System.Drawing.Pen to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath as drawn with the specified System.Drawing.Pen; otherwise, 
             false.
        
        IsOutlineVisible(self: GraphicsPath, x: Single, y: Single, pen: Pen, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath when drawn with the specified System.Drawing.Pen and using 
             the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            pen: The System.Drawing.Pen to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within (under) the outline of this 
             System.Drawing.Drawing2D.GraphicsPath as drawn with the specified System.Drawing.Pen; otherwise, 
             false.
        """
        pass

    def IsVisible(self, *__args):
        """
        IsVisible(self: GraphicsPath, point: Point) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            point: A System.Drawing.Point that represents the point to test.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, x: int, y: int) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, pt: Point, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            pt: A System.Drawing.Point that represents the point to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, x: int, y: int, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath, using the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, point: PointF) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            point: A System.Drawing.PointF that represents the point to test.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, x: Single, y: Single) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        
        IsVisible(self: GraphicsPath, pt: PointF, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            pt: A System.Drawing.PointF that represents the point to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within this; otherwise, false.
        IsVisible(self: GraphicsPath, x: Single, y: Single, graphics: Graphics) -> bool
        
            Indicates whether the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath in the visible clip region of the specified 
             System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            graphics: The System.Drawing.Graphics for which to test visibility.
            Returns: This method returns true if the specified point is contained within this 
             System.Drawing.Drawing2D.GraphicsPath; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Reset(self):
        """
        Reset(self: GraphicsPath)
            Empties the System.Drawing.Drawing2D.GraphicsPath.PathPoints and 
             System.Drawing.Drawing2D.GraphicsPath.PathTypes arrays and sets the 
             System.Drawing.Drawing2D.FillMode to System.Drawing.Drawing2D.FillMode.Alternate.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: GraphicsPath)
            Reverses the order of points in the System.Drawing.Drawing2D.GraphicsPath.PathPoints array of 
             this System.Drawing.Drawing2D.GraphicsPath.
        """
        pass

    def SetMarkers(self):
        """
        SetMarkers(self: GraphicsPath)
            Sets a marker on this System.Drawing.Drawing2D.GraphicsPath.
        """
        pass

    def StartFigure(self):
        """
        StartFigure(self: GraphicsPath)
            Starts a new figure without closing the current figure. All subsequent points added to the path 
             are added to this new figure.
        """
        pass

    def Transform(self, matrix):
        """
        Transform(self: GraphicsPath, matrix: Matrix)
            Applies a transform matrix to this System.Drawing.Drawing2D.GraphicsPath.
        
            matrix: A System.Drawing.Drawing2D.Matrix that represents the transformation to apply.
        """
        pass

    def Warp(self, destPoints, srcRect, matrix=None, warpMode=None, flatness=None):
        """
        Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode)
            Applies a warp transform, defined by a rectangle and a parallelogram, to this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            destPoints: An array of System.Drawing.PointF structures that defines a parallelogram to which the rectangle 
             defined by srcRect is transformed. The array can contain either three or four elements. If the 
             array contains three elements, the lower-right corner of the parallelogram is implied by the 
             first three points.
        
            srcRect: A System.Drawing.RectangleF that represents the rectangle that is transformed to the 
             parallelogram defined by destPoints.
        
            matrix: A System.Drawing.Drawing2D.Matrix that specifies a geometric transform to apply to the path.
            warpMode: A System.Drawing.Drawing2D.WarpMode enumeration that specifies whether this warp operation uses 
             perspective or bilinear mode.
        
        Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode, flatness: Single)
            Applies a warp transform, defined by a rectangle and a parallelogram, to this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            destPoints: An array of System.Drawing.PointF structures that define a parallelogram to which the rectangle 
             defined by srcRect is transformed. The array can contain either three or four elements. If the 
             array contains three elements, the lower-right corner of the parallelogram is implied by the 
             first three points.
        
            srcRect: A System.Drawing.RectangleF that represents the rectangle that is transformed to the 
             parallelogram defined by destPoints.
        
            matrix: A System.Drawing.Drawing2D.Matrix that specifies a geometric transform to apply to the path.
            warpMode: A System.Drawing.Drawing2D.WarpMode enumeration that specifies whether this warp operation uses 
             perspective or bilinear mode.
        
            flatness: A value from 0 through 1 that specifies how flat the resulting path is. For more information, 
             see the System.Drawing.Drawing2D.GraphicsPath.Flatten methods.
        
        Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF)
            Applies a warp transform, defined by a rectangle and a parallelogram, to this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            destPoints: An array of System.Drawing.PointF structures that define a parallelogram to which the rectangle 
             defined by srcRect is transformed. The array can contain either three or four elements. If the 
             array contains three elements, the lower-right corner of the parallelogram is implied by the 
             first three points.
        
            srcRect: A System.Drawing.RectangleF that represents the rectangle that is transformed to the 
             parallelogram defined by destPoints.
        
        Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix)
            Applies a warp transform, defined by a rectangle and a parallelogram, to this 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            destPoints: An array of System.Drawing.PointF structures that define a parallelogram to which the rectangle 
             defined by srcRect is transformed. The array can contain either three or four elements. If the 
             array contains three elements, the lower-right corner of the parallelogram is implied by the 
             first three points.
        
            srcRect: A System.Drawing.RectangleF that represents the rectangle that is transformed to the 
             parallelogram defined by destPoints.
        
            matrix: A System.Drawing.Drawing2D.Matrix that specifies a geometric transform to apply to the path.
        """
        pass

    def Widen(self, pen, matrix=None, flatness=None):
        """
        Widen(self: GraphicsPath, pen: Pen, matrix: Matrix, flatness: Single)
            Replaces this System.Drawing.Drawing2D.GraphicsPath with curves that enclose the area that is 
             filled when this path is drawn by the specified pen.
        
        
            pen: A System.Drawing.Pen that specifies the width between the original outline of the path and the 
             new outline this method creates.
        
            matrix: A System.Drawing.Drawing2D.Matrix that specifies a transform to apply to the path before 
             widening.
        
            flatness: A value that specifies the flatness for curves.
        Widen(self: GraphicsPath, pen: Pen, matrix: Matrix)
            Adds an additional outline to the System.Drawing.Drawing2D.GraphicsPath.
        
            pen: A System.Drawing.Pen that specifies the width between the original outline of the path and the 
             new outline this method creates.
        
            matrix: A System.Drawing.Drawing2D.Matrix that specifies a transform to apply to the path before 
             widening.
        
        Widen(self: GraphicsPath, pen: Pen)
            Adds an additional outline to the path.
        
            pen: A System.Drawing.Pen that specifies the width between the original outline of the path and the 
             new outline this method creates.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, fillMode: FillMode)
        __new__(cls: type, pts: Array[PointF], types: Array[Byte])
        __new__(cls: type, pts: Array[PointF], types: Array[Byte], fillMode: FillMode)
        __new__(cls: type, pts: Array[Point], types: Array[Byte])
        __new__(cls: type, pts: Array[Point], types: Array[Byte], fillMode: FillMode)
        """
        pass

    FillMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.FillMode enumeration that determines how the interiors of shapes in this System.Drawing.Drawing2D.GraphicsPath are filled.

Get: FillMode(self: GraphicsPath) -> FillMode

Set: FillMode(self: GraphicsPath) = value
"""

    PathData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Drawing.Drawing2D.PathData that encapsulates arrays of points (points) and types (types) for this System.Drawing.Drawing2D.GraphicsPath.

Get: PathData(self: GraphicsPath) -> PathData

"""

    PathPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the points in the path.

Get: PathPoints(self: GraphicsPath) -> Array[PointF]

"""

    PathTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the types of the corresponding points in the System.Drawing.Drawing2D.GraphicsPath.PathPoints array.

Get: PathTypes(self: GraphicsPath) -> Array[Byte]

"""

    PointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the System.Drawing.Drawing2D.GraphicsPath.PathPoints or the System.Drawing.Drawing2D.GraphicsPath.PathTypes array.

Get: PointCount(self: GraphicsPath) -> int

"""



class GraphicsPathIterator(MarshalByRefObject, IDisposable):
    """
    Provides the ability to iterate through subpaths in a System.Drawing.Drawing2D.GraphicsPath and test the types of shapes contained in each subpath. This class cannot be inherited.
    
    GraphicsPathIterator(path: GraphicsPath)
    """
    def CopyData(self, points, types, startIndex, endIndex):
        """
        CopyData(self: GraphicsPathIterator, points: Array[PointF], types: Array[Byte], startIndex: int, endIndex: int) -> (int, Array[PointF], Array[Byte])
        
            Copies the System.Drawing.Drawing2D.GraphicsPath.PathPoints property and 
             System.Drawing.Drawing2D.GraphicsPath.PathTypes property arrays of the associated 
             System.Drawing.Drawing2D.GraphicsPath into the two specified arrays.
        
        
            points: Upon return, contains an array of System.Drawing.PointF structures that represents the points in 
             the path.
        
            types: Upon return, contains an array of bytes that represents the types of points in the path.
            startIndex: Specifies the starting index of the arrays.
            endIndex: Specifies the ending index of the arrays.
            Returns: The number of points copied.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: GraphicsPathIterator)
            Releases all resources used by this System.Drawing.Drawing2D.GraphicsPathIterator object.
        """
        pass

    def Enumerate(self, points, types):
        """
        Enumerate(self: GraphicsPathIterator, points: Array[PointF], types: Array[Byte]) -> (int, Array[PointF], Array[Byte])
        
            Copies the System.Drawing.Drawing2D.GraphicsPath.PathPoints property and 
             System.Drawing.Drawing2D.GraphicsPath.PathTypes property arrays of the associated 
             System.Drawing.Drawing2D.GraphicsPath into the two specified arrays.
        
        
            points: Upon return, contains an array of System.Drawing.PointF structures that represents the points in 
             the path.
        
            types: Upon return, contains an array of bytes that represents the types of points in the path.
            Returns: The number of points copied.
        """
        pass

    def HasCurve(self):
        """
        HasCurve(self: GraphicsPathIterator) -> bool
        
            Indicates whether the path associated with this System.Drawing.Drawing2D.GraphicsPathIterator 
             contains a curve.
        
            Returns: This method returns true if the current subpath contains a curve; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NextMarker(self, *__args):
        """
        NextMarker(self: GraphicsPathIterator, path: GraphicsPath) -> int
        
            This System.Drawing.Drawing2D.GraphicsPathIterator object has a 
             System.Drawing.Drawing2D.GraphicsPath object associated with it. The 
             System.Drawing.Drawing2D.GraphicsPathIterator.NextMarker(System.Drawing.Drawing2D.GraphicsPath) 
             method increments the associated System.Drawing.Drawing2D.GraphicsPath to the next marker in its 
             path and copies all the points contained between the current marker and the next marker (or end 
             of path) to a second System.Drawing.Drawing2D.GraphicsPath object passed in to the parameter.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath object to which the points will be copied.
            Returns: The number of points between this marker and the next.
        NextMarker(self: GraphicsPathIterator) -> (int, int, int)
        
            Increments the System.Drawing.Drawing2D.GraphicsPathIterator to the next marker in the path and 
             returns the start and stop indexes by way of the [out] parameters.
        
            Returns: The number of points between this marker and the next.
        """
        pass

    def NextPathType(self, pathType, startIndex, endIndex):
        """
        NextPathType(self: GraphicsPathIterator) -> (int, Byte, int, int)
        
            Gets the starting index and the ending index of the next group of data points that all have the 
             same type.
        
            Returns: This method returns the number of data points in the group. If there are no more groups in the 
             path, this method returns 0.
        """
        pass

    def NextSubpath(self, *__args):
        """
        NextSubpath(self: GraphicsPathIterator, path: GraphicsPath) -> (int, bool)
        
            Gets the next figure (subpath) from the associated path of this 
             System.Drawing.Drawing2D.GraphicsPathIterator.
        
        
            path: A System.Drawing.Drawing2D.GraphicsPath that is to have its data points set to match the data 
             points of the retrieved figure (subpath) for this iterator.
        
            Returns: The number of data points in the retrieved figure (subpath). If there are no more figures to 
             retrieve, zero is returned.
        
        NextSubpath(self: GraphicsPathIterator) -> (int, int, int, bool)
        
            Moves the System.Drawing.Drawing2D.GraphicsPathIterator to the next subpath in the path. The 
             start index and end index of the next subpath are contained in the [out] parameters.
        
            Returns: The number of subpaths in the System.Drawing.Drawing2D.GraphicsPath object.
        """
        pass

    def Rewind(self):
        """
        Rewind(self: GraphicsPathIterator)
            Rewinds this System.Drawing.Drawing2D.GraphicsPathIterator to the beginning of its associated 
             path.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path):
        """ __new__(cls: type, path: GraphicsPath) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of points in the path.

Get: Count(self: GraphicsPathIterator) -> int

"""

    SubpathCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of subpaths in the path.

Get: SubpathCount(self: GraphicsPathIterator) -> int

"""



class GraphicsState(MarshalByRefObject):
    """ Represents the state of a System.Drawing.Graphics object. This object is returned by a call to the System.Drawing.Graphics.Save methods. This class cannot be inherited. """

class HatchBrush(Brush, ICloneable, IDisposable):
    """
    Defines a rectangular brush with a hatch style, a foreground color, and a background color. This class cannot be inherited.
    
    HatchBrush(hatchstyle: HatchStyle, foreColor: Color, backColor: Color)
    HatchBrush(hatchstyle: HatchStyle, foreColor: Color)
    """
    def Clone(self):
        """
        Clone(self: HatchBrush) -> object
        
            Creates an exact copy of this System.Drawing.Drawing2D.HatchBrush object.
            Returns: The System.Drawing.Drawing2D.HatchBrush this method creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Brush, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Brush and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hatchstyle, foreColor, backColor=None):
        """
        __new__(cls: type, hatchstyle: HatchStyle, foreColor: Color)
        __new__(cls: type, hatchstyle: HatchStyle, foreColor: Color, backColor: Color)
        """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the color of spaces between the hatch lines drawn by this System.Drawing.Drawing2D.HatchBrush object.

Get: BackgroundColor(self: HatchBrush) -> Color

"""

    ForegroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the color of hatch lines drawn by this System.Drawing.Drawing2D.HatchBrush object.

Get: ForegroundColor(self: HatchBrush) -> Color

"""

    HatchStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hatch style of this System.Drawing.Drawing2D.HatchBrush object.

Get: HatchStyle(self: HatchBrush) -> HatchStyle

"""



class HatchStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the different patterns available for System.Drawing.Drawing2D.HatchBrush objects.
    
    enum HatchStyle, values: BackwardDiagonal (3), Cross (4), DarkDownwardDiagonal (20), DarkHorizontal (29), DarkUpwardDiagonal (21), DarkVertical (28), DashedDownwardDiagonal (30), DashedHorizontal (32), DashedUpwardDiagonal (31), DashedVertical (33), DiagonalBrick (38), DiagonalCross (5), Divot (42), DottedDiamond (44), DottedGrid (43), ForwardDiagonal (2), Horizontal (0), HorizontalBrick (39), LargeCheckerBoard (50), LargeConfetti (35), LargeGrid (4), LightDownwardDiagonal (18), LightHorizontal (25), LightUpwardDiagonal (19), LightVertical (24), Max (4), Min (0), NarrowHorizontal (27), NarrowVertical (26), OutlinedDiamond (51), Percent05 (6), Percent10 (7), Percent20 (8), Percent25 (9), Percent30 (10), Percent40 (11), Percent50 (12), Percent60 (13), Percent70 (14), Percent75 (15), Percent80 (16), Percent90 (17), Plaid (41), Shingle (45), SmallCheckerBoard (49), SmallConfetti (34), SmallGrid (48), SolidDiamond (52), Sphere (47), Trellis (46), Vertical (1), Wave (37), Weave (40), WideDownwardDiagonal (22), WideUpwardDiagonal (23), ZigZag (36)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BackwardDiagonal = None
    Cross = None
    DarkDownwardDiagonal = None
    DarkHorizontal = None
    DarkUpwardDiagonal = None
    DarkVertical = None
    DashedDownwardDiagonal = None
    DashedHorizontal = None
    DashedUpwardDiagonal = None
    DashedVertical = None
    DiagonalBrick = None
    DiagonalCross = None
    Divot = None
    DottedDiamond = None
    DottedGrid = None
    ForwardDiagonal = None
    Horizontal = None
    HorizontalBrick = None
    LargeCheckerBoard = None
    LargeConfetti = None
    LargeGrid = None
    LightDownwardDiagonal = None
    LightHorizontal = None
    LightUpwardDiagonal = None
    LightVertical = None
    Max = None
    Min = None
    NarrowHorizontal = None
    NarrowVertical = None
    OutlinedDiamond = None
    Percent05 = None
    Percent10 = None
    Percent20 = None
    Percent25 = None
    Percent30 = None
    Percent40 = None
    Percent50 = None
    Percent60 = None
    Percent70 = None
    Percent75 = None
    Percent80 = None
    Percent90 = None
    Plaid = None
    Shingle = None
    SmallCheckerBoard = None
    SmallConfetti = None
    SmallGrid = None
    SolidDiamond = None
    Sphere = None
    Trellis = None
    value__ = None
    Vertical = None
    Wave = None
    Weave = None
    WideDownwardDiagonal = None
    WideUpwardDiagonal = None
    ZigZag = None


class InterpolationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Drawing.Drawing2D.InterpolationMode enumeration specifies the algorithm that is used when images are scaled or rotated.
    
    enum InterpolationMode, values: Bicubic (4), Bilinear (3), Default (0), High (2), HighQualityBicubic (7), HighQualityBilinear (6), Invalid (-1), Low (1), NearestNeighbor (5)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bicubic = None
    Bilinear = None
    Default = None
    High = None
    HighQualityBicubic = None
    HighQualityBilinear = None
    Invalid = None
    Low = None
    NearestNeighbor = None
    value__ = None


class LinearGradientBrush(Brush, ICloneable, IDisposable):
    """
    Encapsulates a System.Drawing.Brush with a linear gradient. This class cannot be inherited.
    
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
    LinearGradientBrush(point1: PointF, point2: PointF, color1: Color, color2: Color)
    LinearGradientBrush(point1: Point, point2: Point, color1: Color, color2: Color)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, angle: Single)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, angle: Single)
    """
    def Clone(self):
        """
        Clone(self: LinearGradientBrush) -> object
        
            Creates an exact copy of this System.Drawing.Drawing2D.LinearGradientBrush.
            Returns: The System.Drawing.Drawing2D.LinearGradientBrush this method creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Brush, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Brush and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MultiplyTransform(self, matrix, order=None):
        """
        MultiplyTransform(self: LinearGradientBrush, matrix: Matrix, order: MatrixOrder)
            Multiplies the System.Drawing.Drawing2D.Matrix that represents the local geometric transform of 
             this System.Drawing.Drawing2D.LinearGradientBrush by the specified 
             System.Drawing.Drawing2D.Matrix in the specified order.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix by which to multiply the geometric transform.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies in which order to multiply the two 
             matrices.
        
        MultiplyTransform(self: LinearGradientBrush, matrix: Matrix)
            Multiplies the System.Drawing.Drawing2D.Matrix that represents the local geometric transform of 
             this System.Drawing.Drawing2D.LinearGradientBrush by the specified 
             System.Drawing.Drawing2D.Matrix by prepending the specified System.Drawing.Drawing2D.Matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix by which to multiply the geometric transform.
        """
        pass

    def ResetTransform(self):
        """
        ResetTransform(self: LinearGradientBrush)
            Resets the System.Drawing.Drawing2D.LinearGradientBrush.Transform property to identity.
        """
        pass

    def RotateTransform(self, angle, order=None):
        """
        RotateTransform(self: LinearGradientBrush, angle: Single, order: MatrixOrder)
            Rotates the local geometric transform by the specified amount in the specified order.
        
            angle: The angle of rotation.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the rotation 
             matrix.
        
        RotateTransform(self: LinearGradientBrush, angle: Single)
            Rotates the local geometric transform by the specified amount. This method prepends the rotation 
             to the transform.
        
        
            angle: The angle of rotation.
        """
        pass

    def ScaleTransform(self, sx, sy, order=None):
        """
        ScaleTransform(self: LinearGradientBrush, sx: Single, sy: Single, order: MatrixOrder)
            Scales the local geometric transform by the specified amounts in the specified order.
        
            sx: The amount by which to scale the transform in the x-axis direction.
            sy: The amount by which to scale the transform in the y-axis direction.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the scaling 
             matrix.
        
        ScaleTransform(self: LinearGradientBrush, sx: Single, sy: Single)
            Scales the local geometric transform by the specified amounts. This method prepends the scaling 
             matrix to the transform.
        
        
            sx: The amount by which to scale the transform in the x-axis direction.
            sy: The amount by which to scale the transform in the y-axis direction.
        """
        pass

    def SetBlendTriangularShape(self, focus, scale=None):
        """
        SetBlendTriangularShape(self: LinearGradientBrush, focus: Single, scale: Single)
            Creates a linear gradient with a center color and a linear falloff to a single color on both 
             ends.
        
        
            focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient 
             is composed of only the ending color).
        
            scale: A value from 0 through1 that specifies how fast the colors falloff from the starting color to 
             focus (ending color)
        
        SetBlendTriangularShape(self: LinearGradientBrush, focus: Single)
            Creates a linear gradient with a center color and a linear falloff to a single color on both 
             ends.
        
        
            focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient 
             is composed of only the ending color).
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def SetSigmaBellShape(self, focus, scale=None):
        """
        SetSigmaBellShape(self: LinearGradientBrush, focus: Single, scale: Single)
            Creates a gradient falloff based on a bell-shaped curve.
        
            focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient 
             is composed of only the ending color).
        
            scale: A value from 0 through 1 that specifies how fast the colors falloff from the focus.
        SetSigmaBellShape(self: LinearGradientBrush, focus: Single)
            Creates a gradient falloff based on a bell-shaped curve.
        
            focus: A value from 0 through 1 that specifies the center of the gradient (the point where the starting 
             color and ending color are blended equally).
        """
        pass

    def TranslateTransform(self, dx, dy, order=None):
        """
        TranslateTransform(self: LinearGradientBrush, dx: Single, dy: Single, order: MatrixOrder)
            Translates the local geometric transform by the specified dimensions in the specified order.
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
            order: The order (prepend or append) in which to apply the translation.
        TranslateTransform(self: LinearGradientBrush, dx: Single, dy: Single)
            Translates the local geometric transform by the specified dimensions. This method prepends the 
             translation to the transform.
        
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, point1: PointF, point2: PointF, color1: Color, color2: Color)
        __new__(cls: type, point1: Point, point2: Point, color1: Color, color2: Color)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, angle: Single)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, angle: Single)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
        """
        pass

    Blend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.Blend that specifies positions and factors that define a custom falloff for the gradient.

Get: Blend(self: LinearGradientBrush) -> Blend

Set: Blend(self: LinearGradientBrush) = value
"""

    GammaCorrection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether gamma correction is enabled for this System.Drawing.Drawing2D.LinearGradientBrush.

Get: GammaCorrection(self: LinearGradientBrush) -> bool

Set: GammaCorrection(self: LinearGradientBrush) = value
"""

    InterpolationColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.ColorBlend that defines a multicolor linear gradient.

Get: InterpolationColors(self: LinearGradientBrush) -> ColorBlend

Set: InterpolationColors(self: LinearGradientBrush) = value
"""

    LinearColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the starting and ending colors of the gradient.

Get: LinearColors(self: LinearGradientBrush) -> Array[Color]

Set: LinearColors(self: LinearGradientBrush) = value
"""

    Rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a rectangular region that defines the starting and ending points of the gradient.

Get: Rectangle(self: LinearGradientBrush) -> RectangleF

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a copy System.Drawing.Drawing2D.Matrix that defines a local geometric transform for this System.Drawing.Drawing2D.LinearGradientBrush.

Get: Transform(self: LinearGradientBrush) -> Matrix

Set: Transform(self: LinearGradientBrush) = value
"""

    WrapMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.WrapMode enumeration that indicates the wrap mode for this System.Drawing.Drawing2D.LinearGradientBrush.

Get: WrapMode(self: LinearGradientBrush) -> WrapMode

Set: WrapMode(self: LinearGradientBrush) = value
"""



class LinearGradientMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the direction of a linear gradient.
    
    enum LinearGradientMode, values: BackwardDiagonal (3), ForwardDiagonal (2), Horizontal (0), Vertical (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BackwardDiagonal = None
    ForwardDiagonal = None
    Horizontal = None
    value__ = None
    Vertical = None


class LineCap(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the available cap styles with which a System.Drawing.Pen object can end a line.
    
    enum LineCap, values: AnchorMask (240), ArrowAnchor (20), Custom (255), DiamondAnchor (19), Flat (0), NoAnchor (16), Round (2), RoundAnchor (18), Square (1), SquareAnchor (17), Triangle (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AnchorMask = None
    ArrowAnchor = None
    Custom = None
    DiamondAnchor = None
    Flat = None
    NoAnchor = None
    Round = None
    RoundAnchor = None
    Square = None
    SquareAnchor = None
    Triangle = None
    value__ = None


class LineJoin(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how to join consecutive line or curve segments in a figure (subpath) contained in a System.Drawing.Drawing2D.GraphicsPath object.
    
    enum LineJoin, values: Bevel (1), Miter (0), MiterClipped (3), Round (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bevel = None
    Miter = None
    MiterClipped = None
    Round = None
    value__ = None


class Matrix(MarshalByRefObject, IDisposable):
    """
    Encapsulates a 3-by-3 affine matrix that represents a geometric transform. This class cannot be inherited.
    
    Matrix()
    Matrix(m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single)
    Matrix(rect: RectangleF, plgpts: Array[PointF])
    Matrix(rect: Rectangle, plgpts: Array[Point])
    """
    def Clone(self):
        """
        Clone(self: Matrix) -> Matrix
        
            Creates an exact copy of this System.Drawing.Drawing2D.Matrix.
            Returns: The System.Drawing.Drawing2D.Matrix that this method creates.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Matrix)
            Releases all resources used by this System.Drawing.Drawing2D.Matrix.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Matrix, obj: object) -> bool
        
            Tests whether the specified object is a System.Drawing.Drawing2D.Matrix and is identical to this 
             System.Drawing.Drawing2D.Matrix.
        
        
            obj: The object to test.
            Returns: This method returns true if obj is the specified System.Drawing.Drawing2D.Matrix identical to 
             this System.Drawing.Drawing2D.Matrix; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Matrix) -> int
        
            Returns a hash code.
            Returns: The hash code for this System.Drawing.Drawing2D.Matrix.
        """
        pass

    def Invert(self):
        """
        Invert(self: Matrix)
            Inverts this System.Drawing.Drawing2D.Matrix, if it is invertible.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Multiply(self, matrix, order=None):
        """
        Multiply(self: Matrix, matrix: Matrix, order: MatrixOrder)
            Multiplies this System.Drawing.Drawing2D.Matrix by the matrix specified in the matrix parameter, 
             and in the order specified in the order parameter.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix by which this System.Drawing.Drawing2D.Matrix is to be 
             multiplied.
        
            order: The System.Drawing.Drawing2D.MatrixOrder that represents the order of the multiplication.
        Multiply(self: Matrix, matrix: Matrix)
            Multiplies this System.Drawing.Drawing2D.Matrix by the matrix specified in the matrix parameter, 
             by prepending the specified System.Drawing.Drawing2D.Matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix by which this System.Drawing.Drawing2D.Matrix is to be 
             multiplied.
        """
        pass

    def Reset(self):
        """
        Reset(self: Matrix)
            Resets this System.Drawing.Drawing2D.Matrix to have the elements of the identity matrix.
        """
        pass

    def Rotate(self, angle, order=None):
        """
        Rotate(self: Matrix, angle: Single, order: MatrixOrder)
            Applies a clockwise rotation of an amount specified in the angle parameter, around the origin 
             (zero x and y coordinates) for this System.Drawing.Drawing2D.Matrix.
        
        
            angle: The angle (extent) of the rotation, in degrees.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies the order (append or prepend) in which the 
             rotation is applied to this System.Drawing.Drawing2D.Matrix.
        
        Rotate(self: Matrix, angle: Single)
            Prepend to this System.Drawing.Drawing2D.Matrix a clockwise rotation, around the origin and by 
             the specified angle.
        
        
            angle: The angle of the rotation, in degrees.
        """
        pass

    def RotateAt(self, angle, point, order=None):
        """
        RotateAt(self: Matrix, angle: Single, point: PointF, order: MatrixOrder)
            Applies a clockwise rotation about the specified point to this System.Drawing.Drawing2D.Matrix 
             in the specified order.
        
        
            angle: The angle of the rotation, in degrees.
            point: A System.Drawing.PointF that represents the center of the rotation.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies the order (append or prepend) in which the 
             rotation is applied.
        
        RotateAt(self: Matrix, angle: Single, point: PointF)
            Applies a clockwise rotation to this System.Drawing.Drawing2D.Matrix around the point specified 
             in the point parameter, and by prepending the rotation.
        
        
            angle: The angle (extent) of the rotation, in degrees.
            point: A System.Drawing.PointF that represents the center of the rotation.
        """
        pass

    def Scale(self, scaleX, scaleY, order=None):
        """
        Scale(self: Matrix, scaleX: Single, scaleY: Single, order: MatrixOrder)
            Applies the specified scale vector (scaleX and scaleY) to this System.Drawing.Drawing2D.Matrix 
             using the specified order.
        
        
            scaleX: The value by which to scale this System.Drawing.Drawing2D.Matrix in the x-axis direction.
            scaleY: The value by which to scale this System.Drawing.Drawing2D.Matrix in the y-axis direction.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies the order (append or prepend) in which the 
             scale vector is applied to this System.Drawing.Drawing2D.Matrix.
        
        Scale(self: Matrix, scaleX: Single, scaleY: Single)
            Applies the specified scale vector to this System.Drawing.Drawing2D.Matrix by prepending the 
             scale vector.
        
        
            scaleX: The value by which to scale this System.Drawing.Drawing2D.Matrix in the x-axis direction.
            scaleY: The value by which to scale this System.Drawing.Drawing2D.Matrix in the y-axis direction.
        """
        pass

    def Shear(self, shearX, shearY, order=None):
        """
        Shear(self: Matrix, shearX: Single, shearY: Single, order: MatrixOrder)
            Applies the specified shear vector to this System.Drawing.Drawing2D.Matrix in the specified 
             order.
        
        
            shearX: The horizontal shear factor.
            shearY: The vertical shear factor.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies the order (append or prepend) in which the 
             shear is applied.
        
        Shear(self: Matrix, shearX: Single, shearY: Single)
            Applies the specified shear vector to this System.Drawing.Drawing2D.Matrix by prepending the 
             shear transformation.
        
        
            shearX: The horizontal shear factor.
            shearY: The vertical shear factor.
        """
        pass

    def TransformPoints(self, pts):
        """
        TransformPoints(self: Matrix, pts: Array[Point])
            Applies the geometric transform represented by this System.Drawing.Drawing2D.Matrix to a 
             specified array of points.
        
        
            pts: An array of System.Drawing.Point structures that represents the points to transform.
        TransformPoints(self: Matrix, pts: Array[PointF])
            Applies the geometric transform represented by this System.Drawing.Drawing2D.Matrix to a 
             specified array of points.
        
        
            pts: An array of System.Drawing.PointF structures that represents the points to transform.
        """
        pass

    def TransformVectors(self, pts):
        """
        TransformVectors(self: Matrix, pts: Array[Point])
            Applies only the scale and rotate components of this System.Drawing.Drawing2D.Matrix to the 
             specified array of points.
        
        
            pts: An array of System.Drawing.Point structures that represents the points to transform.
        TransformVectors(self: Matrix, pts: Array[PointF])
            Multiplies each vector in an array by the matrix. The translation elements of this matrix (third 
             row) are ignored.
        
        
            pts: An array of System.Drawing.Point structures that represents the points to transform.
        """
        pass

    def Translate(self, offsetX, offsetY, order=None):
        """
        Translate(self: Matrix, offsetX: Single, offsetY: Single, order: MatrixOrder)
            Applies the specified translation vector to this System.Drawing.Drawing2D.Matrix in the 
             specified order.
        
        
            offsetX: The x value by which to translate this System.Drawing.Drawing2D.Matrix.
            offsetY: The y value by which to translate this System.Drawing.Drawing2D.Matrix.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies the order (append or prepend) in which the 
             translation is applied to this System.Drawing.Drawing2D.Matrix.
        
        Translate(self: Matrix, offsetX: Single, offsetY: Single)
            Applies the specified translation vector (offsetX and offsetY) to this 
             System.Drawing.Drawing2D.Matrix by prepending the translation vector.
        
        
            offsetX: The x value by which to translate this System.Drawing.Drawing2D.Matrix.
            offsetY: The y value by which to translate this System.Drawing.Drawing2D.Matrix.
        """
        pass

    def VectorTransformPoints(self, pts):
        """
        VectorTransformPoints(self: Matrix, pts: Array[Point])
            Multiplies each vector in an array by the matrix. The translation elements of this matrix (third 
             row) are ignored.
        
        
            pts: An array of System.Drawing.Point structures that represents the points to transform.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single)
        __new__(cls: type, rect: RectangleF, plgpts: Array[PointF])
        __new__(cls: type, rect: Rectangle, plgpts: Array[Point])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of floating-point values that represents the elements of this System.Drawing.Drawing2D.Matrix.

Get: Elements(self: Matrix) -> Array[Single]

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Drawing2D.Matrix is the identity matrix.

Get: IsIdentity(self: Matrix) -> bool

"""

    IsInvertible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Drawing2D.Matrix is invertible.

Get: IsInvertible(self: Matrix) -> bool

"""

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x translation value (the dx value, or the element in the third row and first column) of this System.Drawing.Drawing2D.Matrix.

Get: OffsetX(self: Matrix) -> Single

"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y translation value (the dy value, or the element in the third row and second column) of this System.Drawing.Drawing2D.Matrix.

Get: OffsetY(self: Matrix) -> Single

"""



class MatrixOrder(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the order for matrix transform operations.
    
    enum MatrixOrder, values: Append (1), Prepend (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Append = None
    Prepend = None
    value__ = None


class PathData(object):
    """
    Contains the graphical data that makes up a System.Drawing.Drawing2D.GraphicsPath object. This class cannot be inherited.
    
    PathData()
    """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of System.Drawing.PointF structures that represents the points through which the path is constructed.

Get: Points(self: PathData) -> Array[PointF]

Set: Points(self: PathData) = value
"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the types of the corresponding points in the path.

Get: Types(self: PathData) -> Array[Byte]

Set: Types(self: PathData) = value
"""



class PathGradientBrush(Brush, ICloneable, IDisposable):
    """
    Encapsulates a System.Drawing.Brush object that fills the interior of a System.Drawing.Drawing2D.GraphicsPath object with a gradient. This class cannot be inherited.
    
    PathGradientBrush(points: Array[PointF])
    PathGradientBrush(points: Array[PointF], wrapMode: WrapMode)
    PathGradientBrush(points: Array[Point])
    PathGradientBrush(points: Array[Point], wrapMode: WrapMode)
    PathGradientBrush(path: GraphicsPath)
    """
    def Clone(self):
        """
        Clone(self: PathGradientBrush) -> object
        
            Creates an exact copy of this System.Drawing.Drawing2D.PathGradientBrush.
            Returns: The System.Drawing.Drawing2D.PathGradientBrush this method creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Brush, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Brush and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MultiplyTransform(self, matrix, order=None):
        """
        MultiplyTransform(self: PathGradientBrush, matrix: Matrix, order: MatrixOrder)
            Updates the brush's transformation matrix with the product of the brush's transformation matrix 
             multiplied by another matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix that will be multiplied by the brush's current 
             transformation matrix.
        
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies in which order to multiply the two 
             matrices.
        
        MultiplyTransform(self: PathGradientBrush, matrix: Matrix)
            Updates the brush's transformation matrix with the product of brush's transformation matrix 
             multiplied by another matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix that will be multiplied by the brush's current 
             transformation matrix.
        """
        pass

    def ResetTransform(self):
        """
        ResetTransform(self: PathGradientBrush)
            Resets the System.Drawing.Drawing2D.PathGradientBrush.Transform property to identity.
        """
        pass

    def RotateTransform(self, angle, order=None):
        """
        RotateTransform(self: PathGradientBrush, angle: Single, order: MatrixOrder)
            Rotates the local geometric transform by the specified amount in the specified order.
        
            angle: The angle (extent) of rotation.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the rotation 
             matrix.
        
        RotateTransform(self: PathGradientBrush, angle: Single)
            Rotates the local geometric transform by the specified amount. This method prepends the rotation 
             to the transform.
        
        
            angle: The angle (extent) of rotation.
        """
        pass

    def ScaleTransform(self, sx, sy, order=None):
        """
        ScaleTransform(self: PathGradientBrush, sx: Single, sy: Single, order: MatrixOrder)
            Scales the local geometric transform by the specified amounts in the specified order.
        
            sx: The transform scale factor in the x-axis direction.
            sy: The transform scale factor in the y-axis direction.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the scaling 
             matrix.
        
        ScaleTransform(self: PathGradientBrush, sx: Single, sy: Single)
            Scales the local geometric transform by the specified amounts. This method prepends the scaling 
             matrix to the transform.
        
        
            sx: The transform scale factor in the x-axis direction.
            sy: The transform scale factor in the y-axis direction.
        """
        pass

    def SetBlendTriangularShape(self, focus, scale=None):
        """
        SetBlendTriangularShape(self: PathGradientBrush, focus: Single, scale: Single)
            Creates a gradient with a center color and a linear falloff to each surrounding color.
        
            focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to 
             the path's boundary, the center color will be at its highest intensity. A value of 1 (the 
             default) places the highest intensity at the center of the path.
        
            scale: A value from 0 through 1 that specifies the maximum intensity of the center color that gets 
             blended with the boundary color. A value of 1 causes the highest possible intensity of the 
             center color, and it is the default value.
        
        SetBlendTriangularShape(self: PathGradientBrush, focus: Single)
            Creates a gradient with a center color and a linear falloff to one surrounding color.
        
            focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to 
             the path's boundary, the center color will be at its highest intensity. A value of 1 (the 
             default) places the highest intensity at the center of the path.
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def SetSigmaBellShape(self, focus, scale=None):
        """
        SetSigmaBellShape(self: PathGradientBrush, focus: Single, scale: Single)
            Creates a gradient brush that changes color starting from the center of the path outward to the 
             path's boundary. The transition from one color to another is based on a bell-shaped curve.
        
        
            focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to 
             the path's boundary, the center color will be at its highest intensity. A value of 1 (the 
             default) places the highest intensity at the center of the path.
        
            scale: A value from 0 through 1 that specifies the maximum intensity of the center color that gets 
             blended with the boundary color. A value of 1 causes the highest possible intensity of the 
             center color, and it is the default value.
        
        SetSigmaBellShape(self: PathGradientBrush, focus: Single)
            Creates a gradient brush that changes color starting from the center of the path outward to the 
             path's boundary. The transition from one color to another is based on a bell-shaped curve.
        
        
            focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to 
             the path's boundary, the center color will be at its highest intensity. A value of 1 (the 
             default) places the highest intensity at the center of the path.
        """
        pass

    def TranslateTransform(self, dx, dy, order=None):
        """
        TranslateTransform(self: PathGradientBrush, dx: Single, dy: Single, order: MatrixOrder)
            Applies the specified translation to the local geometric transform in the specified order.
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
            order: The order (prepend or append) in which to apply the translation.
        TranslateTransform(self: PathGradientBrush, dx: Single, dy: Single)
            Applies the specified translation to the local geometric transform. This method prepends the 
             translation to the transform.
        
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, points: Array[PointF])
        __new__(cls: type, points: Array[PointF], wrapMode: WrapMode)
        __new__(cls: type, points: Array[Point])
        __new__(cls: type, points: Array[Point], wrapMode: WrapMode)
        __new__(cls: type, path: GraphicsPath)
        """
        pass

    Blend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.Blend that specifies positions and factors that define a custom falloff for the gradient.

Get: Blend(self: PathGradientBrush) -> Blend

Set: Blend(self: PathGradientBrush) = value
"""

    CenterColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color at the center of the path gradient.

Get: CenterColor(self: PathGradientBrush) -> Color

Set: CenterColor(self: PathGradientBrush) = value
"""

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center point of the path gradient.

Get: CenterPoint(self: PathGradientBrush) -> PointF

Set: CenterPoint(self: PathGradientBrush) = value
"""

    FocusScales = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the focus point for the gradient falloff.

Get: FocusScales(self: PathGradientBrush) -> PointF

Set: FocusScales(self: PathGradientBrush) = value
"""

    InterpolationColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.ColorBlend that defines a multicolor linear gradient.

Get: InterpolationColors(self: PathGradientBrush) -> ColorBlend

Set: InterpolationColors(self: PathGradientBrush) = value
"""

    Rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a bounding rectangle for this System.Drawing.Drawing2D.PathGradientBrush.

Get: Rectangle(self: PathGradientBrush) -> RectangleF

"""

    SurroundColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of colors that correspond to the points in the path this System.Drawing.Drawing2D.PathGradientBrush fills.

Get: SurroundColors(self: PathGradientBrush) -> Array[Color]

Set: SurroundColors(self: PathGradientBrush) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a copy of the System.Drawing.Drawing2D.Matrix that defines a local geometric transform for this System.Drawing.Drawing2D.PathGradientBrush.

Get: Transform(self: PathGradientBrush) -> Matrix

Set: Transform(self: PathGradientBrush) = value
"""

    WrapMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.WrapMode that indicates the wrap mode for this System.Drawing.Drawing2D.PathGradientBrush.

Get: WrapMode(self: PathGradientBrush) -> WrapMode

Set: WrapMode(self: PathGradientBrush) = value
"""



class PathPointType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of point in a System.Drawing.Drawing2D.GraphicsPath object.
    
    enum PathPointType, values: Bezier (3), Bezier3 (3), CloseSubpath (128), DashMode (16), Line (1), PathMarker (32), PathTypeMask (7), Start (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bezier = None
    Bezier3 = None
    CloseSubpath = None
    DashMode = None
    Line = None
    PathMarker = None
    PathTypeMask = None
    Start = None
    value__ = None


class PenAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the alignment of a System.Drawing.Pen object in relation to the theoretical, zero-width line.
    
    enum PenAlignment, values: Center (0), Inset (1), Left (3), Outset (2), Right (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Center = None
    Inset = None
    Left = None
    Outset = None
    Right = None
    value__ = None


class PenType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of fill a System.Drawing.Pen object uses to fill lines.
    
    enum PenType, values: HatchFill (1), LinearGradient (4), PathGradient (3), SolidColor (0), TextureFill (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HatchFill = None
    LinearGradient = None
    PathGradient = None
    SolidColor = None
    TextureFill = None
    value__ = None


class PixelOffsetMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how pixels are offset during rendering.
    
    enum PixelOffsetMode, values: Default (0), Half (4), HighQuality (2), HighSpeed (1), Invalid (-1), None (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    Half = None
    HighQuality = None
    HighSpeed = None
    Invalid = None
    None = None
    value__ = None


class QualityMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the overall quality when rendering GDI+ objects.
    
    enum QualityMode, values: Default (0), High (2), Invalid (-1), Low (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    High = None
    Invalid = None
    Low = None
    value__ = None


class RegionData(object):
    """ Encapsulates the data that makes up a System.Drawing.Region object. This class cannot be inherited. """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of bytes that specify the System.Drawing.Region object.

Get: Data(self: RegionData) -> Array[Byte]

Set: Data(self: RegionData) = value
"""



class SmoothingMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether smoothing (antialiasing) is applied to lines and curves and the edges of filled areas.
    
    enum SmoothingMode, values: AntiAlias (4), Default (0), HighQuality (2), HighSpeed (1), Invalid (-1), None (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AntiAlias = None
    Default = None
    HighQuality = None
    HighSpeed = None
    Invalid = None
    None = None
    value__ = None


class WarpMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of warp transformation applied in a erload:System.Drawing.Drawing2D.GraphicsPath.Warp method.
    
    enum WarpMode, values: Bilinear (1), Perspective (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bilinear = None
    Perspective = None
    value__ = None


class WrapMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how a texture or gradient is tiled when it is smaller than the area being filled.
    
    enum WrapMode, values: Clamp (4), Tile (0), TileFlipX (1), TileFlipXY (3), TileFlipY (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Clamp = None
    Tile = None
    TileFlipX = None
    TileFlipXY = None
    TileFlipY = None
    value__ = None



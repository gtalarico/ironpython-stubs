class StreamGeometryContext(DispatcherObject, IDisposable):
    """ Describes a geometry using drawing commands. This class is used with the System.Windows.Media.StreamGeometry class to create a lightweight geometry that does not support data binding, animation, or modification. """
    def ArcTo(self, point, size, rotationAngle, isLargeArc, sweepDirection, isStroked, isSmoothJoin):
        """
        ArcTo(self: StreamGeometryContext, point: Point, size: Size, rotationAngle: float, isLargeArc: bool, sweepDirection: SweepDirection, isStroked: bool, isSmoothJoin: bool)
            Draws an arc to the specified point.
        
            point: The destination point for the end of the arc.
            size: The radii (half the width and half the height) of an oval whose perimeter is used to draw the angle. If the oval is very rounded in all directions, the arc will be rounded, if it is nearly flat, so will 
             the arc. For example, a very large width and height would represent a very large oval, which would give a slight curvature for the angle.
        
            rotationAngle: The rotation angle of the oval that specifies the curve. The curvature of the arc can be rotated with this parameter.
            isLargeArc: true to draw the arc greater than 180 degrees; otherwise, false.
            sweepDirection: A value that indicates whether the arc is drawn in the System.Windows.Media.SweepDirection.Clockwise or System.Windows.Media.SweepDirection.Counterclockwise direction.
            isStroked: true to make the segment stroked when a System.Windows.Media.Pen is used to render the segment; otherwise, false.
            isSmoothJoin: true to treat the join between this segment and the previous segment as a corner when stroked with a System.Windows.Media.Pen; otherwise, false.
        """
        pass

    def BeginFigure(self, startPoint, isFilled, isClosed):
        """
        BeginFigure(self: StreamGeometryContext, startPoint: Point, isFilled: bool, isClosed: bool)
            Specifies the starting point for a new figure.
        
            startPoint: The System.Windows.Point where the figure begins.
            isFilled: true to use the area contained by this figure for hit-testing, rendering, and clipping; otherwise, false.
            isClosed: true to close the figure; otherwise, false. For example, if two connecting lines are drawn, and isClosed is set to false, the drawing will just be of two lines but if isClosed is set to true, the two lines 
             will be closed to create a triangle.
        """
        pass

    def BezierTo(self, point1, point2, point3, isStroked, isSmoothJoin):
        """
        BezierTo(self: StreamGeometryContext, point1: Point, point2: Point, point3: Point, isStroked: bool, isSmoothJoin: bool)
            Draws a Bezier curve to the specified point.
        
            point1: The first control point used to specify the shape of the curve.
            point2: The second control point used to specify the shape of the curve.
            point3: The destination point for the end of the curve.
            isStroked: true to make the segment stroked when a System.Windows.Media.Pen is used to render the segment; otherwise, false.
            isSmoothJoin: true to treat the join between this segment and the previous segment as a corner when stroked with a System.Windows.Media.Pen; otherwise, false.
        """
        pass

    def Close(self):
        """
        Close(self: StreamGeometryContext)
            Closes this context and flushes its content so that it can be rendered.
        """
        pass

    def LineTo(self, point, isStroked, isSmoothJoin):
        """
        LineTo(self: StreamGeometryContext, point: Point, isStroked: bool, isSmoothJoin: bool)
            Draws a straight line to the specified System.Windows.Point.
        
            point: The destination point for the end of the line.
            isStroked: true to make the segment stroked when a System.Windows.Media.Pen is used to render the segment; otherwise, false.
            isSmoothJoin: true to treat the join between this segment and the previous segment as a corner when stroked with a System.Windows.Media.Pen; otherwise, false.
        """
        pass

    def PolyBezierTo(self, points, isStroked, isSmoothJoin):
        """ PolyBezierTo(self: StreamGeometryContext, points: IList[Point], isStroked: bool, isSmoothJoin: bool) """
        pass

    def PolyLineTo(self, points, isStroked, isSmoothJoin):
        """ PolyLineTo(self: StreamGeometryContext, points: IList[Point], isStroked: bool, isSmoothJoin: bool) """
        pass

    def PolyQuadraticBezierTo(self, points, isStroked, isSmoothJoin):
        """ PolyQuadraticBezierTo(self: StreamGeometryContext, points: IList[Point], isStroked: bool, isSmoothJoin: bool) """
        pass

    def QuadraticBezierTo(self, point1, point2, isStroked, isSmoothJoin):
        """
        QuadraticBezierTo(self: StreamGeometryContext, point1: Point, point2: Point, isStroked: bool, isSmoothJoin: bool)
            Draws a quadratic Bezier curve.
        
            point1: The control point used to specify the shape of the curve.
            point2: The destination point for the end of the curve.
            isStroked: true to make the segment stroked when a System.Windows.Media.Pen is used to render the segment; otherwise, false.
            isSmoothJoin: true to treat the join between this segment and the previous segment as a corner when stroked with a System.Windows.Media.Pen; otherwise, false.
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


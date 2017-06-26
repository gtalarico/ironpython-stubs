class BRepBuilderEdgeGeometry(object, IDisposable):
    """ An abstract class used by BRepBuilder to represent the geometry of an edge. Specific edge-geometry representations are represented by subclasses. """
    @staticmethod
    def Create(*__args):
        """
        Create(curve: Curve) -> BRepBuilderEdgeGeometry
        
            Construct BRepBuilderEdgeGeometry based on any GCurve, including GLine and 
             GArc.
           The curve will be simplified if possible, and the concrete type of 
             the returned value will reflect
           that simplification: 
             BRepBuilderLinearEdgeGeometry if the curve could be simplified to a line,
           
             BRepBuilderArcEdgeGeometry if it could be simplified to an arc, 
             BRepBuilderGenericCurveEdgeGeometry
           otherwise.
        
        
            curve: The 3D curve for this edge. This BRepBuilderEdgeGeometry stores a copy of the 
             input curve.
        
        Create(startPoint: XYZ, endPoint: XYZ) -> BRepBuilderEdgeGeometry
        
            Constructs a BRepBuilderEdgeGeometry representing a straight line between the 
             two given points.
        """
        pass

    def Dispose(self):
        """ Dispose(self: BRepBuilderEdgeGeometry) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BRepBuilderEdgeGeometry, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BRepBuilderEdgeGeometry) -> bool

"""



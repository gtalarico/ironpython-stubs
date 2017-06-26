class LineLoad(LoadBase, IDisposable):
    """ An object that represents a force/moment applied in a linear manner. """
    @staticmethod
    def Create(aDoc, *__args):
        """
        Create(aDoc: Document, host: AnalyticalModelStick, forceVector1: XYZ, momentVector1: XYZ, symbol: LineLoadType) -> LineLoad
        
            Creates a new hosted line load within the project.
        
            aDoc: Document to which new line load will be added.
            host: The analytical model stick host element for the line Load.
            forceVector1: The applied 3d force vector.
            momentVector1: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        Create(aDoc: Document, host: AnalyticalModelSurface, curveIndex: int, forceVector1: XYZ, momentVector1: XYZ, symbol: LineLoadType) -> LineLoad
        
            Creates a new hosted line load within the project.
        
            aDoc: Document to which new line load will be added.
            host: The analytical model surface host element for the line Load.
            curveIndex: The index of a curve in analytical surface element starting from 0.
           Use 
             Autodesk::Revit::DB::Structure::AnalyticalModelSurface::GetLoops(Autodesk::Revit
             ::DB::Structure::AnalyticalLoopType::All) method to obtain appropriate curve 
             index.
           Curve index has a unique value in analytical surface element even if 
             it contains more than one loop. The index should be obtain by iteration through 
             all curves in all loops.
        
            forceVector1: The applied 3d force vector.
            momentVector1: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        Create(aDoc: Document, startPoint: XYZ, endPoint: XYZ, forceVector: XYZ, momentVector: XYZ, symbol: LineLoadType, plane: SketchPlane) -> LineLoad
        
            Creates a new non-hosted line load within the project using data at point.
        
            aDoc: Document to which new line load will be added.
            startPoint: The start point of line load, measured in decimal feet.
            endPoint: The end point of line load, measured in decimal feet.
            forceVector: The applied 3d force vector.
            momentVector: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            plane: The work plane of the LineLoad. Set ll to use default plane.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurve(self):
        """
        GetCurve(self: LineLoad) -> Curve
        
            Returns curve that define geometry of the line load.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPoints(self, startPoint, endPoint):
        """
        SetPoints(self: LineLoad, startPoint: XYZ, endPoint: XYZ) -> bool
        
            Sets start and end point of the line load.
        
            startPoint: The start point.
            endPoint: The end point.
            Returns: Returns true if successful, false otherwise.
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

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the three dimensional location of the end point for the line load.

Get: EndPoint(self: LineLoad) -> XYZ

"""

    ForceVector1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the start point of the line load, oriented according to OrientTo setting.

Get: ForceVector1(self: LineLoad) -> XYZ

Set: ForceVector1(self: LineLoad) = value
"""

    ForceVector2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the end point of the line load, oriented according to OrientTo setting.

Get: ForceVector2(self: LineLoad) -> XYZ

Set: ForceVector2(self: LineLoad) = value
"""

    IsProjected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load is projected.

Get: IsProjected(self: LineLoad) -> bool

Set: IsProjected(self: LineLoad) = value
"""

    IsUniform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load is uniform.

Get: IsUniform(self: LineLoad) -> bool

"""

    MomentVector1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moment vector applied to the start point of the line load, oriented according to OrientTo setting.

Get: MomentVector1(self: LineLoad) -> XYZ

Set: MomentVector1(self: LineLoad) = value
"""

    MomentVector2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moment vector applied to the end point of the line load, oriented according to OrientTo setting.

Get: MomentVector2(self: LineLoad) -> XYZ

Set: MomentVector2(self: LineLoad) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the three dimensional location of the start point for the line load.

Get: StartPoint(self: LineLoad) -> XYZ

"""



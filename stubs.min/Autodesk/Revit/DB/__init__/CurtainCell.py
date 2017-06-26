class CurtainCell(APIObject, IDisposable):
    """ Represents a CurtainCell within Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    CurveLoops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cell boundaries on the reference face. The boundaries can have more than one CurveLoop. Each item in the returned array represents a CurveLoop containing 3 or more than 3 edges.

Get: CurveLoops(self: CurtainCell) -> CurveArrArray

"""

    PlanarizedCurveLoops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The planarized curve loops for cell boundaries. The boundaries can have more than one CurveLoop. Each item in the returned array represents a CurveLoop containing 3 or more than 3 edges.

Get: PlanarizedCurveLoops(self: CurtainCell) -> CurveArrArray

"""



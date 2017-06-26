class ExtrusionAnalyzer(object, IDisposable):
    """
    This geometry utility allows you to attempt to "fit" a given piece of geometry into
       the shape of an extrusion.
    """
    def CalculateFaceAlignment(self):
        """
        CalculateFaceAlignment(self: ExtrusionAnalyzer) -> IDictionary[Face, ExtrusionAnalyzerFaceAlignment]
        
            Calculates the alignment status of each face of the solid.
            Returns: Maps each face of the solid to its alignment status.
        """
        pass

    @staticmethod
    def Create(solidGeometry, plane, direction):
        """
        Create(solidGeometry: Solid, plane: Plane, direction: XYZ) -> ExtrusionAnalyzer
        
            Creates an ExtrusionAnalyzer and computes and stores the solid's shadow.
        
            solidGeometry: The geometry to analyze.
            plane: The plane to use for the base plane for the extrusion.
            direction: The direction to use for the calculation for the extrusion.
           The direction 
             must be transverse to the base plane.
        
            Returns: The newly created ExtrusionAnalyzer object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExtrusionAnalyzer) """
        pass

    def GetExtrusionBase(self):
        """
        GetExtrusionBase(self: ExtrusionAnalyzer) -> Face
        
            Obtains the face that represents the base contour of the extrusion analysis.
            Returns: The face that represents the base contour.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExtrusionAnalyzer, disposing: bool) """
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

    EndParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end parameter (distance along the extrusion direction from the input plane) calculated by the extrusion analysis.

Get: EndParameter(self: ExtrusionAnalyzer) -> float

"""

    ExtrusionDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of extrusion specified for the extrusion analysis.

Get: ExtrusionDirection(self: ExtrusionAnalyzer) -> XYZ

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExtrusionAnalyzer) -> bool

"""

    StartParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start parameter (distance along the extrusion direction from the input plane) calculated by the extrusion analysis.

Get: StartParameter(self: ExtrusionAnalyzer) -> float

"""



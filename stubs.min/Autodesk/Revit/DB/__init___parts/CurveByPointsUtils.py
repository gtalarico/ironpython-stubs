class CurveByPointsUtils(object, IDisposable):
    """ A static class that contains methods for processing curves driven by points. """
    @staticmethod
    def AddCurvesToFaceRegion(document, curveElemIds):
        """ AddCurvesToFaceRegion(document: Document, curveElemIds: IList[ElementId]) """
        pass

    @staticmethod
    def CreateArcThroughPoints(document, startPoint, endPoint, interiorPoint):
        """
        CreateArcThroughPoints(document: Document, startPoint: ReferencePoint, endPoint: ReferencePoint, interiorPoint: ReferencePoint) -> CurveElement
        
            Creates an arc through the given reference points.
        
            document: The Document.
            startPoint: The start point of the arc.
            endPoint: The end end of the arc.
            interiorPoint: The interior point on the arc.
            Returns: The CurveElement to be created.
        """
        pass

    @staticmethod
    def CreateRectangle(document, startPoint, endPoint, projectionType, boundaryReferenceLines, boundaryCurvesFollowSurface, createdCurvesIds, createdCornersIds):
        """ CreateRectangle(document: Document, startPoint: ReferencePoint, endPoint: ReferencePoint, projectionType: CurveProjectionType, boundaryReferenceLines: bool, boundaryCurvesFollowSurface: bool) -> (IList[ElementId], IList[ElementId]) """
        pass

    def Dispose(self):
        """ Dispose(self: CurveByPointsUtils) """
        pass

    @staticmethod
    def GetFaceRegions(cda, referenceOfFace):
        """
        GetFaceRegions(cda: Document, referenceOfFace: Reference) -> IList[Reference]
        
            Gets the FaceRegions in the existing face.
        
            cda: The Document.
            referenceOfFace: The Reference of the existing face.
            Returns: The FaceRegions in the existing face, or an empty collection if no FaceRegions 
             are found.
        """
        pass

    @staticmethod
    def GetHostFace(curveElem):
        """
        GetHostFace(curveElem: CurveElement) -> Reference
        
            Gets the host face to which the CurveElement is added.
        
            curveElem: The CurveElement.
            Returns: The host face to which the CurveElement is added, or an empty Reference if the 
             host is not a face.
        """
        pass

    @staticmethod
    def GetProjectionType(curveElem):
        """
        GetProjectionType(curveElem: CurveElement) -> CurveProjectionType
        
            Gets the projection type of the CurveElement.
        
            curveElem: The CurveElement.
            Returns: The projection type.
        """
        pass

    @staticmethod
    def GetSketchOnSurface(curveElem):
        """
        GetSketchOnSurface(curveElem: CurveElement) -> bool
        
            Gets the relationship between the CurveElement and face.
        
            curveElem: The CurveElement.
            Returns: Whether or not the CurveElement should lie on the face and be able to be added 
             to the face.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CurveByPointsUtils, disposing: bool) """
        pass

    @staticmethod
    def SetProjectionType(curveElem, value):
        """
        SetProjectionType(curveElem: CurveElement, value: CurveProjectionType)
            Sets the projection type of the CurveElement.
        
            curveElem: The CurveElement.
            value: The input projection type.
        """
        pass

    @staticmethod
    def SetSketchOnSurface(curveElem, sketchOnSurface):
        """
        SetSketchOnSurface(curveElem: CurveElement, sketchOnSurface: bool)
            Sets the relationship between the CurveElement and face.
        
            curveElem: The CurveElement.
            sketchOnSurface: Whether or not the CurveElement should lie on the face and be able to be added 
             to the face.
        """
        pass

    @staticmethod
    def ValidateCurveElementIdArrayForFaceRegions(document, curveElemIds):
        """ ValidateCurveElementIdArrayForFaceRegions(document: Document, curveElemIds: IList[ElementId]) -> bool """
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

Get: IsValidObject(self: CurveByPointsUtils) -> bool

"""



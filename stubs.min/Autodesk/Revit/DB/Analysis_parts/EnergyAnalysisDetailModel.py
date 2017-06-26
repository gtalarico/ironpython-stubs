class EnergyAnalysisDetailModel(Element, IDisposable):
    """ Manage the analytical thermal model. """
    @staticmethod
    def Create(document, options):
        """
        Create(document: Document, options: EnergyAnalysisDetailModelOptions) -> EnergyAnalysisDetailModel
        
            Creates a new energy analysis detailed model.
        
            document: The document that contains the physical model of the building.
            options: The options to control the calculation rules.
            Returns: The created model instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAnalyticalOpenings(self):
        """
        GetAnalyticalOpenings(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisOpening]
        
            The collection of analytical openings.
            Returns: Returns the analytical openings after model calculation.
        """
        pass

    def GetAnalyticalShadingSurfaces(self):
        """
        GetAnalyticalShadingSurfaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSurface]
        
            The collection of analytical shading surfaces.
            Returns: Returns the analytical shading surfaces after model calculation.
        """
        pass

    def GetAnalyticalSpaces(self):
        """
        GetAnalyticalSpaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSpace]
        
            The collection of analytical spaces.
            Returns: Returns the analytical spaces after model calculation.
        """
        pass

    def GetAnalyticalSurfaces(self):
        """
        GetAnalyticalSurfaces(self: EnergyAnalysisDetailModel) -> IList[EnergyAnalysisSurface]
        
            The collection of analytical surfaces.
            Returns: Returns the analytical surfaces after model calculation.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetMainEnergyAnalysisDetailModel(document):
        """
        GetMainEnergyAnalysisDetailModel(document: Document) -> EnergyAnalysisDetailModel
        
            Gets the EnergyAnalysisDetailModel in given document.
        
            document: The document that contains the physical model of the building.
            Returns: Returns the EnergyAnalysisDetailModel contained in the document, if it exists. 
             If it does not exist, this returns ll.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def TransformModel(self):
        """
        TransformModel(self: EnergyAnalysisDetailModel)
            Transforms all surfaces in the model according to the document's active
           
             ground plane, shared coordinates and true north.
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

    ExportCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Export elements of this category in energy analysis.

Get: ExportCategory(self: EnergyAnalysisDetailModel) -> ElementId

Set: ExportCategory(self: EnergyAnalysisDetailModel) = value
"""

    ExportMullions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for exporting mullions.

Get: ExportMullions(self: EnergyAnalysisDetailModel) -> bool

"""

    IncludeShadingSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to set and get the setting for if shading surfaces should be included.

Get: IncludeShadingSurfaces(self: EnergyAnalysisDetailModel) -> bool

"""

    SimplifyCurtainSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for simplified curtain systems.

Get: SimplifyCurtainSystems(self: EnergyAnalysisDetailModel) -> bool

"""

    Tier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of computation for energy analysis model.

Get: Tier(self: EnergyAnalysisDetailModel) -> EnergyAnalysisDetailModelTier

"""



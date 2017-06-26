class PathReinforcement(Element, IDisposable):
    """ An object that represents an Path Reinforcement within the Autodesk Revit project. """
    @staticmethod
    def Create(document, hostElement, curveArray, flip, pathReinforcementTypeId, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId, rebarShapeId=None):
        """
        Create(document: Document, hostElement: Element, curveArray: IList[Curve], flip: bool, pathReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId) -> PathReinforcement
        Create(document: Document, hostElement: Element, curveArray: IList[Curve], flip: bool, pathReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId, rebarShapeId: ElementId) -> PathReinforcement
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurveElementIds(self):
        """
        GetCurveElementIds(self: PathReinforcement) -> IList[ElementId]
        
            Retrieves the set of ElementIds of curves forming the boundary of the Path 
             Reinforcement.
        
            Returns: A collection of ElementIds of ModelCurve elements.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: PathReinforcement) -> ElementId
        
            The element that contains the Path Reinforcement.
            Returns: The element that the Path Reinforcement object belongs to, such as a structural
             
           wall, floor or foundation.
        """
        pass

    @staticmethod
    def GetOrCreateDefaultRebarShape(document, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId):
        """
        GetOrCreateDefaultRebarShape(document: Document, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId) -> ElementId
        
            Creates a new RebarShape object with a default name or
           returns existing one 
             which fulfills Path Reinforcement bending data requirements.
        
        
            document: The document.
            rebarBarTypeId: The id of the RebarBarType.
            startRebarHookTypeId: The id of the RebarHookType for the start of the bar.
           If this parameter is 
             InvalidElementId, it means to create a rebar with no start hook.
        
            endRebarHookTypeId: The id of the RebarHookType for the end of the bar.
           If this parameter is 
             InvalidElementId, it means to create a rebar with no end hook.
        
            Returns: Rebar Shape id.
        """
        pass

    def GetRebarInSystemIds(self):
        """
        GetRebarInSystemIds(self: PathReinforcement) -> IList[ElementId]
        
            Returns the ids of the RebarInSystem elements owned by the PathReinforcement
          
              element.
        """
        pass

    def IsAlternatingLayerEnabled(self):
        """
        IsAlternatingLayerEnabled(self: PathReinforcement) -> bool
        
            Checks if alternating bars are present in Path Reinforcement.
            Returns: True if the alternating bars exist in Path Reinforcement instance.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: PathReinforcement, view: View3D) -> bool
        
            Checks if this Path Reinforcement is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if Path Reinforcement is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: PathReinforcement, view: View) -> bool
        
            Checks if Path Reinforcement is shown unobscured in a view.
        
            view: The view element
            Returns: True if Path Reinforcement is shown unobscured, false otherwise.
        """
        pass

    def IsValidAlternatingBarOrientation(self, orientation):
        """
        IsValidAlternatingBarOrientation(self: PathReinforcement, orientation: ReinforcementBarOrientation) -> bool
        
            Checks if orientation for alternating bars is valid.
        
            orientation: An orientation.
            Returns: True if orientation for alternating bars are valid.
        """
        pass

    def IsValidPrimaryBarOrientation(self, orientation):
        """
        IsValidPrimaryBarOrientation(self: PathReinforcement, orientation: ReinforcementBarOrientation) -> bool
        
            Checks if orientation for primary bars is valid.
        
            orientation: An orientation.
            Returns: True if orientation for primary bars are valid.
        """
        pass

    @staticmethod
    def IsValidRebarShapeId(aDoc, elementId):
        """
        IsValidRebarShapeId(aDoc: Document, elementId: ElementId) -> bool
        
            Identifies whether an element id corresponds to a Rebar Shape element which can 
             be used in Path Reinforcement.
        
        
            aDoc: The document.
            elementId: An element id.
            Returns: True if the specified element id corresponds to a Rebar Shape element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def RemovePathReinforcementSystem(doc, system):
        """
        RemovePathReinforcementSystem(doc: Document, system: PathReinforcement) -> IList[ElementId]
        
            Deletes the specified PathReinforcement, and converts its RebarInSystem
           
             elements to equivalent Rebar elements.
        
        
            doc: The document.
            system: A PathReinforcement element in the document.
            Returns: The ids of the newly created Rebar elements.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: PathReinforcement, view: View3D, solid: bool)
            Sets this Path Reinforcement to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if Path Reinforcement is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: PathReinforcement, view: View, unobscured: bool)
            Sets Path Reinforcement to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if Path Reinforcement is shown unobscured, false otherwise.
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

    AdditionalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional offset of rebars in the Path Reinforcement.

Get: AdditionalOffset(self: PathReinforcement) -> float

Set: AdditionalOffset(self: PathReinforcement) = value
"""

    AlternatingBarOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Orientation of alternating bars of Path Reinforcement.

Get: AlternatingBarOrientation(self: PathReinforcement) -> ReinforcementBarOrientation

Set: AlternatingBarOrientation(self: PathReinforcement) = value
"""

    AlternatingBarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the alternating bars of the Path Reinforcement.

Get: AlternatingBarShapeId(self: PathReinforcement) -> ElementId

Set: AlternatingBarShapeId(self: PathReinforcement) = value
"""

    PathReinforcementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the type of the Path Reinforcement.

Get: PathReinforcementType(self: PathReinforcement) -> PathReinforcementType

"""

    PrimaryBarOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Orientation of primary bars of Path Reinforcement.

Get: PrimaryBarOrientation(self: PathReinforcement) -> ReinforcementBarOrientation

Set: PrimaryBarOrientation(self: PathReinforcement) = value
"""

    PrimaryBarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the primary bars of the Path Reinforcement.

Get: PrimaryBarShapeId(self: PathReinforcement) -> ElementId

Set: PrimaryBarShapeId(self: PathReinforcement) = value
"""



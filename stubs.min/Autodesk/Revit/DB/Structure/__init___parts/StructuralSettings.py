class StructuralSettings(Element, IDisposable):
    """ Provides access to project-wide structural settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetStructuralSettings(doc):
        """
        GetStructuralSettings(doc: Document) -> StructuralSettings
        
            Obtains the StructuralSettings object for the specified project document.
        
            doc: A project document.
            Returns: The StructuralSettings object.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    AnalyticalLinkAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for the analytical link distance.

Get: AnalyticalLinkAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalLinkAutofixTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelAutoCheckConsistency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check automatically for consistency between the analytical
   and physical models.

Get: AnalyticalModelAutoCheckConsistency(self: StructuralSettings) -> bool

Set: AnalyticalModelAutoCheckConsistency(self: StructuralSettings) = value
"""

    AnalyticalModelAutoCheckMemberSupports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check automatically for member supports.

Get: AnalyticalModelAutoCheckMemberSupports(self: StructuralSettings) -> bool

Set: AnalyticalModelAutoCheckMemberSupports(self: StructuralSettings) = value
"""

    AnalyticalModelCheckAdjustment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for analytical model distance from default location is
   larger than the tolerance defined by the property
   AnalyticalModelAdjustmentTolerance.

Get: AnalyticalModelCheckAdjustment(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckAdjustment(self: StructuralSettings) = value
"""

    AnalyticalModelCheckBeamSlabDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check the analytical model distance between beam and slab for a level.

Get: AnalyticalModelCheckBeamSlabDistance(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckBeamSlabDistance(self: StructuralSettings) = value
"""

    AnalyticalModelCheckCircularReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check member supports for circular references.

Get: AnalyticalModelCheckCircularReferences(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckCircularReferences(self: StructuralSettings) = value
"""

    AnalyticalModelCheckDiscrepancy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for distance between analytical and physical models
   greater than a tolerance defined by
   AnalyticalModelDiscrepancyTolerance.

Get: AnalyticalModelCheckDiscrepancy(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckDiscrepancy(self: StructuralSettings) = value
"""

    AnalyticalModelCheckInstability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for possible instability based on release conditions.

Get: AnalyticalModelCheckInstability(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckInstability(self: StructuralSettings) = value
"""

    AnalyticalModelCheckSupportDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check that joins in the physical model are consistent
   with proximity in the analytical model.

Get: AnalyticalModelCheckSupportDistance(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckSupportDistance(self: StructuralSettings) = value
"""

    AnalyticalModelDiscrepancyTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for the analytical-to-physical model distance.

Get: AnalyticalModelDiscrepancyTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelDiscrepancyTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelHorizontalAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for horizontal auto-detect for the analytical model.

Get: AnalyticalModelHorizontalAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelHorizontalAutofixTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelSupportDistanceTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum distance between two structural elements,
   where analytical model support rules still apply.

Get: AnalyticalModelSupportDistanceTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelSupportDistanceTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelVerticalAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for vertical auto-detect for the analytical model.

Get: AnalyticalModelVerticalAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelVerticalAutofixTolerance(self: StructuralSettings) = value
"""

    BoundaryConditionAreaAndLineSymbolSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol spacing for boundary conditions.

Get: BoundaryConditionAreaAndLineSymbolSpacing(self: StructuralSettings) -> float

Set: BoundaryConditionAreaAndLineSymbolSpacing(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolFixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a fixed boundary condition.

Get: BoundaryConditionFamilySymbolFixed(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolFixed(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a pinned boundary condition.

Get: BoundaryConditionFamilySymbolPinned(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolPinned(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolRoller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a roller boundary condition.

Get: BoundaryConditionFamilySymbolRoller(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolRoller(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolUserDefined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a user-defined boundary condition.

Get: BoundaryConditionFamilySymbolUserDefined(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolUserDefined(self: StructuralSettings) = value
"""

    BraceAboveSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a brace above a beam in plan view.

Get: BraceAboveSymbol(self: StructuralSettings) -> ElementId

Set: BraceAboveSymbol(self: StructuralSettings) = value
"""

    BraceBelowSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a brace below a beam in plan view.

Get: BraceBelowSymbol(self: StructuralSettings) -> ElementId

Set: BraceBelowSymbol(self: StructuralSettings) = value
"""

    BraceParallelLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance by which brace symbols in plan
   views will be offset.

Get: BraceParallelLineOffset(self: StructuralSettings) -> float

Set: BraceParallelLineOffset(self: StructuralSettings) = value
"""

    CheckAnalyticalModelAsset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for valid Asset within the Material of associated Physical Element.

Get: CheckAnalyticalModelAsset(self: StructuralSettings) -> bool

Set: CheckAnalyticalModelAsset(self: StructuralSettings) = value
"""

    DifferentiateAnalyticalEnds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to use a subcategory for the ends of a linear analytical model, rather than
   the main category.

Get: DifferentiateAnalyticalEnds(self: StructuralSettings) -> bool

Set: DifferentiateAnalyticalEnds(self: StructuralSettings) = value
"""

    KickerBraceSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a kicker brace.

Get: KickerBraceSymbol(self: StructuralSettings) -> ElementId

Set: KickerBraceSymbol(self: StructuralSettings) = value
"""

    ShowBraceAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to show brace symbols above beams in plan views.

Get: ShowBraceAbove(self: StructuralSettings) -> bool

Set: ShowBraceAbove(self: StructuralSettings) = value
"""

    ShowBraceBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to show brace symbols below beams in plan views.

Get: ShowBraceBelow(self: StructuralSettings) -> bool

Set: ShowBraceBelow(self: StructuralSettings) = value
"""

    SymbolicCutbackForBeamAndTruss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all beams and trusses.

Get: SymbolicCutbackForBeamAndTruss(self: StructuralSettings) -> float

Set: SymbolicCutbackForBeamAndTruss(self: StructuralSettings) = value
"""

    SymbolicCutbackForBrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all braces.

Get: SymbolicCutbackForBrace(self: StructuralSettings) -> float

Set: SymbolicCutbackForBrace(self: StructuralSettings) = value
"""

    SymbolicCutbackForColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all columns.

Get: SymbolicCutbackForColumn(self: StructuralSettings) -> float

Set: SymbolicCutbackForColumn(self: StructuralSettings) = value
"""



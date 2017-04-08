# encoding: utf-8
# module Revit.Elements calls itself Elements
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Element(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: Element) """
        pass

    def Equals(self, obj):
        """ Equals(self: Element, obj: object) -> bool """
        pass

    def Geometry(self):
        """ Geometry(self: Element) -> Array[object] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Element) -> int """
        pass

    def GetLocation(self):
        """ GetLocation(self: Element) -> Geometry """
        pass

    def GetMaterials(self, paintMaterials):
        """ GetMaterials(self: Element, paintMaterials: bool) -> IEnumerable[Material] """
        pass

    def GetParameterValueByName(self, parameterName):
        """ GetParameterValueByName(self: Element, parameterName: str) -> object """
        pass

    def MoveByVector(self, vector):
        """ MoveByVector(self: Element, vector: Vector) """
        pass

    def OverrideColorInView(self, color):
        """ OverrideColorInView(self: Element, color: Color) -> Element """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """ SafeInit(self: Element, init: Action) """
        pass

    def SetLocation(self, geometry):
        """ SetLocation(self: Element, geometry: Geometry) """
        pass

    def SetParameterByName(self, parameterName, value):
        """ SetParameterByName(self: Element, parameterName: str, value: object) -> Element """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: Element, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: Element, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: Element) -> str
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Element) -> BoundingBox

"""

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curves(self: Element) -> Array[Curve]

"""

    ElementCurveReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementCurveReferences(self: Element) -> Array[ElementCurveReference]

"""

    ElementFaceReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementFaceReferences(self: Element) -> Array[ElementFaceReference]

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Element) -> Array[Surface]

"""

    GetCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetCategory(self: Element) -> Category

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Element) -> int

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Element) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Element) -> str

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: Element) -> Array[Parameter]

"""

    Solids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Solids(self: Element) -> Array[Solid]

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: Element) -> str

"""


    InternalUniqueId = None
    IsFrozen = None


class AbstractFamilyInstance(Element):
    # no doc
    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: AbstractFamilyInstance) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: AbstractFamilyInstance) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: AbstractFamilyInstance) -> Point

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AbstractFamilyInstance) -> FamilyType

"""


    InternalUniqueId = None


class AdaptiveComponent(AbstractFamilyInstance):
    # no doc
    @staticmethod
    def ByParametersOnCurveReference(parameters, *__args):
        """
        ByParametersOnCurveReference(parameters: Array[Array[float]], revitCurve: ElementCurveReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnCurveReference(parameters: Array[float], curve: Curve, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnCurveReference(parameters: Array[Array[float]], curve: Curve, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnCurveReference(parameters: Array[float], revitCurve: Element, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnCurveReference(parameters: Array[Array[float]], revitCurve: Element, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnCurveReference(parameters: Array[float], revitCurve: ElementCurveReference, familyType: FamilyType) -> AdaptiveComponent
        """
        pass

    @staticmethod
    def ByParametersOnFace(uvs, *__args):
        """
        ByParametersOnFace(uvs: Array[Array[Array[float]]], surface: Surface, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[Array[float]], surface: Surface, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnFace(uvs: Array[Array[UV]], surface: Surface, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[UV], surface: Surface, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnFace(uvs: Array[Array[Array[float]]], faceReference: ElementFaceReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[Array[float]], faceReference: ElementFaceReference, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnFace(uvs: Array[Array[UV]], faceReference: ElementFaceReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[UV], faceReference: ElementFaceReference, familyType: FamilyType) -> AdaptiveComponent
        """
        pass

    @staticmethod
    def ByPoints(points, familyType):
        """ ByPoints(points: Array[Array[Point]], familyType: FamilyType) -> Array[AdaptiveComponent] """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: AdaptiveComponent) -> List[Point]

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AdaptiveComponent) -> FamilyType

"""


    InternalUniqueId = None


class BuiltinNodeCategories(object):
    # no doc
    ANALYZE = 'Analyze'
    REVIT = 'Revit'
    REVIT_API = 'Revit.API'
    REVIT_BAKE = 'Revit.Bake'
    REVIT_DATUMS = 'Revit.Datums'
    REVIT_DOCUMENT = 'Revit.Document'
    REVIT_ELEMENTS_DIVIDEDPATH_ACTION = 'Revit.Elements.DividedPath.Actions'
    REVIT_FAMILIES = 'Revit.Families'
    REVIT_PARAMETERS = 'Revit.Parameters'
    REVIT_REFERENCE = 'Revit.Reference'
    REVIT_SELECTION = 'Revit.Selection'
    REVIT_VIEW = 'Revit.View'
    __all__ = [
        'ANALYZE',
        'REVIT',
        'REVIT_API',
        'REVIT_BAKE',
        'REVIT_DATUMS',
        'REVIT_DOCUMENT',
        'REVIT_ELEMENTS_DIVIDEDPATH_ACTION',
        'REVIT_FAMILIES',
        'REVIT_PARAMETERS',
        'REVIT_REFERENCE',
        'REVIT_SELECTION',
        'REVIT_VIEW',
    ]


class Category(object):
    # no doc
    @staticmethod
    def ById(id):
        """ ById(id: int) -> Category """
        pass

    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> Category """
        pass

    def ToString(self):
        """ ToString(self: Category) -> str """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Category) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Category) -> str

"""



class Coordinates(object):
    # no doc
    @staticmethod
    def BasePoint():
        """ BasePoint() -> Point """
        pass

    @staticmethod
    def ProjectRotation():
        """ ProjectRotation() -> float """
        pass

    @staticmethod
    def SurveyPoint():
        """ SurveyPoint() -> Point """
        pass

    __all__ = [
        'BasePoint',
        'ProjectRotation',
        'SurveyPoint',
    ]


class CurtainPanel(AbstractFamilyInstance):
    # no doc
    def AsFamilyInstance(self):
        """ AsFamilyInstance(self: CurtainPanel) -> FamilyInstance """
        pass

    @staticmethod
    def ByElement(hostingElement):
        """ ByElement(hostingElement: Element) -> Array[CurtainPanel] """
        pass

    def SupportingMullions(self):
        """ SupportingMullions(self: CurtainPanel) -> Array[Mullion] """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: CurtainPanel) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, panelElement: Panel) """
        pass

    Boundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundaries(self: CurtainPanel) -> Array[PolyCurve]

"""

    HasPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPlane(self: CurtainPanel) -> bool

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: CurtainPanel) -> float

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsRectangular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRectangular(self: CurtainPanel) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: CurtainPanel) -> float

"""

    PanelBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PanelPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PanelPlane(self: CurtainPanel) -> Plane

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: CurtainPanel) -> float

"""


    InternalUniqueId = None


class CurveElement(Element):
    # no doc
    def InternalSetCurve(self, *args): #cannot find CLR method
        """ InternalSetCurve(self: CurveElement, c: Curve) """
        pass

    def InternalSetCurveElement(self, *args): #cannot find CLR method
        """ InternalSetCurveElement(self: CurveElement, curveElement: CurveElement) """
        pass

    def setCurveMethod(self, *args): #cannot find CLR method
        """ setCurveMethod(ce: CurveElement, c: Curve) """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: CurveElement, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: CurveElement) -> Curve

"""

    ElementCurveReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementCurveReference(self: CurveElement) -> ElementCurveReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: CurveElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    hasMethodSetCurve = True
    InternalUniqueId = None


class CurveByPoints(CurveElement):
    # no doc
    @staticmethod
    def ByReferencePoints(points, isReferenceLine):
        """ ByReferencePoints(points: Array[ReferencePoint], isReferenceLine: bool) -> CurveByPoints """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: CurveByPoints) -> str """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class DetailCurve(CurveElement):
    # no doc
    @staticmethod
    def ByCurve(view, curve):
        """ ByCurve(view: View, curve: Curve) -> DetailCurve """
        pass

    def SetCurve(self, curve):
        """ SetCurve(self: DetailCurve, curve: Curve) """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: DetailCurve) -> str """
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: DetailCurve) -> Curve

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Dimension(Element):
    # no doc
    @staticmethod
    def ByElements(view, referenceElements, line, suffix, prefix):
        """ ByElements(view: View, referenceElements: IEnumerable[Element], line: Line, suffix: str, prefix: str) -> Dimension """
        pass

    def SetPrefix(self, values):
        """ SetPrefix(self: Dimension, values: IEnumerable[str]) """
        pass

    def SetSuffix(self, values):
        """ SetSuffix(self: Dimension, values: IEnumerable[str]) """
        pass

    def SetValueOverride(self, values):
        """ SetValueOverride(self: Dimension, values: IEnumerable[str]) """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Dimension) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: Dimension) -> IEnumerable[str]

"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: Dimension) -> IEnumerable[str]

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Dimension) -> IEnumerable[float]

"""

    ValueOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueOverride(self: Dimension) -> IEnumerable[str]

"""


    InternalUniqueId = None


class DirectShape(Element):
    # no doc
    @staticmethod
    def ByGeometry(geometry, category, material, name):
        """ ByGeometry(geometry: Geometry, category: Category, material: Material, name: str) -> DirectShape """
        pass

    @staticmethod
    def ByMesh(mesh, category, material, name):
        """ ByMesh(mesh: Mesh, category: Category, material: Material, name: str) -> DirectShape """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: DirectShape) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, shape: DirectShape)
        __new__(cls: type, shapeReference: DesignScriptEntity, shapename: str, category: Category, material: Material)
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: DirectShape) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DynamoPreviewMaterial = None
    InternalUniqueId = None


class DirectShapeState(SerializableId):
    """
    DirectShapeState(ds: DirectShape, syncId: str, materialId: ElementId)
    DirectShapeState(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: DirectShapeState, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, ds: DirectShape, syncId: str, materialId: ElementId)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    materialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: materialId(self: DirectShapeState) -> int

Set: materialId(self: DirectShapeState) = value
"""

    syncId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: syncId(self: DirectShapeState) -> str

Set: syncId(self: DirectShapeState) = value
"""



class DividedPath(Element):
    # no doc
    @staticmethod
    def ByCurveAndDivisions(*__args):
        """
        ByCurveAndDivisions(curve: Curve, divisions: int) -> DividedPath
        ByCurveAndDivisions(element: Element, divisions: int) -> DividedPath
        ByCurveAndDivisions(element: ElementCurveReference, divisions: int) -> DividedPath
        """
        pass

    @staticmethod
    def ByCurvesAndDivisions(*__args):
        """
        ByCurvesAndDivisions(curve: Array[Curve], divisions: int) -> DividedPath
        ByCurvesAndDivisions(elements: Array[Element], divisions: int) -> DividedPath
        ByCurvesAndDivisions(curveReferences: Array[ElementCurveReference], divisions: int) -> DividedPath
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: DividedPath) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: DividedPath) -> IEnumerable[Point]

"""


    InternalUniqueId = None


class DividedSurface(Element):
    # no doc
    @staticmethod
    def ByFaceAndUVDivisions(elementFace, uDivs, vDivs):
        """
        ByFaceAndUVDivisions(elementFace: Surface, uDivs: int, vDivs: int) -> DividedSurface
        ByFaceAndUVDivisions(elementFace: ElementFaceReference, uDivs: int, vDivs: int) -> DividedSurface
        """
        pass

    @staticmethod
    def ByFaceUVDivisionsAndRotation(*__args):
        """
        ByFaceUVDivisionsAndRotation(surface: Surface, uDivs: int, vDivs: int, gridRotation: float) -> DividedSurface
        ByFaceUVDivisionsAndRotation(faceReference: ElementFaceReference, uDivs: int, vDivs: int, gridRotation: float) -> DividedSurface
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: DividedSurface) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: DividedSurface) -> float

"""

    UDivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDivisions(self: DividedSurface) -> int

"""

    VDivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VDivisions(self: DividedSurface) -> int

"""


    InternalUniqueId = None


class ElementSelector(object):
    """ ElementSelector() """
    @staticmethod
    def ByElementId(elementId, isRevitOwned=None):
        """
        ByElementId(elementId: int) -> Element
        ByElementId(elementId: int, isRevitOwned: bool) -> Element
        """
        pass

    @staticmethod
    def ByUniqueId(uniqueId, isRevitOwned):
        """ ByUniqueId(uniqueId: str, isRevitOwned: bool) -> Element """
        pass


class ElementWrapper(object):
    # no doc
    @staticmethod
    def ToDSType(ele, isRevitOwned):
        """ ToDSType(ele: Element, isRevitOwned: bool) -> Element """
        pass

    @staticmethod
    def Wrap(*__args):
        """
        Wrap(topoSurface: TopographySurface, isRevitOwned: bool) -> Topography
        Wrap(view: ViewDrafting, isRevitOwned: bool) -> DraftingView
        Wrap(ele: Panel, isRevitOwned: bool) -> object
        Wrap(ele: Dimension, isRevitOwned: bool) -> Dimension
        Wrap(ele: Mullion, isRevitOwned: bool) -> Mullion
        Wrap(view: View3D, isRevitOwned: bool) -> View3D
        Wrap(ele: WallType, isRevitOwned: bool) -> WallType
        Wrap(view: ViewPlan, isRevitOwned: bool) -> Element
        Wrap(view: ViewSheet, isRevitOwned: bool) -> Sheet
        Wrap(view: ViewSection, isRevitOwned: bool) -> SectionView
        Wrap(ele: RevisionCloud, isRevitOwned: bool) -> RevisionCloud
        Wrap(ele: Revision, isRevitOwned: bool) -> Revision
        Wrap(ele: ParameterFilterElement, isRevitOwned: bool) -> ParameterFilterElement
        Wrap(ele: DetailCurve, isRevitOwned: bool) -> DetailCurve
        Wrap(ele: Room, isRevitOwned: bool) -> Room
        Wrap(ele: FilledRegion, isRevitOwned: bool) -> FilledRegion
        Wrap(ele: FilledRegionType, isRevitOwned: bool) -> FilledRegionType
        Wrap(ele: TextNote, isRevitOwned: bool) -> TextNote
        Wrap(ele: TextNoteType, isRevitOwned: bool) -> TextNoteType
        Wrap(ele: IndependentTag, isRevitOwned: bool) -> Tag
        Wrap(ele: Wall, isRevitOwned: bool) -> Wall
        Wrap(ele: FamilySymbol, isRevitOwned: bool) -> FamilyType
        Wrap(ele: Family, isRevitOwned: bool) -> Family
        Wrap(ele: Floor, isRevitOwned: bool) -> Floor
        Wrap(ele: Form, isRevitOwned: bool) -> Form
        Wrap(ele: FloorType, isRevitOwned: bool) -> FloorType
        Wrap(ele: FamilyInstance, isRevitOwned: bool) -> AbstractFamilyInstance
        Wrap(element: Element, isRevitOwned: bool) -> UnknownElement
        Wrap(ele: DirectShape, isRevitOwned: bool) -> DirectShape
        Wrap(ele: DividedSurface, isRevitOwned: bool) -> DividedSurface
        Wrap(ele: DividedPath, isRevitOwned: bool) -> DividedPath
        Wrap(ele: ModelTextType, isRevitOwned: bool) -> ModelTextType
        Wrap(ele: ModelText, isRevitOwned: bool) -> ModelText
        Wrap(ele: ReferencePlane, isRevitOwned: bool) -> ReferencePlane
        Wrap(ele: SketchPlane, isRevitOwned: bool) -> SketchPlane
        Wrap(ele: ReferencePoint, isRevitOwned: bool) -> ReferencePoint
        Wrap(ele: Grid, isRevitOwned: bool) -> Grid
        Wrap(ele: FreeFormElement, isRevitOwned: bool) -> FreeForm
        Wrap(ele: Level, isRevitOwned: bool) -> Level
        Wrap(ele: CurveByPoints, isRevitOwned: bool) -> CurveByPoints
        Wrap(ele: ModelCurve, isRevitOwned: bool) -> ModelCurve
        """
        pass

    __all__ = [
        'ToDSType',
        'Wrap',
    ]


class Family(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> Family """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Family) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Family) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Family) -> str

"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Types(self: Family) -> Array[FamilyType]

"""


    InternalUniqueId = None


class FamilyInstance(AbstractFamilyInstance):
    # no doc
    @staticmethod
    def ByCoordinates(familyType, x, y, z):
        """ ByCoordinates(familyType: FamilyType, x: float, y: float, z: float) -> FamilyInstance """
        pass

    @staticmethod
    def ByFace(familyType, face, *__args):
        """
        ByFace(familyType: FamilyType, face: Surface, location: Point, referenceDirection: Vector) -> FamilyInstance
        ByFace(familyType: FamilyType, face: Surface, line: Line) -> FamilyInstance
        """
        pass

    @staticmethod
    def ByFamilyType(familyType):
        """ ByFamilyType(familyType: FamilyType) -> Array[FamilyInstance] """
        pass

    @staticmethod
    def ByPoint(familyType, point):
        """ ByPoint(familyType: FamilyType, point: Point) -> FamilyInstance """
        pass

    @staticmethod
    def ByPointAndLevel(familyType, point, level):
        """ ByPointAndLevel(familyType: FamilyType, point: Point, level: Level) -> FamilyInstance """
        pass

    def SetRotation(self, degree):
        """ SetRotation(self: FamilyInstance, degree: float) -> FamilyInstance """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FamilyInstance) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, instance: FamilyInstance) """
        pass

    FacingOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FacingOrientation(self: FamilyInstance) -> Vector

"""

    GetFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetFamily(self: FamilyInstance) -> Family

"""

    GetHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetHost(self: FamilyInstance) -> Element

"""

    GetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetType(self: FamilyInstance) -> FamilyType

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: FamilyInstance) -> Point

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: FamilyInstance) -> FamilyType

"""


    InternalUniqueId = None


class FamilyType(Element):
    # no doc
    @staticmethod
    def ByFamilyAndName(family, name):
        """ ByFamilyAndName(family: Family, name: str) -> FamilyType """
        pass

    @staticmethod
    def ByFamilyNameAndTypeName(familyName, typeName):
        """ ByFamilyNameAndTypeName(familyName: str, typeName: str) -> FamilyType """
        pass

    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> FamilyType """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FamilyType) -> str """
        pass

    Family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Family(self: FamilyType) -> Family

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: FamilyType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FamilyType) -> str

"""


    InternalUniqueId = None


class FilledRegion(Element):
    # no doc
    @staticmethod
    def ByCurves(view, boundary, regionType):
        """ ByCurves(view: View, boundary: IEnumerable[Curve], regionType: FilledRegionType) -> FilledRegion """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: FilledRegion) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class FilledRegionType(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> FilledRegionType """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: FilledRegionType) -> Color

"""

    FillPatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillPatternId(self: FilledRegionType) -> ElementId

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: FilledRegionType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FilledRegionType) -> str

"""


    InternalUniqueId = None


class Floor(Element):
    # no doc
    @staticmethod
    def ByOutlineTypeAndLevel(*__args):
        """
        ByOutlineTypeAndLevel(outline: PolyCurve, floorType: FloorType, level: Level) -> Floor
        ByOutlineTypeAndLevel(outlineCurves: Array[Curve], floorType: FloorType, level: Level) -> Floor
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Floor) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class FloorType(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> FloorType """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FloorType) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: FloorType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FloorType) -> str

"""


    InternalUniqueId = None


class Form(Element):
    # no doc
    @staticmethod
    def ByLoftCrossSections(curves, isSolid):
        """
        ByLoftCrossSections(curves: Array[Array[Element]], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Curve], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Array[Curve]], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[ElementCurveReference], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Array[ElementCurveReference]], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Element], isSolid: bool) -> Form
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Form) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class FreeForm(Element):
    # no doc
    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: FreeForm) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Grid(Element):
    # no doc
    @staticmethod
    def ByArc(arc):
        """ ByArc(arc: Arc) -> Grid """
        pass

    @staticmethod
    def ByLine(line):
        """ ByLine(line: Line) -> Grid """
        pass

    @staticmethod
    def ByStartPointEndPoint(start, end):
        """ ByStartPointEndPoint(start: Point, end: Point) -> Grid """
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: Grid) -> Curve

"""

    ElementCurveReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementCurveReference(self: Grid) -> ElementCurveReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Grid) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class ImportInstance(Element):
    # no doc
    @staticmethod
    def ByGeometries(geometries):
        """ ByGeometries(geometries: Array[Geometry]) -> ImportInstance """
        pass

    @staticmethod
    def ByGeometry(geometry):
        """ ByGeometry(geometry: Geometry) -> ImportInstance """
        pass

    @staticmethod
    def BySATFile(pathToFile):
        """ BySATFile(pathToFile: str) -> ImportInstance """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ImportInstance) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: ImportInstance) -> str

"""


    InternalUniqueId = None


class Level(Element):
    # no doc
    @staticmethod
    def ByElevation(elevation):
        """ ByElevation(elevation: float) -> Level """
        pass

    @staticmethod
    def ByElevationAndName(elevation, name):
        """ ByElevationAndName(elevation: float, name: str) -> Level """
        pass

    @staticmethod
    def ByLevelAndOffset(level, offset):
        """ ByLevelAndOffset(level: Level, offset: float) -> Level """
        pass

    @staticmethod
    def ByLevelOffsetAndName(level, offset, name):
        """ ByLevelOffsetAndName(level: Level, offset: float, name: str) -> Level """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Level) -> str """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: Level) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Level) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Level) -> str

"""

    ProjectElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectElevation(self: Level) -> float

"""


    InternalUniqueId = None


class LevelTraceData(SerializableId):
    """
    LevelTraceData(lev: Level, inputName: str)
    LevelTraceData(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: LevelTraceData, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, lev: Level, inputName: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    InputName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputName(self: LevelTraceData) -> str

Set: InputName(self: LevelTraceData) = value
"""



class Material(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> Material """
        pass

    AppearanceParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppearanceParameters(self: Material) -> IEnumerable[Parameter]

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Material) -> Color

"""

    CutPatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPatternColor(self: Material) -> Color

"""

    CutPatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPatternId(self: Material) -> int

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Material) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaterialCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialCategory(self: Material) -> str

"""

    MaterialClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialClass(self: Material) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Material) -> str

"""

    Shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shininess(self: Material) -> int

"""

    Smoothness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Smoothness(self: Material) -> int

"""

    StructuralParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructuralParameters(self: Material) -> IEnumerable[Parameter]

"""

    SurfacePatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfacePatternColor(self: Material) -> Color

"""

    ThermalParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalParameters(self: Material) -> IEnumerable[Parameter]

"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparency(self: Material) -> int

"""


    InternalUniqueId = None


class ModelCurve(CurveElement):
    # no doc
    @staticmethod
    def ByCurve(curve):
        """ ByCurve(curve: Curve) -> ModelCurve """
        pass

    @staticmethod
    def ReferenceCurveByCurve(curve):
        """ ReferenceCurveByCurve(curve: Curve) -> ModelCurve """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: ModelCurve) -> str """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class ModelText(Element):
    # no doc
    @staticmethod
    def ByTextSketchPlaneAndPosition(text, sketchPlane, xCoordinateInPlane, yCoordinateInPlane, textDepth, modelTextType):
        """ ByTextSketchPlaneAndPosition(text: str, sketchPlane: SketchPlane, xCoordinateInPlane: float, yCoordinateInPlane: float, textDepth: float, modelTextType: ModelTextType) -> ModelText """
        pass

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: ModelText) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ModelText) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ModelText) -> Point

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: ModelText) -> str

"""


    InternalUniqueId = None


class ModelTextType(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> ModelTextType """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ModelTextType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Mullion(AbstractFamilyInstance):
    # no doc
    def AsFamilyInstance(self):
        """ AsFamilyInstance(self: Mullion) -> FamilyInstance """
        pass

    @staticmethod
    def ByElement(hostingElement):
        """ ByElement(hostingElement: Element) -> Array[Mullion] """
        pass

    def InitMullion(self, *args): #cannot find CLR method
        """ InitMullion(self: Mullion, mullionElement: Mullion) """
        pass

    def SupportedPanels(self):
        """ SupportedPanels(self: Mullion) -> Array[CurtainPanel] """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Mullion) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, mullionElement: Mullion) """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LocationCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCurve(self: Mullion) -> Curve

"""


    InternalUniqueId = None


class Parameter(object):
    # no doc
    @staticmethod
    def CreateProjectParameter(parameterName, groupName, type, group, instance, categoryList):
        """ CreateProjectParameter(parameterName: str, groupName: str, type: str, group: str, instance: bool, categoryList: IEnumerable[Category]) """
        pass

    @staticmethod
    def CreateProjectParameterForAllCategories(parameterName, groupName, type, group, instance):
        """ CreateProjectParameterForAllCategories(parameterName: str, groupName: str, type: str, group: str, instance: bool) """
        pass

    @staticmethod
    def CreateSharedParameter(parameterName, groupName, type, group, instance, categoryList):
        """ CreateSharedParameter(parameterName: str, groupName: str, type: str, group: str, instance: bool, categoryList: IEnumerable[Category]) """
        pass

    @staticmethod
    def CreateSharedParameterForAllCategories(parameterName, groupName, type, group, instance):
        """ CreateSharedParameterForAllCategories(parameterName: str, groupName: str, type: str, group: str, instance: bool) """
        pass

    @staticmethod
    def ParameterByName(element, name):
        """ ParameterByName(element: Element, name: str) -> Parameter """
        pass

    @staticmethod
    def SetValue(parameter, value):
        """ SetValue(parameter: Parameter, value: object) """
        pass

    @staticmethod
    def SharedParameterFile():
        """ SharedParameterFile() -> str """
        pass

    def ToString(self):
        """ ToString(self: Parameter) -> str """
        pass

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: Parameter) -> str

"""

    HasValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValue(self: Parameter) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Parameter) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Parameter) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: Parameter) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Parameter) -> str

"""

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterType(self: Parameter) -> str

"""

    StorageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StorageType(self: Parameter) -> str

"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitType(self: Parameter) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Parameter) -> object

"""



class ParseEnum(object):
    """ ParseEnum() """
    @staticmethod
    def ByString(value, typeName):
        """ ByString(value: str, typeName: str) -> object """
        pass


class PlanView(View):
    """ PlanView() """
    def CreatePlanView(self, *args): #cannot find CLR method
        """ CreatePlanView(level: Level, planType: ViewFamily) -> ViewPlan """
        pass

    def InternalSetPlanView(self, *args): #cannot find CLR method
        """ InternalSetPlanView(self: PlanView, plan: ViewPlan) """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: PlanView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class ReferencePlane(Element):
    # no doc
    @staticmethod
    def ByLine(line):
        """ ByLine(line: Line) -> ReferencePlane """
        pass

    @staticmethod
    def ByStartPointEndPoint(start, end):
        """ ByStartPointEndPoint(start: Point, end: Point) -> ReferencePlane """
        pass

    ElementPlaneReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementPlaneReference(self: ReferencePlane) -> ElementPlaneReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ReferencePlane) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: ReferencePlane) -> Plane

"""


    InternalUniqueId = None


class ReferencePoint(Element):
    # no doc
    @staticmethod
    def ByCoordinates(x, y, z):
        """ ByCoordinates(x: float, y: float, z: float) -> ReferencePoint """
        pass

    @staticmethod
    def ByLengthOnCurveReference(elementCurveReference, length):
        """ ByLengthOnCurveReference(elementCurveReference: object, length: float) -> ReferencePoint """
        pass

    @staticmethod
    def ByParameterOnCurveReference(elementCurveReference, parameter):
        """ ByParameterOnCurveReference(elementCurveReference: object, parameter: float) -> ReferencePoint """
        pass

    @staticmethod
    def ByParametersOnFaceReference(elementFaceReference, u, v):
        """ ByParametersOnFaceReference(elementFaceReference: object, u: float, v: float) -> ReferencePoint """
        pass

    @staticmethod
    def ByPoint(pt):
        """ ByPoint(pt: Point) -> ReferencePoint """
        pass

    @staticmethod
    def ByPointVectorDistance(basePoint, direction, distance):
        """ ByPointVectorDistance(basePoint: Point, direction: Vector, distance: float) -> ReferencePoint """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: ReferencePoint, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: ReferencePoint) -> str
        """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ReferencePoint) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ReferencePoint) -> Point

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: ReferencePoint) -> float

Set: X(self: ReferencePoint) = value
"""

    XYPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYPlane(self: ReferencePoint) -> Plane

"""

    XZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XZPlane(self: ReferencePoint) -> Plane

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: ReferencePoint) -> float

Set: Y(self: ReferencePoint) = value
"""

    YZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YZPlane(self: ReferencePoint) -> Plane

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: ReferencePoint) -> float

Set: Z(self: ReferencePoint) = value
"""


    InternalUniqueId = None


class Revision(Element):
    # no doc
    @staticmethod
    def ByName(name, revDate, description, issued, issuedBy, issuedTo, visibility, numberType):
        """ ByName(name: str, revDate: str, description: str, issued: bool, issuedBy: str, issuedTo: str, visibility: str, numberType: str) -> Revision """
        pass

    def SetIssued(self, value):
        """ SetIssued(self: Revision, value: bool) """
        pass

    def SetIssuedBy(self, value):
        """ SetIssuedBy(self: Revision, value: str) """
        pass

    def SetIssuedTo(self, value):
        """ SetIssuedTo(self: Revision, value: str) """
        pass

    def SetRevisionDate(self, value):
        """ SetRevisionDate(self: Revision, value: str) """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Revision) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Issued = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Issued(self: Revision) -> bool

"""

    IssuedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IssuedBy(self: Revision) -> str

"""

    IssuedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IssuedTo(self: Revision) -> str

"""

    RevisionDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RevisionDate(self: Revision) -> str

"""


    InternalUniqueId = None


class RevisionCloud(Element):
    # no doc
    @staticmethod
    def ByCurve(view, curves, revision):
        """ ByCurve(view: View, curves: IEnumerable[Curve], revision: Element) -> RevisionCloud """
        pass

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curves(self: RevisionCloud) -> IEnumerable[Curve]

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: RevisionCloud) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Revision(self: RevisionCloud) -> Revision

"""


    InternalUniqueId = None


class Room(Element):
    # no doc
    @staticmethod
    def ByLocation(level, location, name, number):
        """ ByLocation(level: Level, location: Point, name: str, number: str) -> Room """
        pass

    def IsInsideRoom(self, point):
        """ IsInsideRoom(self: Room, point: Point) -> bool """
        pass

    def SetName(self, value):
        """ SetName(self: Room, value: str) """
        pass

    def SetNumber(self, value):
        """ SetNumber(self: Room, value: str) """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Room) -> float

"""

    CenterBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    CoreBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoreBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    CoreCenterBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoreCenterBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    FinishBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinishBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Room) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Room) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Room) -> Point

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Room) -> str

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: Room) -> str

"""


    InternalUniqueId = None


class SketchPlane(Element):
    # no doc
    @staticmethod
    def ByPlane(plane):
        """ ByPlane(plane: Plane) -> SketchPlane """
        pass

    ElementPlaneReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementPlaneReference(self: SketchPlane) -> ElementPlaneReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: SketchPlane) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: SketchPlane) -> Plane

"""


    InternalUniqueId = None


class StructuralFraming(AbstractFamilyInstance):
    # no doc
    @staticmethod
    def BeamByCurve(curve, level, structuralFramingType):
        """ BeamByCurve(curve: Curve, level: Level, structuralFramingType: FamilyType) -> StructuralFraming """
        pass

    @staticmethod
    def BraceByCurve(curve, level, structuralFramingType):
        """ BraceByCurve(curve: Curve, level: Level, structuralFramingType: FamilyType) -> StructuralFraming """
        pass

    @staticmethod
    def ByCurveLevelUpVectorAndType(curve, level, upVector, structuralType, structuralFramingType):
        """ ByCurveLevelUpVectorAndType(curve: Curve, level: Level, upVector: Vector, structuralType: StructuralType, structuralFramingType: FamilyType) -> StructuralFraming """
        pass

    @staticmethod
    def ColumnByCurve(curve, level, structuralColumnType):
        """ ColumnByCurve(curve: Curve, level: Level, structuralColumnType: FamilyType) -> StructuralFraming """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: StructuralFraming) -> Curve

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: StructuralFraming) -> FamilyType

"""


    InternalUniqueId = None


class StructuralType(Enum):
    """ enum StructuralType, values: Beam (0), Brace (1), Column (2), Footing (3), NonStructural (4) """
    Beam = None
    Brace = None
    Column = None
    Footing = None
    NonStructural = None
    value__ = None


class SunSettings(Element):
    # no doc
    @staticmethod
    def Current():
        """ Current() -> SunSettings """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: SunSettings) -> str """
        pass

    Altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Altitude(self: SunSettings) -> float

"""

    Azimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Azimuth(self: SunSettings) -> float

"""

    CurrentDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDateTime(self: SunSettings) -> DateTime

"""

    EndDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDateTime(self: SunSettings) -> DateTime

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: SunSettings) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    StartDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDateTime(self: SunSettings) -> DateTime

"""

    SunDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SunDirection(self: SunSettings) -> Vector

"""


    InternalUniqueId = None


class TextElement(Element):
    # no doc
    def Tessellate(self, package, parameters):
        """ Tessellate(self: TextElement, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: TextElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Tag(TextElement):
    # no doc
    @staticmethod
    def ByElement(view, element, horizontal, addLeader, horizontalAlignment, verticalAlignment, offset, isOffset):
        """ ByElement(view: View, element: Element, horizontal: bool, addLeader: bool, horizontalAlignment: str, verticalAlignment: str, offset: Vector, isOffset: bool) -> Tag """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    TaggedElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaggedElement(self: Tag) -> Element

"""

    TagText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagText(self: Tag) -> str

"""


    InternalUniqueId = None


class TextNote(TextElement):
    # no doc
    @staticmethod
    def ByLocation(view, location, text, alignment, type, keepRotatedTextReadable, rotation):
        """ ByLocation(view: View, location: Point, text: str, alignment: str, type: TextNoteType, keepRotatedTextReadable: bool, rotation: float) -> TextNote """
        pass

    def SetHorizontalAlignment(self, value):
        """ SetHorizontalAlignment(self: TextNote, value: str) """
        pass

    def SetKeepRotatedTextReadable(self, value):
        """ SetKeepRotatedTextReadable(self: TextNote, value: bool) """
        pass

    def SetText(self, value):
        """ SetText(self: TextNote, value: str) """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: TextNote) -> float

"""

    HorizontalAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizontalAlignment(self: TextNote) -> str

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: TextNote) -> str

"""

    Typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Typename(self: TextNote) -> str

"""

    VerticalAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalAlignment(self: TextNote) -> str

"""


    InternalUniqueId = None


class TextNoteType(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> TextNoteType """
        pass

    @staticmethod
    def Default():
        """ Default() -> TextNoteType """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: TextNoteType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Topography(Element):
    # no doc
    @staticmethod
    def ByPoints(points):
        """ ByPoints(points: IEnumerable[Point]) -> Topography """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Topography) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Topography) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Mesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mesh(self: Topography) -> Mesh

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Topography) -> List[Point]

"""


    InternalUniqueId = None


class UnknownElement(Element):
    # no doc
    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: UnknownElement) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: UnknownElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Wall(Element):
    # no doc
    @staticmethod
    def ByCurveAndHeight(curve, height, level, wallType):
        """ ByCurveAndHeight(curve: Curve, height: float, level: Level, wallType: WallType) -> Wall """
        pass

    @staticmethod
    def ByCurveAndLevels(c, startLevel, endLevel, wallType):
        """ ByCurveAndLevels(c: Curve, startLevel: Level, endLevel: Level, wallType: WallType) -> Wall """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Wall) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class WallType(Element):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> WallType """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: WallType) -> str """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: WallType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: WallType) -> str

"""


    InternalUniqueId = None


# variables with complex values


# encoding: utf-8
# module Tekla.Structures.Model.UI calls itself UI
# from Tekla.Structures.Model, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ClipPlane(object):
    """ ClipPlane() """
    def Delete(self):
        """ Delete(self: ClipPlane) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ClipPlane) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ClipPlane) -> bool """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: ClipPlane) -> Point

Set: Location(self: ClipPlane) = value
"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: ClipPlane) -> Vector

Set: UpVector(self: ClipPlane) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: ClipPlane) -> View

Set: View(self: ClipPlane) = value
"""



class ClipPlaneCollection(object):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: ClipPlaneCollection, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ClipPlaneCollection) -> IEnumerator """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ClipPlaneCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: ClipPlaneCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: ClipPlaneCollection) -> object

"""



class Color(object):
    """
    Color()
    Color(Red: float, Green: float, Blue: float)
    Color(Red: float, Green: float, Blue: float, Transparency: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, Red=None, Green=None, Blue=None, Transparency=None):
        """
        __new__(cls: type)
        __new__(cls: type, Red: float, Green: float, Blue: float)
        __new__(cls: type, Red: float, Green: float, Blue: float, Transparency: float)
        """
        pass

    Blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blue(self: Color) -> float

Set: Blue(self: Color) = value
"""

    Green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Green(self: Color) -> float

Set: Green(self: Color) = value
"""

    Red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Red(self: Color) -> float

Set: Red(self: Color) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparency(self: Color) -> float

Set: Transparency(self: Color) = value
"""



class GraphicPolyLine(object):
    """
    GraphicPolyLine()
    GraphicPolyLine(color: Color, width: int, type: LineType)
    GraphicPolyLine(polyLine: PolyLine, color: Color, width: int, type: LineType)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, color: Color, width: int, type: LineType)
        __new__(cls: type, polyLine: PolyLine, color: Color, width: int, type: LineType)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: GraphicPolyLine) -> Color

Set: Color(self: GraphicPolyLine) = value
"""

    PolyLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolyLine(self: GraphicPolyLine) -> PolyLine

Set: PolyLine(self: GraphicPolyLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GraphicPolyLine) -> LineType

Set: Type(self: GraphicPolyLine) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: GraphicPolyLine) -> int

Set: Width(self: GraphicPolyLine) = value
"""


    LineType = None


class GraphicsDrawer(object):
    """ GraphicsDrawer() """
    def DrawLineSegment(self, *__args):
        """
        DrawLineSegment(self: GraphicsDrawer, Point1: Point, Point2: Point, Color: Color) -> bool
        DrawLineSegment(self: GraphicsDrawer, LineSegment: LineSegment, Color: Color) -> bool
        """
        pass

    def DrawMeshLines(self, Mesh, Color):
        """ DrawMeshLines(self: GraphicsDrawer, Mesh: Mesh, Color: Color) -> bool """
        pass

    def DrawMeshSurface(self, Mesh, Color):
        """ DrawMeshSurface(self: GraphicsDrawer, Mesh: Mesh, Color: Color) -> bool """
        pass

    def DrawPolyLine(self, GraphicPolyLine):
        """ DrawPolyLine(self: GraphicsDrawer, GraphicPolyLine: GraphicPolyLine) -> int """
        pass

    def DrawText(self, Location, Text, Color):
        """ DrawText(self: GraphicsDrawer, Location: Point, Text: str, Color: Color) -> bool """
        pass

    def RemoveTemporaryGraphicsObject(self, GraphicObjectID):
        """ RemoveTemporaryGraphicsObject(self: GraphicsDrawer, GraphicObjectID: int) """
        pass

    def RemoveTemporaryGraphicsObjects(self, GraphicObjectIDs):
        """ RemoveTemporaryGraphicsObjects(self: GraphicsDrawer, GraphicObjectIDs: IEnumerable) """
        pass


class Mesh(object):
    """
    Mesh()
    Mesh(Points: ArrayList, Triangles: ArrayList, Lines: ArrayList)
    """
    def AddLine(self, Index1, Index2):
        """ AddLine(self: Mesh, Index1: int, Index2: int) """
        pass

    def AddPoint(self, Point):
        """ AddPoint(self: Mesh, Point: Point) -> int """
        pass

    def AddTriangle(self, Index1, Index2, Index3):
        """ AddTriangle(self: Mesh, Index1: int, Index2: int, Index3: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Points=None, Triangles=None, Lines=None):
        """
        __new__(cls: type)
        __new__(cls: type, Points: ArrayList, Triangles: ArrayList, Lines: ArrayList)
        """
        pass

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: Mesh) -> ArrayList

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Mesh) -> ArrayList

"""

    Triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangles(self: Mesh) -> ArrayList

"""



class ModelObjectSelector(object):
    """ ModelObjectSelector() """
    def GetObjectsByBoundingBox(self, MinPoint, MaxPoint, View):
        """ GetObjectsByBoundingBox(self: ModelObjectSelector, MinPoint: Point, MaxPoint: Point, View: View) -> ModelObjectEnumerator """
        pass

    def GetSelectedObjects(self):
        """ GetSelectedObjects(self: ModelObjectSelector) -> ModelObjectEnumerator """
        pass

    def Select(self, ModelObjects, ShowDimensions=None):
        """
        Select(self: ModelObjectSelector, ModelObjects: ArrayList, ShowDimensions: bool) -> bool
        Select(self: ModelObjectSelector, ModelObjects: ArrayList) -> bool
        """
        pass


class ModelObjectVisualization(object):
    # no doc
    @staticmethod
    def ClearAllTemporaryStates():
        """ ClearAllTemporaryStates() -> bool """
        pass

    @staticmethod
    def GetRepresentation(modelObject, color):
        """ GetRepresentation(modelObject: ModelObject, color: Color) -> (bool, Color) """
        pass

    @staticmethod
    def SetTemporaryState(modelObjects, color):
        """ SetTemporaryState(modelObjects: List[ModelObject], color: Color) -> bool """
        pass

    @staticmethod
    def SetTemporaryStateForAll(color):
        """ SetTemporaryStateForAll(color: Color) -> bool """
        pass

    @staticmethod
    def SetTransparency(modelObjects, transparency):
        """ SetTransparency(modelObjects: List[ModelObject], transparency: TemporaryTransparency) -> bool """
        pass

    @staticmethod
    def SetTransparencyForAll(transparency):
        """ SetTransparencyForAll(transparency: TemporaryTransparency) -> bool """
        pass

    __all__ = [
        '__reduce_ex__',
        'ClearAllTemporaryStates',
        'GetRepresentation',
        'SetTemporaryState',
        'SetTemporaryStateForAll',
        'SetTransparency',
        'SetTransparencyForAll',
    ]


class ModelViewEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: ModelViewEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: ModelViewEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ModelViewEnumerator) -> int

"""

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ModelViewEnumerator) -> View

"""

    CurrentViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentViewId(self: ModelViewEnumerator) -> int

"""



class Picker(object):
    """ Picker() """
    def PickFace(self, Prompt=None):
        """
        PickFace(self: Picker, Prompt: str) -> PickInput
        PickFace(self: Picker) -> PickInput
        """
        pass

    def PickLine(self, Prompt=None):
        """
        PickLine(self: Picker, Prompt: str) -> ArrayList
        PickLine(self: Picker) -> ArrayList
        """
        pass

    def PickObject(self, Enum, Prompt=None):
        """
        PickObject(self: Picker, Enum: PickObjectEnum, Prompt: str) -> ModelObject
        PickObject(self: Picker, Enum: PickObjectEnum) -> ModelObject
        """
        pass

    def PickObjects(self, Enum, Prompt=None):
        """
        PickObjects(self: Picker, Enum: PickObjectsEnum, Prompt: str) -> ModelObjectEnumerator
        PickObjects(self: Picker, Enum: PickObjectsEnum) -> ModelObjectEnumerator
        """
        pass

    def PickPoint(self, Prompt=None):
        """
        PickPoint(self: Picker, Prompt: str) -> Point
        PickPoint(self: Picker) -> Point
        """
        pass

    def PickPoints(self, Enum, Prompt=None):
        """
        PickPoints(self: Picker, Enum: PickPointEnum, Prompt: str) -> ArrayList
        PickPoints(self: Picker, Enum: PickPointEnum) -> ArrayList
        """
        pass

    PickObjectEnum = None
    PickObjectsEnum = None
    PickPointEnum = None


class PickInput(object):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: PickInput, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PickInput) -> IEnumerator """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PickInput) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: PickInput) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: PickInput) -> object

"""



class TemporaryTransparency(Enum):
    """ enum TemporaryTransparency, values: HIDDEN (0), SEMITRANSPARENT (3), SEMIVISIBLE (5), TRANSPARENT (1), VISIBLE (10) """
    HIDDEN = None
    SEMITRANSPARENT = None
    SEMIVISIBLE = None
    TRANSPARENT = None
    value__ = None
    VISIBLE = None


class View(object):
    """ View() """
    def Delete(self):
        """ Delete(self: View) -> bool """
        pass

    def GetClipPlanes(self):
        """ GetClipPlanes(self: View) -> ClipPlaneCollection """
        pass

    def Insert(self):
        """ Insert(self: View) -> bool """
        pass

    def IsPerspectiveViewProjection(self):
        """ IsPerspectiveViewProjection(self: View) -> bool """
        pass

    def IsVisible(self):
        """ IsVisible(self: View) -> bool """
        pass

    def Modify(self):
        """ Modify(self: View) -> bool """
        pass

    def Select(self):
        """ Select(self: View) -> bool """
        pass

    CurrentRepresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRepresentation(self: View) -> str

Set: CurrentRepresentation(self: View) = value
"""

    DisplayCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayCoordinateSystem(self: View) -> CoordinateSystem

Set: DisplayCoordinateSystem(self: View) = value
"""

    DisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayType(self: View) -> DisplayOrientationType

Set: DisplayType(self: View) = value
"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: View) -> Identifier

Set: Identifier(self: View) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: View) -> str

Set: Name(self: View) = value
"""

    SharedView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SharedView(self: View) -> bool

Set: SharedView(self: View) = value
"""

    ViewCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewCoordinateSystem(self: View) -> CoordinateSystem

Set: ViewCoordinateSystem(self: View) = value
"""

    ViewDepthDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewDepthDown(self: View) -> float

Set: ViewDepthDown(self: View) = value
"""

    ViewDepthUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewDepthUp(self: View) -> float

Set: ViewDepthUp(self: View) = value
"""

    ViewFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewFilter(self: View) -> str

Set: ViewFilter(self: View) = value
"""

    ViewProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewProjection(self: View) -> ViewProjectionType

"""

    ViewRendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewRendering(self: View) -> ViewRenderingType

"""

    VisibilitySettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisibilitySettings(self: View) -> ViewVisibilitySettings

Set: VisibilitySettings(self: View) = value
"""

    WorkArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorkArea(self: View) -> AABB

Set: WorkArea(self: View) = value
"""


    DisplayOrientationType = None
    ViewProjectionType = None
    ViewRenderingType = None


class ViewCamera(object):
    """ ViewCamera() """
    def Modify(self):
        """ Modify(self: ViewCamera) -> bool """
        pass

    def Select(self):
        """ Select(self: ViewCamera) -> bool """
        pass

    DirectionVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionVector(self: ViewCamera) -> Vector

Set: DirectionVector(self: ViewCamera) = value
"""

    FieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldOfView(self: ViewCamera) -> float

Set: FieldOfView(self: ViewCamera) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: ViewCamera) -> Point

Set: Location(self: ViewCamera) = value
"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: ViewCamera) -> Vector

Set: UpVector(self: ViewCamera) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: ViewCamera) -> View

Set: View(self: ViewCamera) = value
"""

    ZoomFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoomFactor(self: ViewCamera) -> float

Set: ZoomFactor(self: ViewCamera) = value
"""



class ViewHandler(object):
    """ ViewHandler() """
    @staticmethod
    def GetAllViews():
        """ GetAllViews() -> ModelViewEnumerator """
        pass

    @staticmethod
    def GetPermanentViews():
        """ GetPermanentViews() -> ModelViewEnumerator """
        pass

    @staticmethod
    def GetSelectedViews():
        """ GetSelectedViews() -> ModelViewEnumerator """
        pass

    @staticmethod
    def GetTemporaryViews():
        """ GetTemporaryViews() -> ModelViewEnumerator """
        pass

    @staticmethod
    def GetVisibleViews():
        """ GetVisibleViews() -> ModelViewEnumerator """
        pass

    @staticmethod
    def HideView(view):
        """ HideView(view: View) -> bool """
        pass

    @staticmethod
    def RedrawView(view):
        """ RedrawView(view: View) -> bool """
        pass

    @staticmethod
    def SetRepresentation(Representation):
        """ SetRepresentation(Representation: str) -> bool """
        pass

    @staticmethod
    def ShowView(view):
        """ ShowView(view: View) -> bool """
        pass

    @staticmethod
    def ZoomToBoundingBox(*__args):
        """
        ZoomToBoundingBox(box: AABB) -> bool
        ZoomToBoundingBox(view: View, B: AABB) -> bool
        """
        pass


class ViewVisibilitySettings(object):
    """ ViewVisibilitySettings() """
    BoltHolesVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltHolesVisible(self: ViewVisibilitySettings) -> bool

Set: BoltHolesVisible(self: ViewVisibilitySettings) = value
"""

    BoltHolesVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltHolesVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: BoltHolesVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    BoltsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltsVisible(self: ViewVisibilitySettings) -> bool

Set: BoltsVisible(self: ViewVisibilitySettings) = value
"""

    BoltsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: BoltsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    ComponentsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentsVisible(self: ViewVisibilitySettings) -> bool

Set: ComponentsVisible(self: ViewVisibilitySettings) = value
"""

    ComponentsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: ComponentsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    ConstructionLinesVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructionLinesVisible(self: ViewVisibilitySettings) -> bool

Set: ConstructionLinesVisible(self: ViewVisibilitySettings) = value
"""

    ConstructionPlanesVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructionPlanesVisible(self: ViewVisibilitySettings) -> bool

Set: ConstructionPlanesVisible(self: ViewVisibilitySettings) = value
"""

    ConstructionPlanesVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructionPlanesVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: ConstructionPlanesVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    CutsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutsVisible(self: ViewVisibilitySettings) -> bool

Set: CutsVisible(self: ViewVisibilitySettings) = value
"""

    CutsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: CutsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    FittingsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingsVisible(self: ViewVisibilitySettings) -> bool

Set: FittingsVisible(self: ViewVisibilitySettings) = value
"""

    FittingsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: FittingsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    GridsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridsVisible(self: ViewVisibilitySettings) -> bool

Set: GridsVisible(self: ViewVisibilitySettings) = value
"""

    LoadsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsVisible(self: ViewVisibilitySettings) -> bool

Set: LoadsVisible(self: ViewVisibilitySettings) = value
"""

    PartsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartsVisible(self: ViewVisibilitySettings) -> bool

Set: PartsVisible(self: ViewVisibilitySettings) = value
"""

    PartsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: PartsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    PointsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsVisible(self: ViewVisibilitySettings) -> bool

Set: PointsVisible(self: ViewVisibilitySettings) = value
"""

    PointsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: PointsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    PourBreaksVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PourBreaksVisible(self: ViewVisibilitySettings) -> bool

Set: PourBreaksVisible(self: ViewVisibilitySettings) = value
"""

    PoursVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PoursVisible(self: ViewVisibilitySettings) -> bool

Set: PoursVisible(self: ViewVisibilitySettings) = value
"""

    RebarsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarsVisible(self: ViewVisibilitySettings) -> bool

Set: RebarsVisible(self: ViewVisibilitySettings) = value
"""

    RebarsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: RebarsVisibleInComponents(self: ViewVisibilitySettings) = value
"""

    ReferenceObjectsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceObjectsVisible(self: ViewVisibilitySettings) -> bool

Set: ReferenceObjectsVisible(self: ViewVisibilitySettings) = value
"""

    SurfaceTreatmentsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceTreatmentsVisible(self: ViewVisibilitySettings) -> bool

Set: SurfaceTreatmentsVisible(self: ViewVisibilitySettings) = value
"""

    WeldsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldsVisible(self: ViewVisibilitySettings) -> bool

Set: WeldsVisible(self: ViewVisibilitySettings) = value
"""

    WeldsVisibleInComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldsVisibleInComponents(self: ViewVisibilitySettings) -> bool

Set: WeldsVisibleInComponents(self: ViewVisibilitySettings) = value
"""




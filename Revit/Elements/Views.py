# encoding: utf-8
# module Revit.Elements.Views calls itself Views
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class View(Element):
    # no doc
    def AddFilter(self, parameterFilter):
        """ AddFilter(self: View, parameterFilter: ParameterFilterElement) """
        pass

    def ExportAsImage(self, path):
        """ ExportAsImage(self: View, path: str) -> Bitmap """
        pass

    def FilterOverrides(self, parameterFilter):
        """ FilterOverrides(self: View, parameterFilter: ParameterFilterElement) -> OverrideGraphicSettings """
        pass

    def SetFilterOverrides(self, parameterFilter, overrides):
        """ SetFilterOverrides(self: View, parameterFilter: ParameterFilterElement, overrides: OverrideGraphicSettings) """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: View) -> str """
        pass

    Filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filters(self: View) -> IEnumerable[ParameterFilterElement]

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class View3D(View):
    # no doc
    def BuildOrientation3D(self, *args): #cannot find CLR method
        """ BuildOrientation3D(eyePoint: XYZ, target: XYZ) -> ViewOrientation3D """
        pass

    def Create3DView(self, *args): #cannot find CLR method
        """ Create3DView(orient: ViewOrientation3D, name: str, isPerspective: bool) -> View3D """
        pass

    @staticmethod
    def CreateUniqueViewName(name):
        """ CreateUniqueViewName(name: str) -> str """
        pass

    def GetPointCloud(self, *args): #cannot find CLR method
        """ GetPointCloud(solid: Solid, pts: List[XYZ])GetPointCloud(geomInst: GeometryInstance, pts: List[XYZ])GetPointCloud(e: Element, pts: List[XYZ]) """
        pass

    def GetVisibleElementFilter(self, *args): #cannot find CLR method
        """ GetVisibleElementFilter() -> FilteredElementCollector """
        pass

    def InternalIsolateInView(self, *args): #cannot find CLR method
        """ InternalIsolateInView(self: View3D, bbox: BoundingBoxXYZ)InternalIsolateInView(self: View3D, element: Element) """
        pass

    def InternalRemoveIsolation(self, *args): #cannot find CLR method
        """ InternalRemoveIsolation(self: View3D) """
        pass

    def InternalSetName(self, *args): #cannot find CLR method
        """ InternalSetName(self: View3D, name: str) """
        pass

    def InternalSetOrientation(self, *args): #cannot find CLR method
        """ InternalSetOrientation(self: View3D, orient: ViewOrientation3D) """
        pass

    def InternalSetView3D(self, *args): #cannot find CLR method
        """ InternalSetView3D(self: View3D, view: View3D) """
        pass

    def IsolateInView(self, *args): #cannot find CLR method
        """ IsolateInView(view: View3D, element: Element) """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: View3D) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DEFAULT_VIEW_NAME = 'dynamo3D'
    InternalUniqueId = None


class AxonometricView(View3D):
    # no doc
    @staticmethod
    def ByEyePointAndTarget(eyePoint, target, name):
        """ ByEyePointAndTarget(eyePoint: Point, target: Point, name: str) -> AxonometricView """
        pass

    @staticmethod
    def ByEyePointTargetAndBoundingBox(eyePoint, target, boundingBox, name, isolateElement):
        """ ByEyePointTargetAndBoundingBox(eyePoint: Point, target: Point, boundingBox: BoundingBox, name: str, isolateElement: bool) -> AxonometricView """
        pass

    @staticmethod
    def ByEyePointTargetAndElement(eyePoint, target, name, element, isolateElement):
        """ ByEyePointTargetAndElement(eyePoint: Point, target: Point, name: str, element: Element, isolateElement: bool) -> AxonometricView """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class CeilingPlanView(PlanView):
    # no doc
    @staticmethod
    def ByLevel(level):
        """ ByLevel(level: Level) -> CeilingPlanView """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class DraftingView(View):
    # no doc
    @staticmethod
    def ByName(name):
        """ ByName(name: str) -> DraftingView """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: DraftingView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class FloorPlanView(PlanView):
    # no doc
    @staticmethod
    def ByLevel(level):
        """ ByLevel(level: Level) -> FloorPlanView """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class PerspectiveView(View3D):
    # no doc
    @staticmethod
    def ByEyePointAndTarget(eyePoint, target, element, name, isolateElement):
        """ ByEyePointAndTarget(eyePoint: Point, target: Point, element: object, name: str, isolateElement: bool) -> PerspectiveView """
        pass

    @staticmethod
    def ByEyePointTargetAndBoundingBox(eyePoint, target, boundingBox, name, isolateElement):
        """ ByEyePointTargetAndBoundingBox(eyePoint: Point, target: Point, boundingBox: BoundingBox, name: str, isolateElement: bool) -> PerspectiveView """
        pass

    @staticmethod
    def ByEyePointTargetAndElement(eyePoint, target, element, name, isolateElement):
        """ ByEyePointTargetAndElement(eyePoint: Point, target: Point, element: Element, name: str, isolateElement: bool) -> PerspectiveView """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class SectionView(View):
    # no doc
    @staticmethod
    def ByBoundingBox(box):
        """ ByBoundingBox(box: BoundingBox) -> SectionView """
        pass

    @staticmethod
    def ByCoordinateSystemMinPointMaxPoint(cs, minPoint, maxPoint):
        """ ByCoordinateSystemMinPointMaxPoint(cs: CoordinateSystem, minPoint: Point, maxPoint: Point) -> SectionView """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: SectionView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None


class Sheet(Element):
    # no doc
    @staticmethod
    def ByNameNumberTitleBlockAndView(sheetName, sheetNumber, titleBlockFamilyType, view):
        """ ByNameNumberTitleBlockAndView(sheetName: str, sheetNumber: str, titleBlockFamilyType: FamilyType, view: View) -> Sheet """
        pass

    @staticmethod
    def ByNameNumberTitleBlockAndViews(sheetName, sheetNumber, titleBlockFamilyType, views):
        """ ByNameNumberTitleBlockAndViews(sheetName: str, sheetNumber: str, titleBlockFamilyType: FamilyType, views: Array[View]) -> Sheet """
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Sheet) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SheetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetName(self: Sheet) -> str

"""

    SheetNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetNumber(self: Sheet) -> str

"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: Sheet) -> Array[View]

"""


    InternalUniqueId = None


class StructuralPlanView(PlanView):
    # no doc
    @staticmethod
    def ByLevel(level):
        """ ByLevel(level: Level) -> StructuralPlanView """
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    InternalUniqueId = None



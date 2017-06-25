# encoding: utf-8
# module Revit.Elements calls itself Elements
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Element(object, IDisposable, IGraphicItem, IFormattable):
    """ Superclass of all Revit element wrappers """
    def Dispose(self):
        """
        Dispose(self: Element)
            Default implementation of dispose that removes the element from the
                   
              document
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Element, obj: object) -> bool
        
            Implement Equals() method.
        """
        pass

    def Geometry(self):
        """
        Geometry(self: Element) -> Array[object]
        
            Get all of the Geometry associated with this object
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Element) -> int
        
            Get hash code.
        """
        pass

    def GetLocation(self):
        """
        GetLocation(self: Element) -> Geometry
        
            Get an exsiting element's location
            Returns: Location Geometry
        """
        pass

    def GetMaterials(self, paintMaterials):
        """
        GetMaterials(self: Element, paintMaterials: bool) -> IEnumerable[Material]
        
            Get Material Names from a Revit Element
        
            paintMaterials: Paint Materials
            Returns: List of Names
        """
        pass

    def GetParameterValueByName(self, parameterName):
        """
        GetParameterValueByName(self: Element, parameterName: str) -> object
        
            Get the value of one of the element's parameters.
        
            parameterName: The name of the parameter whose value you want to obtain.
        """
        pass

    def MoveByVector(self, vector):
        """
        MoveByVector(self: Element, vector: Vector)
            Move Revit Element by Vector
        
            vector: Translation Vector
        """
        pass

    def OverrideColorInView(self, color):
        """
        OverrideColorInView(self: Element, color: Color) -> Element
        
            Override the element's color in the active view.
        
            color: The color to apply to a solid fill on the element.
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetLocation(self, geometry):
        """
        SetLocation(self: Element, geometry: Geometry)
            Update an existing element's location
        
            geometry: New Location Point or Curve
        """
        pass

    def SetParameterByName(self, parameterName, value):
        """
        SetParameterByName(self: Element, parameterName: str, value: object) -> Element
        
            Set one of the element's parameters.
        
            parameterName: The name of the parameter to set.
            value: The value.
        """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: Element, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: Element, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: Element) -> str
        
            A basic implementation of ToString for Elements
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

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get an Axis-aligned BoundingBox of the Element

Get: BoundingBox(self: Element) -> BoundingBox

"""

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Curves in this Element

Get: Curves(self: Element) -> Array[Curve]

"""

    ElementCurveReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementCurveReference's in this Element.  Useful for downstream
            Element creation.

Get: ElementCurveReferences(self: Element) -> Array[ElementCurveReference]

"""

    ElementFaceReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementFaceReference's in this Element.  Useful for downstream
            Element creation.

Get: ElementFaceReferences(self: Element) -> Array[ElementFaceReference]

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Faces in this Element

Get: Faces(self: Element) -> Array[Surface]

"""

    GetCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Element Category

Get: GetCategory(self: Element) -> Category

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Element Id for this element

Get: Id(self: Element) -> int

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A reference to the element

Get: InternalElement(self: Element) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Name of the Element

Get: Name(self: Element) -> str

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Obtain all of the Parameters from an Element

Get: Parameters(self: Element) -> Array[Parameter]

"""

    Solids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Solids in this Element

Get: Solids(self: Element) -> Array[Solid]

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Element Unique Id for this element

Get: UniqueId(self: Element) -> str

"""


    InternalUniqueId = None
    IsFrozen = None


class AbstractFamilyInstance(Element, IDisposable, IGraphicItem, IFormattable):
    """ An abstract Revit FamilyInstance - implementors include FamilyInstance, AdaptiveComponent, StructuralFraming """
    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: AbstractFamilyInstance) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: AbstractFamilyInstance) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: AbstractFamilyInstance) -> Point

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AbstractFamilyInstance) -> FamilyType

"""


    InternalUniqueId = None


class AdaptiveComponent(AbstractFamilyInstance, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Adaptive Component """
    @staticmethod
    def ByParametersOnCurveReference(parameters, *__args):
        """
        ByParametersOnCurveReference(parameters: Array[Array[float]], revitCurve: ElementCurveReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnCurveReference(parameters: Array[float], curve: Curve, familyType: FamilyType) -> AdaptiveComponent
        
            Create an adaptive component referencing the parameters on a Curve reference
        
            parameters: The parameters on the curve
            curve: The curve to reference
            familyType: The family type to construct
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
        
            Create an adaptive component by uv points on a face.
        
            uvs: An array of UV pairs
            surface: The surface on which to place the AdaptiveComponent
        ByParametersOnFace(uvs: Array[Array[Array[float]]], faceReference: ElementFaceReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[Array[float]], faceReference: ElementFaceReference, familyType: FamilyType) -> AdaptiveComponent
        ByParametersOnFace(uvs: Array[Array[UV]], faceReference: ElementFaceReference, familyType: FamilyType) -> Array[AdaptiveComponent]
        ByParametersOnFace(uvs: Array[UV], faceReference: ElementFaceReference, familyType: FamilyType) -> AdaptiveComponent
        """
        pass

    @staticmethod
    def ByPoints(points, familyType):
        """
        ByPoints(points: Array[Array[Point]], familyType: FamilyType) -> Array[AdaptiveComponent]
        
            Create a list of adaptive components from two-dimensional array of points
        
            points: a two-dimensional array of points
            familyType: a family type to use to create the adaptive components
        """
        pass

    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

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
        """
        ById(id: int) -> Category
        
            Gets Revit Built-in category from current document based on category Id
        
            id: Category Id as Integer value
            Returns: Category if present in current document.
        """
        pass

    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> Category
        
            Gets a Revit category by the built-in category name.
        
            name: The built in category name.
        """
        pass

    def ToString(self):
        """ ToString(self: Category) -> str """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the category.

Get: Id(self: Category) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Category.

Get: Name(self: Category) -> str

"""



class Coordinates(object):
    """ Nodes exposing Revit Document Base and Survey Point """
    @staticmethod
    def BasePoint():
        """
        BasePoint() -> Point
        
            Get Project Base Point
            Returns: Project Base Point
        """
        pass

    @staticmethod
    def ProjectRotation():
        """
        ProjectRotation() -> float
        
            Get Project Rotation
            Returns: Rotation in degrees
        """
        pass

    @staticmethod
    def SurveyPoint():
        """
        SurveyPoint() -> Point
        
            Get Survey Point
            Returns: Survey Point
        """
        pass

    __all__ = [
        'BasePoint',
        'ProjectRotation',
        'SurveyPoint',
    ]


class CurtainPanel(AbstractFamilyInstance, IDisposable, IGraphicItem, IFormattable):
    """ A Revit CurtainPanel """
    def AsFamilyInstance(self):
        """
        AsFamilyInstance(self: CurtainPanel) -> FamilyInstance
        
            Gets family instance from curtain Panel
        """
        pass

    @staticmethod
    def ByElement(hostingElement):
        """
        ByElement(hostingElement: Element) -> Array[CurtainPanel]
        
            get all panels of curtain wall, system or slope glazing roof
        """
        pass

    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SupportingMullions(self):
        """
        SupportingMullions(self: CurtainPanel) -> Array[Mullion]
        
            Gets Mullions hosting the specified curtain panel
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: CurtainPanel) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, panelElement: Panel) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets curtain panel boundaries

Get: Boundaries(self: CurtainPanel) -> Array[PolyCurve]

"""

    HasPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the specific curtain panel is planar

Get: HasPlane(self: CurtainPanel) -> bool

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the specific curtain panel, if it's rectangular

Get: Height(self: CurtainPanel) -> float

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    IsRectangular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether the specific curtain panel is rectangular. Returns 
            true if the curtain panel is rectangular. Otherwise returns false

Get: IsRectangular(self: CurtainPanel) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the specific curtain panel boundaries

Get: Length(self: CurtainPanel) -> float

"""

    PanelBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PanelPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a plane of the given curtain panel, if it is planar

Get: PanelPlane(self: CurtainPanel) -> Plane

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the specific curtain panel, if it's rectangular

Get: Width(self: CurtainPanel) -> float

"""


    InternalUniqueId = None


class CurveElement(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    def InternalSetCurve(self, *args): #cannot find CLR method
        """
        InternalSetCurve(self: CurveElement, c: Curve)
            Set the geometry curve used by the ModelCurve
        """
        pass

    def InternalSetCurveElement(self, *args): #cannot find CLR method
        """
        InternalSetCurveElement(self: CurveElement, curveElement: CurveElement)
            Set the internal model curve along with its id's
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def setCurveMethod(self, *args): #cannot find CLR method
        """ setCurveMethod(ce: CurveElement, c: Curve) """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: CurveElement, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Obtain the geometry curve for this geometry curve

Get: Curve(self: CurveElement) -> Curve

"""

    ElementCurveReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Obtain the reference curve for this ModelCurve

Get: ElementCurveReference(self: CurveElement) -> ElementCurveReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: CurveElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    hasMethodSetCurve = True
    InternalUniqueId = None


class CurveByPoints(CurveElement, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Curve By Points """
    @staticmethod
    def ByReferencePoints(points, isReferenceLine):
        """
        ByReferencePoints(points: Array[ReferencePoint], isReferenceLine: bool) -> CurveByPoints
        
            Construct a Revit CurveByPoints Element (a CurveElement) from a collection of 
             ReferencePoint's
        """
        pass

    def InternalSetCurve(self, *args): #cannot find CLR method
        """
        InternalSetCurve(self: CurveElement, c: Curve)
            Set the geometry curve used by the ModelCurve
        """
        pass

    def InternalSetCurveElement(self, *args): #cannot find CLR method
        """
        InternalSetCurveElement(self: CurveElement, curveElement: CurveElement)
            Set the internal model curve along with its id's
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: CurveByPoints) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class DetailCurve(CurveElement, IDisposable, IGraphicItem, IFormattable):
    """ Revit Detail Curve """
    @staticmethod
    def ByCurve(view, curve):
        """
        ByCurve(view: View, curve: Curve) -> DetailCurve
        
            Construct a Revit DetailCurve element from a curve
        
            view: View to place the detail curve on
            curve: Curve to create detailcurve from
        """
        pass

    def InternalSetCurve(self, *args): #cannot find CLR method
        """
        InternalSetCurve(self: CurveElement, c: Curve)
            Set the geometry curve used by the ModelCurve
        """
        pass

    def InternalSetCurveElement(self, *args): #cannot find CLR method
        """
        InternalSetCurveElement(self: CurveElement, curveElement: CurveElement)
            Set the internal model curve along with its id's
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetCurve(self, curve):
        """
        SetCurve(self: DetailCurve, curve: Curve)
            Set Geometry Curve
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: DetailCurve) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Geometry Curve

Get: Curve(self: DetailCurve) -> Curve

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Dimension(Element, IDisposable, IGraphicItem, IFormattable):
    """ Dimension element """
    @staticmethod
    def ByElements(view, referenceElements, line, suffix, prefix):
        """ ByElements(view: View, referenceElements: IEnumerable[Element], line: Line, suffix: str, prefix: str) -> Dimension """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
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

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Dimension) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Prefix

Get: Prefix(self: Dimension) -> IEnumerable[str]

"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Suffix

Get: Suffix(self: Dimension) -> IEnumerable[str]

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Dimension Value

Get: Value(self: Dimension) -> IEnumerable[float]

"""

    ValueOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Value override

Get: ValueOverride(self: Dimension) -> IEnumerable[str]

"""


    InternalUniqueId = None


class DirectShape(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit DirectShape, which is a wrapper for some other geometrical entities """
    @staticmethod
    def ByGeometry(geometry, category, material, name):
        """
        ByGeometry(geometry: Geometry, category: Category, material: Material, name: str) -> DirectShape
        
            Create a Revit DirectShape given some geometry, a name for the shape, a 
             Category, and Material.
                    The geometry will be tessellated before 
             being placed in the Revit model
                    The category of a DirectShape 
             cannot be changed after creation, so
                    a new DirectShape will be 
             generated if the category input is changed.
        
        
            geometry: A Solid or Surface that will be tessellated and placed in the Revit model as a 
             DirectShape
        
            category: Must be a top level Built-in Category
            material: A Material to apply to the faces of the DirectShape
            name: A string name for the DirectShape
            Returns: A DirectShape Element
        """
        pass

    @staticmethod
    def ByMesh(mesh, category, material, name):
        """
        ByMesh(mesh: Mesh, category: Category, material: Material, name: str) -> DirectShape
        
            Create a Revit DirectShape given some geometry, a name for the shape, a 
             Category, and Material.
                    The geometry will be tessellated before 
             being placed in the Revit model
                    The category of a DirectShape 
             cannot be changed after creation, so
                    a new DirectShape will be 
             generated if the category input is changed.
        
        
            mesh: A Mesh that will be tessellated and placed in the Revit model as a DirectShape
            category: Must be a top level Built-in Category
            material: A Material to apply to the faces of the DirectShape
            name: A string name for the DirectShape
            Returns: A DirectShape Element
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: DirectShape) -> str
        
            Please see InternalSetName method
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, shape: DirectShape)
        __new__(cls: type, shapeReference: DesignScriptEntity, shapename: str, category: Category, material: Material)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: DirectShape) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class DirectShapeState(SerializableId, ISerializable):
    """
    This class acts as a representation of a directShape state, we can store it in trace
                and on protogeometry types (in their tags dictionary) to keep track of the state of
                a DirectShape wrapper type, it inherits from SerializeableId so that ElementLifeCycle
                and DocumentEvents continue to function for DirectShapes.
    
    DirectShapeState(ds: DirectShape, syncId: str, materialId: ElementId)
    DirectShapeState(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: DirectShapeState, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, ds: DirectShape, syncId: str, materialId: ElementId)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    materialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: materialId(self: DirectShapeState) -> int

Set: materialId(self: DirectShapeState) = value
"""

    syncId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: syncId(self: DirectShapeState) -> str

Set: syncId(self: DirectShapeState) = value
"""



class DividedPath(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit DividedPath """
    @staticmethod
    def ByCurveAndDivisions(*__args):
        """
        ByCurveAndDivisions(curve: Curve, divisions: int) -> DividedPath
        
            Creates a Revit divided path on the given curve with specified amount of 
             division
        
        ByCurveAndDivisions(element: Element, divisions: int) -> DividedPath
        ByCurveAndDivisions(element: ElementCurveReference, divisions: int) -> DividedPath
        """
        pass

    @staticmethod
    def ByCurvesAndDivisions(*__args):
        """
        ByCurvesAndDivisions(curve: Array[Curve], divisions: int) -> DividedPath
        
            Creates a Revit divided path on the given collection of curves with specified 
             amount of division
        
        ByCurvesAndDivisions(elements: Array[Element], divisions: int) -> DividedPath
        ByCurvesAndDivisions(curveReferences: Array[ElementCurveReference], divisions: int) -> DividedPath
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: DividedPath) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All points along the DividedPath.

Get: Points(self: DividedPath) -> IEnumerable[Point]

"""


    InternalUniqueId = None


class DividedSurface(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit DividedSurface """
    @staticmethod
    def ByFaceAndUVDivisions(elementFace, uDivs, vDivs):
        """
        ByFaceAndUVDivisions(elementFace: Surface, uDivs: int, vDivs: int) -> DividedSurface
        
            Create a Revit DividedSurface on a face given the face and number of divisions 
             in u and v directon
        
        ByFaceAndUVDivisions(elementFace: ElementFaceReference, uDivs: int, vDivs: int) -> DividedSurface
        """
        pass

    @staticmethod
    def ByFaceUVDivisionsAndRotation(*__args):
        """
        ByFaceUVDivisionsAndRotation(surface: Surface, uDivs: int, vDivs: int, gridRotation: float) -> DividedSurface
        
            Create a Revit DividedSurface on a face given the face and number of divisions 
             in u and v directon
                    and the rotation of the grid lines with 
             respect to the natural UV parameterization of the face
        
        ByFaceUVDivisionsAndRotation(faceReference: ElementFaceReference, uDivs: int, vDivs: int, gridRotation: float) -> DividedSurface
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: DividedSurface) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rotation of the grid lines with respect to the UV parameterization
            of the face

Get: Rotation(self: DividedSurface) -> float

"""

    UDivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of divisions in U direction

Get: UDivisions(self: DividedSurface) -> int

"""

    VDivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of divisions in V direction

Get: VDivisions(self: DividedSurface) -> int

"""


    InternalUniqueId = None


class ElementSelector(object):
    """ ElementSelector() """
    @staticmethod
    def ByElementId(elementId, isRevitOwned=None):
        """
        ByElementId(elementId: int) -> Element
        ByElementId(elementId: int, isRevitOwned: bool) -> Element
        
            A factory method for looking up and obtaining elements
                    from the 
             revit project.
        
        
            elementId: The id of the element to select
            isRevitOwned: Whether the returned object should be revit owned or not
        """
        pass

    @staticmethod
    def ByUniqueId(uniqueId, isRevitOwned):
        """
        ByUniqueId(uniqueId: str, isRevitOwned: bool) -> Element
        
            A factory method for looking up and obtaining elements
                    from the 
             revit project
        
        
            uniqueId: The unique id of the element to select
            isRevitOwned: Whether the returned object should be revit owned or not
        """
        pass


class ElementWrapper(object):
    """
    Element wrapper supplies tools for wrapping Autodesk.Revit.DB.Element types
                in their associated Revit.Elements.Element wrapper
    """
    @staticmethod
    def ToDSType(ele, isRevitOwned):
        """
        ToDSType(ele: Element, isRevitOwned: bool) -> Element
        
            If possible, wrap the element in a DS type
        
            isRevitOwned: Whether the returned object should be revit owned or not
        """
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


class Family(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Family """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> Family
        
            Obtain a Family from the current document given it's name
        
            name: The name of the family in the current document
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Family) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Family) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this family

Get: Name(self: Family) -> str

"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Obtain the FamilyTypes from this Family

Get: Types(self: Family) -> Array[FamilyType]

"""


    InternalUniqueId = None


class FamilyInstance(AbstractFamilyInstance, IDisposable, IGraphicItem, IFormattable):
    """ A Revit FamilyInstance """
    @staticmethod
    def ByCoordinates(familyType, x, y, z):
        """
        ByCoordinates(familyType: FamilyType, x: float, y: float, z: float) -> FamilyInstance
        
            Place a Revit FamilyInstance given the FamilyType (also known as the 
             FamilySymbol in the Revit API) and its coordinates in world space
        
        
            x: X coordinate in meters
            y: Y coordinate in meters
            z: Z coordinate in meters
        """
        pass

    @staticmethod
    def ByFace(familyType, face, *__args):
        """
        ByFace(familyType: FamilyType, face: Surface, location: Point, referenceDirection: Vector) -> FamilyInstance
        
            Place a Revit family instance given the FamilyType (also known as the 
             FamilySymbol in the Revit API) 
                    on a surface derived from a 
             backing Revit face as reference, a reference direction and a point location 
             where to place the family.
                    
                    Note: The FamilyType 
             should be workplane based and the input surface must be created from a Revit 
             Face. The reference direction defines the rotation of the instance on the 
             reference, and thus cannot be perpendicular to the face.
        
        
            face: Surface geometry derived from a Revit face as reference element
            location: Point on the face where the instance is to be placed
            referenceDirection: A vector that defines the direction of placement of the family instance
            Returns: FamilyInstance
        ByFace(familyType: FamilyType, face: Surface, line: Line) -> FamilyInstance
        
            Place a Revit family instance of the given the FamilyType (also known as the 
             FamilySymbol in the Revit API) 
                    on a surface derived from a 
             backing Revit face as reference and a line as reference for its position.
             
                    
                    Note: The FamilyPlacementType must be CurveBased and the 
             input surface must be created from a Revit Face
        
        
            face: Surface geometry derived from a Revit face as reference element
            line: A line on the face defining where the symbol is to be placed
            Returns: FamilyInstance
        """
        pass

    @staticmethod
    def ByFamilyType(familyType):
        """
        ByFamilyType(familyType: FamilyType) -> Array[FamilyInstance]
        
            Obtain a collection of FamilyInstances from the Revit Document and use them in 
             the Dynamo graph
        """
        pass

    @staticmethod
    def ByPoint(familyType, point):
        """
        ByPoint(familyType: FamilyType, point: Point) -> FamilyInstance
        
            Place a Revit FamilyInstance given the FamilyType (also known as the 
             FamilySymbol in the Revit API) and its coordinates in world space
        """
        pass

    @staticmethod
    def ByPointAndLevel(familyType, point, level):
        """
        ByPointAndLevel(familyType: FamilyType, point: Point, level: Level) -> FamilyInstance
        
            Place a Revit FamilyInstance given the FamilyType (also known as the 
             FamilySymbol in the Revit API), it's coordinates in world space, and the Level
        
        
            point: Point in meters
        """
        pass

    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetRotation(self, degree):
        """
        SetRotation(self: FamilyInstance, degree: float) -> FamilyInstance
        
            Set the Euler angle of the family instance around its local Z-axis.
        
            degree: The Euler angle around Z-axis.
            Returns: The result family instance.
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FamilyInstance) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, instance: FamilyInstance) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FacingOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the FacingOrientation of the family instance

Get: FacingOrientation(self: FamilyInstance) -> Vector

"""

    GetFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the family of this family instance

Get: GetFamily(self: FamilyInstance) -> Family

"""

    GetHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the host of this fmaily instance (if any). Eg. returns the wall of a window or door family instance.

Get: GetHost(self: FamilyInstance) -> Element

"""

    GetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the family type of this family instance

Get: GetType(self: FamilyInstance) -> FamilyType

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location of the specific family instance

Get: Location(self: FamilyInstance) -> Point

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets family type of the specific family instance

Get: Type(self: FamilyInstance) -> FamilyType

"""


    InternalUniqueId = None


class FamilyType(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit FamilyType, the Revit API refers to this as a FamilySymbol """
    @staticmethod
    def ByFamilyAndName(family, name):
        """
        ByFamilyAndName(family: Family, name: str) -> FamilyType
        
            Select a FamilyType given its parent Family and the FamilyType's name.
        
            family: The FamilyTypes's parent Family
            name: The name of the FamilyType
        """
        pass

    @staticmethod
    def ByFamilyNameAndTypeName(familyName, typeName):
        """
        ByFamilyNameAndTypeName(familyName: str, typeName: str) -> FamilyType
        
            Select a FamilyType give it's family name and type name.
        
            familyName: The FamilyType's parent Family name.
            typeName: The name of the FamilyType.
        """
        pass

    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> FamilyType
        
            Select a FamilyType given it's name.  This method will return the first 
             FamilyType it finds if there are
                    two or more FamilyTypes with the 
             same name.
        
        
            name: The name of the FamilyType
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FamilyType) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the parent family of this FamilyType

Get: Family(self: FamilyType) -> Family

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: FamilyType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the name of this Family Type

Get: Name(self: FamilyType) -> str

"""


    InternalUniqueId = None


class FilledRegion(Element, IDisposable, IGraphicItem, IFormattable):
    """ Revit filled Region """
    @staticmethod
    def ByCurves(view, boundary, regionType):
        """ ByCurves(view: View, boundary: IEnumerable[Curve], regionType: FilledRegionType) -> FilledRegion """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: FilledRegion) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class FilledRegionType(Element, IDisposable, IGraphicItem, IFormattable):
    """ Revit filled Region Type """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> FilledRegionType
        
            Select a FilledRegionType from the current document by name
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Color

Get: Color(self: FilledRegionType) -> Color

"""

    FillPatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get FillPatternId

Get: FillPatternId(self: FilledRegionType) -> ElementId

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: FilledRegionType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Name

Get: Name(self: FilledRegionType) -> str

"""


    InternalUniqueId = None


class Floor(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Floor """
    @staticmethod
    def ByOutlineTypeAndLevel(*__args):
        """
        ByOutlineTypeAndLevel(outline: PolyCurve, floorType: FloorType, level: Level) -> Floor
        
            Create a Revit Floor given it's curve outline and Level
            Returns: The floor
        ByOutlineTypeAndLevel(outlineCurves: Array[Curve], floorType: FloorType, level: Level) -> Floor
        
            Create a Revit Floor given it's curve outline and Level
            Returns: The floor
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Floor) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class FloorType(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit FloorType """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> FloorType
        
            Select a FloorType from the document given
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: FloorType) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: FloorType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the FloorType

Get: Name(self: FloorType) -> str

"""


    InternalUniqueId = None


class Form(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    @staticmethod
    def ByLoftCrossSections(curves, isSolid):
        """
        ByLoftCrossSections(curves: Array[Array[Element]], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Curve], isSolid: bool) -> Form
        
            Creates a Form by lofting a list of curves
        ByLoftCrossSections(curves: Array[Array[Curve]], isSolid: bool) -> Form
        
            Creates a Form by lofting a nested list of curves
        ByLoftCrossSections(curves: Array[ElementCurveReference], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Array[ElementCurveReference]], isSolid: bool) -> Form
        ByLoftCrossSections(curves: Array[Element], isSolid: bool) -> Form
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Form) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class FreeForm(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit FreeForm element """
    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: FreeForm) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Grid(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Grid Element """
    @staticmethod
    def ByArc(arc):
        """
        ByArc(arc: Arc) -> Grid
        
            Create a Revit Grid Element in a project along an Arc
        """
        pass

    @staticmethod
    def ByLine(line):
        """
        ByLine(line: Line) -> Grid
        
            Create a Revit Grid Element in a Project along a Line.
        """
        pass

    @staticmethod
    def ByStartPointEndPoint(start, end):
        """
        ByStartPointEndPoint(start: Point, end: Point) -> Grid
        
            Create a Revit Grid Element in a project between two end points
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the underlying Curve geometry from this Element

Get: Curve(self: Grid) -> Curve

"""

    ElementCurveReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get a Reference to the underlying Curve Geometry of this Element

Get: ElementCurveReference(self: Grid) -> ElementCurveReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Grid) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class ImportInstance(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ImportInstance Element """
    @staticmethod
    def ByGeometries(geometries):
        """
        ByGeometries(geometries: Array[Geometry]) -> ImportInstance
        
            Import a collection of Geometry (Solid, Curve, Surface, etc) into Revit as an 
             ImportInstance.  This variant is much faster than
                    
             ImportInstance.ByGeometry as it uses a batch method.
        
        
            geometries: A collection of Geometry
        """
        pass

    @staticmethod
    def ByGeometry(geometry):
        """
        ByGeometry(geometry: Geometry) -> ImportInstance
        
            Import a collection of Geometry (Solid, Curve, Surface, etc) into Revit as an 
             ImportInstance.
        
        
            geometry: A single piece of geometry
        """
        pass

    @staticmethod
    def BySATFile(pathToFile):
        """
        BySATFile(pathToFile: str) -> ImportInstance
        
            Import Geometry from a SAT file.  The SAT file is assumed to be in Feet.
        
            pathToFile: The path to the SAT file
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: ImportInstance) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets file path of the sat file that represents the geometry of the specified ImportInstance Element

Get: Path(self: ImportInstance) -> str

"""


    InternalUniqueId = None


class Level(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Level """
    @staticmethod
    def ByElevation(elevation):
        """
        ByElevation(elevation: float) -> Level
        
            Create a Revit Level given it's elevation.  The name will be whatever
                 
                Revit gives it.
        """
        pass

    @staticmethod
    def ByElevationAndName(elevation, name):
        """
        ByElevationAndName(elevation: float, name: str) -> Level
        
            Create a Revit Level given it's elevation and name in the project
        """
        pass

    @staticmethod
    def ByLevelAndOffset(level, offset):
        """
        ByLevelAndOffset(level: Level, offset: float) -> Level
        
            Create a Revit Level given it's length offset from an existing level
        """
        pass

    @staticmethod
    def ByLevelOffsetAndName(level, offset, name):
        """
        ByLevelOffsetAndName(level: Level, offset: float, name: str) -> Level
        
            Create a Revit Level given a distance offset from an existing 
                    
             level and a name for the new level
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Level) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The elevation of the level above ground level

Get: Elevation(self: Level) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Level) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the level

Get: Name(self: Level) -> str

"""

    ProjectElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elevation relative to the Project origin

Get: ProjectElevation(self: Level) -> float

"""


    InternalUniqueId = None


class LevelTraceData(SerializableId, ISerializable):
    """
    LevelTraceData(lev: Level, inputName: str)
    LevelTraceData(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: LevelTraceData, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, lev: Level, inputName: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    InputName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputName(self: LevelTraceData) -> str

Set: InputName(self: LevelTraceData) = value
"""



class Material(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> Material
        
            Select a material from the current document by the name
        
            name: The name of the material
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AppearanceParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all apperance parameters

Get: AppearanceParameters(self: Material) -> IEnumerable[Parameter]

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get color

Get: Color(self: Material) -> Color

"""

    CutPatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get cut pattern color

Get: CutPatternColor(self: Material) -> Color

"""

    CutPatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get cut pattern id

Get: CutPatternId(self: Material) -> int

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Material) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    MaterialCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Material category

Get: MaterialCategory(self: Material) -> str

"""

    MaterialClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Material Class

Get: MaterialClass(self: Material) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Material Name

Get: Name(self: Material) -> str

"""

    Shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Shininess

Get: Shininess(self: Material) -> int

"""

    Smoothness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Smoothness

Get: Smoothness(self: Material) -> int

"""

    StructuralParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all structural parameters

Get: StructuralParameters(self: Material) -> IEnumerable[Parameter]

"""

    SurfacePatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get SurfacePatternColor

Get: SurfacePatternColor(self: Material) -> Color

"""

    ThermalParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all thermal parameters

Get: ThermalParameters(self: Material) -> IEnumerable[Parameter]

"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Transparency

Get: Transparency(self: Material) -> int

"""


    InternalUniqueId = None


class ModelCurve(CurveElement, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ModelCurve """
    @staticmethod
    def ByCurve(curve):
        """
        ByCurve(curve: Curve) -> ModelCurve
        
            Construct a Revit ModelCurve element from a Curve
        """
        pass

    def InternalSetCurve(self, *args): #cannot find CLR method
        """
        InternalSetCurve(self: CurveElement, c: Curve)
            Set the geometry curve used by the ModelCurve
        """
        pass

    def InternalSetCurveElement(self, *args): #cannot find CLR method
        """
        InternalSetCurveElement(self: CurveElement, curveElement: CurveElement)
            Set the internal model curve along with its id's
        """
        pass

    @staticmethod
    def ReferenceCurveByCurve(curve):
        """
        ReferenceCurveByCurve(curve: Curve) -> ModelCurve
        
            Construct a Revit ModelCurve element from a Curve
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: ModelCurve) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class ModelText(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ModelText Element Point """
    @staticmethod
    def ByTextSketchPlaneAndPosition(text, sketchPlane, xCoordinateInPlane, yCoordinateInPlane, textDepth, modelTextType):
        """
        ByTextSketchPlaneAndPosition(text: str, sketchPlane: SketchPlane, xCoordinateInPlane: float, yCoordinateInPlane: float, textDepth: float, modelTextType: ModelTextType) -> ModelText
        
            Create a ModelText Element in the Family Document by providing the text, 
             SketchPlane Element host, coordinates (within the plane of the SketchPlane),
          
                       the depth of the text, and the text type name
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Depth of the ModelText Element

Get: Depth(self: ModelText) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: ModelText) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Position of the ModelText Element

Get: Position(self: ModelText) -> Point

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Text of the ModelText Element

Get: Text(self: ModelText) -> str

"""


    InternalUniqueId = None


class ModelTextType(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ModelTextType """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> ModelTextType
        
            Select a ModelTextType from the current document by name
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: ModelTextType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Mullion(AbstractFamilyInstance, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Mullion """
    def AsFamilyInstance(self):
        """
        AsFamilyInstance(self: Mullion) -> FamilyInstance
        
            Returns FamilyInstance object as represented by the specified mullion
        """
        pass

    @staticmethod
    def ByElement(hostingElement):
        """
        ByElement(hostingElement: Element) -> Array[Mullion]
        
            get all mullions of curtain wall, system or slope glazing roof
        """
        pass

    def InitMullion(self, *args): #cannot find CLR method
        """
        InitMullion(self: Mullion, mullionElement: Mullion)
            Initialize a Mullion element
        """
        pass

    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SupportedPanels(self):
        """
        SupportedPanels(self: Mullion) -> Array[CurtainPanel]
        
            Returns curtain panels supported by the specified Mullion Element
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Mullion) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, mullionElement: Mullion) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    LocationCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets curve geometry from the specified Mullion Element

Get: LocationCurve(self: Mullion) -> Curve

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
        """
        CreateProjectParameterForAllCategories(parameterName: str, groupName: str, type: str, group: str, instance: bool)
            Create a new Project Parameter in this current Revit document for all 
             applicable categories
        
        
            parameterName: Name
            groupName: Group of the parameter for shared parameters
            type: Parameter Type
            group: Parameter Group
            instance: Is instance parameter, otherwise its a type parameter
        """
        pass

    @staticmethod
    def CreateSharedParameter(parameterName, groupName, type, group, instance, categoryList):
        """ CreateSharedParameter(parameterName: str, groupName: str, type: str, group: str, instance: bool, categoryList: IEnumerable[Category]) """
        pass

    @staticmethod
    def CreateSharedParameterForAllCategories(parameterName, groupName, type, group, instance):
        """
        CreateSharedParameterForAllCategories(parameterName: str, groupName: str, type: str, group: str, instance: bool)
            Create a new Shared Parameter in the current Revit document for all applicable 
             categories
        
        
            parameterName: Name
            groupName: Group of the parameter for shared parameters
            type: Parameter Type
            group: Parameter Group
            instance: Is instance parameter, otherwise its a type parameter
        """
        pass

    @staticmethod
    def ParameterByName(element, name):
        """
        ParameterByName(element: Element, name: str) -> Parameter
        
            Get Element's Parameter by Name
        
            element: Element
            name: Parameter Name
            Returns: Parameter
        """
        pass

    @staticmethod
    def SetValue(parameter, value):
        """
        SetValue(parameter: Parameter, value: object)
            Set the value of the parameter
        """
        pass

    @staticmethod
    def SharedParameterFile():
        """
        SharedParameterFile() -> str
        
            Gets the path to the shared parameter file of this document
        """
        pass

    def ToString(self):
        """ ToString(self: Parameter) -> str """
        pass

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the parameter's group

Get: Group(self: Parameter) -> str

"""

    HasValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the Parameter has a value

Get: HasValue(self: Parameter) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the parameter's element Id

Get: Id(self: Parameter) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the Parameter is read only

Get: IsReadOnly(self: Parameter) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the Parameter is shared

Get: IsShared(self: Parameter) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the parameter.

Get: Name(self: Parameter) -> str

"""

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the parameter type

Get: ParameterType(self: Parameter) -> str

"""

    StorageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Parameter Storage Type

Get: StorageType(self: Parameter) -> str

"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the parameter's unit type

Get: UnitType(self: Parameter) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the parameter

Get: Value(self: Parameter) -> object

"""



class ParseEnum(object):
    """
    Parse Revit Enum
    
    ParseEnum()
    """
    @staticmethod
    def ByString(value, typeName):
        """
        ByString(value: str, typeName: str) -> object
        
            Parse any Revit Enum by String
        
            value: enum string value
            typeName: full type name
        """
        pass


class PlanView(View, IDisposable, IGraphicItem, IFormattable):
    """
    Base class for Revit Plan views
    
    PlanView()
    """
    def CreatePlanView(self, *args): #cannot find CLR method
        """ CreatePlanView(level: Level, planType: ViewFamily) -> ViewPlan """
        pass

    def InternalSetPlanView(self, *args): #cannot find CLR method
        """
        InternalSetPlanView(self: PlanView, plan: ViewPlan)
            Set the InternalViewPlan property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: PlanView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class ReferencePlane(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ReferencePlane """
    @staticmethod
    def ByLine(line):
        """
        ByLine(line: Line) -> ReferencePlane
        
            Form a ReferencePlane from a line in the Active view.  The cut vector is the Z 
             Axis.
        
        
            line: The line where the bubble wil be located at the start
        """
        pass

    @staticmethod
    def ByStartPointEndPoint(start, end):
        """
        ByStartPointEndPoint(start: Point, end: Point) -> ReferencePlane
        
            Form a Refernece plane from two end points in the Active view.  The cut vector 
             is the Z Axis.
        
        
            start: The location where the bubble will be located
            end: The other end
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ElementPlaneReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get a reference to this plane for downstream Elements requiring it

Get: ElementPlaneReference(self: ReferencePlane) -> ElementPlaneReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: ReferencePlane) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the internal Geometric Plane

Get: Plane(self: ReferencePlane) -> Plane

"""


    InternalUniqueId = None


class ReferencePoint(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit Reference Point """
    @staticmethod
    def ByCoordinates(x, y, z):
        """
        ByCoordinates(x: float, y: float, z: float) -> ReferencePoint
        
            Create a Reference Point by x, y, and z coordinates.
        """
        pass

    @staticmethod
    def ByLengthOnCurveReference(elementCurveReference, length):
        """
        ByLengthOnCurveReference(elementCurveReference: object, length: float) -> ReferencePoint
        
            Create a Reference Point at a particular length along a curve
        
            length: Distance in meters along the curve
        """
        pass

    @staticmethod
    def ByParameterOnCurveReference(elementCurveReference, parameter):
        """
        ByParameterOnCurveReference(elementCurveReference: object, parameter: float) -> ReferencePoint
        
            Create a Reference Point at a parameter on an Curve.  This introduces a 
             persistent relationship between
                    Elements in the Revit document.
        """
        pass

    @staticmethod
    def ByParametersOnFaceReference(elementFaceReference, u, v):
        """
        ByParametersOnFaceReference(elementFaceReference: object, u: float, v: float) -> ReferencePoint
        
            Create a Reference Point by UV coordinates on a Face. This introduces a 
             persistent relationship between
                    Elements in the Revit document.
        """
        pass

    @staticmethod
    def ByPoint(pt):
        """
        ByPoint(pt: Point) -> ReferencePoint
        
            Create a Reference Point from a point.
        """
        pass

    @staticmethod
    def ByPointVectorDistance(basePoint, direction, distance):
        """
        ByPointVectorDistance(basePoint: Point, direction: Vector, distance: float) -> ReferencePoint
        
            Create a Reference Point Element offset from a point along a vector
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: ReferencePoint, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: ReferencePoint) -> str
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: ReferencePoint) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets point geometry from the specified ReferencePoint

Get: Point(self: ReferencePoint) -> Point

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets 'X' coordinate of the specified ReferencePoint

Get: X(self: ReferencePoint) -> float

Set: X(self: ReferencePoint) = value
"""

    XYPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets XY plane of the specified ReferencePoint

Get: XYPlane(self: ReferencePoint) -> Plane

"""

    XZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets XZ plane of the specified ReferencePoint

Get: XZPlane(self: ReferencePoint) -> Plane

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets 'Y' coordinate of the specified ReferencePoint

Get: Y(self: ReferencePoint) -> float

Set: Y(self: ReferencePoint) = value
"""

    YZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets YZ plane of the specified ReferencePoint

Get: YZPlane(self: ReferencePoint) -> Plane

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets 'Z' coordinate of the specified ReferencePoint

Get: Z(self: ReferencePoint) -> float

Set: Z(self: ReferencePoint) = value
"""


    InternalUniqueId = None


class Revision(Element, IDisposable, IGraphicItem, IFormattable):
    """ Revit Revision """
    @staticmethod
    def ByName(name, revDate, description, issued, issuedBy, issuedTo, visibility, numberType):
        """
        ByName(name: str, revDate: str, description: str, issued: bool, issuedBy: str, issuedTo: str, visibility: str, numberType: str) -> Revision
        
            Construct a new Revit Revision by Name
        
            name: Revision Name
            revDate: Revision Date
            description: Description
            issued: Issuing status
            issuedBy: Issued by
            issuedTo: Issued to
            visibility: Visibility settings
            numberType: Number type
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetIssued(self, value):
        """
        SetIssued(self: Revision, value: bool)
            Set Issued
        
            value: Issued
        """
        pass

    def SetIssuedBy(self, value):
        """
        SetIssuedBy(self: Revision, value: str)
            Set IssuedBy
        
            value: IssuedBy
        """
        pass

    def SetIssuedTo(self, value):
        """
        SetIssuedTo(self: Revision, value: str)
            Set IssuedTo
        
            value: IssuedTo
        """
        pass

    def SetRevisionDate(self, value):
        """
        SetRevisionDate(self: Revision, value: str)
            Set Revision Date
        
            value: Revision Date
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Revision) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Issued = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Issued

Get: Issued(self: Revision) -> bool

"""

    IssuedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get IssuedBy

Get: IssuedBy(self: Revision) -> str

"""

    IssuedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get IssuedTo

Get: IssuedTo(self: Revision) -> str

"""

    RevisionDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Revision Date

Get: RevisionDate(self: Revision) -> str

"""


    InternalUniqueId = None


class RevisionCloud(Element, IDisposable, IGraphicItem, IFormattable):
    """ Revit Revision Cloud """
    @staticmethod
    def ByCurve(view, curves, revision):
        """ ByCurve(view: View, curves: IEnumerable[Curve], revision: Element) -> RevisionCloud """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Revision cloud's curves

Get: Curves(self: RevisionCloud) -> IEnumerable[Curve]

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: RevisionCloud) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Revision cloud's revision

Get: Revision(self: RevisionCloud) -> Revision

"""


    InternalUniqueId = None


class Room(Element, IDisposable, IGraphicItem, IFormattable):
    """ Room Element """
    @staticmethod
    def ByLocation(level, location, name, number):
        """
        ByLocation(level: Level, location: Point, name: str, number: str) -> Room
        
            Create a Revit Room Element
        
            level: Level the room is hosted on
            location: Location for the center of the room
            name: Room name
            number: Room number
        """
        pass

    def IsInsideRoom(self, point):
        """
        IsInsideRoom(self: Room, point: Point) -> bool
        
            Check if a point is inside of a room
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetName(self, value):
        """
        SetName(self: Room, value: str)
            Set name
        
            value: Name
        """
        pass

    def SetNumber(self, value):
        """
        SetNumber(self: Room, value: str)
            Set number
        
            value: Number
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get room area

Get: Area(self: Room) -> float

"""

    CenterBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Centerline boundary

Get: CenterBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    CoreBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Core boundary

Get: CoreBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    CoreCenterBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Core center boundary

Get: CoreCenterBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    FinishBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Finish boundary

Get: FinishBoundary(self: Room) -> IEnumerable[IEnumerable[Curve]]

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get room height

Get: Height(self: Room) -> float

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Room) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Room Location

Get: Location(self: Room) -> Point

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get room name

Get: Name(self: Room) -> str

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get room number

Get: Number(self: Room) -> str

"""


    InternalUniqueId = None


class SketchPlane(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit SketchPlane """
    @staticmethod
    def ByPlane(plane):
        """
        ByPlane(plane: Plane) -> SketchPlane
        
            Make a Revit SketchPlane given a plane
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ElementPlaneReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get an element plane reference from a specified sketch plane

Get: ElementPlaneReference(self: SketchPlane) -> ElementPlaneReference

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: SketchPlane) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plane geometry of the specified sketch plane

Get: Plane(self: SketchPlane) -> Plane

"""


    InternalUniqueId = None


class StructuralFraming(AbstractFamilyInstance, IDisposable, IGraphicItem, IFormattable):
    """ A Revit FamilyInstance """
    @staticmethod
    def BeamByCurve(curve, level, structuralFramingType):
        """
        BeamByCurve(curve: Curve, level: Level, structuralFramingType: FamilyType) -> StructuralFraming
        
            Create a beam.
        
            curve: The curve which defines the center line of the beam.
            level: The level with which you'd like the beam to be associated.
            structuralFramingType: The structural framing type representing the beam.
        """
        pass

    @staticmethod
    def BraceByCurve(curve, level, structuralFramingType):
        """
        BraceByCurve(curve: Curve, level: Level, structuralFramingType: FamilyType) -> StructuralFraming
        
            Create a brace.
        
            curve: The cruve which defines the center line of the brace.
            level: The level with which you'd like the brace to be associated.
            structuralFramingType: The structural framing type representing the brace.
        """
        pass

    @staticmethod
    def ByCurveLevelUpVectorAndType(curve, level, upVector, structuralType, structuralFramingType):
        """
        ByCurveLevelUpVectorAndType(curve: Curve, level: Level, upVector: Vector, structuralType: StructuralType, structuralFramingType: FamilyType) -> StructuralFraming
        
            Create a Revit Structural Member - a special FamilyInstance
        
            curve: The curve path for the structural member
            level: The level on which the member should appear
            upVector: The up vector for the element - this is required to determine the orientation 
             of the element
        
            structuralType: The type of the structural element - a beam, column, etc
            structuralFramingType: The structural framing type representing the structural type
        """
        pass

    @staticmethod
    def ColumnByCurve(curve, level, structuralColumnType):
        """
        ColumnByCurve(curve: Curve, level: Level, structuralColumnType: FamilyType) -> StructuralFraming
        
            Create a column.
        
            curve: The curve which defines the center line of the column.
            level: The level with which you'd like the column to be associated.
            structuralColumnType: The structural column type representing the column.
        """
        pass

    def InternalSetFamilyInstance(self, *args): #cannot find CLR method
        """ InternalSetFamilyInstance(self: AbstractFamilyInstance, fi: FamilyInstance) """
        pass

    def InternalSetFamilySymbol(self, *args): #cannot find CLR method
        """ InternalSetFamilySymbol(self: AbstractFamilyInstance, fs: FamilySymbol) """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets curve geometry from location of the specified structural element

Get: Location(self: StructuralFraming) -> Curve

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets family type from the specified structural element

Get: Type(self: StructuralFraming) -> FamilyType

"""


    InternalUniqueId = None


class StructuralType(Enum, IComparable, IFormattable, IConvertible):
    """ enum StructuralType, values: Beam (0), Brace (1), Column (2), Footing (3), NonStructural (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beam = None
    Brace = None
    Column = None
    Footing = None
    NonStructural = None
    value__ = None


class SunSettings(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    @staticmethod
    def Current():
        """ Current() -> SunSettings """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: SunSettings) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extracts the Altitude.

Get: Altitude(self: SunSettings) -> float

"""

    Azimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extracts the Azimuth.

Get: Azimuth(self: SunSettings) -> float

"""

    CurrentDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Date and Time for the current frame of the solar study given in the local time of the solar study location.

Get: CurrentDateTime(self: SunSettings) -> DateTime

"""

    EndDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the End Date and Time of the solar study given in the local time of the solar study location.

Get: EndDateTime(self: SunSettings) -> DateTime

"""

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: SunSettings) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    StartDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Start Date and Time of the solar study given in the local time of the solar study location.

Get: StartDateTime(self: SunSettings) -> DateTime

"""

    SunDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Calculates the direction of the sun.

Get: SunDirection(self: SunSettings) -> Vector

"""


    InternalUniqueId = None


class TextElement(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def Tessellate(self, package, parameters):
        """
        Tessellate(self: TextElement, package: IRenderPackage, parameters: TessellationParameters)
            Text Tesselation
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Internal Revit Element

Get: InternalElement(self: TextElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Tag(TextElement, IDisposable, IGraphicItem, IFormattable):
    """ Revit Tag Element """
    @staticmethod
    def ByElement(view, element, horizontal, addLeader, horizontalAlignment, verticalAlignment, offset, isOffset):
        """
        ByElement(view: View, element: Element, horizontal: bool, addLeader: bool, horizontalAlignment: str, verticalAlignment: str, offset: Vector, isOffset: bool) -> Tag
        
            Create a Revit Tag for a Revit Element
        
            view: View to Tag
            element: Element to tag
            horizontal: Horizontal alignment
            addLeader: Add a leader
            horizontalAlignment: Horizontal Alignment
            verticalAlignment: Vertical Alignment
            offset: Offset Vector or Tag Location
            isOffset: Specifies if the point is being used as an offset vector or if it specifies the 
             tags location
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    TaggedElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Tagged Element

Get: TaggedElement(self: Tag) -> Element

"""

    TagText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Tag's Text

Get: TagText(self: Tag) -> str

"""


    InternalUniqueId = None


class TextNote(TextElement, IDisposable, IGraphicItem, IFormattable):
    """ Revit Text Note Element """
    @staticmethod
    def ByLocation(view, location, text, alignment, type, keepRotatedTextReadable, rotation):
        """
        ByLocation(view: View, location: Point, text: str, alignment: str, type: TextNoteType, keepRotatedTextReadable: bool, rotation: float) -> TextNote
        
            Construct a new Revit TextNote by Location
        
            view: View to place text element on
            location: Location in view
            text: Text
            alignment: Text alignment
            type: Revit TextNote Type
            keepRotatedTextReadable: Keep text horizontal
            rotation: Rotation in degrees
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetHorizontalAlignment(self, value):
        """
        SetHorizontalAlignment(self: TextNote, value: str)
            Set Horizontal Text Alignment
        """
        pass

    def SetKeepRotatedTextReadable(self, value):
        """
        SetKeepRotatedTextReadable(self: TextNote, value: bool)
            Set Keep Rotated Text Readable
        """
        pass

    def SetText(self, value):
        """
        SetText(self: TextNote, value: str)
            Set Text
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Height

Get: Height(self: TextNote) -> float

"""

    HorizontalAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Horizontal Alignment

Get: HorizontalAlignment(self: TextNote) -> str

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Text

Get: Text(self: TextNote) -> str

"""

    Typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Typename

Get: Typename(self: TextNote) -> str

"""

    VerticalAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Vertical Alignment

Get: VerticalAlignment(self: TextNote) -> str

"""


    InternalUniqueId = None


class TextNoteType(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit TextNoteType """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> TextNoteType
        
            Select a ModelTextType from the current document by name
        """
        pass

    @staticmethod
    def Default():
        """
        Default() -> TextNoteType
        
            Return a default TextNoteType
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: TextNoteType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Topography(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    @staticmethod
    def ByPoints(points):
        """ ByPoints(points: IEnumerable[Point]) -> Topography """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: Topography) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: Topography) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Mesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the underlying triangular Mesh from the Topography

Get: Mesh(self: Topography) -> Mesh

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The set of points from which this TopographySurface is constructed.

Get: Points(self: Topography) -> List[Point]

"""


    InternalUniqueId = None


class UnknownElement(Element, IDisposable, IGraphicItem, IFormattable):
    """
    A Revit Element of an unknown type.  This allows an arbitrary element
                to be passed around in the graph.
    """
    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: UnknownElement) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalElement(self: UnknownElement) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Wall(Element, IDisposable, IGraphicItem, IFormattable):
    # no doc
    @staticmethod
    def ByCurveAndHeight(curve, height, level, wallType):
        """
        ByCurveAndHeight(curve: Curve, height: float, level: Level, wallType: WallType) -> Wall
        
            Create a Revit Wall from a guiding Curve, height, Level, and WallType
        """
        pass

    @staticmethod
    def ByCurveAndLevels(c, startLevel, endLevel, wallType):
        """
        ByCurveAndLevels(c: Curve, startLevel: Level, endLevel: Level, wallType: WallType) -> Wall
        
            Create a Revit Wall from a guiding Curve, start Level, end Level, and WallType
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Wall) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class WallType(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit WallType """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> WallType
        
            Select a walltype from the current document by name
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: WallType) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: WallType) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the specified wall type

Get: Name(self: WallType) -> str

"""


    InternalUniqueId = None


# variables with complex values


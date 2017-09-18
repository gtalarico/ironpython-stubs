# encoding: utf-8
# module Rhino.UI.Gumball calls itself Gumball
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GumballAppearanceSettings(object):
    """ GumballAppearanceSettings() """
    ArcThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: ArcThickness(self: GumballAppearanceSettings) -> int

Set: ArcThickness(self: GumballAppearanceSettings) = value
"""

    ArrowHeadLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: ArrowHeadLength(self: GumballAppearanceSettings) -> int

Set: ArrowHeadLength(self: GumballAppearanceSettings) = value
"""

    ArrowHeadWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: ArrowHeadWidth(self: GumballAppearanceSettings) -> int

Set: ArrowHeadWidth(self: GumballAppearanceSettings) = value
"""

    AxisThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: AxisThickness(self: GumballAppearanceSettings) -> int

Set: AxisThickness(self: GumballAppearanceSettings) = value
"""

    ColorMenuButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorMenuButton(self: GumballAppearanceSettings) -> Color

Set: ColorMenuButton(self: GumballAppearanceSettings) = value
"""

    ColorX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default is Red.

Get: ColorX(self: GumballAppearanceSettings) -> Color

Set: ColorX(self: GumballAppearanceSettings) = value
"""

    ColorY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default is Green.

Get: ColorY(self: GumballAppearanceSettings) -> Color

Set: ColorY(self: GumballAppearanceSettings) = value
"""

    ColorZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default is Blue.

Get: ColorZ(self: GumballAppearanceSettings) -> Color

Set: ColorZ(self: GumballAppearanceSettings) = value
"""

    FreeTranslate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When FreeTranslate is 1, the center translation control can be dragged
            in any direction and moves the object the gumball controls. When
            FreeTranslate is 2, the center translation control can be dragged in any
            direction and moves the object the gumball itself. The default value is 2.

Get: FreeTranslate(self: GumballAppearanceSettings) -> int

Set: FreeTranslate(self: GumballAppearanceSettings) = value
"""

    MenuDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance of menu ball from center.

Get: MenuDistance(self: GumballAppearanceSettings) -> int

Set: MenuDistance(self: GumballAppearanceSettings) = value
"""

    MenuEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When MenuEnabled is true, the menu "button" is drawn on the gumball.
            The default setting is true.

Get: MenuEnabled(self: GumballAppearanceSettings) -> bool

Set: MenuEnabled(self: GumballAppearanceSettings) = value
"""

    MenuSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radius of menu circle.

Get: MenuSize(self: GumballAppearanceSettings) -> int

Set: MenuSize(self: GumballAppearanceSettings) = value
"""

    PlanarTranslationGripCorner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: PlanarTranslationGripCorner(self: GumballAppearanceSettings) -> int

Set: PlanarTranslationGripCorner(self: GumballAppearanceSettings) = value
"""

    PlanarTranslationGripSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: PlanarTranslationGripSize(self: GumballAppearanceSettings) -> int

Set: PlanarTranslationGripSize(self: GumballAppearanceSettings) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: Radius(self: GumballAppearanceSettings) -> int

Set: Radius(self: GumballAppearanceSettings) = value
"""

    RelocateEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When RelocateEnabled is true, the user can reposition the gumball by
            tapping the control key while dragging.  Once the repostion drag is
            terminated by releasing the/ mouse button, ordinary editing resumes.
            The default setting is true.

Get: RelocateEnabled(self: GumballAppearanceSettings) -> bool

Set: RelocateEnabled(self: GumballAppearanceSettings) = value
"""

    RotateXEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When RotateX is true, the X rotation control is available. The default
            setting is true.

Get: RotateXEnabled(self: GumballAppearanceSettings) -> bool

Set: RotateXEnabled(self: GumballAppearanceSettings) = value
"""

    RotateYEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When RotateY is true, the Y rotation control is available. The default
            setting is true.

Get: RotateYEnabled(self: GumballAppearanceSettings) -> bool

Set: RotateYEnabled(self: GumballAppearanceSettings) = value
"""

    RotateZEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When RotateZ is true, the Z rotation control is available. The default
            setting is true.

Get: RotateZEnabled(self: GumballAppearanceSettings) -> bool

Set: RotateZEnabled(self: GumballAppearanceSettings) = value
"""

    ScaleGripSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """in pixels.

Get: ScaleGripSize(self: GumballAppearanceSettings) -> int

Set: ScaleGripSize(self: GumballAppearanceSettings) = value
"""

    ScaleXEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When ScaleXEnabled is true, the X scale control is available. The
            default setting is true.

Get: ScaleXEnabled(self: GumballAppearanceSettings) -> bool

Set: ScaleXEnabled(self: GumballAppearanceSettings) = value
"""

    ScaleYEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When ScaleYEnabled is true, the Y scale control is available. The
            default setting is true.

Get: ScaleYEnabled(self: GumballAppearanceSettings) -> bool

Set: ScaleYEnabled(self: GumballAppearanceSettings) = value
"""

    ScaleZEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When ScaleZEnabled is true, the Z scale control is available. The
            default setting is true.

Get: ScaleZEnabled(self: GumballAppearanceSettings) -> bool

Set: ScaleZEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateXEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TranslateXEnabled is true, the X axis translation control is available.
            The default setting is true.

Get: TranslateXEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateXEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateXYEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When TranslateXY is true, the XY plane translation control is available
            in appropriate views. The default setting is true.

Get: TranslateXYEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateXYEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateYEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TranslateYEnabled is true, the Y axis translation control is available.
            The default setting is true.

Get: TranslateYEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateYEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateYZEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When TranslateYZ is true, the YZ plane translation control is available
            in appropriate views. The default setting is true.

Get: TranslateYZEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateYZEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateZEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TranslateZEnabled is true, the Z axis translation control is available.
            The default setting is true.

Get: TranslateZEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateZEnabled(self: GumballAppearanceSettings) = value
"""

    TranslateZXEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When TranslateZX is true, the ZX plane translation control is available
            in appropriate views. The default setting is true.

Get: TranslateZXEnabled(self: GumballAppearanceSettings) -> bool

Set: TranslateZXEnabled(self: GumballAppearanceSettings) = value
"""



class GumballDisplayConduit(object, IDisposable):
    """ GumballDisplayConduit() """
    def CheckShiftAndControlKeys(self):
        """ CheckShiftAndControlKeys(self: GumballDisplayConduit) """
        pass

    def Dispose(self):
        """ Dispose(self: GumballDisplayConduit) """
        pass

    def PickGumball(self, pickContext, getPoint):
        """ PickGumball(self: GumballDisplayConduit, pickContext: PickContext, getPoint: GetPoint) -> bool """
        pass

    def SetBaseGumball(self, gumball, appearanceSettings=None):
        """
        SetBaseGumball(self: GumballDisplayConduit, gumball: GumballObject, appearanceSettings: GumballAppearanceSettings)
            Contents of the gumball are copied to the base gumball of this class.
        
            gumball: The gumball source.
            appearanceSettings: The gumball appearance and behavior settings.
        SetBaseGumball(self: GumballDisplayConduit, gumball: GumballObject)
            Contents of the gumball are copied to the base gumball of this class.
        
            gumball: The gumball source.
        """
        pass

    def UpdateGumball(self, point, worldLine):
        """ UpdateGumball(self: GumballDisplayConduit, point: Point3d, worldLine: Line) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BaseGumball = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Starting location.

Get: BaseGumball(self: GumballDisplayConduit) -> GumballObject

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: GumballDisplayConduit) -> bool

Set: Enabled(self: GumballDisplayConduit) = value
"""

    Gumball = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gumball(self: GumballDisplayConduit) -> GumballObject

"""

    GumballTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gumball transformation is the transformation calculated by comparing
            the current gumball to the starting BaseGumball.

Get: GumballTransform(self: GumballDisplayConduit) -> Transform

"""

    InRelocate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InRelocate(self: GumballDisplayConduit) -> bool

"""

    PickResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The inital mouse down event sets PickResult.

Get: PickResult(self: GumballDisplayConduit) -> GumballPickResult

"""

    PreTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pre-transform is a transformation that needs to be applied before
            the gumball transformation.

Get: PreTransform(self: GumballDisplayConduit) -> Transform

Set: PreTransform(self: GumballDisplayConduit) = value
"""

    TotalTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total transformation is GumballTransform * PreTransform.

Get: TotalTransform(self: GumballDisplayConduit) -> Transform

"""



class GumballFrame(object):
    # no doc
    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: GumballFrame) -> Plane

Set: Plane(self: GumballFrame) = value
"""

    ScaleGripDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleGripDistance(self: GumballFrame) -> Vector3d

Set: ScaleGripDistance(self: GumballFrame) = value
"""

    ScaleMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleMode(self: GumballFrame) -> GumballScaleMode

Set: ScaleMode(self: GumballFrame) = value
"""



class GumballMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Transformation modes for gumballs.
    
    enum GumballMode, values: Menu (1), None (0), RotateX (12), RotateY (13), RotateZ (14), ScaleX (9), ScaleY (10), ScaleZ (11), TranslateFree (2), TranslateX (3), TranslateXY (6), TranslateY (4), TranslateYZ (7), TranslateZ (5), TranslateZX (8)
    """
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

    Menu = None
    None = None
    RotateX = None
    RotateY = None
    RotateZ = None
    ScaleX = None
    ScaleY = None
    ScaleZ = None
    TranslateFree = None
    TranslateX = None
    TranslateXY = None
    TranslateY = None
    TranslateYZ = None
    TranslateZ = None
    TranslateZX = None
    value__ = None


class GumballObject(object, IDisposable):
    """ GumballObject() """
    def Dispose(self):
        """ Dispose(self: GumballObject) """
        pass

    def SetFromArc(self, arc):
        """ SetFromArc(self: GumballObject, arc: Arc) -> bool """
        pass

    def SetFromBoundingBox(self, *__args):
        """
        SetFromBoundingBox(self: GumballObject, frame: Plane, frameBoundingBox: BoundingBox) -> bool
        
            Sets the gumball bounding box with respect to a frame.
        
            frame: The frame.
            frameBoundingBox: Bounding box with respect to frame.
            Returns: true if input is valid and gumball is set. false if input is not valid.
                    In this 
             case, gumball is set to the default.
        
        SetFromBoundingBox(self: GumballObject, boundingBox: BoundingBox) -> bool
        """
        pass

    def SetFromCircle(self, circle):
        """ SetFromCircle(self: GumballObject, circle: Circle) -> bool """
        pass

    def SetFromCurve(self, curve):
        """ SetFromCurve(self: GumballObject, curve: Curve) -> bool """
        pass

    def SetFromEllipse(self, ellipse):
        """ SetFromEllipse(self: GumballObject, ellipse: Ellipse) -> bool """
        pass

    def SetFromExtrusion(self, extrusion):
        """ SetFromExtrusion(self: GumballObject, extrusion: Extrusion) -> bool """
        pass

    def SetFromHatch(self, hatch):
        """ SetFromHatch(self: GumballObject, hatch: Hatch) -> bool """
        pass

    def SetFromLight(self, light):
        """ SetFromLight(self: GumballObject, light: Light) -> bool """
        pass

    def SetFromLine(self, line):
        """ SetFromLine(self: GumballObject, line: Line) -> bool """
        pass

    def SetFromPlane(self, plane):
        """ SetFromPlane(self: GumballObject, plane: Plane) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Frame(self: GumballObject) -> GumballFrame

Set: Frame(self: GumballObject) = value
"""



class GumballPickResult(object):
    # no doc
    def SetToDefault(self):
        """ SetToDefault(self: GumballPickResult) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mode(self: GumballPickResult) -> GumballMode

"""



class GumballScaleMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GumballScaleMode, values: Independent (0), XY (1), XYZ (4), YZ (2), ZX (3) """
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

    Independent = None
    value__ = None
    XY = None
    XYZ = None
    YZ = None
    ZX = None



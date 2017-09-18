# encoding: utf-8
# module Grasshopper.GUI.Theme calls itself Theme
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_BackgroundSettings(object):
    # no doc
    Colour1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colour1(self: GH_BackgroundSettings) -> Color

Set: Colour1(self: GH_BackgroundSettings) = value
"""

    Colour2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colour2(self: GH_BackgroundSettings) -> Color

Set: Colour2(self: GH_BackgroundSettings) = value
"""

    Hatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hatch(self: GH_BackgroundSettings) -> HatchStyle

Set: Hatch(self: GH_BackgroundSettings) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: GH_BackgroundSettings) -> GH_BackgroundStyle

Set: Style(self: GH_BackgroundSettings) = value
"""



class GH_BackgroundStyle(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_BackgroundStyle, values: GradientLeftRight (10), GradientTopBottom (11), Hatch (1), Solid (0) """
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

    GradientLeftRight = None
    GradientTopBottom = None
    Hatch = None
    Solid = None
    value__ = None


class GH_ObjectSettings(object):
    # no doc
    GroupColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupColour(self: GH_ObjectSettings) -> Color

Set: GroupColour(self: GH_ObjectSettings) = value
"""

    PanelColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PanelColour(self: GH_ObjectSettings) -> Color

Set: PanelColour(self: GH_ObjectSettings) = value
"""

    ZuiEdgeColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZuiEdgeColour(self: GH_ObjectSettings) -> Color

Set: ZuiEdgeColour(self: GH_ObjectSettings) = value
"""

    ZuiFillColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZuiFillColour(self: GH_ObjectSettings) -> Color

Set: ZuiFillColour(self: GH_ObjectSettings) = value
"""



class GH_PageSettings(object):
    # no doc
    DrawGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawGrid(self: GH_PageSettings) -> bool

Set: DrawGrid(self: GH_PageSettings) = value
"""

    DrawPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawPage(self: GH_PageSettings) -> bool

Set: DrawPage(self: GH_PageSettings) = value
"""

    DrawShadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawShadow(self: GH_PageSettings) -> bool

Set: DrawShadow(self: GH_PageSettings) = value
"""

    EdgeColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeColour(self: GH_PageSettings) -> Color

Set: EdgeColour(self: GH_PageSettings) = value
"""

    FillColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillColour(self: GH_PageSettings) -> Color

Set: FillColour(self: GH_PageSettings) = value
"""

    GridColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridColour(self: GH_PageSettings) -> Color

Set: GridColour(self: GH_PageSettings) = value
"""

    GridHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridHeight(self: GH_PageSettings) -> int

Set: GridHeight(self: GH_PageSettings) = value
"""

    GridPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridPattern(self: GH_PageSettings) -> Array[Single]

Set: GridPattern(self: GH_PageSettings) = value
"""

    GridWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridWidth(self: GH_PageSettings) -> int

Set: GridWidth(self: GH_PageSettings) = value
"""

    ShadowColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowColour(self: GH_PageSettings) -> Color

Set: ShadowColour(self: GH_PageSettings) = value
"""

    ShadowSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowSize(self: GH_PageSettings) -> int

Set: ShadowSize(self: GH_PageSettings) = value
"""



class GH_PaletteSettings(object):
    # no doc
    ErrorSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorSelected(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: ErrorSelected(self: GH_PaletteSettings) = value
"""

    ErrorStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorStandard(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: ErrorStandard(self: GH_PaletteSettings) = value
"""

    HiddenSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HiddenSelected(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: HiddenSelected(self: GH_PaletteSettings) = value
"""

    HiddenStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HiddenStandard(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: HiddenStandard(self: GH_PaletteSettings) = value
"""

    LockedSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockedSelected(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: LockedSelected(self: GH_PaletteSettings) = value
"""

    LockedStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockedStandard(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: LockedStandard(self: GH_PaletteSettings) = value
"""

    NormalSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalSelected(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: NormalSelected(self: GH_PaletteSettings) = value
"""

    NormalStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalStandard(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: NormalStandard(self: GH_PaletteSettings) = value
"""

    WarningSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarningSelected(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: WarningSelected(self: GH_PaletteSettings) = value
"""

    WarningStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarningStandard(self: GH_PaletteSettings) -> GH_PaletteStyle

Set: WarningStandard(self: GH_PaletteSettings) = value
"""



class GH_Theme(object, GH_ISerializable):
    """
    GH_Theme()
    GH_Theme(other: GH_Theme)
    """
    def LoadTheme(self):
        """ LoadTheme(self: GH_Theme) """
        pass

    def Read(self, reader):
        """ Read(self: GH_Theme, reader: GH_IReader) -> bool """
        pass

    def SaveTheme(self):
        """ SaveTheme(self: GH_Theme) """
        pass

    def Write(self, writer):
        """ Write(self: GH_Theme, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GH_Theme)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BackGround = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackGround(self: GH_Theme) -> GH_BackgroundSettings

"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: GH_Theme) -> GH_ObjectSettings

"""

    Page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Page(self: GH_Theme) -> GH_PageSettings

"""

    Palettes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Palettes(self: GH_Theme) -> GH_PaletteSettings

"""

    Wires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wires(self: GH_Theme) -> GH_WireSettings

"""


    DefaultTheme = None


class GH_WireSettings(object):
    # no doc
    DefaultColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultColour(self: GH_WireSettings) -> Color

Set: DefaultColour(self: GH_WireSettings) = value
"""

    EmptyColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EmptyColour(self: GH_WireSettings) -> Color

Set: EmptyColour(self: GH_WireSettings) = value
"""

    SelectedColour0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedColour0(self: GH_WireSettings) -> Color

Set: SelectedColour0(self: GH_WireSettings) = value
"""

    SelectedColour1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedColour1(self: GH_WireSettings) -> Color

Set: SelectedColour1(self: GH_WireSettings) = value
"""




# encoding: utf-8
# module Grasshopper.GUI.Base calls itself Base
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_ColourCube(object):
    """ GH_ColourCube(box: Rectangle, space: GH_ColourSpace, color: Point4d) """
    def Average(self, A, B, C=None, D=None):
        """
        Average(self: GH_ColourCube, A: Color, B: Color, C: Color, D: Color) -> Color
        Average(self: GH_ColourCube, A: Color, B: Color) -> Color
        """
        pass

    def Blend(self, A, B, t):
        """ Blend(self: GH_ColourCube, A: Color, B: Color, t: float) -> Color """
        pass

    def ColorAtRail(self, pt):
        """ ColorAtRail(self: GH_ColourCube, pt: PointF) -> Point4d """
        pass

    def ColorAtSlice(self, pt):
        """ ColorAtSlice(self: GH_ColourCube, pt: PointF) -> Point4d """
        pass

    def RenderAll(self, G):
        """ RenderAll(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderBackEdges(self, G):
        """ RenderBackEdges(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderBackFaces(self, G):
        """ RenderBackFaces(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderDropShadow(self, G):
        """ RenderDropShadow(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderEdgeShadows(self, G):
        """ RenderEdgeShadows(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderForeEdges(self, G):
        """ RenderForeEdges(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderGrip(self, G):
        """ RenderGrip(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderPivot(self, G):
        """ RenderPivot(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderSilhouetteEdges(self, G):
        """ RenderSilhouetteEdges(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderSlice(self, G):
        """ RenderSlice(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderSliceDropShadow(self, G):
        """ RenderSliceDropShadow(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderSliceEdgeShadows(self, G):
        """ RenderSliceEdgeShadows(self: GH_ColourCube, G: Graphics) """
        pass

    def RenderSliceSilhouetteEdges(self, G):
        """ RenderSliceSilhouetteEdges(self: GH_ColourCube, G: Graphics) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, box, space, color):
        """ __new__(cls: type, box: Rectangle, space: GH_ColourSpace, color: Point4d) """
        pass

    BackFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackFace(self: GH_ColourCube) -> GraphicsPath

"""

    BottomFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomFace(self: GH_ColourCube) -> GraphicsPath

"""

    C0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C0(self: GH_ColourCube) -> Point

"""

    C1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C1(self: GH_ColourCube) -> Point

"""

    C2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C2(self: GH_ColourCube) -> Point

"""

    C3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C3(self: GH_ColourCube) -> Point

"""

    C4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C4(self: GH_ColourCube) -> Point

"""

    C5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C5(self: GH_ColourCube) -> Point

"""

    C6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C6(self: GH_ColourCube) -> Point

"""

    C7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C7(self: GH_ColourCube) -> Point

"""

    Grip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grip(self: GH_ColourCube) -> Rectangle

"""

    LeftFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftFace(self: GH_ColourCube) -> GraphicsPath

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: GH_ColourCube) -> Point

"""

    S0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S0(self: GH_ColourCube) -> Point

"""

    S1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S1(self: GH_ColourCube) -> Point

"""

    S2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S2(self: GH_ColourCube) -> Point

"""

    S3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S3(self: GH_ColourCube) -> Point

"""

    S4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S4(self: GH_ColourCube) -> Point

"""

    Shadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shadow(self: GH_ColourCube) -> GraphicsPath

"""

    Silhouette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Silhouette(self: GH_ColourCube) -> GraphicsPath

"""

    Slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slice(self: GH_ColourCube) -> Rectangle

"""



class GH_ColourPickerBase(object, IGH_ToolstripItemKeyHandler):
    """ GH_ColourPickerBase() """
    def Invalidate(self):
        """ Invalidate(self: GH_ColourPickerBase) """
        pass

    def MouseClick(self, args, pt):
        """ MouseClick(self: GH_ColourPickerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseDoubleClick(self, args, pt, owner, transform):
        """ MouseDoubleClick(self: GH_ColourPickerBase, args: MouseEventArgs, pt: PointF, owner: Control, transform: Matrix) -> bool """
        pass

    def MouseDown(self, args, pt):
        """ MouseDown(self: GH_ColourPickerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseMove(self, args, pt):
        """ MouseMove(self: GH_ColourPickerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseUp(self, args, pt):
        """ MouseUp(self: GH_ColourPickerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def OnColorChanged(self, intermediate):
        """ OnColorChanged(self: GH_ColourPickerBase, intermediate: bool) """
        pass

    def Render(self, G):
        """ Render(self: GH_ColourPickerBase, G: Graphics) """
        pass

    def RespondToEnter(self):
        """ RespondToEnter(self: GH_ColourPickerBase) -> GH_ToolstripItemKeyHandlerResult """
        pass

    def RespondToEscape(self):
        """ RespondToEscape(self: GH_ColourPickerBase) -> GH_ToolstripItemKeyHandlerResult """
        pass

    def SetupColourPicker(self, col0, col1, space):
        """ SetupColourPicker(self: GH_ColourPickerBase, col0: Color, col1: Point4d, space: GH_ColourSpace)SetupColourPicker(self: GH_ColourPickerBase, col0: Color, col1: Color, space: GH_ColourSpace) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AutoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSize(self: GH_ColourPickerBase) -> bool

Set: AutoSize(self: GH_ColourPickerBase) = value
"""

    BackColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackColour(self: GH_ColourPickerBase) -> Color

Set: BackColour(self: GH_ColourPickerBase) = value
"""

    BaseColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseColour(self: GH_ColourPickerBase) -> Color

"""

    BaseColourBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseColourBox(self: GH_ColourPickerBase) -> Rectangle

"""

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_ColourPickerBase) -> Rectangle

Set: Bounds(self: GH_ColourPickerBase) = value
"""

    ChannelBox0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelBox0(self: GH_ColourPickerBase) -> Rectangle

"""

    ChannelBox1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelBox1(self: GH_ColourPickerBase) -> Rectangle

"""

    ChannelBox2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelBox2(self: GH_ColourPickerBase) -> Rectangle

"""

    ChannelBox3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelBox3(self: GH_ColourPickerBase) -> Rectangle

"""

    ColourCubeBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourCubeBox(self: GH_ColourPickerBase) -> Rectangle

"""

    ColourSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourSpace(self: GH_ColourPickerBase) -> GH_ColourSpace

"""

    Cube = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cube(self: GH_ColourPickerBase) -> GH_ColourCube

"""

    DesiredHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesiredHeight(self: GH_ColourPickerBase) -> int

"""

    DrawAlphaSlider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawAlphaSlider(self: GH_ColourPickerBase) -> bool

Set: DrawAlphaSlider(self: GH_ColourPickerBase) = value
"""

    DrawBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawBackground(self: GH_ColourPickerBase) -> bool

Set: DrawBackground(self: GH_ColourPickerBase) = value
"""

    DrawChannelSliders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawChannelSliders(self: GH_ColourPickerBase) -> bool

Set: DrawChannelSliders(self: GH_ColourPickerBase) = value
"""

    DropperPreviewBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DropperPreviewBox(self: GH_ColourPickerBase) -> Rectangle

"""

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Font(self: GH_ColourPickerBase) -> Font

Set: Font(self: GH_ColourPickerBase) = value
"""

    HSVSpaceBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HSVSpaceBox(self: GH_ColourPickerBase) -> Rectangle

"""

    IsTextInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTextInput(self: GH_ColourPickerBase) -> bool

"""

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Padding(self: GH_ColourPickerBase) -> Padding

Set: Padding(self: GH_ColourPickerBase) = value
"""

    PickColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickColour(self: GH_ColourPickerBase) -> Color

"""

    PickColourBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickColourBox(self: GH_ColourPickerBase) -> Rectangle

"""

    RGBSpaceBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RGBSpaceBox(self: GH_ColourPickerBase) -> Rectangle

"""

    SRCSpaceBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRCSpaceBox(self: GH_ColourPickerBase) -> Rectangle

"""


    ColorChanged = None
    ColorChangedEventHandler = None
    Invalidated = None
    InvalidatedEventHandler = None
    MinWidth = 100
    SliderSize = 20
    Spacing = 12
    SwatchSize = 24


class GH_ColourPickerEventArgs(EventArgs):
    # no doc
    Colour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colour(self: GH_ColourPickerEventArgs) -> Color

"""

    ColourPicker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourPicker(self: GH_ColourPickerEventArgs) -> GH_ColourPickerBase

"""

    Intermediate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intermediate(self: GH_ColourPickerEventArgs) -> bool

"""

    Original = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Original(self: GH_ColourPickerEventArgs) -> Color

"""



class GH_ColourSpace(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_ColourSpace, values: HSV (2), None (0), RGB (1) """
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

    HSV = None
    None = None
    RGB = None
    value__ = None


class GH_ColourSphere(object):
    """ GH_ColourSphere(bounds: Rectangle) """
    def MouseDown(self, e):
        """ MouseDown(self: GH_ColourSphere, e: MouseEventArgs) -> bool """
        pass

    def MouseMove(self, e):
        """ MouseMove(self: GH_ColourSphere, e: MouseEventArgs) -> bool """
        pass

    def MouseUp(self, e):
        """ MouseUp(self: GH_ColourSphere, e: MouseEventArgs) -> bool """
        pass

    def RenderSphere(self, G):
        """ RenderSphere(self: GH_ColourSphere, G: Graphics) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bounds):
        """ __new__(cls: type, bounds: Rectangle) """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_ColourSphere) -> Rectangle

Set: Bounds(self: GH_ColourSphere) = value
"""

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: GH_ColourSphere) -> Rectangle

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: GH_ColourSphere) -> Single

"""



class GH_DigitAlign(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_DigitAlign, values: Center (2), Justify (0), Left (1), Right (3) """
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

    Center = None
    Justify = None
    Left = None
    Right = None
    value__ = None


class GH_DigitNumber(object):
    """
    GH_DigitNumber(decimalPlaces: int)
    GH_DigitNumber(decimalPlaces: int, radixPosition: int)
    GH_DigitNumber(other: GH_DigitNumber)
    """
    def AssignOffset(self, index, offset):
        """ AssignOffset(self: GH_DigitNumber, index: int, offset: Decimal) -> bool """
        pass

    def LimitValue(self):
        """ LimitValue(self: GH_DigitNumber) """
        pass

    def Reset(self):
        """ Reset(self: GH_DigitNumber) """
        pass

    def Round(self):
        """ Round(self: GH_DigitNumber) """
        pass

    def ToString(self):
        """ ToString(self: GH_DigitNumber) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, decimalPlaces: int)
        __new__(cls: type, decimalPlaces: int, radixPosition: int)
        __new__(cls: type, other: GH_DigitNumber)
        """
        pass

    DigitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitCount(self: GH_DigitNumber) -> int

"""

    Epsilon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsilon(self: GH_DigitNumber) -> Decimal

"""

    Maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Maximum(self: GH_DigitNumber) -> Decimal

Set: Maximum(self: GH_DigitNumber) = value
"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minimum(self: GH_DigitNumber) -> Decimal

Set: Minimum(self: GH_DigitNumber) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: GH_DigitNumber) -> Decimal

"""

    PrimaryDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryDigits(self: GH_DigitNumber) -> IList[int]

"""

    PrimaryPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryPositive(self: GH_DigitNumber) -> bool

Set: PrimaryPositive(self: GH_DigitNumber) = value
"""

    Radix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radix(self: GH_DigitNumber) -> int

Set: Radix(self: GH_DigitNumber) = value
"""

    RadixIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadixIndex(self: GH_DigitNumber) -> int

"""

    SecondaryDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryDigits(self: GH_DigitNumber) -> IList[int]

"""

    SecondaryPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryPositive(self: GH_DigitNumber) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_DigitNumber) -> Decimal

Set: Value(self: GH_DigitNumber) = value
"""



class GH_TextBoxInputBase(object, IGH_ToolstripItemKeyHandler):
    # no doc
    def HandleTextInputAccepted(self, *args): #cannot find CLR method
        """ HandleTextInputAccepted(self: GH_TextBoxInputBase, text: str) """
        pass

    def HideTextInputBox(self):
        """ HideTextInputBox(self: GH_TextBoxInputBase) """
        pass

    def RespondToEnter(self):
        """ RespondToEnter(self: GH_TextBoxInputBase) -> GH_ToolstripItemKeyHandlerResult """
        pass

    def RespondToEscape(self):
        """ RespondToEscape(self: GH_TextBoxInputBase) -> GH_ToolstripItemKeyHandlerResult """
        pass

    def ShowTextInputBox(self, owner, content, selectContent, limitToBoundary=None, transform=None):
        """ ShowTextInputBox(self: GH_TextBoxInputBase, owner: Control, content: str, selectContent: bool, limitToBoundary: bool, transform: Matrix)ShowTextInputBox(self: GH_TextBoxInputBase, owner: Control, content: str, selectContent: bool, limitToBoundary: bool)ShowTextInputBox(self: GH_TextBoxInputBase, owner: Control, content: str, selectContent: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_TextBoxInputBase) -> Rectangle

Set: Bounds(self: GH_TextBoxInputBase) = value
"""

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Font(self: GH_TextBoxInputBase) -> Font

Set: Font(self: GH_TextBoxInputBase) = value
"""

    IsTextInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTextInput(self: GH_TextBoxInputBase) -> bool

"""



class GH_DigitScrollerBase(GH_TextBoxInputBase, IGH_ToolstripItemKeyHandler):
    """ GH_DigitScrollerBase() """
    def HandleTextInputAccepted(self, *args): #cannot find CLR method
        """ HandleTextInputAccepted(self: GH_DigitScrollerBase, text: str) """
        pass

    def MouseDown(self, args, pt):
        """ MouseDown(self: GH_DigitScrollerBase, args: MouseEventArgs, pt: PointF) -> GH_MouseAction """
        pass

    def MouseMove(self, args, pt):
        """ MouseMove(self: GH_DigitScrollerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseUp(self, args, pt):
        """ MouseUp(self: GH_DigitScrollerBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def OnInvalidated(self):
        """ OnInvalidated(self: GH_DigitScrollerBase) """
        pass

    def OnValueChanged(self, intermediate):
        """ OnValueChanged(self: GH_DigitScrollerBase, intermediate: bool) """
        pass

    def Render(self, G):
        """ Render(self: GH_DigitScrollerBase, G: Graphics) """
        pass

    def SetupScroller(self, minimum, maximum, value):
        """ SetupScroller(self: GH_DigitScrollerBase, minimum: Decimal, maximum: Decimal, value: Decimal) """
        pass

    def ShowTextInputBox(self, owner, *__args):
        """ ShowTextInputBox(self: GH_DigitScrollerBase, owner: Control, limitToBoundary: bool, transform: Matrix)ShowTextInputBox(self: GH_DigitScrollerBase, owner: Control, limitToBoundary: bool)ShowTextInputBox(self: GH_DigitScrollerBase, owner: Control) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllowRadixDrag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowRadixDrag(self: GH_DigitScrollerBase) -> bool

Set: AllowRadixDrag(self: GH_DigitScrollerBase) = value
"""

    AllowTextInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowTextInput(self: GH_DigitScrollerBase) -> bool

Set: AllowTextInput(self: GH_DigitScrollerBase) = value
"""

    AmplifyMotion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmplifyMotion(self: GH_DigitScrollerBase) -> bool

Set: AmplifyMotion(self: GH_DigitScrollerBase) = value
"""

    BackgroundGradient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundGradient(self: GH_DigitScrollerBase) -> GH_Gradient

Set: BackgroundGradient(self: GH_DigitScrollerBase) = value
"""

    BottomColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomColour(self: GH_DigitScrollerBase) -> Color

Set: BottomColour(self: GH_DigitScrollerBase) = value
"""

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_DigitScrollerBase) -> Rectangle

Set: Bounds(self: GH_DigitScrollerBase) = value
"""

    DecimalPlaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimalPlaces(self: GH_DigitScrollerBase) -> int

Set: DecimalPlaces(self: GH_DigitScrollerBase) = value
"""

    DigitAlign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitAlign(self: GH_DigitScrollerBase) -> GH_DigitAlign

Set: DigitAlign(self: GH_DigitScrollerBase) = value
"""

    Digits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Digits(self: GH_DigitScrollerBase) -> int

Set: Digits(self: GH_DigitScrollerBase) = value
"""

    DrawBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawBackground(self: GH_DigitScrollerBase) -> bool

Set: DrawBackground(self: GH_DigitScrollerBase) = value
"""

    DrawBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawBorder(self: GH_DigitScrollerBase) -> bool

Set: DrawBorder(self: GH_DigitScrollerBase) = value
"""

    DrawShadows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawShadows(self: GH_DigitScrollerBase) -> bool

Set: DrawShadows(self: GH_DigitScrollerBase) = value
"""

    EdgeColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeColour(self: GH_DigitScrollerBase) -> Color

Set: EdgeColour(self: GH_DigitScrollerBase) = value
"""

    Epsilon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsilon(self: GH_DigitScrollerBase) -> Decimal

"""

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Font(self: GH_DigitScrollerBase) -> Font

Set: Font(self: GH_DigitScrollerBase) = value
"""

    MaximumValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumValue(self: GH_DigitScrollerBase) -> Decimal

Set: MaximumValue(self: GH_DigitScrollerBase) = value
"""

    MinimumValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumValue(self: GH_DigitScrollerBase) -> Decimal

Set: MinimumValue(self: GH_DigitScrollerBase) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: GH_DigitScrollerBase) -> str

Set: Prefix(self: GH_DigitScrollerBase) = value
"""

    PrefixBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrefixBox(self: GH_DigitScrollerBase) -> Rectangle

"""

    Radix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radix(self: GH_DigitScrollerBase) -> int

Set: Radix(self: GH_DigitScrollerBase) = value
"""

    RadixBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadixBox(self: GH_DigitScrollerBase) -> Rectangle

"""

    RailColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailColour(self: GH_DigitScrollerBase) -> Color

Set: RailColour(self: GH_DigitScrollerBase) = value
"""

    RaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RaiseEvents(self: GH_DigitScrollerBase) -> bool

Set: RaiseEvents(self: GH_DigitScrollerBase) = value
"""

    ScrollBoxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScrollBoxes(self: GH_DigitScrollerBase) -> List[Rectangle]

"""

    ShadowColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowColour(self: GH_DigitScrollerBase) -> Color

Set: ShadowColour(self: GH_DigitScrollerBase) = value
"""

    ShadowSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowSize(self: GH_DigitScrollerBase) -> Padding

Set: ShadowSize(self: GH_DigitScrollerBase) = value
"""

    SignBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignBox(self: GH_DigitScrollerBase) -> Rectangle

"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: GH_DigitScrollerBase) -> str

Set: Suffix(self: GH_DigitScrollerBase) = value
"""

    SuffixBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuffixBox(self: GH_DigitScrollerBase) -> Rectangle

"""

    TextColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextColour(self: GH_DigitScrollerBase) -> Color

Set: TextColour(self: GH_DigitScrollerBase) = value
"""

    TopColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopColour(self: GH_DigitScrollerBase) -> Color

Set: TopColour(self: GH_DigitScrollerBase) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_DigitScrollerBase) -> Decimal

Set: Value(self: GH_DigitScrollerBase) = value
"""


    DigitBoxWidth = 13
    GH_MouseAction = None
    Invalidated = None
    InvalidatedEventHandler = None
    SymbolBoxWidth = 9
    ValueChanged = None
    ValueChangedEventHandler = None


class GH_DigitScrollerEventArgs(EventArgs):
    # no doc
    Intermediate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intermediate(self: GH_DigitScrollerEventArgs) -> bool

"""

    Scroller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scroller(self: GH_DigitScrollerEventArgs) -> GH_DigitScrollerBase

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_DigitScrollerEventArgs) -> Decimal

"""



class GH_ScrollBarVerticalBase(object):
    """ GH_ScrollBarVerticalBase() """
    def BeginDrag(self, region, start):
        """ BeginDrag(self: GH_ScrollBarVerticalBase, region: RectangleF, start: float) """
        pass

    def ContinueDrag(self, position):
        """ ContinueDrag(self: GH_ScrollBarVerticalBase, position: float) -> bool """
        pass

    def ScrollBar(self, rail):
        """
        ScrollBar(self: GH_ScrollBarVerticalBase, rail: RectangleF) -> RectangleF
        ScrollBar(self: GH_ScrollBarVerticalBase, rail: Rectangle) -> Rectangle
        """
        pass

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: GH_ScrollBarVerticalBase) -> int

Set: Content(self: GH_ScrollBarVerticalBase) = value
"""

    ContentOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentOffset(self: GH_ScrollBarVerticalBase) -> float

"""

    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: GH_ScrollBarVerticalBase) -> int

Set: Display(self: GH_ScrollBarVerticalBase) = value
"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minimum(self: GH_ScrollBarVerticalBase) -> int

Set: Minimum(self: GH_ScrollBarVerticalBase) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: GH_ScrollBarVerticalBase) -> int

"""

    OffsetNormalised = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetNormalised(self: GH_ScrollBarVerticalBase) -> float

Set: OffsetNormalised(self: GH_ScrollBarVerticalBase) = value
"""



class GH_SliderAccuracy(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_SliderAccuracy, values: Even (2), Float (0), Integer (1), Odd (3) """
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

    Even = None
    Float = None
    Integer = None
    Odd = None
    value__ = None


class GH_SliderBase(GH_TextBoxInputBase, IGH_ToolstripItemKeyHandler):
    """ GH_SliderBase() """
    def FixDomain(self):
        """ FixDomain(self: GH_SliderBase) """
        pass

    def FixValue(self):
        """ FixValue(self: GH_SliderBase) """
        pass

    def HandleTextInputAccepted(self, *args): #cannot find CLR method
        """ HandleTextInputAccepted(self: GH_SliderBase, text: str) """
        pass

    def KeyDown(self, args):
        """ KeyDown(self: GH_SliderBase, args: KeyEventArgs) -> bool """
        pass

    def MouseDown(self, args, pt):
        """ MouseDown(self: GH_SliderBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseMove(self, args, pt):
        """ MouseMove(self: GH_SliderBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def MouseUp(self, args, pt):
        """ MouseUp(self: GH_SliderBase, args: MouseEventArgs, pt: PointF) -> bool """
        pass

    def OnValueChanged(self, intermediate):
        """ OnValueChanged(self: GH_SliderBase, intermediate: bool) """
        pass

    @staticmethod
    def ProcessNumber(val, accuracy, digits):
        """ ProcessNumber(val: Decimal, accuracy: GH_SliderAccuracy, digits: int) -> Decimal """
        pass

    def Render(self, G):
        """ Render(self: GH_SliderBase, G: Graphics) """
        pass

    def SetSnapRanges(self, ranges):
        """ SetSnapRanges(self: GH_SliderBase, ranges: IEnumerable[SliderSnapRange]) """
        pass

    def ShowTextInputBox(self, owner, *__args):
        """ ShowTextInputBox(self: GH_SliderBase, owner: Control, limitToBoundary: bool, transform: Matrix)ShowTextInputBox(self: GH_SliderBase, owner: Control, limitToBoundary: bool, transform: Matrix, content: str)ShowTextInputBox(self: GH_SliderBase, owner: Control)ShowTextInputBox(self: GH_SliderBase, owner: Control, limitToBoundary: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_SliderBase) -> Rectangle

Set: Bounds(self: GH_SliderBase) = value
"""

    ControlBackColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlBackColour(self: GH_SliderBase) -> Color

Set: ControlBackColour(self: GH_SliderBase) = value
"""

    ControlEdgeColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlEdgeColour(self: GH_SliderBase) -> Color

Set: ControlEdgeColour(self: GH_SliderBase) = value
"""

    ControlShadowColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlShadowColour(self: GH_SliderBase) -> Color

Set: ControlShadowColour(self: GH_SliderBase) = value
"""

    DecimalPlaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimalPlaces(self: GH_SliderBase) -> int

Set: DecimalPlaces(self: GH_SliderBase) = value
"""

    DrawControlBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawControlBackground(self: GH_SliderBase) -> bool

Set: DrawControlBackground(self: GH_SliderBase) = value
"""

    DrawControlBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawControlBorder(self: GH_SliderBase) -> bool

Set: DrawControlBorder(self: GH_SliderBase) = value
"""

    DrawControlShadows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawControlShadows(self: GH_SliderBase) -> bool

Set: DrawControlShadows(self: GH_SliderBase) = value
"""

    Epsilon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsilon(self: GH_SliderBase) -> Decimal

"""

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Font(self: GH_SliderBase) -> Font

Set: Font(self: GH_SliderBase) = value
"""

    FormatMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatMask(self: GH_SliderBase) -> str

Set: FormatMask(self: GH_SliderBase) = value
"""

    Grip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grip(self: GH_SliderBase) -> RectangleF

"""

    GripBottomColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripBottomColour(self: GH_SliderBase) -> Color

Set: GripBottomColour(self: GH_SliderBase) = value
"""

    GripDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripDisplay(self: GH_SliderBase) -> GH_SliderGripDisplay

Set: GripDisplay(self: GH_SliderBase) = value
"""

    GripEdgeColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripEdgeColour(self: GH_SliderBase) -> Color

Set: GripEdgeColour(self: GH_SliderBase) = value
"""

    GripText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripText(self: GH_SliderBase) -> str

"""

    GripTextPure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripTextPure(self: GH_SliderBase) -> str

"""

    GripTopColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripTopColour(self: GH_SliderBase) -> Color

Set: GripTopColour(self: GH_SliderBase) = value
"""

    GripWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripWidth(self: GH_SliderBase) -> int

"""

    Maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Maximum(self: GH_SliderBase) -> Decimal

Set: Maximum(self: GH_SliderBase) = value
"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minimum(self: GH_SliderBase) -> Decimal

Set: Minimum(self: GH_SliderBase) = value
"""

    NormalizedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalizedValue(self: GH_SliderBase) -> float

Set: NormalizedValue(self: GH_SliderBase) = value
"""

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Padding(self: GH_SliderBase) -> Padding

Set: Padding(self: GH_SliderBase) = value
"""

    Rail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rail(self: GH_SliderBase) -> Rectangle

"""

    RailBrightColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailBrightColour(self: GH_SliderBase) -> Color

Set: RailBrightColour(self: GH_SliderBase) = value
"""

    RailDarkColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailDarkColour(self: GH_SliderBase) -> Color

Set: RailDarkColour(self: GH_SliderBase) = value
"""

    RailDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailDisplay(self: GH_SliderBase) -> GH_SliderRailDisplay

Set: RailDisplay(self: GH_SliderBase) = value
"""

    RailEmptyColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailEmptyColour(self: GH_SliderBase) -> Color

Set: RailEmptyColour(self: GH_SliderBase) = value
"""

    RailFullColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailFullColour(self: GH_SliderBase) -> Color

Set: RailFullColour(self: GH_SliderBase) = value
"""

    RaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RaiseEvents(self: GH_SliderBase) -> bool

Set: RaiseEvents(self: GH_SliderBase) = value
"""

    RenderDelegate_Background = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDelegate_Background(self: GH_SliderBase) -> DrawSliderChannel

Set: RenderDelegate_Background(self: GH_SliderBase) = value
"""

    RenderDelegate_Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDelegate_Border(self: GH_SliderBase) -> DrawSliderChannel

Set: RenderDelegate_Border(self: GH_SliderBase) = value
"""

    RenderDelegate_Grip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDelegate_Grip(self: GH_SliderBase) -> DrawSliderChannel

Set: RenderDelegate_Grip(self: GH_SliderBase) = value
"""

    RenderDelegate_Rail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDelegate_Rail(self: GH_SliderBase) -> DrawSliderChannel

Set: RenderDelegate_Rail(self: GH_SliderBase) = value
"""

    RenderDelegate_Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDelegate_Ticks(self: GH_SliderBase) -> DrawSliderChannel

Set: RenderDelegate_Ticks(self: GH_SliderBase) = value
"""

    ShadowSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowSize(self: GH_SliderBase) -> Padding

Set: ShadowSize(self: GH_SliderBase) = value
"""

    SnapDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SnapDistance(self: GH_SliderBase) -> Decimal

Set: SnapDistance(self: GH_SliderBase) = value
"""

    TextColour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextColour(self: GH_SliderBase) -> Color

Set: TextColour(self: GH_SliderBase) = value
"""

    TextInputHandlerDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextInputHandlerDelegate(self: GH_SliderBase) -> TextInputHandler

Set: TextInputHandlerDelegate(self: GH_SliderBase) = value
"""

    TickCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TickCount(self: GH_SliderBase) -> int

Set: TickCount(self: GH_SliderBase) = value
"""

    TickDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TickDisplay(self: GH_SliderBase) -> GH_SliderTickDisplay

Set: TickDisplay(self: GH_SliderBase) = value
"""

    TickFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TickFrequency(self: GH_SliderBase) -> int

Set: TickFrequency(self: GH_SliderBase) = value
"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ticks(self: GH_SliderBase) -> List[int]

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GH_SliderBase) -> GH_SliderAccuracy

Set: Type(self: GH_SliderBase) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_SliderBase) -> Decimal

Set: Value(self: GH_SliderBase) = value
"""

    ValueF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueF(self: GH_SliderBase) -> Single

Set: ValueF(self: GH_SliderBase) = value
"""


    DrawSliderChannel = None
    TextInputHandler = None
    ValueChanged = None
    ValueChangedEventHandler = None


class GH_SliderEventArgs(EventArgs):
    # no doc
    Intermediate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intermediate(self: GH_SliderEventArgs) -> bool

"""

    Slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slider(self: GH_SliderEventArgs) -> GH_SliderBase

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_SliderEventArgs) -> Decimal

"""



class GH_SliderGripDisplay(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_SliderGripDisplay, values: None (0), Numeric (1), Shape (2), ShapeAndText (3) """
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

    None = None
    Numeric = None
    Shape = None
    ShapeAndText = None
    value__ = None


class GH_SliderRailDisplay(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_SliderRailDisplay, values: Etched (2), Filled (3), None (0), Simple (1) """
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

    Etched = None
    Filled = None
    None = None
    Simple = None
    value__ = None


class GH_SliderTickDisplay(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_SliderTickDisplay, values: Etched (2), None (0), Simple (1) """
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

    Etched = None
    None = None
    Simple = None
    value__ = None


class SliderSnapRange(object, IComparable[SliderSnapRange]):
    """
    SliderSnapRange(value: Decimal)
    SliderSnapRange(value0: Decimal, value1: Decimal)
    """
    def CanMerge(self, other):
        """ CanMerge(self: SliderSnapRange, other: SliderSnapRange) -> bool """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: SliderSnapRange, other: SliderSnapRange) -> int """
        pass

    def DistanceTo(self, value):
        """ DistanceTo(self: SliderSnapRange, value: Decimal) -> Decimal """
        pass

    def Merge(self, other):
        """ Merge(self: SliderSnapRange, other: SliderSnapRange) -> SliderSnapRange """
        pass

    def SnapValue(self, value):
        """ SnapValue(self: SliderSnapRange, value: Decimal) -> Decimal """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, value: Decimal)
        __new__(cls: type, value0: Decimal, value1: Decimal)
        __new__[SliderSnapRange]() -> SliderSnapRange
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsSingleton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingleton(self: SliderSnapRange) -> bool

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Max(self: SliderSnapRange) -> Decimal

"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Min(self: SliderSnapRange) -> Decimal

"""




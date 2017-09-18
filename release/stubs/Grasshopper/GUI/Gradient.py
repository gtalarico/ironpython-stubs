# encoding: utf-8
# module Grasshopper.GUI.Gradient calls itself Gradient
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_Gradient(object, GH_ISerializable):
    """
    GH_Gradient()
    GH_Gradient(other: GH_Gradient)
    GH_Gradient(parameters: IEnumerable[float], colours: IEnumerable[Color])
    """
    def AddGrip(self, *__args):
        """
        AddGrip(self: GH_Gradient, t: float, c0: Color, c1: Color) -> GH_Grip
        AddGrip(self: GH_Gradient, grip: GH_Grip)AddGrip(self: GH_Gradient, t: float) -> GH_Grip
        AddGrip(self: GH_Gradient, t: float, c: Color) -> GH_Grip
        """
        pass

    def ColourAt(self, t):
        """ ColourAt(self: GH_Gradient, t: float) -> Color """
        pass

    @staticmethod
    def DeleteGripRegion(destination):
        """ DeleteGripRegion(destination: RectangleF) -> RectangleF """
        pass

    def DisplayGradientEditor(self):
        """ DisplayGradientEditor(self: GH_Gradient) """
        pass

    def DisplayGripColourPicker(self, grip):
        """ DisplayGripColourPicker(self: GH_Gradient, grip: GH_Grip) """
        pass

    @staticmethod
    def EarthlyBrown():
        """ EarthlyBrown() -> GH_Gradient """
        pass

    @staticmethod
    def Forest():
        """ Forest() -> GH_Gradient """
        pass

    @staticmethod
    def GreyScale():
        """ GreyScale() -> GH_Gradient """
        pass

    @staticmethod
    def Heat():
        """ Heat() -> GH_Gradient """
        pass

    def MouseDown(self, dest, pt):
        """ MouseDown(self: GH_Gradient, dest: RectangleF, pt: PointF) -> bool """
        pass

    def MouseDragAbort(self):
        """ MouseDragAbort(self: GH_Gradient) -> bool """
        pass

    def MouseMove(self, dest, pt):
        """ MouseMove(self: GH_Gradient, dest: RectangleF, pt: PointF) -> bool """
        pass

    def MouseUp(self, dest, pt):
        """ MouseUp(self: GH_Gradient, dest: RectangleF, pt: PointF) -> bool """
        pass

    def NearestGrip(self, *__args):
        """
        NearestGrip(self: GH_Gradient, t: float, side: GH_GripSide) -> int
        NearestGrip(self: GH_Gradient, t: float) -> int
        NearestGrip(self: GH_Gradient, dest: RectangleF, pt: PointF, maxRadius: float) -> int
        """
        pass

    @staticmethod
    def NewGripRegion(destination):
        """ NewGripRegion(destination: RectangleF) -> RectangleF """
        pass

    def NormalizeGrips(self):
        """ NormalizeGrips(self: GH_Gradient) """
        pass

    def OnGradientChanged(self):
        """ OnGradientChanged(self: GH_Gradient) """
        pass

    def OnGradientChangedIntermediate(self):
        """ OnGradientChangedIntermediate(self: GH_Gradient) """
        pass

    def OnSelectionChanged(self):
        """ OnSelectionChanged(self: GH_Gradient) """
        pass

    def Read(self, reader):
        """ Read(self: GH_Gradient, reader: GH_IReader) -> bool """
        pass

    def RemoveGrip(self, *__args):
        """ RemoveGrip(self: GH_Gradient, grip: GH_Grip)RemoveGrip(self: GH_Gradient, index: int) """
        pass

    def Render_Background(self, g, dest):
        """ Render_Background(self: GH_Gradient, g: Graphics, dest: RectangleF) """
        pass

    def Render_Gradient(self, g, dest):
        """ Render_Gradient(self: GH_Gradient, g: Graphics, dest: RectangleF) """
        pass

    def Render_Grips(self, g, dest):
        """ Render_Grips(self: GH_Gradient, g: Graphics, dest: RectangleF) """
        pass

    @staticmethod
    def SoGay():
        """ SoGay() -> GH_Gradient """
        pass

    @staticmethod
    def Spectrum():
        """ Spectrum() -> GH_Gradient """
        pass

    @staticmethod
    def Traffic():
        """ Traffic() -> GH_Gradient """
        pass

    def Write(self, writer):
        """ Write(self: GH_Gradient, writer: GH_IWriter) -> bool """
        pass

    @staticmethod
    def Zebra():
        """ Zebra() -> GH_Gradient """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: GH_Gradient)
        __new__(cls: type, parameters: IEnumerable[float], colours: IEnumerable[Color])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    GripCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripCount(self: GH_Gradient) -> int

"""

    Linear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linear(self: GH_Gradient) -> bool

Set: Linear(self: GH_Gradient) = value
"""

    Locked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locked(self: GH_Gradient) -> bool

Set: Locked(self: GH_Gradient) = value
"""

    SelectedGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedGrip(self: GH_Gradient) -> GH_Grip

Set: SelectedGrip(self: GH_Gradient) = value
"""


    GradientChanged = None
    GradientChangedEventHandler = None
    SelectionChanged = None
    SelectionChangedEventHandler = None


class GH_GradientChangedEventArgs(EventArgs):
    """ GH_GradientChangedEventArgs(gradient: GH_Gradient, intermediate: bool) """
    @staticmethod # known case of __new__
    def __new__(self, gradient, intermediate):
        """ __new__(cls: type, gradient: GH_Gradient, intermediate: bool) """
        pass

    Gradient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gradient(self: GH_GradientChangedEventArgs) -> GH_Gradient

"""

    Intermediate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intermediate(self: GH_GradientChangedEventArgs) -> bool

"""



class GH_Grip(object, IComparable[GH_Grip], GH_ISerializable):
    """
    GH_Grip()
    GH_Grip(parameter: float, colour: Color)
    GH_Grip(parameter: float, colourLeft: Color, colourRight: Color)
    GH_Grip(other: GH_Grip)
    """
    @staticmethod
    def Blend(A, B, t):
        """ Blend(A: Color, B: Color, t: float) -> Color """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: GH_Grip, other: GH_Grip) -> int """
        pass

    def MutateId(self):
        """ MutateId(self: GH_Grip) """
        pass

    def Read(self, reader):
        """ Read(self: GH_Grip, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_Grip, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, parameter: float, colour: Color)
        __new__(cls: type, parameter: float, colourLeft: Color, colourRight: Color)
        __new__(cls: type, other: GH_Grip)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColourLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourLeft(self: GH_Grip) -> Color

Set: ColourLeft(self: GH_Grip) = value
"""

    ColourRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourRight(self: GH_Grip) -> Color

Set: ColourRight(self: GH_Grip) = value
"""

    GripId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripId(self: GH_Grip) -> Guid

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Grip) -> bool

"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameter(self: GH_Grip) -> float

Set: Parameter(self: GH_Grip) = value
"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: GH_Grip) -> bool

Set: Selected(self: GH_Grip) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GH_Grip) -> GH_GripType

"""



class GH_GripSide(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_GripSide, values: Both (0), Left (1), Right (2) """
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

    Both = None
    Left = None
    Right = None
    value__ = None


class GH_GripType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_GripType, values: Continuous (0), Discontinuous (1) """
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

    Continuous = None
    Discontinuous = None
    value__ = None



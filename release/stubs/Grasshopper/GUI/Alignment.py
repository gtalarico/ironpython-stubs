# encoding: utf-8
# module Grasshopper.GUI.Alignment calls itself Alignment
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_Align(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Align, values: Bottom (4), Horizontal (6), Left (1), None (0), Right (2), Top (3), Vertical (5) """
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

    Bottom = None
    Horizontal = None
    Left = None
    None = None
    Right = None
    Top = None
    value__ = None
    Vertical = None


class GH_Distribute(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Distribute, values: Horizontal (2), None (0), Vertical (1) """
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

    Horizontal = None
    None = None
    value__ = None
    Vertical = None


class GH_Solver(object):
    """
    GH_Solver()
    GH_Solver(boxes: IEnumerable[RectangleF])
    """
    def AddBox(self, box):
        """ AddBox(self: GH_Solver, box: RectangleF) """
        pass

    @staticmethod
    def Align_Bottom(region, boxes):
        """ Align_Bottom(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Align_Horizontal(region, boxes):
        """ Align_Horizontal(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Align_Left(region, boxes):
        """ Align_Left(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Align_Right(region, boxes):
        """ Align_Right(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Align_Top(region, boxes):
        """ Align_Top(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Align_Vertical(region, boxes):
        """ Align_Vertical(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    def CreateAutoRegion(self):
        """ CreateAutoRegion(self: GH_Solver) """
        pass

    @staticmethod
    def Distribute_Horizontal(region, boxes):
        """ Distribute_Horizontal(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    @staticmethod
    def Distribute_Vertical(region, boxes):
        """ Distribute_Vertical(region: RectangleF, boxes: List[RectangleF]) -> List[RectangleF] """
        pass

    def Inflate(self, x, y):
        """ Inflate(self: GH_Solver, x: Single, y: Single) """
        pass

    def Solve(self, align, distribute):
        """ Solve(self: GH_Solver, align: GH_Align, distribute: GH_Distribute) -> List[RectangleF] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, boxes=None):
        """
        __new__(cls: type)
        __new__(cls: type, boxes: IEnumerable[RectangleF])
        """
        pass

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region(self: GH_Solver) -> RectangleF

Set: Region(self: GH_Solver) = value
"""


    m_boxes = None
    m_region = None



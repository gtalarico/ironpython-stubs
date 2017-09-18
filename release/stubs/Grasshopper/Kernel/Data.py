# encoding: utf-8
# module Grasshopper.Kernel.Data calls itself Data
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_BracketMismatchException(Exception, ISerializable, _Exception):
    """
    GH_BracketMismatchException()
    GH_BracketMismatchException(message: str)
    GH_BracketMismatchException(message: str, location: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, location=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, location: int)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: GH_BracketMismatchException) -> int

"""



class GH_DirtyCaster(object):
    # no doc
    @staticmethod
    def CastToList(in):
        """ CastToList[T](in: object) -> List[T] """
        pass

    @staticmethod
    def CastToTree(in):
        """ CastToTree[T](in: object) -> DataTree[T] """
        pass


class GH_ExpandMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_ExpandMode, values: None (0), Recursive (3), SimpleAppend (2), SimpleReplace (1) """
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
    Recursive = None
    SimpleAppend = None
    SimpleReplace = None
    value__ = None


class GH_GraftMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) GH_GraftMode, values: GraftAll (3), GraftEmptyLists (2), GraftNullItems (1), None (0) """
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

    GraftAll = None
    GraftEmptyLists = None
    GraftNullItems = None
    None = None
    value__ = None


class GH_GraphicBranch(object):
    """ GH_GraphicBranch() """
    def BG_Colour(self, *args): #cannot find CLR method
        """ BG_Colour(self: GH_GraphicBranch) -> Color """
        pass

    def Distribute_Phylogenetic(self, max_path_length_inverse):
        """ Distribute_Phylogenetic(self: GH_GraphicBranch, max_path_length_inverse: float) """
        pass

    def FG_Colour(self, *args): #cannot find CLR method
        """ FG_Colour(self: GH_GraphicBranch) -> Color """
        pass

    def GrowTree(self, paths):
        """ GrowTree(self: GH_GraphicBranch, paths: List[GH_Path]) """
        pass

    def RenderBranchTag(self, *args): #cannot find CLR method
        """ RenderBranchTag(self: GH_GraphicBranch, G: Graphics, anchor: PointF, font: Font, color_fg: Color, color_bg: Color) """
        pass

    def RenderDot(self, *args): #cannot find CLR method
        """ RenderDot(self: GH_GraphicBranch, G: Graphics, center: PointF, radius: Single, colour: Color) """
        pass

    def RenderNodes(self, G, e):
        """ RenderNodes(self: GH_GraphicBranch, G: Graphics, e: GH_GraphicTreeDisplayArgs) """
        pass

    def RenderTags(self, G, e):
        """ RenderTags(self: GH_GraphicBranch, G: Graphics, e: GH_GraphicTreeDisplayArgs) """
        pass

    def RenderTextDot(self, *args): #cannot find CLR method
        """ RenderTextDot(self: GH_GraphicBranch, G: Graphics, pt: Point, text: str, font: Font, size: SizeF, color_bg: Color, color_fg: Color) """
        pass

    def RenderWires_Organic(self, G, e):
        """ RenderWires_Organic(self: GH_GraphicBranch, G: Graphics, e: GH_GraphicTreeDisplayArgs) """
        pass

    def RenderWires_Schematic(self, G, e):
        """ RenderWires_Schematic(self: GH_GraphicBranch, G: Graphics, e: GH_GraphicTreeDisplayArgs) """
        pass

    def SelectAll(self, *__args):
        """ SelectAll(self: GH_GraphicBranch, b_path: GH_Path)SelectAll(self: GH_GraphicBranch, bSelect: bool) """
        pass

    def SolveBezier(self, *args): #cannot find CLR method
        """ SolveBezier(self: GH_GraphicBranch, twig: GH_GraphicBranch, e: GH_GraphicTreeDisplayArgs) -> (PointF, PointF, PointF, PointF) """
        pass

    def SolveLeafAngles(self, angle, spread, angle_per_item, args):
        """ SolveLeafAngles(self: GH_GraphicBranch, angle: Single, spread: Single, angle_per_item: Single, args: GH_GraphicTreeDisplayArgs) """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: GH_GraphicBranch) -> Single

Set: Angle(self: GH_GraphicBranch) = value
"""

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: GH_GraphicBranch) -> IList

Set: Data(self: GH_GraphicBranch) = value
"""

    DataCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataCount(self: GH_GraphicBranch) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: GH_GraphicBranch) -> bool

"""

    IsLeaf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLeaf(self: GH_GraphicBranch) -> bool

"""

    IsRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoot(self: GH_GraphicBranch) -> bool

"""

    IsTrunk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTrunk(self: GH_GraphicBranch) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GH_GraphicBranch) -> Single

Set: Length(self: GH_GraphicBranch) = value
"""

    LongestPathLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongestPathLength(self: GH_GraphicBranch) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: GH_GraphicBranch) -> Single

Set: Offset(self: GH_GraphicBranch) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: GH_GraphicBranch) -> GH_GraphicBranch

Set: Parent(self: GH_GraphicBranch) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: GH_GraphicBranch) -> GH_Path

Set: Path(self: GH_GraphicBranch) = value
"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: GH_GraphicBranch) -> bool

Set: Selected(self: GH_GraphicBranch) = value
"""

    Twigs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Twigs(self: GH_GraphicBranch) -> List[GH_GraphicBranch]

Set: Twigs(self: GH_GraphicBranch) = value
"""


    DomainAngleFactor = None
    m_angle = None
    m_data = None
    m_length = None
    m_offset = None
    m_parent = None
    m_path = None
    m_selected = None
    m_twigs = None
    TwigLengthFactor = None
    TwigLengthMin = None


class GH_GraphicTreeDisplayArgs(object):
    """ GH_GraphicTreeDisplayArgs() """
    def AdjustMaxPathLength(self, potential_new_length):
        """ AdjustMaxPathLength(self: GH_GraphicTreeDisplayArgs, potential_new_length: int) """
        pass

    @staticmethod
    def Distance(A, B, P=None):
        """
        Distance(A: PointF, B: PointF, P: PointF) -> Single
        Distance(A: PointF, B: PointF) -> Single
        """
        pass

    @staticmethod
    def DistanceSquared(A, B):
        """ DistanceSquared(A: PointF, B: PointF) -> Single """
        pass

    def RadialBox(self, box_edge):
        """ RadialBox(self: GH_GraphicTreeDisplayArgs, box_edge: Single) -> RectangleF """
        pass

    def RadialCrd(self, angle, offset):
        """ RadialCrd(self: GH_GraphicTreeDisplayArgs, angle: Single, offset: Single) -> PointF """
        pass

    def RadialX(self, angle, offset):
        """ RadialX(self: GH_GraphicTreeDisplayArgs, angle: Single, offset: Single) -> Single """
        pass

    def RadialY(self, angle, offset):
        """ RadialY(self: GH_GraphicTreeDisplayArgs, angle: Single, offset: Single) -> Single """
        pass

    @staticmethod
    def RadToDeg(a):
        """ RadToDeg(a: Single) -> Single """
        pass

    @staticmethod
    def RemapDegrees(a):
        """ RemapDegrees(a: Single) -> Single """
        pass

    def SetupViewport(self, vport):
        """ SetupViewport(self: GH_GraphicTreeDisplayArgs, vport: GH_Viewport) """
        pass

    def Visible(self, *__args):
        """
        Visible(self: GH_GraphicTreeDisplayArgs, rec: RectangleF, margin: Single) -> bool
        Visible(self: GH_GraphicTreeDisplayArgs, ptA: PointF, ptB: PointF, fuzz: Single) -> bool
        Visible(self: GH_GraphicTreeDisplayArgs, P0: PointF, P1: PointF, P2: PointF, P3: PointF, fuzz: Single) -> bool
        Visible(self: GH_GraphicTreeDisplayArgs, pt: PointF) -> bool
        Visible(self: GH_GraphicTreeDisplayArgs, pt: PointF, radius: Single) -> bool
        Visible(self: GH_GraphicTreeDisplayArgs, rec: RectangleF) -> bool
        """
        pass

    maxPathLength = None
    origin = None
    radius = None
    vp = None


class GH_IndexRange(object, GH_ISerializable):
    """
    GH_IndexRange(index: int)
    GH_IndexRange(index0: int, index1: int)
    """
    def AdjacentTo(self, range):
        """ AdjacentTo(self: GH_IndexRange, range: GH_IndexRange) -> bool """
        pass

    def Contains(self, *__args):
        """
        Contains(self: GH_IndexRange, index: int) -> bool
        Contains(self: GH_IndexRange, range: GH_IndexRange) -> bool
        """
        pass

    @staticmethod
    def Intersection(range0, range1):
        """ Intersection(range0: GH_IndexRange, range1: GH_IndexRange) -> GH_IndexRange """
        pass

    def IntersectsWith(self, range):
        """ IntersectsWith(self: GH_IndexRange, range: GH_IndexRange) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_IndexRange, reader: GH_IReader) -> bool """
        pass

    @staticmethod
    def Split(range, splitter, result0, result1):
        """ Split(range: GH_IndexRange, splitter: GH_IndexRange) -> (int, GH_IndexRange, GH_IndexRange) """
        pass

    def ToString(self):
        """ ToString(self: GH_IndexRange) -> str """
        pass

    @staticmethod
    def Union(range0, range1):
        """ Union(range0: GH_IndexRange, range1: GH_IndexRange) -> GH_IndexRange """
        pass

    def Write(self, writer):
        """ Write(self: GH_IndexRange, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, index: int)
        __new__(cls: type, index0: int, index1: int)
        __new__[GH_IndexRange]() -> GH_IndexRange
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Index0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index0(self: GH_IndexRange) -> int

"""

    Index1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index1(self: GH_IndexRange) -> int

"""

    IsSingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingular(self: GH_IndexRange) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_IndexRange) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GH_IndexRange) -> int

"""


    InvalidRange = None
    MaxValue = None


class GH_IndexRanges(object, GH_ISerializable):
    """ GH_IndexRanges() """
    def InsertRange(self, range):
        """ InsertRange(self: GH_IndexRanges, range: GH_IndexRange) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_IndexRanges, reader: GH_IReader) -> bool """
        pass

    def RemoveRange(self, range):
        """ RemoveRange(self: GH_IndexRanges, range: GH_IndexRange) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_IndexRanges) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_IndexRanges, writer: GH_IWriter) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GH_IndexRanges) -> int

"""



class GH_IndexRuleSet(object):
    """ GH_IndexRuleSet() """
    def AddAnyDigitRule(self):
        """ AddAnyDigitRule(self: GH_IndexRuleSet) """
        pass

    def AddAnyDigitsRule(self):
        """ AddAnyDigitsRule(self: GH_IndexRuleSet) """
        pass

    def AddDigitPatternRule(self, *__args):
        """ AddDigitPatternRule(self: GH_IndexRuleSet, pattern: Array[int])AddDigitPatternRule(self: GH_IndexRuleSet, firstDigit: int, nextDigit: int, lastDigit: int)AddDigitPatternRule(self: GH_IndexRuleSet, firstDigit: int, nextDigit: int) """
        pass

    def AddDigitRule(self, digit, invert):
        """ AddDigitRule(self: GH_IndexRuleSet, digit: int, invert: bool) """
        pass

    def AddRangePatternRule(self, pattern):
        """ AddRangePatternRule(self: GH_IndexRuleSet, pattern: Array[GH_IndexRange]) """
        pass

    def AddRangeRule(self, range, invert):
        """ AddRangeRule(self: GH_IndexRuleSet, range: GH_IndexRange, invert: bool) """
        pass

    def Evaluate(self, index):
        """ Evaluate(self: GH_IndexRuleSet, index: int) -> GH_RuleResult """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GH_IndexRuleSet) -> int

"""



class GH_Lexer(object):
    """
    GH_Lexer()
    GH_Lexer(M: str)
    """
    def EvaluatePath(self, evaluator, path, index):
        """ EvaluatePath(self: GH_Lexer, evaluator: GH_ExpressionParser, path: GH_Path, index: int) -> (bool, GH_Path, int) """
        pass

    @staticmethod
    def PerformLexicalReplace(source, target, *__args):
        """ PerformLexicalReplace[T](source: GH_Lexer, target: GH_Lexer, tree_in: DataTree[T], tree_out: DataTree[T])PerformLexicalReplace[T](source: GH_Lexer, target: GH_Lexer, structure_in: IGH_Structure, structure_out: GH_Structure[T]) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, M=None):
        """
        __new__(cls: type)
        __new__(cls: type, M: str)
        """
        pass

    IsItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsItem(self: GH_Lexer) -> bool

"""

    IsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPath(self: GH_Lexer) -> bool

"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: GH_Lexer) -> str

"""

    Mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mask(self: GH_Lexer) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: GH_Lexer) -> List[str]

"""



class GH_LexerCombo(object):
    """
    GH_LexerCombo()
    GH_LexerCombo(n_source: GH_Lexer, n_target: GH_Lexer)
    GH_LexerCombo(n_source: str, n_target: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, n_source=None, n_target=None):
        """
        __new__(cls: type)
        __new__(cls: type, n_source: GH_Lexer, n_target: GH_Lexer)
        __new__(cls: type, n_source: str, n_target: str)
        """
        pass

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: GH_LexerCombo) -> GH_Lexer

Set: Source(self: GH_LexerCombo) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: GH_LexerCombo) -> GH_Lexer

Set: Target(self: GH_LexerCombo) = value
"""



class GH_Path(object, IComparable[GH_Path], IComparer[GH_Path], GH_ISerializable):
    """
    GH_Path()
    GH_Path(index: int)
    GH_Path(*args: Array[int])
    GH_Path(Other: GH_Path)
    """
    def AppendElement(self, index):
        """ AppendElement(self: GH_Path, index: int) -> GH_Path """
        pass

    def Compare(self, x, y):
        """ Compare(self: GH_Path, x: GH_Path, y: GH_Path) -> int """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: GH_Path, other: GH_Path) -> int """
        pass

    def CullElement(self):
        """ CullElement(self: GH_Path) -> GH_Path """
        pass

    def CullFirstElement(self):
        """ CullFirstElement(self: GH_Path) -> GH_Path """
        pass

    def Format(self, format_provider, separator):
        """ Format(self: GH_Path, format_provider: str, separator: str) -> str """
        pass

    def FromString(self, s):
        """ FromString(self: GH_Path, s: str) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GH_Path) -> int """
        pass

    def Increment(self, index, offset=None):
        """
        Increment(self: GH_Path, index: int, offset: int) -> GH_Path
        Increment(self: GH_Path, index: int) -> GH_Path
        """
        pass

    def IsAncestor(self, potential_ancestor, additional_generations):
        """ IsAncestor(self: GH_Path, potential_ancestor: GH_Path, additional_generations: int) -> (bool, int) """
        pass

    def IsCoincident(self, *__args):
        """
        IsCoincident(self: GH_Path, *index_list: Array[int]) -> bool
        IsCoincident(self: GH_Path, other: GH_Path) -> bool
        """
        pass

    def PrependElement(self, index):
        """ PrependElement(self: GH_Path, index: int) -> GH_Path """
        pass

    def Read(self, reader):
        """ Read(self: GH_Path, reader: GH_IReader) -> bool """
        pass

    @staticmethod
    def SplitPathLikeString(s, path_segments, index_segment):
        """ SplitPathLikeString(s: str) -> (bool, Array[str], str) """
        pass

    def ToString(self, includeBrackets=None):
        """
        ToString(self: GH_Path, includeBrackets: bool) -> str
        ToString(self: GH_Path) -> str
        """
        pass

    def Write(self, writer):
        """ Write(self: GH_Path, writer: GH_IWriter) -> bool """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, index: int)
        __new__(cls: type, *args: Array[int])
        __new__(cls: type, Other: GH_Path)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DebuggerDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebuggerDisplay(self: GH_Path) -> str

"""

    Indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Indices(self: GH_Path) -> Array[int]

Set: Indices(self: GH_Path) = value
"""

    InternalPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalPath(self: GH_Path) -> Array[int]

Set: InternalPath(self: GH_Path) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GH_Path) -> int

"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valid(self: GH_Path) -> bool

"""


    PathLengthComparer = None


class GH_PathOffset(object):
    """
    GH_PathOffset()
    GH_PathOffset(pathShift: IEnumerable[int])
    GH_PathOffset(pathShift: IEnumerable[int], itemShift: int)
    GH_PathOffset(pathShift: IEnumerable[int], itemShift: int, pathWrap: bool, itemWrap: bool)
    """
    def OffsetPath(self, path, index, *__args):
        """
        OffsetPath(self: GH_PathOffset, path: GH_Path, index: int, tree: IGH_Structure) -> (bool, GH_Path, int)
        OffsetPath(self: GH_PathOffset, path: GH_Path, index: int, rel_path: GH_Path, rel_index: int) -> (bool, GH_Path, int)
        """
        pass

    @staticmethod
    def ParseString(mask):
        """ ParseString(mask: str) -> GH_PathOffset """
        pass

    def ToString(self):
        """ ToString(self: GH_PathOffset) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pathShift=None, itemShift=None, pathWrap=None, itemWrap=None):
        """
        __new__(cls: type)
        __new__(cls: type, pathShift: IEnumerable[int])
        __new__(cls: type, pathShift: IEnumerable[int], itemShift: int)
        __new__(cls: type, pathShift: IEnumerable[int], itemShift: int, pathWrap: bool, itemWrap: bool)
        """
        pass

    ItemOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemOffset(self: GH_PathOffset) -> int

Set: ItemOffset(self: GH_PathOffset) = value
"""

    ItemWrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemWrap(self: GH_PathOffset) -> bool

Set: ItemWrap(self: GH_PathOffset) = value
"""

    PathOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathOffset(self: GH_PathOffset) -> List[int]

"""

    PathWrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathWrap(self: GH_PathOffset) -> bool

Set: PathWrap(self: GH_PathOffset) = value
"""



class GH_RuleAnyNumber(object, IGH_Rule):
    """ GH_RuleAnyNumber() """
    def Apply(self, number):
        """ Apply(self: GH_RuleAnyNumber, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleAnyNumber) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleAnyNumber) -> str

"""



class GH_RuleAnyNumbers(object, IGH_Rule):
    """ GH_RuleAnyNumbers() """
    def Apply(self, number):
        """ Apply(self: GH_RuleAnyNumbers, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleAnyNumbers) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleAnyNumbers) -> str

"""



class GH_RuleComplex(object, IGH_Rule):
    """ GH_RuleComplex(fragments: IEnumerable[IGH_Rule], operators: IEnumerable[GH_RuleOperator]) """
    def Apply(self, number):
        """ Apply(self: GH_RuleComplex, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fragments, operators):
        """ __new__(cls: type, fragments: IEnumerable[IGH_Rule], operators: IEnumerable[GH_RuleOperator]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleComplex) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleComplex) -> str

"""



class GH_RuleGroup(object, IGH_Rule):
    """ GH_RuleGroup(numbers: IEnumerable[int], negate: bool) """
    def Apply(self, number):
        """ Apply(self: GH_RuleGroup, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, numbers, negate):
        """ __new__(cls: type, numbers: IEnumerable[int], negate: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleGroup) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleGroup) -> str

"""



class GH_RuleKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_RuleKind, values: AnyNumber (1), AnyNumbers (2), Complex (7), Group (4), None (0), Number (3), Range (5), Sequence (6) """
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

    AnyNumber = None
    AnyNumbers = None
    Complex = None
    Group = None
    None = None
    Number = None
    Range = None
    Sequence = None
    value__ = None


class GH_RuleNumber(object, IGH_Rule):
    """ GH_RuleNumber(number: int, negate: bool) """
    def Apply(self, number):
        """ Apply(self: GH_RuleNumber, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, number, negate):
        """ __new__(cls: type, number: int, negate: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleNumber) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleNumber) -> str

"""



class GH_RuleOperator(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_RuleOperator, values: Conjunction (0), Disjunction (1) """
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

    Conjunction = None
    Disjunction = None
    value__ = None


class GH_RuleRange(object, IGH_Rule):
    """ GH_RuleRange(min: int, max: int, negate: bool) """
    def Apply(self, number):
        """ Apply(self: GH_RuleRange, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, min, max, negate):
        """ __new__(cls: type, min: int, max: int, negate: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleRange) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleRange) -> str

"""



class GH_RuleResult(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_RuleResult, values: Exclude (-1), Include (1), NoOpinion (0) """
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

    Exclude = None
    Include = None
    NoOpinion = None
    value__ = None


class GH_RuleSequence(object, IGH_Rule):
    """ GH_RuleSequence(sequence: IEnumerable[int], limit: int, negate: bool) """
    def Apply(self, number):
        """ Apply(self: GH_RuleSequence, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sequence, limit, negate):
        """ __new__(cls: type, sequence: IEnumerable[int], limit: int, negate: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: GH_RuleSequence) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: GH_RuleSequence) -> str

"""



class GH_SimplificationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_SimplificationMode, values: CollapseAllOverlaps (2), CollapseLeadingOverlaps (1), None (0) """
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

    CollapseAllOverlaps = None
    CollapseLeadingOverlaps = None
    None = None
    value__ = None


class GH_StringMismatchException(Exception, ISerializable, _Exception):
    """
    GH_StringMismatchException()
    GH_StringMismatchException(message: str)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class GH_Structure(object, IGH_Structure, IEnumerable[T], IEnumerable, GH_ISerializable):
    """
    GH_Structure[T]()
    GH_Structure[T](other: GH_Structure[T], shallowCopy: bool)
    """
    def AllData(self, skipNulls):
        """ AllData(self: GH_Structure[T], skipNulls: bool) -> IGH_StructureEnumerator """
        pass

    def Append(self, data, path=None):
        """ Append(self: GH_Structure[T], data: T, path: GH_Path)Append(self: GH_Structure[T], data: T) """
        pass

    def AppendRange(self, data, path=None):
        """ AppendRange(self: GH_Structure[T], data: IEnumerable[T], path: GH_Path)AppendRange(self: GH_Structure[T], data: IEnumerable[T]) """
        pass

    def Clear(self):
        """ Clear(self: GH_Structure[T]) """
        pass

    def ClearData(self):
        """ ClearData(self: GH_Structure[T]) """
        pass

    def DataDescription(self, includeIndices, includePaths):
        """ DataDescription(self: GH_Structure[T], includeIndices: bool, includePaths: bool) -> str """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Structure[T]) -> GH_Structure[T] """
        pass

    def DuplicateCast(self, conversion):
        """ DuplicateCast[Q](self: GH_Structure[T], conversion: ConversionDelegate[T, T, Q]) -> GH_Structure[Q] """
        pass

    def EnsureCapacity(self, capacity):
        """ EnsureCapacity(self: GH_Structure[T], capacity: int) """
        pass

    def EnsurePath(self, path):
        """
        EnsurePath(self: GH_Structure[T], path: GH_Path) -> List[T]
        EnsurePath(self: GH_Structure[T], *path: Array[int]) -> List[T]
        """
        pass

    def ExpandPath(self, path, element, mode):
        """ ExpandPath(self: GH_Structure[T], path: GH_Path, element: int, mode: GH_ExpandMode) """
        pass

    def Flatten(self, flat_path):
        """ Flatten(self: GH_Structure[T], flat_path: GH_Path) """
        pass

    def FlattenData(self):
        """ FlattenData(self: GH_Structure[T]) -> List[T] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GH_Structure[T]) -> IEnumerator """
        pass

    def GetEnumerator_Generic(self):
        """ GetEnumerator_Generic(self: GH_Structure[T]) -> IEnumerator[T] """
        pass

    def Graft(self, *__args):
        """ Graft(self: GH_Structure[T], mode: GH_GraftMode)Graft(self: GH_Structure[T], mode: GH_GraftMode, path: GH_Path)Graft(self: GH_Structure[T], clearSingleNulls: bool)Graft(self: GH_Structure[T], path: GH_Path, clearSingleNulls: bool) """
        pass

    def Insert(self, data, path, index):
        """ Insert(self: GH_Structure[T], data: T, path: GH_Path, index: int) """
        pass

    def LongestPathIndex(self):
        """ LongestPathIndex(self: GH_Structure[T]) -> int """
        pass

    def MergeStructure(self, other):
        """ MergeStructure(self: GH_Structure[T], other: GH_Structure[T]) """
        pass

    def PathExists(self, path):
        """ PathExists(self: GH_Structure[T], path: GH_Path) -> bool """
        pass

    def PathIndex(self, path, idx0, idx1):
        """ PathIndex(self: GH_Structure[T], path: GH_Path, idx0: int, idx1: int) -> (int, int) """
        pass

    def Read(self, reader):
        """ Read(self: GH_Structure[T], reader: GH_IReader) -> bool """
        pass

    def RemoveData(self, data):
        """ RemoveData(self: GH_Structure[T], data: T) """
        pass

    def RemovePath(self, path):
        """ RemovePath(self: GH_Structure[T], path: GH_Path) """
        pass

    def ReplacePath(self, find, replace):
        """ ReplacePath(self: GH_Structure[T], find: GH_Path, replace: GH_Path) """
        pass

    def Reverse(self):
        """ Reverse(self: GH_Structure[T]) """
        pass

    def ShallowDuplicate(self):
        """ ShallowDuplicate(self: GH_Structure[T]) -> GH_Structure[T] """
        pass

    def ShortestPathIndex(self):
        """ ShortestPathIndex(self: GH_Structure[T]) -> int """
        pass

    def Simplify(self, mode):
        """ Simplify(self: GH_Structure[T], mode: GH_SimplificationMode) """
        pass

    def ToString(self):
        """ ToString(self: GH_Structure[T]) -> str """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: GH_Structure[T]) """
        pass

    def Write(self, writer):
        """ Write(self: GH_Structure[T], writer: GH_IWriter) -> bool """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None, shallowCopy=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GH_Structure[T], shallowCopy: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Branches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Branches(self: GH_Structure[T]) -> IList[List[T]]

"""

    DataCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataCount(self: GH_Structure[T]) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: GH_Structure[T]) -> bool

"""

    NonNulls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonNulls(self: GH_Structure[T]) -> IEnumerable[T]

"""

    PathCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathCount(self: GH_Structure[T]) -> int

"""

    Paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paths(self: GH_Structure[T]) -> IList[GH_Path]

"""

    StructureProxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProxy(self: GH_Structure[T]) -> IList[IList]

"""

    TopologyDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyDescription(self: GH_Structure[T]) -> str

"""


    ConversionDelegate`2 = None


class GH_TreeBuilder(object):
    """ GH_TreeBuilder() """
    def AddPath(self, p):
        """ AddPath(self: GH_TreeBuilder, p: GH_Path) """
        pass

    def AddPathRecursive(self, p):
        """ AddPathRecursive(self: GH_TreeBuilder, p: GH_Path) """
        pass

    AllPaths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllPaths(self: GH_TreeBuilder) -> List[GH_Path]

"""


    m_set = None


class GH_TreeFilter(object):
    """ GH_TreeFilter() """
    @staticmethod
    def FindItemBrackets(text, index0, index1):
        """ FindItemBrackets(text: str) -> (bool, int, int) """
        pass

    @staticmethod
    def FindNextLevelChar(text, index, char):
        """ FindNextLevelChar(text: str, index: int, char: Char) -> int """
        pass

    @staticmethod
    def FindPathBrackets(text, index0, index1):
        """ FindPathBrackets(text: str) -> (bool, int, int) """
        pass

    @staticmethod
    def FindPrevLevelChar(text, index, char):
        """ FindPrevLevelChar(text: str, index: int, char: Char) -> int """
        pass

    @staticmethod
    def ParsePattern(filter):
        """ ParsePattern(filter: str) -> GH_TreeFilter """
        pass

    @staticmethod
    def SplitStringWithExpressions(text, separator):
        """ SplitStringWithExpressions(text: str, separator: Char) -> List[str] """
        pass

    ItemClose = None
    ItemOpen = None
    PathClose = None
    PathOpen = None
    PathSeparator = None
    SegmentSeparator = None
    StringDelimeter = None


class GH_TreeIndex(object):
    """ GH_TreeIndex(path: GH_Path, item: int) """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path, item):
        """
        __new__(cls: type, path: GH_Path, item: int)
        __new__[GH_TreeIndex]() -> GH_TreeIndex
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: GH_TreeIndex) -> int

Set: Item(self: GH_TreeIndex) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: GH_TreeIndex) -> GH_Path

Set: Path(self: GH_TreeIndex) = value
"""



class GH_TreeRules(object):
    """ GH_TreeRules(pathRules: IEnumerable[IGH_Rule], indexRule: IGH_Rule) """
    def Apply(self, path, index=None):
        """
        Apply(self: GH_TreeRules, path: GH_Path) -> bool
        Apply(self: GH_TreeRules, path: GH_Path, index: int) -> bool
        """
        pass

    @staticmethod
    def FromString(text, message):
        """ FromString(text: str, message: str) -> (GH_TreeRules, str) """
        pass

    def ToString(self):
        """ ToString(self: GH_TreeRules) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pathRules, indexRule):
        """ __new__(cls: type, pathRules: IEnumerable[IGH_Rule], indexRule: IGH_Rule) """
        pass

    HasItemRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasItemRule(self: GH_TreeRules) -> bool

"""

    HasPathRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPathRules(self: GH_TreeRules) -> bool

"""

    PathRuleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathRuleCount(self: GH_TreeRules) -> int

"""


    AllowedChars = '0123456789-|~&!,.;?*{}[]()<>='
    AndOperator = None
    AnyNumbersSymbol = None
    AnyNumberSymbol = None
    ItemBrackets = '[ ]'
    ItemCloseBracket = None
    ItemOpenBracket = None
    NotOperator = None
    OrOperator = None
    PathBrackets = '{ }'
    PathCloseBracket = None
    PathOpenBracket = None
    PathSeparator = None
    RangeSymbol = None
    RuleBrackets = '( )'
    RuleCloseBracket = None
    RuleOpenBracket = None
    Separator = None
    SequenceCode = '...'
    SequenceSymbol = None


class IGH_DataTree:
    # no doc
    def MergeWithParameter(self, param):
        """ MergeWithParameter(self: IGH_DataTree, param: IGH_Param) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGH_IndexRule:
    # no doc
    def Evaluate(self, index):
        """ Evaluate(self: IGH_IndexRule, index: int) -> GH_RuleResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGH_Rule:
    # no doc
    def Apply(self, number):
        """ Apply(self: IGH_Rule, number: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: IGH_Rule) -> GH_RuleKind

"""

    Notation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notation(self: IGH_Rule) -> str

"""



class IGH_Structure:
    # no doc
    def AllData(self, skipNulls):
        """ AllData(self: IGH_Structure, skipNulls: bool) -> IGH_StructureEnumerator """
        pass

    def Clear(self):
        """ Clear(self: IGH_Structure) """
        pass

    def ClearData(self):
        """ ClearData(self: IGH_Structure) """
        pass

    def DataDescription(self, includeIndices, includePaths):
        """ DataDescription(self: IGH_Structure, includeIndices: bool, includePaths: bool) -> str """
        pass

    def EnsureCapacity(self, capacity):
        """ EnsureCapacity(self: IGH_Structure, capacity: int) """
        pass

    def ExpandPath(self, path, element, mode):
        """ ExpandPath(self: IGH_Structure, path: GH_Path, element: int, mode: GH_ExpandMode) """
        pass

    def Flatten(self, path):
        """ Flatten(self: IGH_Structure, path: GH_Path) """
        pass

    def Graft(self, *__args):
        """ Graft(self: IGH_Structure, mode: GH_GraftMode)Graft(self: IGH_Structure, mode: GH_GraftMode, path: GH_Path)Graft(self: IGH_Structure, clearSingleNulls: bool)Graft(self: IGH_Structure, path: GH_Path, clearSingleNulls: bool) """
        pass

    def LongestPathIndex(self):
        """ LongestPathIndex(self: IGH_Structure) -> int """
        pass

    def PathExists(self, path):
        """ PathExists(self: IGH_Structure, path: GH_Path) -> bool """
        pass

    def PathIndex(self, path, idx0, idx1):
        """ PathIndex(self: IGH_Structure, path: GH_Path, idx0: int, idx1: int) -> (int, int) """
        pass

    def RemovePath(self, path):
        """ RemovePath(self: IGH_Structure, path: GH_Path) """
        pass

    def ReplacePath(self, find, replace):
        """ ReplacePath(self: IGH_Structure, find: GH_Path, replace: GH_Path) """
        pass

    def ShortestPathIndex(self):
        """ ShortestPathIndex(self: IGH_Structure) -> int """
        pass

    def Simplify(self, mode):
        """ Simplify(self: IGH_Structure, mode: GH_SimplificationMode) """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: IGH_Structure) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataCount(self: IGH_Structure) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: IGH_Structure) -> bool

"""

    PathCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathCount(self: IGH_Structure) -> int

"""

    Paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paths(self: IGH_Structure) -> IList[GH_Path]

"""

    StructureProxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProxy(self: IGH_Structure) -> IList[IList]

"""

    TopologyDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyDescription(self: IGH_Structure) -> str

"""



class IGH_StructureEnumerator(IEnumerable[IGH_Goo], IEnumerable):
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IGH_Goo](enumerable: IEnumerable[IGH_Goo], value: IGH_Goo) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass



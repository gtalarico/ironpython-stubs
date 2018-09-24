# encoding: utf-8
# module DSCore
# from DSCoreNodes, Version=2.0.1.5055, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Color(object):
    # no doc
    @staticmethod
    def Add(c1, c2):
        """ Add(c1: Color, c2: Color) -> Color """
        pass

    @staticmethod
    def Blerp(colors, parameter):
        """ Blerp(colors: IList[IndexedColor2D], parameter: UV) -> Color """
        pass

    @staticmethod
    def Brightness(c):
        """ Brightness(c: Color) -> Single """
        pass

    @staticmethod
    def BuildColorFrom1DRange(colors, parameters, parameter):
        """ BuildColorFrom1DRange(colors: List[Color], parameters: List[float], parameter: float) -> Color """
        pass

    @staticmethod
    def BuildColorFrom2DRange(colors, parameters, parameter):
        """ BuildColorFrom2DRange(colors: IList[Color], parameters: IList[UV], parameter: UV) -> Color """
        pass

    @staticmethod
    def ByARGB(a, r, g, b):
        """ ByARGB(a: int, r: int, g: int, b: int) -> Color """
        pass

    @staticmethod
    def Components(c):
        """ Components(c: Color) -> Dictionary[str, Byte] """
        pass

    @staticmethod
    def Divide(c1, div):
        """ Divide(c1: Color, div: float) -> Color """
        pass

    def Equals(self, obj):
        """ Equals(self: Color, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Color) -> int """
        pass

    @staticmethod
    def Hue(c):
        """ Hue(c: Color) -> Single """
        pass

    @staticmethod
    def Lerp(start, end, t):
        """ Lerp(start: Color, end: Color, t: float) -> Color """
        pass

    @staticmethod
    def Multiply(c1, div):
        """ Multiply(c1: Color, div: float) -> Color """
        pass

    @staticmethod
    def Saturation(c):
        """ Saturation(c: Color) -> Single """
        pass

    def ToString(self):
        """ ToString(self: Color) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(c1: Color, c2: Color) -> Color """
        pass

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alpha(self: Color) -> Byte

"""

    Blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blue(self: Color) -> Byte

"""

    Green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Green(self: Color) -> Byte

"""

    Red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Red(self: Color) -> Byte

"""


    IndexedColor1D = None
    IndexedColor2D = None


class ColorRange(object):
    # no doc
    @staticmethod
    def ByColorsAndParameters(colors, parameters):
        """ ByColorsAndParameters(colors: IList[Color], parameters: IList[UV]) -> ColorRange """
        pass

    def GetColorAtParameter(self, parameter):
        """ GetColorAtParameter(self: ColorRange, parameter: UV) -> Color """
        pass


class ColorRange1D(object):
    # no doc
    @staticmethod
    def ByColorsAndParameters(colors, parameters):
        """ ByColorsAndParameters(colors: List[Color], parameters: List[float]) -> ColorRange1D """
        pass

    @staticmethod
    def Default():
        """ Default() -> ColorRange1D """
        pass

    @staticmethod
    def GetColorAtParameter(colorRange, parameter):
        """ GetColorAtParameter(colorRange: ColorRange1D, parameter: float) -> Color """
        pass

    def ToString(self):
        """ ToString(self: ColorRange1D) -> str """
        pass

    IndexedColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndexedColors(self: ColorRange1D) -> IEnumerable[IndexedColor1D]

"""



class Compare(object):
    # no doc
    @staticmethod
    def GreaterThan(a, b):
        """ GreaterThan(a: object, b: object) -> bool """
        pass

    @staticmethod
    def GreaterThanOrEqual(a, b):
        """ GreaterThanOrEqual(a: object, b: object) -> bool """
        pass

    @staticmethod
    def LessThan(a, b):
        """ LessThan(a: object, b: object) -> bool """
        pass

    @staticmethod
    def LessThanOrEqual(a, b):
        """ LessThanOrEqual(a: object, b: object) -> bool """
        pass

    __all__ = [
        'GreaterThan',
        'GreaterThanOrEqual',
        'LessThan',
        'LessThanOrEqual',
    ]


class DateTime(object):
    # no doc
    @staticmethod
    def AddTimeSpan(dateTime, timeSpan):
        """ AddTimeSpan(dateTime: DateTime, timeSpan: TimeSpan) -> DateTime """
        pass

    @staticmethod
    def ByDate(year, month, day):
        """ ByDate(year: int, month: int, day: int) -> DateTime """
        pass

    @staticmethod
    def ByDateAndTime(year, month, day, hour, minute, second, millisecond):
        """ ByDateAndTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> DateTime """
        pass

    @staticmethod
    def Components(dateTime):
        """ Components(dateTime: DateTime) -> Dictionary[str, int] """
        pass

    @staticmethod
    def Date(dateTime):
        """ Date(dateTime: DateTime) -> DateTime """
        pass

    @staticmethod
    def DayOfWeek(dateTime):
        """ DayOfWeek(dateTime: DateTime) -> DayOfWeek """
        pass

    @staticmethod
    def DayOfYear(dateTime):
        """ DayOfYear(dateTime: DateTime) -> int """
        pass

    @staticmethod
    def DaysInMonth(year, month):
        """ DaysInMonth(year: int, month: int) -> int """
        pass

    @staticmethod
    def Format(dateTime, format):
        """ Format(dateTime: DateTime, format: str) -> str """
        pass

    @staticmethod
    def FromString(str):
        """ FromString(str: str) -> DateTime """
        pass

    @staticmethod
    def IsDaylightSavingsTime(dateTime):
        """ IsDaylightSavingsTime(dateTime: DateTime) -> bool """
        pass

    @staticmethod
    def IsLeapYear(year):
        """ IsLeapYear(year: int) -> bool """
        pass

    @staticmethod
    def SubtractTimeSpan(dateTime, timeSpan):
        """ SubtractTimeSpan(dateTime: DateTime, timeSpan: TimeSpan) -> DateTime """
        pass

    @staticmethod
    def TimeOfDay(dateTime):
        """ TimeOfDay(dateTime: DateTime) -> TimeSpan """
        pass

    MaxValue = None
    MinValue = None
    Now = None
    Today = None
    __all__ = [
        'AddTimeSpan',
        'ByDate',
        'ByDateAndTime',
        'Components',
        'Date',
        'DayOfWeek',
        'DayOfYear',
        'DaysInMonth',
        'Format',
        'FromString',
        'IsDaylightSavingsTime',
        'IsLeapYear',
        'SubtractTimeSpan',
        'TimeOfDay',
    ]


class DayOfWeek(Enum):
    """ enum DayOfWeek, values: Friday (5), Monday (1), Saturday (6), Sunday (0), Thursday (4), Tuesday (2), Wednesday (3) """
    Friday = None
    Monday = None
    Saturday = None
    Sunday = None
    Thursday = None
    Tuesday = None
    value__ = None
    Wednesday = None


class DefaultColorRanges(object):
    # no doc
    Analysis = None
    __all__ = [
        'Analysis',
    ]


class List(object):
    # no doc
    @staticmethod
    def AddItemToEnd(item, list):
        """ AddItemToEnd(item: object, list: IList) -> IList """
        pass

    @staticmethod
    def AddItemToFront(item, list):
        """ AddItemToFront(item: object, list: IList) -> IList """
        pass

    @staticmethod
    def AllFalse(list):
        """ AllFalse(list: IList) -> bool """
        pass

    @staticmethod
    def AllIndicesOf(list, item):
        """ AllIndicesOf(list: IList, item: object) -> IList """
        pass

    @staticmethod
    def AllTrue(list):
        """ AllTrue(list: IList) -> bool """
        pass

    @staticmethod
    def Chop(list, lengths):
        """ Chop(list: IList, lengths: List[int]) -> IList """
        pass

    @staticmethod
    def Clean(list, preserveIndices):
        """ Clean(list: IList, preserveIndices: bool) -> IList """
        pass

    @staticmethod
    def Combinations(list, length, replace):
        """ Combinations(list: IList, length: int, replace: bool) -> IList """
        pass

    @staticmethod
    def Contains(list, item):
        """ Contains(list: IList, item: object) -> bool """
        pass

    @staticmethod
    def Count(list):
        """ Count(list: IList) -> int """
        pass

    @staticmethod
    def CountFalse(list):
        """ CountFalse(list: IList) -> int """
        pass

    @staticmethod
    def CountTrue(list):
        """ CountTrue(list: IList) -> int """
        pass

    @staticmethod
    def Cycle(list, amount):
        """ Cycle(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def Deconstruct(list):
        """ Deconstruct(list: IList) -> IDictionary """
        pass

    @staticmethod
    def DiagonalLeft(list, rowLength):
        """ DiagonalLeft(list: IList, rowLength: int) -> IList """
        pass

    @staticmethod
    def DiagonalRight(list, subLength):
        """ DiagonalRight(list: IList, subLength: int) -> IList """
        pass

    @staticmethod
    def DropEveryNthItem(list, n, offset):
        """ DropEveryNthItem(list: IList, n: int, offset: int) -> IList """
        pass

    @staticmethod
    def DropItems(list, amount):
        """ DropItems(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def FilterByBoolMask(list, mask):
        """ FilterByBoolMask(list: IList, mask: IList) -> Dictionary[str, object] """
        pass

    @staticmethod
    def FirstIndexOf(list, item):
        """ FirstIndexOf(list: IList, item: object) -> int """
        pass

    @staticmethod
    def FirstItem(list):
        """ FirstItem(list: IList) -> object """
        pass

    @staticmethod
    def Flatten(list, amt):
        """ Flatten(list: IList, amt: int) -> IList """
        pass

    @staticmethod
    def GetItemAtIndex(list, index):
        """ GetItemAtIndex(list: IList, index: int) -> object """
        pass

    @staticmethod
    def GroupByKey(list, keys):
        """ GroupByKey(list: IList, keys: IList) -> IDictionary """
        pass

    @staticmethod
    def IndexOf(list, element):
        """ IndexOf(list: IList, element: object) -> int """
        pass

    @staticmethod
    def Insert(list, element, index):
        """ Insert(list: IList, element: object, index: int) -> IList """
        pass

    @staticmethod
    def IsEmpty(list):
        """ IsEmpty(list: IList) -> bool """
        pass

    @staticmethod
    def IsHomogeneous(list):
        """ IsHomogeneous(list: IList) -> bool """
        pass

    @staticmethod
    def IsRectangular(list):
        """ IsRectangular(list: IList) -> bool """
        pass

    @staticmethod
    def IsUniformDepth(list):
        """ IsUniformDepth(list: IList) -> bool """
        pass

    @staticmethod
    def Join(lists):
        """ Join(*lists: Array[IList]) -> IList """
        pass

    @staticmethod
    def LastItem(list):
        """ LastItem(list: IList) -> object """
        pass

    @staticmethod
    def MaximumItem(list):
        """ MaximumItem(list: IEnumerable[object]) -> object """
        pass

    @staticmethod
    def MinimumItem(list):
        """ MinimumItem(list: IEnumerable[object]) -> object """
        pass

    @staticmethod
    def NormalizeDepth(list, rank):
        """ NormalizeDepth(list: IList, rank: int) -> IList """
        pass

    @staticmethod
    def OfRepeatedItem(item, amount):
        """ OfRepeatedItem(item: object, amount: int) -> IList """
        pass

    @staticmethod
    def Permutations(list, length):
        """ Permutations(list: IList, length: Nullable[int]) -> IList """
        pass

    @staticmethod
    def RemoveItemAtIndex(list, indices):
        """ RemoveItemAtIndex(list: IList, indices: Array[int]) -> IList """
        pass

    @staticmethod
    def Reorder(list, indices):
        """ Reorder(list: IList, indices: IList) -> IList """
        pass

    @staticmethod
    def Repeat(list, amount):
        """ Repeat(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def ReplaceItemAtIndex(list, index, item):
        """ ReplaceItemAtIndex(list: IList, index: int, item: object) -> IList """
        pass

    @staticmethod
    def RestOfItems(list):
        """ RestOfItems(list: IList) -> IList """
        pass

    @staticmethod
    def Reverse(list):
        """ Reverse(list: IList) -> IList """
        pass

    @staticmethod
    def SetDifference(list1, list2):
        """ SetDifference(list1: IList[object], list2: IList[object]) -> IList """
        pass

    @staticmethod
    def SetIntersection(list1, list2):
        """ SetIntersection(list1: IList[object], list2: IList[object]) -> IList """
        pass

    @staticmethod
    def SetUnion(list1, list2):
        """ SetUnion(list1: IList[object], list2: IList[object]) -> IList """
        pass

    @staticmethod
    def ShiftIndices(list, amount):
        """ ShiftIndices(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def Shuffle(list):
        """ Shuffle(list: IList) -> IList """
        pass

    @staticmethod
    def Slice(list, start, end, step):
        """ Slice(list: IList, start: Nullable[int], end: Nullable[int], step: int) -> IList """
        pass

    @staticmethod
    def Sort(list):
        """ Sort(list: IEnumerable[object]) -> IList """
        pass

    @staticmethod
    def SortByKey(list, keys):
        """ SortByKey(list: IList, keys: IList) -> IDictionary """
        pass

    @staticmethod
    def SortIndexByValue(list):
        """ SortIndexByValue(list: List[float]) -> IEnumerable """
        pass

    @staticmethod
    def Sublists(list, ranges, offset):
        """ Sublists(list: IList, ranges: IList, offset: int) -> IList """
        pass

    @staticmethod
    def TakeEveryNthItem(list, n, offset):
        """ TakeEveryNthItem(list: IList, n: int, offset: int) -> IList """
        pass

    @staticmethod
    def TakeItems(list, amount):
        """ TakeItems(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def Transpose(lists):
        """ Transpose(lists: IList) -> IList """
        pass

    @staticmethod
    def UniqueItems(list):
        """ UniqueItems(list: IList) -> IList """
        pass

    @staticmethod
    def __Create(items):
        """ __Create(items: IList) -> IList """
        pass

    Empty = None
    __all__ = [
        '__Create',
        'AddItemToEnd',
        'AddItemToFront',
        'AllFalse',
        'AllIndicesOf',
        'AllTrue',
        'Chop',
        'Clean',
        'Combinations',
        'Contains',
        'Count',
        'CountFalse',
        'CountTrue',
        'Cycle',
        'Deconstruct',
        'DiagonalLeft',
        'DiagonalRight',
        'DropEveryNthItem',
        'DropItems',
        'FilterByBoolMask',
        'FirstIndexOf',
        'FirstItem',
        'Flatten',
        'GetItemAtIndex',
        'GroupByKey',
        'IndexOf',
        'Insert',
        'IsEmpty',
        'IsHomogeneous',
        'IsRectangular',
        'IsUniformDepth',
        'Join',
        'LastItem',
        'MaximumItem',
        'MinimumItem',
        'NormalizeDepth',
        'OfRepeatedItem',
        'Permutations',
        'RemoveItemAtIndex',
        'Reorder',
        'Repeat',
        'ReplaceItemAtIndex',
        'RestOfItems',
        'Reverse',
        'SetDifference',
        'SetIntersection',
        'SetUnion',
        'ShiftIndices',
        'Shuffle',
        'Slice',
        'Sort',
        'SortByKey',
        'SortIndexByValue',
        'Sublists',
        'TakeEveryNthItem',
        'TakeItems',
        'Transpose',
        'UniqueItems',
    ]


class Math(object):
    # no doc
    @staticmethod
    def Abs(*__args):
        """
        Abs(integer: Int64) -> Int64
        Abs(number: float) -> float
        """
        pass

    @staticmethod
    def Acos(ratio):
        """ Acos(ratio: float) -> float """
        pass

    @staticmethod
    def Asin(ratio):
        """ Asin(ratio: float) -> float """
        pass

    @staticmethod
    def Atan(ratio):
        """ Atan(ratio: float) -> float """
        pass

    @staticmethod
    def Atan2(numerator, denominator):
        """ Atan2(numerator: float, denominator: float) -> float """
        pass

    @staticmethod
    def Average(numbers):
        """ Average(numbers: IList[float]) -> float """
        pass

    @staticmethod
    def Ceiling(number):
        """ Ceiling(number: float) -> Int64 """
        pass

    @staticmethod
    def Cos(angle):
        """ Cos(angle: float) -> float """
        pass

    @staticmethod
    def Cosh(angle):
        """ Cosh(angle: float) -> float """
        pass

    @staticmethod
    def DegreesToRadians(degrees):
        """ DegreesToRadians(degrees: float) -> float """
        pass

    @staticmethod
    def DivRem(dividend, divisor):
        """ DivRem(dividend: Int64, divisor: Int64) -> Int64 """
        pass

    @staticmethod
    def EvaluateFormula(formulaString, parameters, args):
        """ EvaluateFormula(formulaString: str, parameters: Array[str], args: Array[object]) -> object """
        pass

    @staticmethod
    def Exp(number):
        """ Exp(number: float) -> float """
        pass

    @staticmethod
    def Factorial(number):
        """ Factorial(number: Int64) -> Int64 """
        pass

    @staticmethod
    def Floor(number):
        """ Floor(number: float) -> Int64 """
        pass

    @staticmethod
    def IEEERemainder(value1, value2):
        """ IEEERemainder(value1: float, value2: float) -> float """
        pass

    @staticmethod
    def Log(number, logBase=None):
        """
        Log(number: float, logBase: float) -> float
        Log(number: float) -> float
        """
        pass

    @staticmethod
    def Log10(number):
        """ Log10(number: float) -> float """
        pass

    @staticmethod
    def Map(rangeMin, rangeMax, inputValue):
        """ Map(rangeMin: float, rangeMax: float, inputValue: float) -> float """
        pass

    @staticmethod
    def MapTo(rangeMin, rangeMax, inputValue, targetRangeMin, targetRangeMax):
        """ MapTo(rangeMin: float, rangeMax: float, inputValue: float, targetRangeMin: float, targetRangeMax: float) -> float """
        pass

    @staticmethod
    def Max(*__args):
        """
        Max(int1: Int64, int2: Int64) -> Int64
        Max(value1: float, value2: float) -> float
        """
        pass

    @staticmethod
    def Min(*__args):
        """
        Min(int1: Int64, int2: Int64) -> Int64
        Min(value1: float, value2: float) -> float
        """
        pass

    @staticmethod
    def Pow(number, power):
        """ Pow(number: float, power: float) -> float """
        pass

    @staticmethod
    def RadiansToDegrees(radians):
        """ RadiansToDegrees(radians: float) -> float """
        pass

    @staticmethod
    def Rand():
        """ Rand() -> float """
        pass

    @staticmethod
    def Random(*__args):
        """
        Random(value1: float, value2: float) -> float
        Random(seed: Nullable[int]) -> float
        """
        pass

    @staticmethod
    def RandomList(amount):
        """ RandomList(amount: int) -> IList """
        pass

    @staticmethod
    def RemapRange(numbers, newMin, newMax):
        """ RemapRange(numbers: IList[float], newMin: float, newMax: float) -> IList """
        pass

    @staticmethod
    def Round(number, digits=None):
        """
        Round(number: float, digits: int) -> float
        Round(number: float) -> float
        """
        pass

    @staticmethod
    def Sign(*__args):
        """
        Sign(integer: Int64) -> Int64
        Sign(number: float) -> Int64
        """
        pass

    @staticmethod
    def Sin(angle):
        """ Sin(angle: float) -> float """
        pass

    @staticmethod
    def Sinh(angle):
        """ Sinh(angle: float) -> float """
        pass

    @staticmethod
    def Sqrt(number):
        """ Sqrt(number: float) -> float """
        pass

    @staticmethod
    def Sum(values):
        """ Sum(values: IEnumerable[float]) -> float """
        pass

    @staticmethod
    def Tan(angle):
        """ Tan(angle: float) -> float """
        pass

    @staticmethod
    def Tanh(angle):
        """ Tanh(angle: float) -> float """
        pass

    @staticmethod
    def Truncate(value):
        """ Truncate(value: float) -> float """
        pass

    @staticmethod
    def Xor(a, b):
        """ Xor(a: bool, b: bool) -> bool """
        pass

    E = 2.718281828459045
    GoldenRatio = 1.61803398875
    PI = 3.141592653589793
    PiTimes2 = 6.283185307179586
    __all__ = [
        'Abs',
        'Acos',
        'Asin',
        'Atan',
        'Atan2',
        'Average',
        'Ceiling',
        'Cos',
        'Cosh',
        'DegreesToRadians',
        'DivRem',
        'EvaluateFormula',
        'Exp',
        'Factorial',
        'Floor',
        'IEEERemainder',
        'Log',
        'Log10',
        'Map',
        'MapTo',
        'Max',
        'Min',
        'Pow',
        'RadiansToDegrees',
        'Rand',
        'Random',
        'RandomList',
        'RemapRange',
        'Round',
        'Sign',
        'Sin',
        'Sinh',
        'Sqrt',
        'Sum',
        'Tan',
        'Tanh',
        'Truncate',
        'Xor',
    ]


class Node(object):
    """ Node(min: UV, max: UV) """
    def Contains(self, uv):
        """ Contains(self: Node, uv: UV) -> bool """
        pass

    def FindAllNodesUpLevel(self, count):
        """ FindAllNodesUpLevel(self: Node, count: int) -> List[Node] """
        pass

    def FindNodesIntersectingRectangle(self, rectangle):
        """ FindNodesIntersectingRectangle(self: Node, rectangle: UVRect) -> List[Node] """
        pass

    def FindNodesWithinRadius(self, location, radius):
        """ FindNodesWithinRadius(self: Node, location: UV, radius: float) -> List[Node] """
        pass

    def FindNodeWhichContains(self, point):
        """ FindNodeWhichContains(self: Node, point: UV) -> Node """
        pass

    def GetAllNodes(self):
        """ GetAllNodes(self: Node) -> List[Node] """
        pass

    def Insert(self, uv):
        """ Insert(self: Node, uv: UV) """
        pass

    def TryFind(self, uv, node):
        """ TryFind(self: Node, uv: UV) -> (bool, Node) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, min, max):
        """ __new__(cls: type, min: UV, max: UV) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: Node) -> UVRect

Set: Bounds(self: Node) = value
"""

    IsLeafNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLeafNode(self: Node) -> bool

"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: Node) -> object

Set: Item(self: Node) = value
"""

    NE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NE(self: Node) -> Node

"""

    NW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NW(self: Node) -> Node

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: Node) -> Node

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Node) -> UV

Set: Point(self: Node) = value
"""

    SE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SE(self: Node) -> Node

"""

    SW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SW(self: Node) -> Node

"""



class Object(object):
    # no doc
    @staticmethod
    def Identity(obj):
        """ Identity(obj: object) -> object """
        pass

    @staticmethod
    def IsNull(obj):
        """ IsNull(obj: object) -> bool """
        pass

    @staticmethod
    def Type(obj):
        """ Type(obj: object) -> str """
        pass

    __all__ = [
        'Identity',
        'IsNull',
        'Type',
    ]


class Quadtree(object):
    # no doc
    @staticmethod
    def ByUVs(uvs):
        """ ByUVs(uvs: IEnumerable[UV]) -> Quadtree """
        pass

    def FindPointsInRectangle(self, rectangle):
        """ FindPointsInRectangle(self: Quadtree, rectangle: UVRect) -> List[UV] """
        pass

    def FindPointsWithinRadius(self, center, radius):
        """ FindPointsWithinRadius(self: Quadtree, center: UV, radius: float) -> List[UV] """
        pass

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Root(self: Quadtree) -> Node

Set: Root(self: Quadtree) = value
"""



class Sorting(object):
    # no doc
    @staticmethod
    def groupByKey(list, keys):
        """ groupByKey(list: IList, keys: IList) -> IList """
        pass

    @staticmethod
    def maxByKey(list, keys):
        """ maxByKey(list: IList, keys: IList) -> object """
        pass

    @staticmethod
    def minByKey(list, keys):
        """ minByKey(list: IList, keys: IList) -> object """
        pass

    @staticmethod
    def sortByKey(list, keys):
        """ sortByKey(list: IList, keys: IList) -> IList """
        pass

    __all__ = [
        'groupByKey',
        'maxByKey',
        'minByKey',
        'sortByKey',
    ]


class String(object):
    # no doc
    @staticmethod
    def AllIndicesOf(str, searchFor, ignoreCase):
        """ AllIndicesOf(str: str, searchFor: str, ignoreCase: bool) -> Array[int] """
        pass

    @staticmethod
    def Center(str, newWidth, padChars):
        """ Center(str: str, newWidth: int, padChars: str) -> str """
        pass

    @staticmethod
    def ChangeCase(str, upper):
        """ ChangeCase(str: str, upper: bool) -> str """
        pass

    @staticmethod
    def Concat(strings):
        """ Concat(*strings: Array[str]) -> str """
        pass

    @staticmethod
    def Contains(str, searchFor, ignoreCase):
        """ Contains(str: str, searchFor: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def CountOccurrences(str, searchFor, ignoreCase):
        """ CountOccurrences(str: str, searchFor: str, ignoreCase: bool) -> int """
        pass

    @staticmethod
    def EndsWith(str, searchFor, ignoreCase):
        """ EndsWith(str: str, searchFor: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def FromObject(obj):
        """ FromObject(obj: object) -> str """
        pass

    @staticmethod
    def IndexOf(str, searchFor, ignoreCase):
        """ IndexOf(str: str, searchFor: str, ignoreCase: bool) -> int """
        pass

    @staticmethod
    def Insert(str, index, toInsert):
        """ Insert(str: str, index: int, toInsert: str) -> str """
        pass

    @staticmethod
    def Join(separator, strings):
        """ Join(separator: str, *strings: Array[str]) -> str """
        pass

    @staticmethod
    def LastIndexOf(str, searchFor, ignoreCase):
        """ LastIndexOf(str: str, searchFor: str, ignoreCase: bool) -> int """
        pass

    @staticmethod
    def Length(str):
        """ Length(str: str) -> int """
        pass

    @staticmethod
    def PadLeft(str, newWidth, padChars):
        """ PadLeft(str: str, newWidth: int, padChars: str) -> str """
        pass

    @staticmethod
    def PadRight(str, newWidth, padChars):
        """ PadRight(str: str, newWidth: int, padChars: str) -> str """
        pass

    @staticmethod
    def Remove(str, startIndex, count):
        """ Remove(str: str, startIndex: int, count: Nullable[int]) -> str """
        pass

    @staticmethod
    def Replace(str, searchFor, replaceWith):
        """ Replace(str: str, searchFor: str, replaceWith: str) -> str """
        pass

    @staticmethod
    def Split(str, separaters):
        """ Split(str: str, *separaters: Array[str]) -> Array[str] """
        pass

    @staticmethod
    def StartsWith(str, searchFor, ignoreCase):
        """ StartsWith(str: str, searchFor: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def Substring(str, startIndex, length):
        """ Substring(str: str, startIndex: int, length: int) -> str """
        pass

    @staticmethod
    def ToLower(str):
        """ ToLower(str: str) -> str """
        pass

    @staticmethod
    def ToNumber(str):
        """ ToNumber(str: str) -> object """
        pass

    @staticmethod
    def ToUpper(str):
        """ ToUpper(str: str) -> str """
        pass

    @staticmethod
    def TrimLeadingWhitespace(str):
        """ TrimLeadingWhitespace(str: str) -> str """
        pass

    @staticmethod
    def TrimTrailingWhitespace(str):
        """ TrimTrailingWhitespace(str: str) -> str """
        pass

    @staticmethod
    def TrimWhitespace(str):
        """ TrimWhitespace(str: str) -> str """
        pass

    __all__ = [
        'AllIndicesOf',
        'Center',
        'ChangeCase',
        'Concat',
        'Contains',
        'CountOccurrences',
        'EndsWith',
        'FromObject',
        'IndexOf',
        'Insert',
        'Join',
        'LastIndexOf',
        'Length',
        'PadLeft',
        'PadRight',
        'Remove',
        'Replace',
        'Split',
        'StartsWith',
        'Substring',
        'ToLower',
        'ToNumber',
        'ToUpper',
        'TrimLeadingWhitespace',
        'TrimTrailingWhitespace',
        'TrimWhitespace',
    ]


class Thread(object):
    # no doc
    @staticmethod
    def Pause(x, msTimeout):
        """ Pause(x: object, msTimeout: int) -> object """
        pass

    __all__ = [
        'Pause',
    ]


class TimeSpan(object):
    # no doc
    @staticmethod
    def Add(timeSpan1, timeSpan2):
        """ Add(timeSpan1: TimeSpan, timeSpan2: TimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def ByDateDifference(date1, date2):
        """ ByDateDifference(date1: DateTime, date2: DateTime) -> TimeSpan """
        pass

    @staticmethod
    def Components(timeSpan):
        """ Components(timeSpan: TimeSpan) -> Dictionary[str, int] """
        pass

    @staticmethod
    def Create(days, hours, minutes, seconds, milliseconds):
        """ Create(days: float, hours: float, minutes: float, seconds: float, milliseconds: float) -> TimeSpan """
        pass

    @staticmethod
    def FromString(str):
        """ FromString(str: str) -> TimeSpan """
        pass

    @staticmethod
    def Negate(timeSpan):
        """ Negate(timeSpan: TimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def Scale(timeSpan, scaleFactor):
        """ Scale(timeSpan: TimeSpan, scaleFactor: float) -> TimeSpan """
        pass

    @staticmethod
    def Subtract(timeSpan1, timeSpan2):
        """ Subtract(timeSpan1: TimeSpan, timeSpan2: TimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def TotalDays(timeSpan):
        """ TotalDays(timeSpan: TimeSpan) -> float """
        pass

    @staticmethod
    def TotalHours(timeSpan):
        """ TotalHours(timeSpan: TimeSpan) -> float """
        pass

    @staticmethod
    def TotalMilliseconds(timeSpan):
        """ TotalMilliseconds(timeSpan: TimeSpan) -> float """
        pass

    @staticmethod
    def TotalMinutes(timeSpan):
        """ TotalMinutes(timeSpan: TimeSpan) -> float """
        pass

    @staticmethod
    def TotalSeconds(timeSpan):
        """ TotalSeconds(timeSpan: TimeSpan) -> float """
        pass

    MaxValue = None
    MinValue = None
    Zero = None
    __all__ = [
        'Add',
        'ByDateDifference',
        'Components',
        'Create',
        'FromString',
        'Negate',
        'Scale',
        'Subtract',
        'TotalDays',
        'TotalHours',
        'TotalMilliseconds',
        'TotalMinutes',
        'TotalSeconds',
    ]


class Types(object):
    """ Types() """
    @staticmethod
    def FindTypeByNameInAssembly(typeName, assemblyName):
        """ FindTypeByNameInAssembly(typeName: str, assemblyName: str) -> Type """
        pass


class UVRect(object):
    """ UVRect(min: UV, max: UV) """
    def Contains(self, uv):
        """ Contains(self: UVRect, uv: UV) -> bool """
        pass

    def Intersects(self, rect):
        """ Intersects(self: UVRect, rect: UVRect) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, min, max):
        """ __new__(cls: type, min: UV, max: UV) """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: UVRect) -> UV

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: UVRect) -> float

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Max(self: UVRect) -> UV

Set: Max(self: UVRect) = value
"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Min(self: UVRect) -> UV

Set: Min(self: UVRect) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: UVRect) -> float

"""



class Web(object):
    """ Web() """
    @staticmethod
    def WebRequestByUrl(url):
        """ WebRequestByUrl(url: str) -> str """
        pass


# variables with complex values


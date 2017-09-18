# encoding: utf-8
# module DSCore
# from DSCoreNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
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
        """
        Brightness(c: Color) -> Single
        
            Returns the brightness value for this color.
            Returns: double between 0 and 1 inclusive.
        """
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
        """
        ByARGB(a: int, r: int, g: int, b: int) -> Color
        
            Construct a color by alpha, red, green, and blue components.
        
            a: The alpha value.
            r: The red value.
            g: The green value.
            b: The blue value.
            Returns: Color.
        """
        pass

    @staticmethod
    def Components(c):
        """
        Components(c: Color) -> Dictionary[str, Byte]
        
            Lists the components for the color in the order: alpha, red, green, blue.
            Returns: Saturation value for the color.
        """
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
        """
        Hue(c: Color) -> Single
        
            Returns the hue value for this color.
            Returns: double between 0 and 1 inclusive.
        """
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
        """
        Saturation(c: Color) -> Single
        
            Returns the saturation value for this color.
            Returns: double between 0 and 1 inclusive.
        """
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
    """Find the alpha component of a color, 0 to 255.

Get: Alpha(self: Color) -> Byte

"""

    Blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Find the blue component of a color, 0 to 255.

Get: Blue(self: Color) -> Byte

"""

    Green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Find the green component of a color, 0 to 255.

Get: Green(self: Color) -> Byte

"""

    Red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Find the red component of a color, 0 to 255.

Get: Red(self: Color) -> Byte

"""


    IndexedColor1D = None
    IndexedColor2D = None


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



class ColorRange2D(object):
    # no doc
    @staticmethod
    def ByColorsAndParameters(colors, parameters):
        """ ByColorsAndParameters(colors: IList[Color], parameters: IList[UV]) -> ColorRange2D """
        pass

    def GetColorAtParameter(self, parameter):
        """
        GetColorAtParameter(self: ColorRange2D, parameter: UV) -> Color
        
            Returns the color in this color range at the specified parameter.
        
            parameter: A UV between (0.0,0.0) and (1.0,1.0).
            Returns: A Color.
        """
        pass


class Compare(object):
    """ Comparison methods. """
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
    """ Object representing a specific Date and Time. """
    @staticmethod
    def AddTimeSpan(dateTime, timeSpan):
        """
        AddTimeSpan(dateTime: DateTime, timeSpan: TimeSpan) -> DateTime
        
            Adds a TimeSpan to a DateTime, yielding a new DateTime.
        
            dateTime: Starting DateTime.
            timeSpan: Amount of time to add.
            Returns: DateTime
        """
        pass

    @staticmethod
    def ByDate(year, month, day):
        """
        ByDate(year: int, month: int, day: int) -> DateTime
        
            Creates a new DateTime at an exact date.
        
            year: Exact year (1-9999)
            month: Exact month (1-12)
            day: Exact day (1-[days in month])
            Returns: DateTime
        """
        pass

    @staticmethod
    def ByDateAndTime(year, month, day, hour, minute, second, millisecond):
        """
        ByDateAndTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> DateTime
        
            Creates a new DateTime at an exact date and time.
        
            year: Exact year (1-9999)
            month: Exact month (1-12)
            day: Exact day (1-[days in month])
            hour: Exact hour (0-23)
            minute: Exact minute (0-59)
            second: Exact second (0-59)
            millisecond: Exact millisecond (0-999)
            Returns: DateTime
        """
        pass

    @staticmethod
    def Components(dateTime):
        """
        Components(dateTime: DateTime) -> Dictionary[str, int]
        
            Extracts the individual components of a DateTime.
        
            dateTime: A DateTime.
        """
        pass

    @staticmethod
    def Date(dateTime):
        """
        Date(dateTime: DateTime) -> DateTime
        
            Extracts only the date from a DateTime. Time components are set to 0.
        
            dateTime: A DateTime.
        """
        pass

    @staticmethod
    def DayOfWeek(dateTime):
        """
        DayOfWeek(dateTime: DateTime) -> DayOfWeek
        
            Returns the Day of the Week from a given DateTime.
        
            dateTime: A DateTime object.
            Returns: Day of the week
        """
        pass

    @staticmethod
    def DayOfYear(dateTime):
        """
        DayOfYear(dateTime: DateTime) -> int
        
            Returns the day of the year (0-366)
        
            dateTime: A DateTime.
        """
        pass

    @staticmethod
    def DaysInMonth(year, month):
        """
        DaysInMonth(year: int, month: int) -> int
        
            Calculates how many days are in the given month of the given year.
        
            year: Exact year (1-9999)
            month: Exact month (1-12)
        """
        pass

    @staticmethod
    def FromString(str):
        """
        FromString(str: str) -> DateTime
        
            Attempts to parse a DateTime from a string.
        
            str: String representation of a DateTime.
            Returns: DateTime
        """
        pass

    @staticmethod
    def IsDaylightSavingsTime(dateTime):
        """
        IsDaylightSavingsTime(dateTime: DateTime) -> bool
        
            Determines if it is Daylight Savings Time at the given DateTime.
        
            dateTime: A DateTime.
        """
        pass

    @staticmethod
    def IsLeapYear(year):
        """
        IsLeapYear(year: int) -> bool
        
            Determines if the given year is a leap year.
        
            year: Exact year (1-9999)
        """
        pass

    @staticmethod
    def SubtractTimeSpan(dateTime, timeSpan):
        """
        SubtractTimeSpan(dateTime: DateTime, timeSpan: TimeSpan) -> DateTime
        
            Subtracts a TimeSpan from a DateTime, yielding a new DateTime.
        
            dateTime: Starting DateTime.
            timeSpan: Amount of time to subtract.
            Returns: DateTime
        """
        pass

    @staticmethod
    def TimeOfDay(dateTime):
        """
        TimeOfDay(dateTime: DateTime) -> TimeSpan
        
            Yields a new TimeSpan representing the amount of time passed since midnight of the
                     
                given DateTime.
        
        
            dateTime: A DateTime.
        """
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
        'FromString',
        'IsDaylightSavingsTime',
        'IsLeapYear',
        'SubtractTimeSpan',
        'TimeOfDay',
    ]


class DayOfWeek(Enum, IComparable, IFormattable, IConvertible):
    """
    Days of the Week
    
    enum DayOfWeek, values: Friday (5), Monday (1), Saturday (6), Sunday (0), Thursday (4), Tuesday (2), Wednesday (3)
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


class Formula(object):
    """ Backend implementation for Formula node. """
    @staticmethod
    def Evaluate(formulaString, parameters, args):
        """
        Evaluate(formulaString: str, parameters: Array[str], args: Array[object]) -> object
        
            Evaluates an NCalc formula with given parameter mappings.
        
            formulaString: NCalc formula
            parameters: Variable names
            args: Variable bindings
            Returns: Result of the formula calculation.
        """
        pass

    __all__ = [
        'Evaluate',
    ]


class List(object):
    """ Methods for creating and manipulating Lists. """
    @staticmethod
    def AddItemToEnd(item, list):
        """
        AddItemToEnd(item: object, list: IList) -> IList
        
            Adds an item to the end of a list.
        
            item: Item to be added.Item could be an object or a list.
            list: List to add on to.
        """
        pass

    @staticmethod
    def AddItemToFront(item, list):
        """
        AddItemToFront(item: object, list: IList) -> IList
        
            Adds an item to the beginning of a list.
        
            item: Item to be added. Item could be an object or a list.
            list: List to add on to.
            Returns: New list.
        """
        pass

    @staticmethod
    def AllIndicesOf(list, item):
        """
        AllIndicesOf(list: IList, item: object) -> IList
        
            Given an item, returns the zero-based indices of all its occurrences
                        in the 
             list. If the item cannot be found, an empty list is returned.
        
        
            list: List to search in. If this argument is null, an empty list is returned.
            item: Item to look for.
            Returns: A list of zero-based indices of all occurrences of the item if 
                    found, or an empty 
             list if the item does not exist in the list.
        """
        pass

    @staticmethod
    def Chop(list, lengths):
        """ Chop(list: IList, lengths: List[int]) -> IList """
        pass

    @staticmethod
    def Clean(list, preserveIndices):
        """
        Clean(list: IList, preserveIndices: bool) -> IList
        
            Cleans data of nulls and empty lists from a given list of arbitrary dimension
        
            preserveIndices: Provide an option to preserve the indices of the data
                    such that non-trailing nulls 
             may not be filtered out
        
            Returns: A list cleaned of nulls and empty lists
        """
        pass

    @staticmethod
    def Combinations(list, length, replace):
        """
        Combinations(list: IList, length: int, replace: bool) -> IList
        
            Produces all combinations of the given length of a given list.
        
            list: List to generate combinations of.
            length: Length of each combination.
            replace: Whether or not items are removed once selected for combination, defaults
                        to 
             false.
        
            Returns: Combinations of the list of the given length.
        """
        pass

    @staticmethod
    def ContainsItem(list, item):
        """
        ContainsItem(list: IList, item: object) -> bool
        
            Determines if the given list contains the given item.
        
            list: List to search in.
            item: Item to look for.
            Returns: Whether list contains the given item.
        """
        pass

    @staticmethod
    def Count(list):
        """
        Count(list: IList) -> int
        
            Returns the number of items stored in the given list.
        
            list: List to get the item count of.
            Returns: List length.
        """
        pass

    @staticmethod
    def Cycle(list, amount):
        """
        Cycle(list: IList, amount: int) -> IList
        
            Creates a new list by concatenining copies of a given list.
        
            list: List to repeat.
            amount: Number of times to repeat.
            Returns: List of repeated lists.
        """
        pass

    @staticmethod
    def Deconstruct(list):
        """
        Deconstruct(list: IList) -> IDictionary
        
            Given a list, produces the first item in the list, and a new list containing all items
                 
                    except the first.
        
        
            list: List to be split.
            Returns: Rest of the list.
        """
        pass

    @staticmethod
    def DiagonalLeft(list, rowLength):
        """
        DiagonalLeft(list: IList, rowLength: int) -> IList
        
            List elements along each diagonal in the matrix from the top right to the lower left.
        
            list: A flat list.
            rowLength: Length of each new sib-list.
            Returns: Lists of elements along matrix diagonals.
        """
        pass

    @staticmethod
    def DiagonalRight(list, subLength):
        """
        DiagonalRight(list: IList, subLength: int) -> IList
        
            List elements along each diagonal in the matrix from the top left to the lower right.
        
            list: A flat list
            subLength: Length of each new sub-list.
            Returns: Lists of elements along matrix diagonals.
        """
        pass

    @staticmethod
    def DropEveryNthItem(list, n, offset):
        """
        DropEveryNthItem(list: IList, n: int, offset: int) -> IList
        
            Removes items from the given list at indices that are multiples
                        of the given 
             value, after the given offset.
        
        
            list: List to remove items from/
            n: Indices that are multiples of this argument will be removed.
            offset: Amount of items to be ignored from the start of the list.
            Returns: List with items removed.
        """
        pass

    @staticmethod
    def DropItems(list, amount):
        """
        DropItems(list: IList, amount: int) -> IList
        
            Removes an amount of items from the start of the list. If the amount is a negative value,
              
                       items are removed from the end of the list.
        
        
            list: List to remove items from.
            amount: Amount of items to remove. If negative, items are removed from the end of the list.
            Returns: List of remaining items.
        """
        pass

    @staticmethod
    def FilterByBoolMask(list, mask):
        """
        FilterByBoolMask(list: IList, mask: IList) -> Dictionary[str, object]
        
            Filters a sequence by lookng up corresponding indices in a separate list of
                        
             booleans.
        
        
            list: List to filter.
            mask: List of booleans representing a mask.
            Returns: Items whose mask index is false.
        """
        pass

    @staticmethod
    def FirstIndexOf(list, item):
        """
        FirstIndexOf(list: IList, item: object) -> int
        
            Given an item, returns the zero-based index of its first occurrence 
                        in the 
             list. If the item cannot be found in the list, -1 is returned.
        
        
            list: List to search in. If this argument is null, -1 is returned.
            item: Item to look for.
            Returns: Zero-based index of the item in the list, or -1 if it is not found.
        """
        pass

    @staticmethod
    def FirstItem(list):
        """
        FirstItem(list: IList) -> object
        
            Returns the first item in a list.
        
            list: List to get the first item from.
            Returns: First item in the list.
        """
        pass

    @staticmethod
    def Flatten(list, amt):
        """
        Flatten(list: IList, amt: int) -> IList
        
            Flattens a nested list of lists by a certain amount.
        
            list: List to flatten.
            amt: Layers of nesting to remove.
        """
        pass

    @staticmethod
    def GetItemAtIndex(list, index):
        """
        GetItemAtIndex(list: IList, index: int) -> object
        
            Returns an item from the given list that's located at the specified index.
        
            list: List to fetch an item from.
            index: Index of the item to be fetched.
            Returns: Item in the list at the given index.
        """
        pass

    @staticmethod
    def GroupByKey(list, keys):
        """
        GroupByKey(list: IList, keys: IList) -> IDictionary
        
            Group items into sub-lists based on their like key values
        
            list: List of items to group as sublists
            keys: Key values, one per item in the input list, used for grouping the items
            Returns: key value corresponding to each group
        """
        pass

    @staticmethod
    def IsEmpty(list):
        """
        IsEmpty(list: IList) -> bool
        
            Determines if the given list is empty.
        
            list: List to check for items.
            Returns: Whether the list is empty.
        """
        pass

    @staticmethod
    def Join(lists):
        """
        Join(*lists: Array[IList]) -> IList
        
            Concatenates all given lists into a single list.
        
            lists: Lists to join into one.
            Returns: Joined list.
        """
        pass

    @staticmethod
    def LastItem(list):
        """
        LastItem(list: IList) -> object
        
            Retrieves the last item in a list.
        
            list: List to get the last item of.
            Returns: Last item in the list.
        """
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
    def OfRepeatedItem(item, amount):
        """
        OfRepeatedItem(item: object, amount: int) -> IList
        
            Creates a list containing the given item the given number of times.
        
            item: The item to repeat.
            amount: The number of times to repeat.
            Returns: List of repeated items.
        """
        pass

    @staticmethod
    def Permutations(list, length):
        """ Permutations(list: IList, length: Nullable[int]) -> IList """
        pass

    @staticmethod
    def RemoveItemAtIndex(list, indices):
        """
        RemoveItemAtIndex(list: IList, indices: Array[int]) -> IList
        
            Removes an item from the given list at the specified index.
        
            list: List to remove an item or items from.
            indices: Index or indices of the item(s) to be removed.
            Returns: List with items removed.
        """
        pass

    @staticmethod
    def Repeat(list, amount):
        """ Repeat(list: IList, amount: int) -> IList """
        pass

    @staticmethod
    def ReplaceItemAtIndex(list, index, item):
        """
        ReplaceItemAtIndex(list: IList, index: int, item: object) -> IList
        
            Replace an item from the given list that's located at the specified index.
        
            list: List to replace an item in.
            index: Index of the item to be replaced.
            item: The item to insert.
            Returns: A new list with the item replaced.
        """
        pass

    @staticmethod
    def RestOfItems(list):
        """
        RestOfItems(list: IList) -> IList
        
            Removes the first item from the given list.
        
            list: List to get the rest of.
            Returns: Rest of the list.
        """
        pass

    @staticmethod
    def Reverse(list):
        """
        Reverse(list: IList) -> IList
        
            Creates a new list containing the items of the given list but in reverse order.
        
            list: List to be reversed.
            Returns: New list.
        """
        pass

    @staticmethod
    def ShiftIndices(list, amount):
        """
        ShiftIndices(list: IList, amount: int) -> IList
        
            Shifts indices in the list to the right by the given amount.
        
            list: List to be shifted.
            amount: Amount to shift indices by. If negative, indices will be shifted to the left.
            Returns: Shifted list.
        """
        pass

    @staticmethod
    def Shuffle(list):
        """
        Shuffle(list: IList) -> IList
        
            Shuffles a list, randomizing the order of its items.
        
            list: List to shuffle.
            Returns: Randomized list.
        """
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
        """
        SortByKey(list: IList, keys: IList) -> IDictionary
        
            Sort list based on its keys
        
            list: list to be sorted
            keys: list of keys
            Returns: sorted keys
        """
        pass

    @staticmethod
    def Sublists(list, ranges, offset):
        """
        Sublists(list: IList, ranges: IList, offset: int) -> IList
        
            Build sublists from a list using DesignScript range syntax.
        
            list: The list from which to create sublists.
            ranges: The index ranges of the sublist elements.
                        Ex. \"{0..3,5,2}\"
            offset: The offset to apply to the sublist.
                        Ex. the range \"0..3\" with an offset of 2 
             will yield
                        {0,1,2,3}{2,3,4,5}{4,5,6,7}...
        
            Returns: Sublists of the given list.
        """
        pass

    @staticmethod
    def TakeEveryNthItem(list, n, offset):
        """
        TakeEveryNthItem(list: IList, n: int, offset: int) -> IList
        
            Fetches items from the given list at indices that are multiples
                        of the given 
             value, after the given offset.
        
        
            list: List to take items from.
            n: Indices that are multiples of this number (after the offset)
                        will be fetched.
            offset: Amount of items to be ignored from the start of the list.
            Returns: Items from the list.
        """
        pass

    @staticmethod
    def TakeItems(list, amount):
        """
        TakeItems(list: IList, amount: int) -> IList
        
            Fetches an amount of items from the start of the list.
        
            list: List to take from.
            amount: Amount of items to take. If negative, items are taken from the end of the list.
            Returns: List of extracted items.
        """
        pass

    @staticmethod
    def Transpose(lists):
        """
        Transpose(lists: IList) -> IList
        
            Swaps rows and columns in a list of lists. 
                        If there are some rows that are 
             shorter than others,
                        null values are inserted as place holders in the resultant 
             
                        array such that it is always rectangular.
        
        
            lists: A list of lists to be transposed.
            Returns: A list of transposed lists.
        """
        pass

    @staticmethod
    def UniqueItems(list):
        """
        UniqueItems(list: IList) -> IList
        
            Creates a new list containing all unique items in the given list.
        
            list: List to filter duplicates out of.
            Returns: Filtered list.
        """
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
        'AllIndicesOf',
        'Chop',
        'Clean',
        'Combinations',
        'ContainsItem',
        'Count',
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
        'IsEmpty',
        'Join',
        'LastItem',
        'MaximumItem',
        'MinimumItem',
        'OfRepeatedItem',
        'Permutations',
        'RemoveItemAtIndex',
        'Repeat',
        'ReplaceItemAtIndex',
        'RestOfItems',
        'Reverse',
        'ShiftIndices',
        'Shuffle',
        'Slice',
        'Sort',
        'SortByKey',
        'Sublists',
        'TakeEveryNthItem',
        'TakeItems',
        'Transpose',
        'UniqueItems',
    ]


class Logic(object):
    """ Boolean logic methods. """
    @staticmethod
    def Xor(a, b):
        """
        Xor(a: bool, b: bool) -> bool
        
            Boolean XOR: Returns true if and only if exactly one of the inputs is true.
        
            a: A boolean.
            b: A boolean.
            Returns: Boolean result.
        """
        pass

    __all__ = [
        'Xor',
    ]


class Math(object):
    """ Methods for performing Mathematical operations. """
    @staticmethod
    def Abs(*__args):
        """
        Abs(integer: Int64) -> Int64
        
            Finds the absolute value of a number.
        
            integer: A number.
            Returns: Absolute value of the number.
        Abs(number: float) -> float
        
            Finds the absolute value of a number.
        
            number: A number.
            Returns: Absolute value of the number.
        """
        pass

    @staticmethod
    def Acos(ratio):
        """
        Acos(ratio: float) -> float
        
            Finds the inverse cosine, the angle whose cosine is the given ratio.
        
            ratio: The cosine of the angle, a number in the range [-1, 1].
            Returns: The angle whose cosine is the input ratio.
        """
        pass

    @staticmethod
    def Asin(ratio):
        """
        Asin(ratio: float) -> float
        
            Finds the inverse sine, the angle whose sine is the given ratio.
        
            ratio: The sine of the angle, a number in the range [-1, 1].
            Returns: The angle whose sine is the input ratio.
        """
        pass

    @staticmethod
    def Atan(ratio):
        """
        Atan(ratio: float) -> float
        
            Finds the inverse tangent, the angle whose tangent is the given ratio.
        
            ratio: The tangent of the angle.
            Returns: The angle whose tangent is the input ratio.
        """
        pass

    @staticmethod
    def Atan2(numerator, denominator):
        """
        Atan2(numerator: float, denominator: float) -> float
        
            Finds the inverse tangent of quotient of two numbers. Returns the angle
                        whose 
             tangent is the ratio: numerator/denominator.
        
        
            numerator: The numerator of the tangent of the angle.
            denominator: The denominator of the tangent of the angle.
            Returns: The angle whose tangent is numerator/denominator.
        """
        pass

    @staticmethod
    def Average(numbers):
        """ Average(numbers: IList[float]) -> float """
        pass

    @staticmethod
    def Ceiling(number):
        """
        Ceiling(number: float) -> Int64
        
            Returns the first integer greater than the number
        
            number: Number to round up.
            Returns: First integer greater than the number.
        """
        pass

    @staticmethod
    def Cos(angle):
        """
        Cos(angle: float) -> float
        
            Finds the cosine of an angle.
        
            angle: Angle in degrees to take the cosine of.
            Returns: Cosine of the angle.
        """
        pass

    @staticmethod
    def Cosh(angle):
        """
        Cosh(angle: float) -> float
        
            Finds the hyperbolic cosine of an angle (radians).
        
            angle: An angle in radians.
            Returns: Hyperbolic cosine of the angle.
        """
        pass

    @staticmethod
    def DegreesToRadians(degrees):
        """
        DegreesToRadians(degrees: float) -> float
        
            Converts an angle in degrees to an angle in radians.
        
            degrees: Angle in degrees.
            Returns: Angle in radians.
        """
        pass

    @staticmethod
    def DivRem(dividend, divisor):
        """
        DivRem(dividend: Int64, divisor: Int64) -> Int64
        
            Finds the remainder of dividend/divisor.
        
            dividend: The number to be divided.
            divisor: The number to be divided by.
            Returns: The remainder of the division.
        """
        pass

    @staticmethod
    def Exp(number):
        """
        Exp(number: float) -> float
        
            Returns the exponential of the number, the constant e raised to the value number.
        
            number: Number.
            Returns: The exponential of the number.
        """
        pass

    @staticmethod
    def Factorial(number):
        """
        Factorial(number: Int64) -> Int64
        
            Finds the factorial result of a positive integer.
        
            number: A positive integer.
            Returns: The factorial result of the integer.
        """
        pass

    @staticmethod
    def Floor(number):
        """
        Floor(number: float) -> Int64
        
            Returns the first integer smaller than the number.
        
            number: Number to round up.
            Returns: First integer smaller than the number.
        """
        pass

    @staticmethod
    def IEEERemainder(value1, value2):
        """ IEEERemainder(value1: float, value2: float) -> float """
        pass

    @staticmethod
    def Log(number, logBase=None):
        """
        Log(number: float, logBase: float) -> float
        
            Finds the logarithm of a number with the specified base.
        
            number: Number greater than 0.
                    Returns: Logarithm of the number.
        Log(number: float) -> float
        
                
            number: Number greater than 0.
            Returns: Natural log of the number.
        """
        pass

    @staticmethod
    def Log10(number):
        """
        Log10(number: float) -> float
        
            Finds the base-10 logarithm of a number.
        
            number: Number greater than 0.
            Returns: Logarithm of the number.
        """
        pass

    @staticmethod
    def Max(*__args):
        """
        Max(int1: Int64, int2: Int64) -> Int64
        
            Returns the greater of two numbers.
        
            int1: Number to compare.
            int2: Number to compare.
            Returns: Greater of the two numbers.
        Max(value1: float, value2: float) -> float
        
            Returns the greater of two numbers.
        
            value1: Number to compare.
            value2: Number to compare.
            Returns: Greater of the two numbers.
        """
        pass

    @staticmethod
    def Min(*__args):
        """
        Min(int1: Int64, int2: Int64) -> Int64
        
            Returns the lesser of two numbers.
        
            int1: Number to compare.
            int2: Number to compare.
            Returns: Smaler of the two numbers.
        Min(value1: float, value2: float) -> float
        
            Returns the lesser of two numbers.
        
            value1: Number to compare.
            value2: Number to compare.
            Returns: Smaler of the two numbers.
        """
        pass

    @staticmethod
    def Pow(number, power):
        """
        Pow(number: float, power: float) -> float
        
            Raises a number to the specified power.
        
            number: Number to be raised to a power.
            power: Power to raise the number to.
            Returns: Number raised to the power.
        """
        pass

    @staticmethod
    def RadiansToDegrees(radians):
        """
        RadiansToDegrees(radians: float) -> float
        
            Converts an angle in radians to an angle in degrees.
        
            radians: Angle in radians.
            Returns: Angle in degrees.
        """
        pass

    @staticmethod
    def Rand():
        """
        Rand() -> float
        
            Produce a random number in the range [0, 1).
            Returns: Random number in the range [0, 1).
        """
        pass

    @staticmethod
    def Random(*__args):
        """
        Random(value1: float, value2: float) -> float
        
            Produce a random number in the range [lower_number, higher_number).
        
            value1: One end of the range for the random number.
            value2: One end of the range for the random number.
            Returns: Random number in the range [lowValue, highValue).
        Random(seed: Nullable[int]) -> float
        """
        pass

    @staticmethod
    def RandomList(amount):
        """
        RandomList(amount: int) -> IList
        
            Produces a list containing the given amount of random doubles
                        in the range of 
             [0, 1).
        
        
            amount: Amount of random numbers the result list will contain.
            Returns: List of random numbers between 0 and 1.
        """
        pass

    @staticmethod
    def RemapRange(numbers, newMin, newMax):
        """ RemapRange(numbers: IList[float], newMin: float, newMax: float) -> IList """
        pass

    @staticmethod
    def Round(number, digits=None):
        """
        Round(number: float, digits: int) -> float
        
            Rounds a number to a specified number of fractional digits.
        
            number: Number to be rounded.
            digits: Number of fractional digits in the return value.
            Returns: The number nearest to value that contains a number of fractional digits equal to digits.
        Round(number: float) -> float
        
            Rounds a number to the closest integral value.
                    Note that this method returns a 
             double-precision floating-point number instead of an integral type.
        
        
            number: Number to round.
            Returns: Integral value closes to the number.
        """
        pass

    @staticmethod
    def Sign(*__args):
        """
        Sign(integer: Int64) -> Int64
        
            Returns the sign of the number: -1, 0, or 1.
        
            integer: A number.
            Returns: The sign of the number: -1, 0, or 1.
        Sign(number: float) -> Int64
        
            Returns the sign of the number: -1, 0, or 1.
        
            number: A number.
            Returns: The sign of the number: -1, 0, or 1.
        """
        pass

    @staticmethod
    def Sin(angle):
        """
        Sin(angle: float) -> float
        
            Finds the sine of an angle.
        
            angle: Angle in degrees to take the cosine of.
            Returns: Sine of the angle.
        """
        pass

    @staticmethod
    def Sinh(angle):
        """
        Sinh(angle: float) -> float
        
            Finds the hyperbolic sine of an angle (radians).
        
            angle: An angle in radians.
            Returns: Hyperbolic sine of the angle.
        """
        pass

    @staticmethod
    def Sqrt(number):
        """
        Sqrt(number: float) -> float
        
                
                    Returns: Positive square root of the number.
        """
        pass

    @staticmethod
    def Sum(values):
        """ Sum(values: IEnumerable[float]) -> float """
        pass

    @staticmethod
    def Tan(angle):
        """
        Tan(angle: float) -> float
        
            Finds the tangent of an angle.
        
            angle: Angle in degrees to take the tangent of.
            Returns: Tangent of the angle.
        """
        pass

    @staticmethod
    def Tanh(angle):
        """
        Tanh(angle: float) -> float
        
            Finds the hyperbolic tangent of an angle (radians).
        
            angle: An angle in radians.
            Returns: Hyperbolic tangent of the angle.
        """
        pass

    @staticmethod
    def Truncate(value):
        """ Truncate(value: float) -> float """
        pass

    E = 2.7182818284590451
    GoldenRatio = 1.6180339887499999
    PI = 3.1415926535897931
    PiTimes2 = 6.2831853071795862
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
        'Exp',
        'Factorial',
        'Floor',
        'IEEERemainder',
        'Log',
        'Log10',
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
    """ Generic functions that operate on all data. """
    @staticmethod
    def Identity(obj):
        """
        Identity(obj: object) -> object
        
            Returns what is passed in, doing nothing.
        
            obj: An object.
        """
        pass

    @staticmethod
    def IsNull(obj):
        """
        IsNull(obj: object) -> bool
        
            Determines the if the given object is null.
        
            obj: Object to test.
            Returns: Whether object is null.
        """
        pass

    @staticmethod
    def Type(obj):
        """
        Type(obj: object) -> str
        
            Returns the type of object represented as string.
        
            obj: An object.
            Returns: Type of object.
        """
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
        """
        FindPointsWithinRadius(self: Quadtree, center: UV, radius: float) -> List[UV]
        
            Find all quadtree points (UVs) in the quadtree within a radius of the given UV location.
        
            center: The UV at the center of the search area.
            radius: The radius of the search area.
            Returns: A list of UVs.
        """
        pass

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Root(self: Quadtree) -> Node

Set: Root(self: Quadtree) = value
"""



class Sorting(object):
    """
    Utility methods for sorting by keys. These should be suppressed from becoming nodes, instead
                they will be wrapped by DS implementations that accept a key mapping function.
    """
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
    """ Methods for managing strings. """
    @staticmethod
    def Center(str, newWidth, padChars):
        """
        Center(str: str, newWidth: int, padChars: str) -> str
        
            Increases the width of a string by encasing the original characters with spaces on
                     
                either side.
        
        
            str: String to center.
            newWidth: Total length of the string after centering.
            padChars: Character to center with, defaults to space.
            Returns: Strings center-aligned by padding them with leading and trailing
                        whitespaces 
             for a specified total length.
        """
        pass

    @staticmethod
    def ChangeCase(str, upper):
        """
        ChangeCase(str: str, upper: bool) -> str
        
            Converts the given string to all uppercase characters or all
                        lowercase 
             characters based on a boolean parameter.
        
        
            str: String to be made uppercase or lowercase.
            upper: True to convert to uppercase, false to convert to lowercase.
            Returns: String with converted case.
        """
        pass

    @staticmethod
    def Concat(strings):
        """
        Concat(*strings: Array[str]) -> str
        
            Concatenates multiple strings into a single string.
        
            strings: List of strings to concatenate.
            Returns: String made from list of strings.
        """
        pass

    @staticmethod
    def Contains(str, searchFor, ignoreCase):
        """
        Contains(str: str, searchFor: str, ignoreCase: bool) -> bool
        
            Determines if the given string contains the given substring.
        
            str: String to search in.
            searchFor: Substring to search for.
            ignoreCase: Whether or not comparison takes case into account.
            Returns: Whether the string contains the substring.
        """
        pass

    @staticmethod
    def CountOccurrences(str, searchFor, ignoreCase):
        """
        CountOccurrences(str: str, searchFor: str, ignoreCase: bool) -> int
        
            Counts the number of non-overlapping occurrences of a substring inside a given string.
        
            str: String to search in.
            searchFor: Substring to search for.
            ignoreCase: Whether or not comparison takes case into account.
            Returns: Number of non-overlapping occurrences of the substring in the string.
        """
        pass

    @staticmethod
    def EndsWith(str, searchFor, ignoreCase):
        """
        EndsWith(str: str, searchFor: str, ignoreCase: bool) -> bool
        
            Determines if the given string ends with the given substring.
        
            str: String to search the end of.
            searchFor: Substring to search the end for.
            ignoreCase: Whether or not comparison takes case into account.
            Returns: Whether the string ends with the substring.
        """
        pass

    @staticmethod
    def FromObject(obj):
        """ FromObject(obj: object) -> str """
        pass

    @staticmethod
    def IndexOf(str, searchFor, ignoreCase):
        """
        IndexOf(str: str, searchFor: str, ignoreCase: bool) -> int
        
            Finds the zero-based index of the first occurrence of a sub-string inside a string.
                    
                 Returns -1 if no index could be found.
        
        
            str: A string to search in.
            searchFor: Substring to search for.
            ignoreCase: Whether or not comparison takes case into account.
            Returns: Index of the first occurrence of the substring or -1 if not found.
        """
        pass

    @staticmethod
    def Insert(str, index, toInsert):
        """
        Insert(str: str, index: int, toInsert: str) -> str
        
            Inserts a string into another string at a given index.
        
            str: String to insert into.
            index: Index to insert at.
            toInsert: String to be inserted.
            Returns: String with inserted substring.
        """
        pass

    @staticmethod
    def Join(separator, strings):
        """
        Join(separator: str, *strings: Array[str]) -> str
        
            Concatenates multiple strings into a single string, inserting the given
                        
             separator between each joined string.
        
        
            separator: String to be inserted between joined strings.
            strings: Strings to be joined into a single string.
            Returns: A string made from the list of strings including the separator character.
        """
        pass

    @staticmethod
    def LastIndexOf(str, searchFor, ignoreCase):
        """
        LastIndexOf(str: str, searchFor: str, ignoreCase: bool) -> int
        
            Finds the zero-based index of the last occurrence of a sub-string inside a string.
                     
                Returns -1 if no index could be found.
        
        
            str: A string to search in.
            searchFor: Substring to search for.
            ignoreCase: Whether comparison takes case into account.
            Returns: Index of the last occurrence of the substring or -1 if not found.
        """
        pass

    @staticmethod
    def Length(str):
        """
        Length(str: str) -> int
        
            Returns the number of characters contained in the given string.
        
            str: String to find the length of.
            Returns: Number of characters in the string.
        """
        pass

    @staticmethod
    def PadLeft(str, newWidth, padChars):
        """
        PadLeft(str: str, newWidth: int, padChars: str) -> str
        
            Right-aligns the characters in the given string by padding them with spaces on the left,
               
                      for a specified total length.
        
        
            str: String to pad.
            newWidth: Total length of the string after padding.
            padChars: Character to pad with, defaults to space.
            Returns: Strings right-aligned by padding with leading whitespaces for a specified total length.
        """
        pass

    @staticmethod
    def PadRight(str, newWidth, padChars):
        """
        PadRight(str: str, newWidth: int, padChars: str) -> str
        
            Left-aligns the characters in the given string by padding them with spaces on the right,
               
                      for a specified total length.
        
        
            str: String to pad.
            newWidth: Total length of the string after padding.
            padChars: Character to pad with, defaults to space.
            Returns: Strings left-aligned by padding with trailing whitespaces for a specified total length.
        """
        pass

    @staticmethod
    def Remove(str, startIndex, count):
        """ Remove(str: str, startIndex: int, count: Nullable[int]) -> str """
        pass

    @staticmethod
    def Replace(str, searchFor, replaceWith):
        """
        Replace(str: str, searchFor: str, replaceWith: str) -> str
        
            Replaces all occurrances of text in a string with other text.
        
            str: String to replace substrings in.
            searchFor: Text to be replaced.
            replaceWith: Text to replace with.
            Returns: String with replacements made.
        """
        pass

    @staticmethod
    def Split(str, separaters):
        """
        Split(str: str, *separaters: Array[str]) -> Array[str]
        
            Divides a single string into a list of strings, with divisions
                        determined by 
             the given separater strings.
        
        
            str: String to split up.
            separaters: Strings that, if present, determine the end and start of a split.
            Returns: List of strings made from the input string.
        """
        pass

    @staticmethod
    def StartsWith(str, searchFor, ignoreCase):
        """
        StartsWith(str: str, searchFor: str, ignoreCase: bool) -> bool
        
            Determines if the given string starts with the given substring.
        
            str: String to search the start of.
            searchFor: Substring to search the start for.
            ignoreCase: Whether or not comparison takes case into account.
            Returns: Whether the string starts with the substring.
        """
        pass

    @staticmethod
    def Substring(str, startIndex, length):
        """
        Substring(str: str, startIndex: int, length: int) -> str
        
            Retrieves a substring from the given string. The substring starts at the given
                        
             character position and has the given length.
        
        
            str: String to take substring of.
            startIndex: Starting character position of the substring in the original string.
            length: Number of characters in the substring.
            Returns: Substring made from the original string.
        """
        pass

    @staticmethod
    def ToLower(str):
        """
        ToLower(str: str) -> str
        
            Converts the given string to all lowercase characters.
        
            str: String to be made lowercase.
            Returns: Lowercase string.
        """
        pass

    @staticmethod
    def ToNumber(str):
        """
        ToNumber(str: str) -> object
        
            Converts a string to an integer or a double.
        
            str: String to be converted.
            Returns: Integer or double-type number.
        """
        pass

    @staticmethod
    def ToUpper(str):
        """
        ToUpper(str: str) -> str
        
            Converts the given string to all uppercase characters.
        
            str: String to be made uppercase.
            Returns: Uppercase string.
        """
        pass

    @staticmethod
    def TrimLeadingWhitespace(str):
        """
        TrimLeadingWhitespace(str: str) -> str
        
            Removes all whitespace from the start of the given string.
        
            str: String to trim.
            Returns: String with leading white spaces removed.
        """
        pass

    @staticmethod
    def TrimTrailingWhitespace(str):
        """
        TrimTrailingWhitespace(str: str) -> str
        
            Removes all whitespace from the end of the given string.
        
            str: String to trim.
            Returns: String with white spaces at end removed.
        """
        pass

    @staticmethod
    def TrimWhitespace(str):
        """
        TrimWhitespace(str: str) -> str
        
            Removes all whitespace from the start and end of the given string.
        
            str: String to trim.
            Returns: String with beginning and ending whitespaces removed.
        """
        pass

    __all__ = [
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
    """ Functions for manipulating evaluation threads. """
    @staticmethod
    def Pause(x, msTimeout):
        """
        Pause(x: object, msTimeout: int) -> object
        
            Pauses the current evaluation thread for a given amount of time.
        
            x: Object to pass through.
            msTimeout: Amount of time to pause the thread, in milliseconds.
            Returns: Object passed through.
        """
        pass

    __all__ = [
        'Pause',
    ]


class TimeSpan(object):
    """ Object representing an elapsed period of time, with no specific start or end date. """
    @staticmethod
    def Add(timeSpan1, timeSpan2):
        """
        Add(timeSpan1: TimeSpan, timeSpan2: TimeSpan) -> TimeSpan
        
            Adds two TimeSpans.
        
            timeSpan1: A TimeSpan.
            timeSpan2: A TimeSpan.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def ByDateDifference(date1, date2):
        """
        ByDateDifference(date1: DateTime, date2: DateTime) -> TimeSpan
        
            Yields a new TimeSpan calculated from the time difference between two DateTimes.
        
            date1: Starting DateTime.
            date2: Ending DateTime.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def Components(timeSpan):
        """
        Components(timeSpan: TimeSpan) -> Dictionary[str, int]
        
            Extracts the individual components of a TimeSpan.
        
            timeSpan: A TimeSpan.
        """
        pass

    @staticmethod
    def Create(days, hours, minutes, seconds, milliseconds):
        """
        Create(days: float, hours: float, minutes: float, seconds: float, milliseconds: float) -> TimeSpan
        
            Creates a new TimeSpan from a span of time.
        
            days: Days spanned.
            hours: Hours spanned.
            minutes: Minutes spanned.
            seconds: Seconds spanned.
            milliseconds: Milliseconds spanned.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def FromString(str):
        """
        FromString(str: str) -> TimeSpan
        
            Attempts to parse a TimeSpan from a string.
        
            str: String representation of a TimeSpan.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def Negate(timeSpan):
        """
        Negate(timeSpan: TimeSpan) -> TimeSpan
        
            Negates a TimeSpan.
        
            timeSpan: A TimeSpan.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def Scale(timeSpan, scaleFactor):
        """
        Scale(timeSpan: TimeSpan, scaleFactor: float) -> TimeSpan
        
            Multiplies a TimeSpan by a scaling factor.
        
            timeSpan: A TimeSpan.
            scaleFactor: Amount to scale the TimeSpan. For example, a scaling factor of 2 will yield
                    double 
             the amount of time spanned.
        
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def Subtract(timeSpan1, timeSpan2):
        """
        Subtract(timeSpan1: TimeSpan, timeSpan2: TimeSpan) -> TimeSpan
        
            Subtracts two TimeSpans.
        
            timeSpan1: A TimeSpan.
            timeSpan2: A TimeSpan.
            Returns: TimeSpan
        """
        pass

    @staticmethod
    def TotalDays(timeSpan):
        """
        TotalDays(timeSpan: TimeSpan) -> float
        
            Converts the total amount of time represented by a TimeSpan to an
                        inexact 
             number of days.
        
        
            timeSpan: A TimeSpan.
        """
        pass

    @staticmethod
    def TotalHours(timeSpan):
        """
        TotalHours(timeSpan: TimeSpan) -> float
        
            Converts the total amount of time represented by a TimeSpan to an
                        inexact 
             number of hours.
        
        
            timeSpan: A TimeSpan.
        """
        pass

    @staticmethod
    def TotalMilliseconds(timeSpan):
        """
        TotalMilliseconds(timeSpan: TimeSpan) -> float
        
            Converts the total amount of time represented by a TimeSpan to an
                        inexact 
             number of milliseconds.
        
        
            timeSpan: A TimeSpan.
        """
        pass

    @staticmethod
    def TotalMinutes(timeSpan):
        """
        TotalMinutes(timeSpan: TimeSpan) -> float
        
            Converts the total amount of time represented by a TimeSpan to an
                        inexact 
             number of minutes.
        
        
            timeSpan: A TimeSpan.
        """
        pass

    @staticmethod
    def TotalSeconds(timeSpan):
        """
        TotalSeconds(timeSpan: TimeSpan) -> float
        
            Converts the total amount of time represented by a TimeSpan to an
                        inexact 
             number of seconds.
        
        
            timeSpan: A TimeSpan.
        """
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
    """
    Helper class used to define a Rectangle described
                by a minimum and a maximum UV.
    
    UVRect(min: UV, max: UV)
    """
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


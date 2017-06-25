# encoding: utf-8
# module System.Collections.Generic calls itself Generic
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Comparer(object):
    # no doc
    def Compare(self, x, y):
        """ Compare(self: Comparer[T], x: T, y: T) -> int """
        pass

    @staticmethod
    def Create(comparison):
        """ Create(comparison: Comparison[T]) -> Comparer[T] """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass


class Dictionary(object):
    """
    Dictionary[TKey, TValue]()
    Dictionary[TKey, TValue](capacity: int)
    Dictionary[TKey, TValue](comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](capacity: int, comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    """
    def Add(self, key, value):
        """ Add(self: Dictionary[TKey, TValue], key: TKey, value: TValue) """
        pass

    def Clear(self):
        """ Clear(self: Dictionary[TKey, TValue]) """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: Dictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def ContainsValue(self, value):
        """ ContainsValue(self: Dictionary[TKey, TValue], value: TValue) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Dictionary[TKey, TValue]) -> Enumerator """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Dictionary[TKey, TValue], info: SerializationInfo, context: StreamingContext) """
        pass

    def OnDeserialization(self, sender):
        """ OnDeserialization(self: Dictionary[TKey, TValue], sender: object) """
        pass

    def Remove(self, key):
        """ Remove(self: Dictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: Dictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary[TKey, TValue], key: TKey) -> bool
        __contains__(self: IDictionary, key: object) -> bool
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, comparer: IEqualityComparer[TKey])
        __new__(cls: type, capacity: int, comparer: IEqualityComparer[TKey])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comparer(self: Dictionary[TKey, TValue]) -> IEqualityComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Dictionary[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: Dictionary[TKey, TValue]) -> KeyCollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: Dictionary[TKey, TValue]) -> ValueCollection

"""


    Enumerator = None
    KeyCollection = None
    ValueCollection = None


class EqualityComparer(object):
    # no doc
    def Equals(self, *__args):
        """ Equals(self: EqualityComparer[T], x: T, y: T) -> bool """
        pass

    def GetHashCode(self, obj=None):
        """ GetHashCode(self: EqualityComparer[T], obj: T) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass


class ICollection(IEnumerable[T], IEnumerable):
    # no doc
    def Add(self, item):
        """ Add(self: ICollection[T], item: T) """
        pass

    def Clear(self):
        """ Clear(self: ICollection[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: ICollection[T], item: T) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: ICollection[T], array: Array[T], arrayIndex: int) """
        pass

    def Remove(self, item):
        """ Remove(self: ICollection[T], item: T) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ICollection[T]) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ICollection[T]) -> bool

"""



class IComparer:
    # no doc
    def Compare(self, x, y):
        """ Compare(self: IComparer[T], x: T, y: T) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDictionary(ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable):
    # no doc
    def Add(self, key, value):
        """ Add(self: IDictionary[TKey, TValue], key: TKey, value: TValue) """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: IDictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def Remove(self, key):
        """ Remove(self: IDictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: IDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[KeyValuePair[TKey, TValue]], item: KeyValuePair[TKey, TValue]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: IDictionary[TKey, TValue]) -> ICollection[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: IDictionary[TKey, TValue]) -> ICollection[TValue]

"""



class IEnumerable(IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: IEnumerable[T]) -> IEnumerator[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumerator(IDisposable, IEnumerator):
    # no doc
    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__[T](self: IEnumerator[T]) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: IEnumerator[T]) -> T

"""



class IEqualityComparer:
    # no doc
    def Equals(self, x, y):
        """ Equals(self: IEqualityComparer[T], x: T, y: T) -> bool """
        pass

    def GetHashCode(self, obj):
        """ GetHashCode(self: IEqualityComparer[T], obj: T) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IList(ICollection[T], IEnumerable[T], IEnumerable):
    # no doc
    def IndexOf(self, item):
        """ IndexOf(self: IList[T], item: T) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: IList[T], index: int, item: T) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: IList[T], index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[T], item: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class IReadOnlyCollection(IEnumerable[T], IEnumerable):
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IReadOnlyCollection[T]) -> int

"""



class IReadOnlyDictionary(IReadOnlyCollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable):
    # no doc
    def ContainsKey(self, key):
        """ ContainsKey(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair`2](enumerable: IEnumerable[KeyValuePair[TKey, TValue]], value: KeyValuePair[TKey, TValue]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TValue]

"""



class IReadOnlyList(IReadOnlyCollection[T], IEnumerable[T], IEnumerable):
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ISet(ICollection[T], IEnumerable[T], IEnumerable):
    # no doc
    def Add(self, item):
        """ Add(self: ISet[T], item: T) -> bool """
        pass

    def ExceptWith(self, other):
        """ ExceptWith(self: ISet[T], other: IEnumerable[T]) """
        pass

    def IntersectWith(self, other):
        """ IntersectWith(self: ISet[T], other: IEnumerable[T]) """
        pass

    def IsProperSubsetOf(self, other):
        """ IsProperSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsProperSupersetOf(self, other):
        """ IsProperSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsSubsetOf(self, other):
        """ IsSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsSupersetOf(self, other):
        """ IsSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def Overlaps(self, other):
        """ Overlaps(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def SetEquals(self, other):
        """ SetEquals(self: ISet[T], other: IEnumerable[T]) -> bool """
        pass

    def SymmetricExceptWith(self, other):
        """ SymmetricExceptWith(self: ISet[T], other: IEnumerable[T]) """
        pass

    def UnionWith(self, other):
        """ UnionWith(self: ISet[T], other: IEnumerable[T]) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[T], item: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass


class KeyNotFoundException(SystemException):
    """
    KeyNotFoundException()
    KeyNotFoundException(message: str)
    KeyNotFoundException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class KeyValuePair(object):
    """ KeyValuePair[TKey, TValue](key: TKey, value: TValue) """
    def ToString(self):
        """ ToString(self: KeyValuePair[TKey, TValue]) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, key, value):
        """
        __new__[KeyValuePair`2]() -> KeyValuePair[TKey, TValue]
        
        __new__(cls: type, key: TKey, value: TValue)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: KeyValuePair[TKey, TValue]) -> TKey

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: KeyValuePair[TKey, TValue]) -> TValue

"""



class LinkedList(object):
    """
    LinkedList[T]()
    LinkedList[T](collection: IEnumerable[T])
    """
    def AddAfter(self, node, *__args):
        """
        AddAfter(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]
        AddAfter(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])
        """
        pass

    def AddBefore(self, node, *__args):
        """ AddBefore(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])AddBefore(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T] """
        pass

    def AddFirst(self, *__args):
        """ AddFirst(self: LinkedList[T], node: LinkedListNode[T])AddFirst(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        pass

    def AddLast(self, *__args):
        """ AddLast(self: LinkedList[T], node: LinkedListNode[T])AddLast(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        pass

    def Clear(self):
        """ Clear(self: LinkedList[T]) """
        pass

    def Contains(self, value):
        """ Contains(self: LinkedList[T], value: T) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: LinkedList[T], array: Array[T], index: int) """
        pass

    def Find(self, value):
        """ Find(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        pass

    def FindLast(self, value):
        """ FindLast(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LinkedList[T]) -> Enumerator """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: LinkedList[T], info: SerializationInfo, context: StreamingContext) """
        pass

    def OnDeserialization(self, sender):
        """ OnDeserialization(self: LinkedList[T], sender: object) """
        pass

    def Remove(self, *__args):
        """ Remove(self: LinkedList[T], node: LinkedListNode[T])Remove(self: LinkedList[T], value: T) -> bool """
        pass

    def RemoveFirst(self):
        """ RemoveFirst(self: LinkedList[T]) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: LinkedList[T]) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[T], item: T) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[T])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: LinkedList[T]) -> int

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: First(self: LinkedList[T]) -> LinkedListNode[T]

"""

    Last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Last(self: LinkedList[T]) -> LinkedListNode[T]

"""


    Enumerator = None


class LinkedListNode(object):
    """ LinkedListNode[T](value: T) """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: T) """
        pass

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: List(self: LinkedListNode[T]) -> LinkedList[T]

"""

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Next(self: LinkedListNode[T]) -> LinkedListNode[T]

"""

    Previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Previous(self: LinkedListNode[T]) -> LinkedListNode[T]

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: LinkedListNode[T]) -> T

Set: Value(self: LinkedListNode[T]) = value
"""



class List(object):
    """
    List[T]()
    List[T](capacity: int)
    List[T](collection: IEnumerable[T])
    """
    def Add(self, item):
        """ Add(self: List[T], item: T) """
        pass

    def AddRange(self, collection):
        """ AddRange(self: List[T], collection: IEnumerable[T]) """
        pass

    def AsReadOnly(self):
        """ AsReadOnly(self: List[T]) -> ReadOnlyCollection[T] """
        pass

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: List[T], item: T, comparer: IComparer[T]) -> int
        BinarySearch(self: List[T], item: T) -> int
        BinarySearch(self: List[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int
        """
        pass

    def Clear(self):
        """ Clear(self: List[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: List[T], item: T) -> bool """
        pass

    def ConvertAll(self, converter):
        """ ConvertAll[TOutput](self: List[T], converter: Converter[T, TOutput]) -> List[TOutput] """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: List[T], array: Array[T], arrayIndex: int)CopyTo(self: List[T], array: Array[T])CopyTo(self: List[T], index: int, array: Array[T], arrayIndex: int, count: int) """
        pass

    def Exists(self, match):
        """ Exists(self: List[T], match: Predicate[T]) -> bool """
        pass

    def Find(self, match):
        """ Find(self: List[T], match: Predicate[T]) -> T """
        pass

    def FindAll(self, match):
        """ FindAll(self: List[T], match: Predicate[T]) -> List[T] """
        pass

    def FindIndex(self, *__args):
        """
        FindIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        FindIndex(self: List[T], match: Predicate[T]) -> int
        """
        pass

    def FindLast(self, match):
        """ FindLast(self: List[T], match: Predicate[T]) -> T """
        pass

    def FindLastIndex(self, *__args):
        """
        FindLastIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindLastIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        FindLastIndex(self: List[T], match: Predicate[T]) -> int
        """
        pass

    def ForEach(self, action):
        """ ForEach(self: List[T], action: Action[T]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: List[T]) -> Enumerator """
        pass

    def GetRange(self, index, count):
        """ GetRange(self: List[T], index: int, count: int) -> List[T] """
        pass

    def IndexOf(self, item, index=None, count=None):
        """
        IndexOf(self: List[T], item: T, index: int, count: int) -> int
        IndexOf(self: List[T], item: T, index: int) -> int
        IndexOf(self: List[T], item: T) -> int
        """
        pass

    def Insert(self, index, item):
        """ Insert(self: List[T], index: int, item: T) """
        pass

    def InsertRange(self, index, collection):
        """ InsertRange(self: List[T], index: int, collection: IEnumerable[T]) """
        pass

    def LastIndexOf(self, item, index=None, count=None):
        """
        LastIndexOf(self: List[T], item: T, index: int, count: int) -> int
        LastIndexOf(self: List[T], item: T, index: int) -> int
        LastIndexOf(self: List[T], item: T) -> int
        """
        pass

    def Remove(self, item):
        """ Remove(self: List[T], item: T) -> bool """
        pass

    def RemoveAll(self, match):
        """ RemoveAll(self: List[T], match: Predicate[T]) -> int """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: List[T], index: int) """
        pass

    def RemoveRange(self, index, count):
        """ RemoveRange(self: List[T], index: int, count: int) """
        pass

    def Reverse(self, index=None, count=None):
        """ Reverse(self: List[T])Reverse(self: List[T], index: int, count: int) """
        pass

    def Sort(self, *__args):
        """ Sort(self: List[T], index: int, count: int, comparer: IComparer[T])Sort(self: List[T], comparison: Comparison[T])Sort(self: List[T])Sort(self: List[T], comparer: IComparer[T]) """
        pass

    def ToArray(self):
        """ ToArray(self: List[T]) -> Array[T] """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: List[T]) """
        pass

    def TrueForAll(self, match):
        """ TrueForAll(self: List[T], match: Predicate[T]) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        __contains__(self: IList, value: object) -> bool
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: List[T]) -> int

Set: Capacity(self: List[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: List[T]) -> int

"""


    Enumerator = None


class Queue(object):
    """
    Queue[T]()
    Queue[T](capacity: int)
    Queue[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """ Clear(self: Queue[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: Queue[T], item: T) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: Queue[T], array: Array[T], arrayIndex: int) """
        pass

    def Dequeue(self):
        """ Dequeue(self: Queue[T]) -> T """
        pass

    def Enqueue(self, item):
        """ Enqueue(self: Queue[T], item: T) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Queue[T]) -> Enumerator """
        pass

    def Peek(self):
        """ Peek(self: Queue[T]) -> T """
        pass

    def ToArray(self):
        """ ToArray(self: Queue[T]) -> Array[T] """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: Queue[T]) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Queue[T]) -> int

"""


    Enumerator = None


class SortedDictionary(object):
    """
    SortedDictionary[TKey, TValue]()
    SortedDictionary[TKey, TValue](comparer: IComparer[TKey])
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    def Add(self, key, value):
        """ Add(self: SortedDictionary[TKey, TValue], key: TKey, value: TValue) """
        pass

    def Clear(self):
        """ Clear(self: SortedDictionary[TKey, TValue]) """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: SortedDictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def ContainsValue(self, value):
        """ ContainsValue(self: SortedDictionary[TKey, TValue], value: TValue) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: SortedDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SortedDictionary[TKey, TValue]) -> Enumerator """
        pass

    def Remove(self, key):
        """ Remove(self: SortedDictionary[TKey, TValue], key: TKey) -> bool """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: SortedDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary[TKey, TValue], key: TKey) -> bool
        __contains__(self: IDictionary, key: object) -> bool
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
        __new__(cls: type, comparer: IComparer[TKey])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comparer(self: SortedDictionary[TKey, TValue]) -> IComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SortedDictionary[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: SortedDictionary[TKey, TValue]) -> KeyCollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: SortedDictionary[TKey, TValue]) -> ValueCollection

"""


    Enumerator = None
    KeyCollection = None
    ValueCollection = None


class SortedList(object):
    """
    SortedList[TKey, TValue]()
    SortedList[TKey, TValue](capacity: int)
    SortedList[TKey, TValue](comparer: IComparer[TKey])
    SortedList[TKey, TValue](capacity: int, comparer: IComparer[TKey])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    def Add(self, key, value):
        """ Add(self: SortedList[TKey, TValue], key: TKey, value: TValue) """
        pass

    def Clear(self):
        """ Clear(self: SortedList[TKey, TValue]) """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: SortedList[TKey, TValue], key: TKey) -> bool """
        pass

    def ContainsValue(self, value):
        """ ContainsValue(self: SortedList[TKey, TValue], value: TValue) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SortedList[TKey, TValue]) -> IEnumerator[KeyValuePair[TKey, TValue]] """
        pass

    def IndexOfKey(self, key):
        """ IndexOfKey(self: SortedList[TKey, TValue], key: TKey) -> int """
        pass

    def IndexOfValue(self, value):
        """ IndexOfValue(self: SortedList[TKey, TValue], value: TValue) -> int """
        pass

    def Remove(self, key):
        """ Remove(self: SortedList[TKey, TValue], key: TKey) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SortedList[TKey, TValue], index: int) """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: SortedList[TKey, TValue]) """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: SortedList[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary[TKey, TValue], key: TKey) -> bool
        __contains__(self: IDictionary, key: object) -> bool
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, comparer: IComparer[TKey])
        __new__(cls: type, capacity: int, comparer: IComparer[TKey])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: SortedList[TKey, TValue]) -> int

Set: Capacity(self: SortedList[TKey, TValue]) = value
"""

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comparer(self: SortedList[TKey, TValue]) -> IComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SortedList[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: SortedList[TKey, TValue]) -> IList[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: SortedList[TKey, TValue]) -> IList[TValue]

"""



class SortedSet(object):
    """
    SortedSet[T]()
    SortedSet[T](collection: IEnumerable[T])
    SortedSet[T](collection: IEnumerable[T], comparer: IComparer[T])
    SortedSet[T](comparer: IComparer[T])
    """
    def Add(self, item):
        """ Add(self: SortedSet[T], item: T) -> bool """
        pass

    def Clear(self):
        """ Clear(self: SortedSet[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: SortedSet[T], item: T) -> bool """
        pass

    def CopyTo(self, array, index=None, count=None):
        """ CopyTo(self: SortedSet[T], array: Array[T], index: int, count: int)CopyTo(self: SortedSet[T], array: Array[T], index: int)CopyTo(self: SortedSet[T], array: Array[T]) """
        pass

    @staticmethod
    def CreateSetComparer(memberEqualityComparer=None):
        """
        CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]
        CreateSetComparer() -> IEqualityComparer[SortedSet[T]]
        """
        pass

    def ExceptWith(self, other):
        """ ExceptWith(self: SortedSet[T], other: IEnumerable[T]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SortedSet[T]) -> Enumerator """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: SortedSet[T], info: SerializationInfo, context: StreamingContext) """
        pass

    def GetViewBetween(self, lowerValue, upperValue):
        """ GetViewBetween(self: SortedSet[T], lowerValue: T, upperValue: T) -> SortedSet[T] """
        pass

    def IntersectWith(self, other):
        """ IntersectWith(self: SortedSet[T], other: IEnumerable[T]) """
        pass

    def IsProperSubsetOf(self, other):
        """ IsProperSubsetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsProperSupersetOf(self, other):
        """ IsProperSupersetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsSubsetOf(self, other):
        """ IsSubsetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def IsSupersetOf(self, other):
        """ IsSupersetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def OnDeserialization(self, *args): #cannot find CLR method
        """ OnDeserialization(self: SortedSet[T], sender: object) """
        pass

    def Overlaps(self, other):
        """ Overlaps(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def Remove(self, item):
        """ Remove(self: SortedSet[T], item: T) -> bool """
        pass

    def RemoveWhere(self, match):
        """ RemoveWhere(self: SortedSet[T], match: Predicate[T]) -> int """
        pass

    def Reverse(self):
        """ Reverse(self: SortedSet[T]) -> IEnumerable[T] """
        pass

    def SetEquals(self, other):
        """ SetEquals(self: SortedSet[T], other: IEnumerable[T]) -> bool """
        pass

    def SymmetricExceptWith(self, other):
        """ SymmetricExceptWith(self: SortedSet[T], other: IEnumerable[T]) """
        pass

    def UnionWith(self, other):
        """ UnionWith(self: SortedSet[T], other: IEnumerable[T]) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[T], item: T) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, comparer: IComparer[T])
        __new__(cls: type, collection: IEnumerable[T])
        __new__(cls: type, collection: IEnumerable[T], comparer: IComparer[T])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comparer(self: SortedSet[T]) -> IComparer[T]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SortedSet[T]) -> int

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Max(self: SortedSet[T]) -> T

"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Min(self: SortedSet[T]) -> T

"""


    Enumerator = None


class Stack(object):
    """
    Stack[T]()
    Stack[T](capacity: int)
    Stack[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """ Clear(self: Stack[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: Stack[T], item: T) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: Stack[T], array: Array[T], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Stack[T]) -> Enumerator """
        pass

    def Peek(self):
        """ Peek(self: Stack[T]) -> T """
        pass

    def Pop(self):
        """ Pop(self: Stack[T]) -> T """
        pass

    def Push(self, item):
        """ Push(self: Stack[T], item: T) """
        pass

    def ToArray(self):
        """ ToArray(self: Stack[T]) -> Array[T] """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: Stack[T]) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Stack[T]) -> int

"""


    Enumerator = None



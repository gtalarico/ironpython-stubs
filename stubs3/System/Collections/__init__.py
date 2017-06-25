# encoding: utf-8
# module System.Collections calls itself Collections
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArrayList(object):
    """
    ArrayList()
    ArrayList(capacity: int)
    ArrayList(c: ICollection)
    """
    @staticmethod
    def Adapter(list):
        """ Adapter(list: IList) -> ArrayList """
        pass

    def Add(self, value):
        """ Add(self: ArrayList, value: object) -> int """
        pass

    def AddRange(self, c):
        """ AddRange(self: ArrayList, c: ICollection) """
        pass

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: ArrayList, value: object, comparer: IComparer) -> int
        BinarySearch(self: ArrayList, value: object) -> int
        BinarySearch(self: ArrayList, index: int, count: int, value: object, comparer: IComparer) -> int
        """
        pass

    def Clear(self):
        """ Clear(self: ArrayList) """
        pass

    def Clone(self):
        """ Clone(self: ArrayList) -> object """
        pass

    def Contains(self, item):
        """ Contains(self: ArrayList, item: object) -> bool """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: ArrayList, index: int, array: Array, arrayIndex: int, count: int)CopyTo(self: ArrayList, array: Array, arrayIndex: int)CopyTo(self: ArrayList, array: Array) """
        pass

    @staticmethod
    def FixedSize(list):
        """
        FixedSize(list: ArrayList) -> ArrayList
        FixedSize(list: IList) -> IList
        """
        pass

    def GetEnumerator(self, index=None, count=None):
        """
        GetEnumerator(self: ArrayList, index: int, count: int) -> IEnumerator
        GetEnumerator(self: ArrayList) -> IEnumerator
        """
        pass

    def GetRange(self, index, count):
        """ GetRange(self: ArrayList, index: int, count: int) -> ArrayList """
        pass

    def IndexOf(self, value, startIndex=None, count=None):
        """
        IndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int
        IndexOf(self: ArrayList, value: object, startIndex: int) -> int
        IndexOf(self: ArrayList, value: object) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: ArrayList, index: int, value: object) """
        pass

    def InsertRange(self, index, c):
        """ InsertRange(self: ArrayList, index: int, c: ICollection) """
        pass

    def LastIndexOf(self, value, startIndex=None, count=None):
        """
        LastIndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int
        LastIndexOf(self: ArrayList, value: object, startIndex: int) -> int
        LastIndexOf(self: ArrayList, value: object) -> int
        """
        pass

    @staticmethod
    def ReadOnly(list):
        """
        ReadOnly(list: ArrayList) -> ArrayList
        ReadOnly(list: IList) -> IList
        """
        pass

    def Remove(self, obj):
        """ Remove(self: ArrayList, obj: object) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ArrayList, index: int) """
        pass

    def RemoveRange(self, index, count):
        """ RemoveRange(self: ArrayList, index: int, count: int) """
        pass

    @staticmethod
    def Repeat(value, count):
        """ Repeat(value: object, count: int) -> ArrayList """
        pass

    def Reverse(self, index=None, count=None):
        """ Reverse(self: ArrayList, index: int, count: int)Reverse(self: ArrayList) """
        pass

    def SetRange(self, index, c):
        """ SetRange(self: ArrayList, index: int, c: ICollection) """
        pass

    def Sort(self, *__args):
        """ Sort(self: ArrayList, index: int, count: int, comparer: IComparer)Sort(self: ArrayList, comparer: IComparer)Sort(self: ArrayList) """
        pass

    @staticmethod
    def Synchronized(list):
        """
        Synchronized(list: ArrayList) -> ArrayList
        Synchronized(list: IList) -> IList
        """
        pass

    def ToArray(self, type=None):
        """
        ToArray(self: ArrayList, type: Type) -> Array
        ToArray(self: ArrayList) -> Array[object]
        """
        pass

    def TrimToSize(self):
        """ TrimToSize(self: ArrayList) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
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
        __new__(cls: type, c: ICollection)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: ArrayList) -> int

Set: Capacity(self: ArrayList) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ArrayList) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: ArrayList) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ArrayList) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: ArrayList) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: ArrayList) -> object

"""



class BitArray(object):
    """
    BitArray(length: int)
    BitArray(length: int, defaultValue: bool)
    BitArray(bytes: Array[Byte])
    BitArray(values: Array[bool])
    BitArray(values: Array[int])
    BitArray(bits: BitArray)
    """
    def And(self, value):
        """ And(self: BitArray, value: BitArray) -> BitArray """
        pass

    def Clone(self):
        """ Clone(self: BitArray) -> object """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: BitArray, array: Array, index: int) """
        pass

    def Get(self, index):
        """ Get(self: BitArray, index: int) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BitArray) -> IEnumerator """
        pass

    def Not(self):
        """ Not(self: BitArray) -> BitArray """
        pass

    def Or(self, value):
        """ Or(self: BitArray, value: BitArray) -> BitArray """
        pass

    def Set(self, index, value):
        """ Set(self: BitArray, index: int, value: bool) """
        pass

    def SetAll(self, value):
        """ SetAll(self: BitArray, value: bool) """
        pass

    def Xor(self, value):
        """ Xor(self: BitArray, value: BitArray) -> BitArray """
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
        __new__(cls: type, length: int)
        __new__(cls: type, length: int, defaultValue: bool)
        __new__(cls: type, bytes: Array[Byte])
        __new__(cls: type, values: Array[bool])
        __new__(cls: type, values: Array[int])
        __new__(cls: type, bits: BitArray)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BitArray) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: BitArray) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: BitArray) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: BitArray) -> int

Set: Length(self: BitArray) = value
"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: BitArray) -> object

"""



class CaseInsensitiveComparer(object):
    """
    CaseInsensitiveComparer()
    CaseInsensitiveComparer(culture: CultureInfo)
    """
    def Compare(self, a, b):
        """ Compare(self: CaseInsensitiveComparer, a: object, b: object) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture=None):
        """
        __new__(cls: type)
        __new__(cls: type, culture: CultureInfo)
        """
        pass

    Default = None
    DefaultInvariant = None


class CaseInsensitiveHashCodeProvider(object):
    """
    CaseInsensitiveHashCodeProvider()
    CaseInsensitiveHashCodeProvider(culture: CultureInfo)
    """
    def GetHashCode(self, obj=None):
        """ GetHashCode(self: CaseInsensitiveHashCodeProvider, obj: object) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture=None):
        """
        __new__(cls: type)
        __new__(cls: type, culture: CultureInfo)
        """
        pass

    Default = None
    DefaultInvariant = None


class IEnumerable:
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: IEnumerable) -> IEnumerator """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ICollection(IEnumerable):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: ICollection, array: Array, index: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ICollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: ICollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: ICollection) -> object

"""



class IList(ICollection, IEnumerable):
    # no doc
    def Add(self, value):
        """ Add(self: IList, value: object) -> int """
        pass

    def Clear(self):
        """ Clear(self: IList) """
        pass

    def Contains(self, value):
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: IList, value: object) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: IList, index: int, value: object) """
        pass

    def Remove(self, value):
        """ Remove(self: IList, value: object) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: IList, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: IList) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: IList) -> bool

"""



class CollectionBase(object):
    # no doc
    def Clear(self):
        """ Clear(self: CollectionBase) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CollectionBase) -> IEnumerator """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: CollectionBase) """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: CollectionBase) """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """ OnInsert(self: CollectionBase, index: int, value: object) """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """ OnInsertComplete(self: CollectionBase, index: int, value: object) """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: CollectionBase, index: int, value: object) """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: CollectionBase, index: int, value: object) """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """ OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object) """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """ OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object) """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: CollectionBase, value: object) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CollectionBase, index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: CollectionBase) -> int

Set: Capacity(self: CollectionBase) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CollectionBase) -> int

"""

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Comparer(object):
    """ Comparer(culture: CultureInfo) """
    def Compare(self, a, b):
        """ Compare(self: Comparer, a: object, b: object) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Comparer, info: SerializationInfo, context: StreamingContext) """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture):
        """ __new__(cls: type, culture: CultureInfo) """
        pass

    Default = None
    DefaultInvariant = None


class IDictionary(ICollection, IEnumerable):
    # no doc
    def Add(self, key, value):
        """ Add(self: IDictionary, key: object, value: object) """
        pass

    def Clear(self):
        """ Clear(self: IDictionary) """
        pass

    def Contains(self, key):
        """ Contains(self: IDictionary, key: object) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IDictionary) -> IDictionaryEnumerator """
        pass

    def Remove(self, key):
        """ Remove(self: IDictionary, key: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: IDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: IDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: IDictionary) -> ICollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: IDictionary) -> ICollection

"""



class DictionaryBase(object):
    # no doc
    def Clear(self):
        """ Clear(self: DictionaryBase) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: DictionaryBase, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DictionaryBase) -> IDictionaryEnumerator """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: DictionaryBase) """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: DictionaryBase) """
        pass

    def OnGet(self, *args): #cannot find CLR method
        """ OnGet(self: DictionaryBase, key: object, currentValue: object) -> object """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """ OnInsert(self: DictionaryBase, key: object, value: object) """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """ OnInsertComplete(self: DictionaryBase, key: object, value: object) """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: DictionaryBase, key: object, value: object) """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: DictionaryBase, key: object, value: object) """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """ OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object) """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """ OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object) """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: DictionaryBase, key: object, value: object) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IDictionary, key: object) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DictionaryBase) -> int

"""

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InnerHashtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DictionaryEntry(object):
    """ DictionaryEntry(key: object, value: object) """
    @staticmethod # known case of __new__
    def __new__(self, key, value):
        """
        __new__[DictionaryEntry]() -> DictionaryEntry
        
        __new__(cls: type, key: object, value: object)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: DictionaryEntry) -> object

Set: Key(self: DictionaryEntry) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DictionaryEntry) -> object

Set: Value(self: DictionaryEntry) = value
"""



class Hashtable(object):
    """
    Hashtable()
    Hashtable(capacity: int)
    Hashtable(capacity: int, loadFactor: Single)
    Hashtable(capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)
    Hashtable(hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(equalityComparer: IEqualityComparer)
    Hashtable(capacity: int, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary)
    Hashtable(d: IDictionary, loadFactor: Single)
    Hashtable(d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
    """
    def Add(self, key, value):
        """ Add(self: Hashtable, key: object, value: object) """
        pass

    def Clear(self):
        """ Clear(self: Hashtable) """
        pass

    def Clone(self):
        """ Clone(self: Hashtable) -> object """
        pass

    def Contains(self, key):
        """ Contains(self: Hashtable, key: object) -> bool """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: Hashtable, key: object) -> bool """
        pass

    def ContainsValue(self, value):
        """ ContainsValue(self: Hashtable, value: object) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: Hashtable, array: Array, arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Hashtable) -> IDictionaryEnumerator """
        pass

    def GetHash(self, *args): #cannot find CLR method
        """ GetHash(self: Hashtable, key: object) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Hashtable, info: SerializationInfo, context: StreamingContext) """
        pass

    def KeyEquals(self, *args): #cannot find CLR method
        """ KeyEquals(self: Hashtable, item: object, key: object) -> bool """
        pass

    def OnDeserialization(self, sender):
        """ OnDeserialization(self: Hashtable, sender: object) """
        pass

    def Remove(self, key):
        """ Remove(self: Hashtable, key: object) """
        pass

    @staticmethod
    def Synchronized(table):
        """ Synchronized(table: Hashtable) -> Hashtable """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IDictionary, key: object) -> bool """
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
        __new__(cls: type, capacity: int, loadFactor: Single)
        __new__(cls: type, capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)
        __new__(cls: type, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, equalityComparer: IEqualityComparer)
        __new__(cls: type, capacity: int, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int, equalityComparer: IEqualityComparer)
        __new__(cls: type, d: IDictionary)
        __new__(cls: type, d: IDictionary, loadFactor: Single)
        __new__(cls: type, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, d: IDictionary, equalityComparer: IEqualityComparer)
        __new__(cls: type, d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Hashtable) -> int

"""

    EqualityComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hcp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: Hashtable) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Hashtable) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: Hashtable) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: Hashtable) -> ICollection

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: Hashtable) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: Hashtable) -> ICollection

"""



class IComparer:
    # no doc
    def Compare(self, x, y):
        """ Compare(self: IComparer, x: object, y: object) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumerator:
    # no doc
    def MoveNext(self):
        """ MoveNext(self: IEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: IEnumerator) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: IEnumerator) -> object

"""



class IDictionaryEnumerator(IEnumerator):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entry(self: IDictionaryEnumerator) -> DictionaryEntry

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: IDictionaryEnumerator) -> object

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: IDictionaryEnumerator) -> object

"""



class IEqualityComparer:
    # no doc
    def Equals(self, x, y):
        """ Equals(self: IEqualityComparer, x: object, y: object) -> bool """
        pass

    def GetHashCode(self, obj):
        """ GetHashCode(self: IEqualityComparer, obj: object) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IHashCodeProvider:
    # no doc
    def GetHashCode(self, obj):
        """ GetHashCode(self: IHashCodeProvider, obj: object) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStructuralComparable:
    # no doc
    def CompareTo(self, other, comparer):
        """ CompareTo(self: IStructuralComparable, other: object, comparer: IComparer) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class IStructuralEquatable:
    # no doc
    def Equals(self, other, comparer):
        """ Equals(self: IStructuralEquatable, other: object, comparer: IEqualityComparer) -> bool """
        pass

    def GetHashCode(self, comparer):
        """ GetHashCode(self: IStructuralEquatable, comparer: IEqualityComparer) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class Queue(object):
    """
    Queue()
    Queue(capacity: int)
    Queue(capacity: int, growFactor: Single)
    Queue(col: ICollection)
    """
    def Clear(self):
        """ Clear(self: Queue) """
        pass

    def Clone(self):
        """ Clone(self: Queue) -> object """
        pass

    def Contains(self, obj):
        """ Contains(self: Queue, obj: object) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Queue, array: Array, index: int) """
        pass

    def Dequeue(self):
        """ Dequeue(self: Queue) -> object """
        pass

    def Enqueue(self, obj):
        """ Enqueue(self: Queue, obj: object) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Queue) -> IEnumerator """
        pass

    def Peek(self):
        """ Peek(self: Queue) -> object """
        pass

    @staticmethod
    def Synchronized(queue):
        """ Synchronized(queue: Queue) -> Queue """
        pass

    def ToArray(self):
        """ ToArray(self: Queue) -> Array[object] """
        pass

    def TrimToSize(self):
        """ TrimToSize(self: Queue) """
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
        __new__(cls: type, capacity: int, growFactor: Single)
        __new__(cls: type, col: ICollection)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Queue) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: Queue) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: Queue) -> object

"""



class ReadOnlyCollectionBase(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ReadOnlyCollectionBase) -> IEnumerator """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ReadOnlyCollectionBase) -> int

"""

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SortedList(object):
    """
    SortedList()
    SortedList(initialCapacity: int)
    SortedList(comparer: IComparer)
    SortedList(comparer: IComparer, capacity: int)
    SortedList(d: IDictionary)
    SortedList(d: IDictionary, comparer: IComparer)
    """
    def Add(self, key, value):
        """ Add(self: SortedList, key: object, value: object) """
        pass

    def Clear(self):
        """ Clear(self: SortedList) """
        pass

    def Clone(self):
        """ Clone(self: SortedList) -> object """
        pass

    def Contains(self, key):
        """ Contains(self: SortedList, key: object) -> bool """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: SortedList, key: object) -> bool """
        pass

    def ContainsValue(self, value):
        """ ContainsValue(self: SortedList, value: object) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: SortedList, array: Array, arrayIndex: int) """
        pass

    def GetByIndex(self, index):
        """ GetByIndex(self: SortedList, index: int) -> object """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SortedList) -> IDictionaryEnumerator """
        pass

    def GetKey(self, index):
        """ GetKey(self: SortedList, index: int) -> object """
        pass

    def GetKeyList(self):
        """ GetKeyList(self: SortedList) -> IList """
        pass

    def GetValueList(self):
        """ GetValueList(self: SortedList) -> IList """
        pass

    def IndexOfKey(self, key):
        """ IndexOfKey(self: SortedList, key: object) -> int """
        pass

    def IndexOfValue(self, value):
        """ IndexOfValue(self: SortedList, value: object) -> int """
        pass

    def Remove(self, key):
        """ Remove(self: SortedList, key: object) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SortedList, index: int) """
        pass

    def SetByIndex(self, index, value):
        """ SetByIndex(self: SortedList, index: int, value: object) """
        pass

    @staticmethod
    def Synchronized(list):
        """ Synchronized(list: SortedList) -> SortedList """
        pass

    def TrimToSize(self):
        """ TrimToSize(self: SortedList) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IDictionary, key: object) -> bool """
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
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, comparer: IComparer)
        __new__(cls: type, comparer: IComparer, capacity: int)
        __new__(cls: type, d: IDictionary)
        __new__(cls: type, d: IDictionary, comparer: IComparer)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: SortedList) -> int

Set: Capacity(self: SortedList) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SortedList) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: SortedList) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: SortedList) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: SortedList) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: SortedList) -> ICollection

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: SortedList) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: SortedList) -> ICollection

"""



class Stack(object):
    """
    Stack()
    Stack(initialCapacity: int)
    Stack(col: ICollection)
    """
    def Clear(self):
        """ Clear(self: Stack) """
        pass

    def Clone(self):
        """ Clone(self: Stack) -> object """
        pass

    def Contains(self, obj):
        """ Contains(self: Stack, obj: object) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Stack, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Stack) -> IEnumerator """
        pass

    def Peek(self):
        """ Peek(self: Stack) -> object """
        pass

    def Pop(self):
        """ Pop(self: Stack) -> object """
        pass

    def Push(self, obj):
        """ Push(self: Stack, obj: object) """
        pass

    @staticmethod
    def Synchronized(stack):
        """ Synchronized(stack: Stack) -> Stack """
        pass

    def ToArray(self):
        """ ToArray(self: Stack) -> Array[object] """
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
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, col: ICollection)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Stack) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: Stack) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: Stack) -> object

"""



class StructuralComparisons(object):
    # no doc
    StructuralComparer = None
    StructuralEqualityComparer = None
    __all__ = []


# variables with complex values


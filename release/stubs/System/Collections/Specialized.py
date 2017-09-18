# encoding: utf-8
# module System.Collections.Specialized calls itself Specialized
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitVector32(object):
    """
    Provides a simple structure that stores Boolean values and small integers in 32 bits of memory.
    
    BitVector32(data: int)
    BitVector32(value: BitVector32)
    """
    @staticmethod
    def CreateMask(previous=None):
        """
        CreateMask(previous: int) -> int
        
            Creates an additional mask following the specified mask in a series of masks that can be used to 
             retrieve individual bits in a System.Collections.Specialized.BitVector32 that is set up as bit 
             flags.
        
        
            previous: The mask that indicates the previous bit flag.
            Returns: A mask that isolates the bit flag following the one that previous points to in 
             System.Collections.Specialized.BitVector32.
        
        CreateMask() -> int
        
            Creates the first mask in a series of masks that can be used to retrieve individual bits in a 
             System.Collections.Specialized.BitVector32 that is set up as bit flags.
        
            Returns: A mask that isolates the first bit flag in the System.Collections.Specialized.BitVector32.
        """
        pass

    @staticmethod
    def CreateSection(maxValue, previous=None):
        """
        CreateSection(maxValue: Int16, previous: Section) -> Section
        CreateSection(maxValue: Int16) -> Section
        
            Creates the first System.Collections.Specialized.BitVector32.Section in a series of sections 
             that contain small integers.
        
        
            maxValue: A 16-bit signed integer that specifies the maximum value for the new 
             System.Collections.Specialized.BitVector32.Section.
        
            Returns: A System.Collections.Specialized.BitVector32.Section that can hold a number from zero to 
             maxValue.
        """
        pass

    def Equals(self, o):
        """
        Equals(self: BitVector32, o: object) -> bool
        
            Determines whether the specified object is equal to the 
             System.Collections.Specialized.BitVector32.
        
        
            o: The object to compare with the current System.Collections.Specialized.BitVector32.
            Returns: true if the specified object is equal to the System.Collections.Specialized.BitVector32; 
             otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: BitVector32) -> int
        
            Serves as a hash function for the System.Collections.Specialized.BitVector32.
            Returns: A hash code for the System.Collections.Specialized.BitVector32.
        """
        pass

    @staticmethod
    def ToString(value=None):
        """
        ToString(self: BitVector32) -> str
        
            Returns a string that represents the current System.Collections.Specialized.BitVector32.
            Returns: A string that represents the current System.Collections.Specialized.BitVector32.
        ToString(value: BitVector32) -> str
        
            Returns a string that represents the specified System.Collections.Specialized.BitVector32.
        
            value: The System.Collections.Specialized.BitVector32 to represent.
            Returns: A string that represents the specified System.Collections.Specialized.BitVector32.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[BitVector32]() -> BitVector32
        
        __new__(cls: type, data: int)
        __new__(cls: type, value: BitVector32)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the System.Collections.Specialized.BitVector32 as an integer.

Get: Data(self: BitVector32) -> int

"""


    Section = None


class CollectionsUtil(object):
    """
    Creates collections that ignore the case in strings.
    
    CollectionsUtil()
    """
    @staticmethod
    def CreateCaseInsensitiveHashtable(*__args):
        """
        CreateCaseInsensitiveHashtable(d: IDictionary) -> Hashtable
        
            Copies the entries from the specified dictionary to a new case-insensitive instance of the 
             System.Collections.Hashtable class with the same initial capacity as the number of entries 
             copied.
        
        
            d: The System.Collections.IDictionary to copy to a new case-insensitive 
             System.Collections.Hashtable.
        
            Returns: A new case-insensitive instance of the System.Collections.Hashtable class containing the entries 
             from the specified System.Collections.IDictionary.
        
        CreateCaseInsensitiveHashtable() -> Hashtable
        
            Creates a new case-insensitive instance of the System.Collections.Hashtable class with the 
             default initial capacity.
        
            Returns: A new case-insensitive instance of the System.Collections.Hashtable class with the default 
             initial capacity.
        
        CreateCaseInsensitiveHashtable(capacity: int) -> Hashtable
        
            Creates a new case-insensitive instance of the System.Collections.Hashtable class with the 
             specified initial capacity.
        
        
            capacity: The approximate number of entries that the System.Collections.Hashtable can initially contain.
            Returns: A new case-insensitive instance of the System.Collections.Hashtable class with the specified 
             initial capacity.
        """
        pass

    @staticmethod
    def CreateCaseInsensitiveSortedList():
        """
        CreateCaseInsensitiveSortedList() -> SortedList
        
            Creates a new instance of the System.Collections.SortedList class that ignores the case of 
             strings.
        
            Returns: A new instance of the System.Collections.SortedList class that ignores the case of strings.
        """
        pass


class HybridDictionary(object, IDictionary, ICollection, IEnumerable):
    """
    Implements IDictionary by using a System.Collections.Specialized.ListDictionary while the collection is small, and then switching to a System.Collections.Hashtable when the collection gets large.
    
    HybridDictionary()
    HybridDictionary(initialSize: int)
    HybridDictionary(caseInsensitive: bool)
    HybridDictionary(initialSize: int, caseInsensitive: bool)
    """
    def Add(self, key, value):
        """
        Add(self: HybridDictionary, key: object, value: object)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.HybridDictionary.
        
        
            key: The key of the entry to add.
            value: The value of the entry to add. The value can be null.
        """
        pass

    def Clear(self):
        """
        Clear(self: HybridDictionary)
            Removes all entries from the System.Collections.Specialized.HybridDictionary.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: HybridDictionary, key: object) -> bool
        
            Determines whether the System.Collections.Specialized.HybridDictionary contains a specific key.
        
            key: The key to locate in the System.Collections.Specialized.HybridDictionary.
            Returns: true if the System.Collections.Specialized.HybridDictionary contains an entry with the specified 
             key; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: HybridDictionary, array: Array, index: int)
            Copies the System.Collections.Specialized.HybridDictionary entries to a one-dimensional 
             System.Array instance at the specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the 
             System.Collections.DictionaryEntry objects copied from 
             System.Collections.Specialized.HybridDictionary. The System.Array must have zero-based indexing.
        
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HybridDictionary) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that iterates through the 
             System.Collections.Specialized.HybridDictionary.
        
            Returns: An System.Collections.IDictionaryEnumerator for the 
             System.Collections.Specialized.HybridDictionary.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: HybridDictionary, key: object)
            Removes the entry with the specified key from the 
             System.Collections.Specialized.HybridDictionary.
        
        
            key: The key of the entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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
        __new__(cls: type, initialSize: int)
        __new__(cls: type, caseInsensitive: bool)
        __new__(cls: type, initialSize: int, caseInsensitive: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Specialized.HybridDictionary.

Get: Count(self: HybridDictionary) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.HybridDictionary has a fixed size.

Get: IsFixedSize(self: HybridDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.HybridDictionary is read-only.

Get: IsReadOnly(self: HybridDictionary) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.HybridDictionary is synchronized (thread safe).

Get: IsSynchronized(self: HybridDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection containing the keys in the System.Collections.Specialized.HybridDictionary.

Get: Keys(self: HybridDictionary) -> ICollection

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Collections.Specialized.HybridDictionary.

Get: SyncRoot(self: HybridDictionary) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection containing the values in the System.Collections.Specialized.HybridDictionary.

Get: Values(self: HybridDictionary) -> ICollection

"""



class INotifyCollectionChanged:
    """ Notifies listeners of dynamic changes, such as when items get added and removed or the whole list is refreshed. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CollectionChanged = None


class IOrderedDictionary(IDictionary, ICollection, IEnumerable):
    """ Represents an indexed collection of key/value pairs. """
    def GetEnumerator(self):
        """
        GetEnumerator(self: IOrderedDictionary) -> IDictionaryEnumerator
        
            Returns an enumerator that iterates through the 
             System.Collections.Specialized.IOrderedDictionary collection.
        
            Returns: An System.Collections.IDictionaryEnumerator for the entire 
             System.Collections.Specialized.IOrderedDictionary collection.
        """
        pass

    def Insert(self, index, key, value):
        """
        Insert(self: IOrderedDictionary, index: int, key: object, value: object)
            Inserts a key/value pair into the collection at the specified index.
        
            index: The zero-based index at which the key/value pair should be inserted.
            key: The object to use as the key of the element to add.
            value: The object to use as the value of the element to add.  The value can be null.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: IOrderedDictionary, index: int)
            Removes the element at the specified index.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
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


class ListDictionary(object, IDictionary, ICollection, IEnumerable):
    """
    Implements IDictionary using a singly linked list. Recommended for collections that typically contain 10 items or less.
    
    ListDictionary()
    ListDictionary(comparer: IComparer)
    """
    def Add(self, key, value):
        """
        Add(self: ListDictionary, key: object, value: object)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.ListDictionary.
        
        
            key: The key of the entry to add.
            value: The value of the entry to add. The value can be null.
        """
        pass

    def Clear(self):
        """
        Clear(self: ListDictionary)
            Removes all entries from the System.Collections.Specialized.ListDictionary.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: ListDictionary, key: object) -> bool
        
            Determines whether the System.Collections.Specialized.ListDictionary contains a specific key.
        
            key: The key to locate in the System.Collections.Specialized.ListDictionary.
            Returns: true if the System.Collections.Specialized.ListDictionary contains an entry with the specified 
             key; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ListDictionary, array: Array, index: int)
            Copies the System.Collections.Specialized.ListDictionary entries to a one-dimensional 
             System.Array instance at the specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the 
             System.Collections.DictionaryEntry objects copied from 
             System.Collections.Specialized.ListDictionary. The System.Array must have zero-based indexing.
        
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ListDictionary) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that iterates through the 
             System.Collections.Specialized.ListDictionary.
        
            Returns: An System.Collections.IDictionaryEnumerator for the 
             System.Collections.Specialized.ListDictionary.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: ListDictionary, key: object)
            Removes the entry with the specified key from the System.Collections.Specialized.ListDictionary.
        
            key: The key of the entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, comparer=None):
        """
        __new__(cls: type)
        __new__(cls: type, comparer: IComparer)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Specialized.ListDictionary.

Get: Count(self: ListDictionary) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.ListDictionary has a fixed size.

Get: IsFixedSize(self: ListDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.ListDictionary is read-only.

Get: IsReadOnly(self: ListDictionary) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.ListDictionary is synchronized (thread safe).

Get: IsSynchronized(self: ListDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection containing the keys in the System.Collections.Specialized.ListDictionary.

Get: Keys(self: ListDictionary) -> ICollection

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Collections.Specialized.ListDictionary.

Get: SyncRoot(self: ListDictionary) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection containing the values in the System.Collections.Specialized.ListDictionary.

Get: Values(self: ListDictionary) -> ICollection

"""



class NameObjectCollectionBase(object, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    """ Provides the abstract base class for a collection of associated System.String keys and System.Object values that can be accessed either with the key or with the index. """
    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: NameObjectCollectionBase, name: str, value: object)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to add. The key can be null.
            value: The System.Object value of the entry to add. The value can be null.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: NameObjectCollectionBase)
            Removes all entries from the System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: NameObjectCollectionBase, index: int) -> object
        
            Gets the value of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the value to get.
            Returns: An System.Object that represents the value of the entry at the specified index.
        BaseGet(self: NameObjectCollectionBase, name: str) -> object
        
            Gets the value of the first entry with the specified key from the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to get. The key can be null.
            Returns: An System.Object that represents the value of the first entry with the specified key, if found; 
             otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: NameObjectCollectionBase) -> Array[str]
        
            Returns a System.String array that contains all the keys in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
            Returns: A System.String array that contains all the keys in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGetAllValues(self, *args): #cannot find CLR method
        """
        BaseGetAllValues(self: NameObjectCollectionBase, type: Type) -> Array[object]
        
            Returns an array of the specified type that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            type: A System.Type that represents the type of array to return.
            Returns: An array of the specified type that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        BaseGetAllValues(self: NameObjectCollectionBase) -> Array[object]
        
            Returns an System.Object array that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
            Returns: An System.Object array that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: NameObjectCollectionBase, index: int) -> str
        
            Gets the key of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the key to get.
            Returns: A System.String that represents the key of the entry at the specified index.
        """
        pass

    def BaseHasKeys(self, *args): #cannot find CLR method
        """
        BaseHasKeys(self: NameObjectCollectionBase) -> bool
        
            Gets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase 
             instance contains entries whose keys are not null.
        
            Returns: true if the System.Collections.Specialized.NameObjectCollectionBase instance contains entries 
             whose keys are not null; otherwise, false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: NameObjectCollectionBase, name: str)
            Removes the entries with the specified key from the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entries to remove. The key can be null.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: NameObjectCollectionBase, index: int)
            Removes the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the entry to remove.
        """
        pass

    def BaseSet(self, *args): #cannot find CLR method
        """
        BaseSet(self: NameObjectCollectionBase, index: int, value: object)
            Sets the value of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the entry to set.
            value: The System.Object that represents the new value of the entry to set. The value can be null.
        BaseSet(self: NameObjectCollectionBase, name: str, value: object)
            Sets the value of the first entry with the specified key in the 
             System.Collections.Specialized.NameObjectCollectionBase instance, if found; otherwise, adds an 
             entry with the specified key and value into the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to set. The key can be null.
            value: The System.Object that represents the new value of the entry to set. The value can be null.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: NameObjectCollectionBase) -> IEnumerator
        
            Returns an enumerator that iterates through the 
             System.Collections.Specialized.NameObjectCollectionBase.
        
            Returns: An System.Collections.IEnumerator for the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: NameObjectCollectionBase, info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed 
             to serialize the System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            info: A System.Runtime.Serialization.SerializationInfo object that contains the information required 
             to serialize the System.Collections.Specialized.NameObjectCollectionBase instance.
        
            context: A System.Runtime.Serialization.StreamingContext object that contains the source and destination 
             of the serialized stream associated with the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def OnDeserialization(self, sender):
        """
        OnDeserialization(self: NameObjectCollectionBase, sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface and raises the 
             deserialization event when the deserialization is complete.
        
        
            sender: The source of the deserialization event.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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
        __new__(cls: type, equalityComparer: IEqualityComparer)
        __new__(cls: type, capacity: int, equalityComparer: IEqualityComparer)
        __new__(cls: type, hashProvider: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Specialized.NameObjectCollectionBase instance.

Get: Count(self: NameObjectCollectionBase) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase instance is read-only.

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Specialized.NameObjectCollectionBase.KeysCollection instance that contains all the keys in the System.Collections.Specialized.NameObjectCollectionBase instance.

Get: Keys(self: NameObjectCollectionBase) -> KeysCollection

"""


    KeysCollection = None


class NameValueCollection(NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    """
    Represents a collection of associated System.String keys and System.String values that can be accessed either with the key or with the index.
    
    NameValueCollection()
    NameValueCollection(col: NameValueCollection)
    NameValueCollection(hashProvider: IHashCodeProvider, comparer: IComparer)
    NameValueCollection(capacity: int)
    NameValueCollection(equalityComparer: IEqualityComparer)
    NameValueCollection(capacity: int, equalityComparer: IEqualityComparer)
    NameValueCollection(capacity: int, col: NameValueCollection)
    NameValueCollection(capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer)
    """
    def Add(self, *__args):
        """
        Add(self: NameValueCollection, name: str, value: str)
            Adds an entry with the specified name and value to the 
             System.Collections.Specialized.NameValueCollection.
        
        
            name: The System.String key of the entry to add. The key can be null.
            value: The System.String value of the entry to add. The value can be null.
        Add(self: NameValueCollection, c: NameValueCollection)
            Copies the entries in the specified System.Collections.Specialized.NameValueCollection to the 
             current System.Collections.Specialized.NameValueCollection.
        
        
            c: The System.Collections.Specialized.NameValueCollection to copy to the current 
             System.Collections.Specialized.NameValueCollection.
        """
        pass

    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: NameObjectCollectionBase, name: str, value: object)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to add. The key can be null.
            value: The System.Object value of the entry to add. The value can be null.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: NameObjectCollectionBase)
            Removes all entries from the System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: NameObjectCollectionBase, index: int) -> object
        
            Gets the value of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the value to get.
            Returns: An System.Object that represents the value of the entry at the specified index.
        BaseGet(self: NameObjectCollectionBase, name: str) -> object
        
            Gets the value of the first entry with the specified key from the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to get. The key can be null.
            Returns: An System.Object that represents the value of the first entry with the specified key, if found; 
             otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: NameObjectCollectionBase) -> Array[str]
        
            Returns a System.String array that contains all the keys in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
            Returns: A System.String array that contains all the keys in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGetAllValues(self, *args): #cannot find CLR method
        """
        BaseGetAllValues(self: NameObjectCollectionBase, type: Type) -> Array[object]
        
            Returns an array of the specified type that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            type: A System.Type that represents the type of array to return.
            Returns: An array of the specified type that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        BaseGetAllValues(self: NameObjectCollectionBase) -> Array[object]
        
            Returns an System.Object array that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
            Returns: An System.Object array that contains all the values in the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: NameObjectCollectionBase, index: int) -> str
        
            Gets the key of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the key to get.
            Returns: A System.String that represents the key of the entry at the specified index.
        """
        pass

    def BaseHasKeys(self, *args): #cannot find CLR method
        """
        BaseHasKeys(self: NameObjectCollectionBase) -> bool
        
            Gets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase 
             instance contains entries whose keys are not null.
        
            Returns: true if the System.Collections.Specialized.NameObjectCollectionBase instance contains entries 
             whose keys are not null; otherwise, false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: NameObjectCollectionBase, name: str)
            Removes the entries with the specified key from the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entries to remove. The key can be null.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: NameObjectCollectionBase, index: int)
            Removes the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the entry to remove.
        """
        pass

    def BaseSet(self, *args): #cannot find CLR method
        """
        BaseSet(self: NameObjectCollectionBase, index: int, value: object)
            Sets the value of the entry at the specified index of the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            index: The zero-based index of the entry to set.
            value: The System.Object that represents the new value of the entry to set. The value can be null.
        BaseSet(self: NameObjectCollectionBase, name: str, value: object)
            Sets the value of the first entry with the specified key in the 
             System.Collections.Specialized.NameObjectCollectionBase instance, if found; otherwise, adds an 
             entry with the specified key and value into the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to set. The key can be null.
            value: The System.Object that represents the new value of the entry to set. The value can be null.
        """
        pass

    def Clear(self):
        """
        Clear(self: NameValueCollection)
            Invalidates the cached arrays and removes all entries from the 
             System.Collections.Specialized.NameValueCollection.
        """
        pass

    def CopyTo(self, dest, index):
        """
        CopyTo(self: NameValueCollection, dest: Array, index: int)
            Copies the entire System.Collections.Specialized.NameValueCollection to a compatible 
             one-dimensional System.Array, starting at the specified index of the target array.
        
        
            dest: The one-dimensional System.Array that is the destination of the elements copied from 
             System.Collections.Specialized.NameValueCollection. The System.Array must have zero-based 
             indexing.
        
            index: The zero-based index in dest at which copying begins.
        """
        pass

    def Get(self, *__args):
        """
        Get(self: NameValueCollection, index: int) -> str
        
            Gets the values at the specified index of the System.Collections.Specialized.NameValueCollection 
             combined into one comma-separated list.
        
        
            index: The zero-based index of the entry that contains the values to get from the collection.
            Returns: A System.String that contains a comma-separated list of the values at the specified index of the 
             System.Collections.Specialized.NameValueCollection, if found; otherwise, null.
        
        Get(self: NameValueCollection, name: str) -> str
        
            Gets the values associated with the specified key from the 
             System.Collections.Specialized.NameValueCollection combined into one comma-separated list.
        
        
            name: The System.String key of the entry that contains the values to get. The key can be null.
            Returns: A System.String that contains a comma-separated list of the values associated with the specified 
             key from the System.Collections.Specialized.NameValueCollection, if found; otherwise, null.
        """
        pass

    def GetKey(self, index):
        """
        GetKey(self: NameValueCollection, index: int) -> str
        
            Gets the key at the specified index of the System.Collections.Specialized.NameValueCollection.
        
            index: The zero-based index of the key to get from the collection.
            Returns: A System.String that contains the key at the specified index of the 
             System.Collections.Specialized.NameValueCollection, if found; otherwise, null.
        """
        pass

    def GetValues(self, *__args):
        """
        GetValues(self: NameValueCollection, index: int) -> Array[str]
        
            Gets the values at the specified index of the System.Collections.Specialized.NameValueCollection.
        
            index: The zero-based index of the entry that contains the values to get from the collection.
            Returns: A System.String array that contains the values at the specified index of the 
             System.Collections.Specialized.NameValueCollection, if found; otherwise, null.
        
        GetValues(self: NameValueCollection, name: str) -> Array[str]
        
            Gets the values associated with the specified key from the 
             System.Collections.Specialized.NameValueCollection.
        
        
            name: The System.String key of the entry that contains the values to get. The key can be null.
            Returns: A System.String array that contains the values associated with the specified key from the 
             System.Collections.Specialized.NameValueCollection, if found; otherwise, null.
        """
        pass

    def HasKeys(self):
        """
        HasKeys(self: NameValueCollection) -> bool
        
            Gets a value indicating whether the System.Collections.Specialized.NameValueCollection contains 
             keys that are not null.
        
            Returns: true if the System.Collections.Specialized.NameValueCollection contains keys that are not null; 
             otherwise, false.
        """
        pass

    def InvalidateCachedArrays(self, *args): #cannot find CLR method
        """
        InvalidateCachedArrays(self: NameValueCollection)
            Resets the cached arrays of the collection to null.
        """
        pass

    def Remove(self, name):
        """
        Remove(self: NameValueCollection, name: str)
            Removes the entries with the specified key from the 
             System.Collections.Specialized.NameObjectCollectionBase instance.
        
        
            name: The System.String key of the entry to remove. The key can be null.
        """
        pass

    def Set(self, name, value):
        """
        Set(self: NameValueCollection, name: str, value: str)
            Sets the value of an entry in the System.Collections.Specialized.NameValueCollection.
        
            name: The System.String key of the entry to add the new value to. The key can be null.
            value: The System.Object that represents the new value to add to the specified entry. The value can be 
             null.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, col: NameValueCollection)
        __new__(cls: type, hashProvider: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int)
        __new__(cls: type, equalityComparer: IEqualityComparer)
        __new__(cls: type, capacity: int, equalityComparer: IEqualityComparer)
        __new__(cls: type, capacity: int, col: NameValueCollection)
        __new__(cls: type, capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    AllKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the keys in the System.Collections.Specialized.NameValueCollection.

Get: AllKeys(self: NameValueCollection) -> Array[str]

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase instance is read-only.

"""



class NotifyCollectionChangedAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the action that caused a System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event.
    
    enum NotifyCollectionChangedAction, values: Add (0), Move (3), Remove (1), Replace (2), Reset (4)
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

    Add = None
    Move = None
    Remove = None
    Replace = None
    Reset = None
    value__ = None


class NotifyCollectionChangedEventArgs(EventArgs):
    """
    Provides data for the System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event.
    
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object, index: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItem: object, oldItem: object)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, action, *__args):
        """
        __new__(cls: type, action: NotifyCollectionChangedAction)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object, index: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItem: object, oldItem: object)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int)
        """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the action that caused the event.

Get: Action(self: NotifyCollectionChangedEventArgs) -> NotifyCollectionChangedAction

"""

    NewItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of new items involved in the change.

Get: NewItems(self: NotifyCollectionChangedEventArgs) -> IList

"""

    NewStartingIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index at which the change occurred.

Get: NewStartingIndex(self: NotifyCollectionChangedEventArgs) -> int

"""

    OldItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of items affected by a System.Collections.Specialized.NotifyCollectionChangedAction.Replace, Remove, or Move action.

Get: OldItems(self: NotifyCollectionChangedEventArgs) -> IList

"""

    OldStartingIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index at which a System.Collections.Specialized.NotifyCollectionChangedAction.Move, Remove, or Replace action occurred.

Get: OldStartingIndex(self: NotifyCollectionChangedEventArgs) -> int

"""



class NotifyCollectionChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event.
    
    NotifyCollectionChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: NotifyCollectionChangedEventHandler, sender: object, e: NotifyCollectionChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: NotifyCollectionChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: NotifyCollectionChangedEventHandler, sender: object, e: NotifyCollectionChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class OrderedDictionary(object, IOrderedDictionary, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    """
    Represents a collection of key/value pairs that are accessible by the key or index.
    
    OrderedDictionary()
    OrderedDictionary(capacity: int)
    OrderedDictionary(comparer: IEqualityComparer)
    OrderedDictionary(capacity: int, comparer: IEqualityComparer)
    """
    def Add(self, key, value):
        """
        Add(self: OrderedDictionary, key: object, value: object)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.OrderedDictionary collection with the lowest available index.
        
        
            key: The key of the entry to add.
            value: The value of the entry to add. This value can be null.
        """
        pass

    def AsReadOnly(self):
        """
        AsReadOnly(self: OrderedDictionary) -> OrderedDictionary
        
            Returns a read-only copy of the current System.Collections.Specialized.OrderedDictionary 
             collection.
        
            Returns: A read-only copy of the current System.Collections.Specialized.OrderedDictionary collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: OrderedDictionary)
            Removes all elements from the System.Collections.Specialized.OrderedDictionary collection.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: OrderedDictionary, key: object) -> bool
        
            Determines whether the System.Collections.Specialized.OrderedDictionary collection contains a 
             specific key.
        
        
            key: The key to locate in the System.Collections.Specialized.OrderedDictionary collection.
            Returns: true if the System.Collections.Specialized.OrderedDictionary collection contains an element with 
             the specified key; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: OrderedDictionary, array: Array, index: int)
            Copies the System.Collections.Specialized.OrderedDictionary elements to a one-dimensional 
             System.Array object at the specified index.
        
        
            array: The one-dimensional System.Array object that is the destination of the 
             System.Collections.DictionaryEntry objects copied from 
             System.Collections.Specialized.OrderedDictionary collection. The System.Array must have 
             zero-based indexing.
        
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: OrderedDictionary) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator object that iterates through the 
             System.Collections.Specialized.OrderedDictionary collection.
        
            Returns: An System.Collections.IDictionaryEnumerator object for the 
             System.Collections.Specialized.OrderedDictionary collection.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: OrderedDictionary, info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed 
             to serialize the System.Collections.Specialized.OrderedDictionary collection.
        
        
            info: A System.Runtime.Serialization.SerializationInfo object containing the information required to 
             serialize the System.Collections.Specialized.OrderedDictionary collection.
        
            context: A System.Runtime.Serialization.StreamingContext object containing the source and destination of 
             the serialized stream associated with the System.Collections.Specialized.OrderedDictionary.
        """
        pass

    def Insert(self, index, key, value):
        """
        Insert(self: OrderedDictionary, index: int, key: object, value: object)
            Inserts a new entry into the System.Collections.Specialized.OrderedDictionary collection with 
             the specified key and value at the specified index.
        
        
            index: The zero-based index at which the element should be inserted.
            key: The key of the entry to add.
            value: The value of the entry to add. The value can be null.
        """
        pass

    def OnDeserialization(self, *args): #cannot find CLR method
        """
        OnDeserialization(self: OrderedDictionary, sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface and is called back by the 
             deserialization event when deserialization is complete.
        
        
            sender: The source of the deserialization event.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: OrderedDictionary, key: object)
            Removes the entry with the specified key from the 
             System.Collections.Specialized.OrderedDictionary collection.
        
        
            key: The key of the entry to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: OrderedDictionary, index: int)
            Removes the entry at the specified index from the 
             System.Collections.Specialized.OrderedDictionary collection.
        
        
            index: The zero-based index of the entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, comparer: IEqualityComparer)
        __new__(cls: type, capacity: int, comparer: IEqualityComparer)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/values pairs contained in the System.Collections.Specialized.OrderedDictionary collection.

Get: Count(self: OrderedDictionary) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.OrderedDictionary collection is read-only.

Get: IsReadOnly(self: OrderedDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection object containing the keys in the System.Collections.Specialized.OrderedDictionary collection.

Get: Keys(self: OrderedDictionary) -> ICollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ICollection object containing the values in the System.Collections.Specialized.OrderedDictionary collection.

Get: Values(self: OrderedDictionary) -> ICollection

"""



class StringCollection(object, IList, ICollection, IEnumerable):
    """
    Represents a collection of strings.
    
    StringCollection()
    """
    def Add(self, value):
        """
        Add(self: StringCollection, value: str) -> int
        
            Adds a string to the end of the System.Collections.Specialized.StringCollection.
        
            value: The string to add to the end of the System.Collections.Specialized.StringCollection. The value 
             can be null.
        
            Returns: The zero-based index at which the new element is inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: StringCollection, value: Array[str])
            Copies the elements of a string array to the end of the 
             System.Collections.Specialized.StringCollection.
        
        
            value: An array of strings to add to the end of the System.Collections.Specialized.StringCollection. 
             The array itself can not be null but it can contain elements that are null.
        """
        pass

    def Clear(self):
        """
        Clear(self: StringCollection)
            Removes all the strings from the System.Collections.Specialized.StringCollection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: StringCollection, value: str) -> bool
        
            Determines whether the specified string is in the 
             System.Collections.Specialized.StringCollection.
        
        
            value: The string to locate in the System.Collections.Specialized.StringCollection. The value can be 
             null.
        
            Returns: true if value is found in the System.Collections.Specialized.StringCollection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: StringCollection, array: Array[str], index: int)
            Copies the entire System.Collections.Specialized.StringCollection values to a one-dimensional 
             array of strings, starting at the specified index of the target array.
        
        
            array: The one-dimensional array of strings that is the destination of the elements copied from 
             System.Collections.Specialized.StringCollection. The System.Array must have zero-based indexing.
        
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: StringCollection) -> StringEnumerator
        
            Returns a System.Collections.Specialized.StringEnumerator that iterates through the 
             System.Collections.Specialized.StringCollection.
        
            Returns: A System.Collections.Specialized.StringEnumerator for the 
             System.Collections.Specialized.StringCollection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: StringCollection, value: str) -> int
        
            Searches for the specified string and returns the zero-based index of the first occurrence 
             within the System.Collections.Specialized.StringCollection.
        
        
            value: The string to locate. The value can be null.
            Returns: The zero-based index of the first occurrence of value in the 
             System.Collections.Specialized.StringCollection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: StringCollection, index: int, value: str)
            Inserts a string into the System.Collections.Specialized.StringCollection at the specified index.
        
            index: The zero-based index at which value is inserted.
            value: The string to insert. The value can be null.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: StringCollection, value: str)
            Removes the first occurrence of a specific string from the 
             System.Collections.Specialized.StringCollection.
        
        
            value: The string to remove from the System.Collections.Specialized.StringCollection. The value can be 
             null.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: StringCollection, index: int)
            Removes the string at the specified index of the System.Collections.Specialized.StringCollection.
        
            index: The zero-based index of the string to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of strings contained in the System.Collections.Specialized.StringCollection.

Get: Count(self: StringCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Specialized.StringCollection is read-only.

Get: IsReadOnly(self: StringCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to the System.Collections.Specialized.StringCollection is synchronized (thread safe).

Get: IsSynchronized(self: StringCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Collections.Specialized.StringCollection.

Get: SyncRoot(self: StringCollection) -> object

"""



class StringDictionary(object, IEnumerable):
    """
    Implements a hash table with the key and the value strongly typed to be strings rather than objects.
    
    StringDictionary()
    """
    def Add(self, key, value):
        """
        Add(self: StringDictionary, key: str, value: str)
            Adds an entry with the specified key and value into the 
             System.Collections.Specialized.StringDictionary.
        
        
            key: The key of the entry to add.
            value: The value of the entry to add. The value can be null.
        """
        pass

    def Clear(self):
        """
        Clear(self: StringDictionary)
            Removes all entries from the System.Collections.Specialized.StringDictionary.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: StringDictionary, key: str) -> bool
        
            Determines if the System.Collections.Specialized.StringDictionary contains a specific key.
        
            key: The key to locate in the System.Collections.Specialized.StringDictionary.
            Returns: true if the System.Collections.Specialized.StringDictionary contains an entry with the specified 
             key; otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        """
        ContainsValue(self: StringDictionary, value: str) -> bool
        
            Determines if the System.Collections.Specialized.StringDictionary contains a specific value.
        
            value: The value to locate in the System.Collections.Specialized.StringDictionary. The value can be 
             null.
        
            Returns: true if the System.Collections.Specialized.StringDictionary contains an element with the 
             specified value; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: StringDictionary, array: Array, index: int)
            Copies the string dictionary values to a one-dimensional System.Array instance at the specified 
             index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             System.Collections.Specialized.StringDictionary.
        
            index: The index in the array where copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: StringDictionary) -> IEnumerator
        
            Returns an enumerator that iterates through the string dictionary.
            Returns: An System.Collections.IEnumerator that iterates through the string dictionary.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: StringDictionary, key: str)
            Removes the entry with the specified key from the string dictionary.
        
            key: The key of the entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs in the System.Collections.Specialized.StringDictionary.

Get: Count(self: StringDictionary) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to the System.Collections.Specialized.StringDictionary is synchronized (thread safe).

Get: IsSynchronized(self: StringDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of keys in the System.Collections.Specialized.StringDictionary.

Get: Keys(self: StringDictionary) -> ICollection

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Collections.Specialized.StringDictionary.

Get: SyncRoot(self: StringDictionary) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of values in the System.Collections.Specialized.StringDictionary.

Get: Values(self: StringDictionary) -> ICollection

"""



class StringEnumerator(object):
    """ Supports a simple iteration over a System.Collections.Specialized.StringCollection. """
    def MoveNext(self):
        """
        MoveNext(self: StringEnumerator) -> bool
        
            Advances the enumerator to the next element of the collection.
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def Reset(self):
        """
        Reset(self: StringEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the collection.
        """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the collection.

Get: Current(self: StringEnumerator) -> str

"""




# encoding: utf-8
# module System.Collections.Generic calls itself Generic
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Comparer(object, IComparer, IComparer[T]):
    # no doc
    def Compare(self, x, y):
        """
        Compare(self: Comparer[T], x: T, y: T) -> int
        
            When overridden in a derived class, performs a comparison of two objects of the same type and 
             returns a value indicating whether one object is less than, equal to, or greater than the other.
        
        
            x: The first object to compare.
            y: The second object to compare.
            Returns: A signed integer that indicates the relative values of x and y, as shown in the following 
             table.Value Meaning Less than zero x is less than y.Zero x equals y.Greater than zero x is 
             greater than y.
        """
        pass

    @staticmethod
    def Create(comparison):
        """ Create(comparison: Comparison[T]) -> Comparer[T] """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class Dictionary(object, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]], ISerializable, IDeserializationCallback):
    """
    Dictionary[TKey, TValue]()
    Dictionary[TKey, TValue](capacity: int)
    Dictionary[TKey, TValue](comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](capacity: int, comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
    """
    def Add(self, key, value):
        """
        Add(self: Dictionary[TKey, TValue], key: TKey, value: TValue)
            Adds the specified key and value to the dictionary.
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be null for reference types.
        """
        pass

    def Clear(self):
        """
        Clear(self: Dictionary[TKey, TValue])
            Removes all keys and values from the System.Collections.Generic.Dictionary.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: Dictionary[TKey, TValue], key: TKey) -> bool
        
            Determines whether the System.Collections.Generic.Dictionary contains the specified key.
        
            key: The key to locate in the System.Collections.Generic.Dictionary.
            Returns: true if the System.Collections.Generic.Dictionary contains an element with the specified key; 
             otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        """
        ContainsValue(self: Dictionary[TKey, TValue], value: TValue) -> bool
        
            Determines whether the System.Collections.Generic.Dictionary contains a specific value.
        
            value: The value to locate in the System.Collections.Generic.Dictionary. The value can be null for 
             reference types.
        
            Returns: true if the System.Collections.Generic.Dictionary contains an element with the specified value; 
             otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: Dictionary[TKey, TValue]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.Dictionary.
            Returns: A System.Collections.Generic.Dictionary structure for the System.Collections.Generic.Dictionary.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: Dictionary[TKey, TValue], info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed 
             to serialize the System.Collections.Generic.Dictionary instance.
        
        
            info: A System.Runtime.Serialization.SerializationInfo object that contains the information required 
             to serialize the System.Collections.Generic.Dictionary instance.
        
            context: A System.Runtime.Serialization.StreamingContext structure that contains the source and 
             destination of the serialized stream associated with the System.Collections.Generic.Dictionary 
             instance.
        """
        pass

    def OnDeserialization(self, sender):
        """
        OnDeserialization(self: Dictionary[TKey, TValue], sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface and raises the 
             deserialization event when the deserialization is complete.
        
        
            sender: The source of the deserialization event.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: Dictionary[TKey, TValue], key: TKey) -> bool
        
            Removes the value with the specified key from the System.Collections.Generic.Dictionary.
        
            key: The key of the element to remove.
            Returns: true if the element is successfully found and removed; otherwise, false.  This method returns 
             false if key is not found in the System.Collections.Generic.Dictionary.
        """
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
        
            Determines whether the System.Collections.Generic.IDictionary contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.Generic.IDictionary.
            Returns: true if the System.Collections.Generic.IDictionary contains an element with the key; otherwise, 
             false.
        
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
        __new__(cls: type, capacity: int)
        __new__(cls: type, comparer: IEqualityComparer[TKey])
        __new__(cls: type, capacity: int, comparer: IEqualityComparer[TKey])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """
        __repr__(self: Dictionary[TKey, TValue]) -> str
        __repr__(self: Dictionary[K, V]) -> str
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.Generic.IEqualityComparer that is used to determine equality of keys for the dictionary.

Get: Comparer(self: Dictionary[TKey, TValue]) -> IEqualityComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Generic.Dictionary.

Get: Count(self: Dictionary[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the keys in the System.Collections.Generic.Dictionary.

Get: Keys(self: Dictionary[TKey, TValue]) -> KeyCollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the values in the System.Collections.Generic.Dictionary.

Get: Values(self: Dictionary[TKey, TValue]) -> ValueCollection

"""


    Enumerator = None
    KeyCollection = None
    ValueCollection = None


class EqualityComparer(object, IEqualityComparer, IEqualityComparer[T]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: EqualityComparer[T], x: T, y: T) -> bool
        
            When overridden in a derived class, determines whether two objects of type T are equal.
        
            x: The first object to compare.
            y: The second object to compare.
            Returns: true if the specified objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self, obj=None):
        """
        GetHashCode(self: EqualityComparer[T], obj: T) -> int
        
            When overridden in a derived class, serves as a hash function for the specified object for 
             hashing algorithms and data structures, such as a hash table.
        
        
            obj: The object for which to get a hash code.
            Returns: A hash code for the specified object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ICollection(IEnumerable[T], IEnumerable):
    # no doc
    def Add(self, item):
        """
        Add(self: ICollection[T], item: T)
            Adds an item to the System.Collections.Generic.ICollection.
        
            item: The object to add to the System.Collections.Generic.ICollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: ICollection[T])
            Removes all items from the System.Collections.Generic.ICollection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: ICollection[T], array: Array[T], arrayIndex: int) """
        pass

    def Remove(self, item):
        """
        Remove(self: ICollection[T], item: T) -> bool
        
            Removes the first occurrence of a specific object from the 
             System.Collections.Generic.ICollection.
        
        
            item: The object to remove from the System.Collections.Generic.ICollection.
            Returns: true if item was successfully removed from the System.Collections.Generic.ICollection; 
             otherwise, false. This method also returns false if item is not found in the original 
             System.Collections.Generic.ICollection.
        """
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
    """Gets the number of elements contained in the System.Collections.Generic.ICollection.

Get: Count(self: ICollection[T]) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Generic.ICollection is read-only.

Get: IsReadOnly(self: ICollection[T]) -> bool

"""



class IComparer:
    # no doc
    def Compare(self, x, y):
        """
        Compare(self: IComparer[T], x: T, y: T) -> int
        
            Compares two objects and returns a value indicating whether one is less than, equal to, or 
             greater than the other.
        
        
            x: The first object to compare.
            y: The second object to compare.
            Returns: A signed integer that indicates the relative values of x and y, as shown in the following 
             table.Value Meaning Less than zerox is less than y.Zerox equals y.Greater than zerox is greater 
             than y.
        """
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
        """
        Add(self: IDictionary[TKey, TValue], key: TKey, value: TValue)
            Adds an element with the provided key and value to the System.Collections.Generic.IDictionary.
        
            key: The object to use as the key of the element to add.
            value: The object to use as the value of the element to add.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: IDictionary[TKey, TValue], key: TKey) -> bool
        
            Determines whether the System.Collections.Generic.IDictionary contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.Generic.IDictionary.
            Returns: true if the System.Collections.Generic.IDictionary contains an element with the key; otherwise, 
             false.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: IDictionary[TKey, TValue], key: TKey) -> bool
        
            Removes the element with the specified key from the System.Collections.Generic.IDictionary.
        
            key: The key of the element to remove.
            Returns: true if the element is successfully removed; otherwise, false.  This method also returns false 
             if key was not found in the original System.Collections.Generic.IDictionary.
        """
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
    """Gets an System.Collections.Generic.ICollection containing the keys of the System.Collections.Generic.IDictionary.

Get: Keys(self: IDictionary[TKey, TValue]) -> ICollection[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

Get: Values(self: IDictionary[TKey, TValue]) -> ICollection[TValue]

"""



class IEnumerable(IEnumerable):
    # no doc
    def GetEnumerator(self):
        """
        GetEnumerator(self: IEnumerable[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
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
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__[T](self: IEnumerator[T]) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element in the collection at the current position of the enumerator.

Get: Current(self: IEnumerator[T]) -> T

"""



class IEqualityComparer:
    # no doc
    def Equals(self, x, y):
        """
        Equals(self: IEqualityComparer[T], x: T, y: T) -> bool
        
            Determines whether the specified objects are equal.
        
            x: The first object of type T to compare.
            y: The second object of type T to compare.
            Returns: true if the specified objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self, obj):
        """
        GetHashCode(self: IEqualityComparer[T], obj: T) -> int
        
            Returns a hash code for the specified object.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the specified object.
        """
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
        """
        IndexOf(self: IList[T], item: T) -> int
        
            Determines the index of a specific item in the System.Collections.Generic.IList.
        
            item: The object to locate in the System.Collections.Generic.IList.
            Returns: The index of item if found in the list; otherwise, -1.
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: IList[T], index: int, item: T)
            Inserts an item to the System.Collections.Generic.IList at the specified index.
        
            index: The zero-based index at which item should be inserted.
            item: The object to insert into the System.Collections.Generic.IList.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: IList[T], index: int)
            Removes the System.Collections.Generic.IList item at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
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
        """
        Add(self: ISet[T], item: T) -> bool
        
            Adds an element to the current set and returns a value to indicate if the element was 
             successfully added.
        
        
            item: The element to add to the set.
            Returns: true if the element is added to the set; false if the element is already in the set.
        """
        pass

    def ExceptWith(self, other):
        """
        ExceptWith(self: ISet[T], other: IEnumerable[T])
            Removes all elements in the specified collection from the current set.
        
            other: The collection of items to remove from the set.
        """
        pass

    def IntersectWith(self, other):
        """
        IntersectWith(self: ISet[T], other: IEnumerable[T])
            Modifies the current set so that it contains only elements that are also in a specified 
             collection.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def IsProperSubsetOf(self, other):
        """
        IsProperSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a proper (strict) subset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a proper subset of other; otherwise, false.
        """
        pass

    def IsProperSupersetOf(self, other):
        """
        IsProperSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a proper (strict) superset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a proper superset of other; otherwise, false.
        """
        pass

    def IsSubsetOf(self, other):
        """
        IsSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a set is a subset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a subset of other; otherwise, false.
        """
        pass

    def IsSupersetOf(self, other):
        """
        IsSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a superset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a superset of other; otherwise, false.
        """
        pass

    def Overlaps(self, other):
        """
        Overlaps(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set overlaps with the specified collection.
        
            other: The collection to compare to the current set.
            Returns: true if the current set and other share at least one common element; otherwise, false.
        """
        pass

    def SetEquals(self, other):
        """
        SetEquals(self: ISet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set and the specified collection contain the same elements.
        
            other: The collection to compare to the current set.
            Returns: true if the current set is equal to other; otherwise, false.
        """
        pass

    def SymmetricExceptWith(self, other):
        """
        SymmetricExceptWith(self: ISet[T], other: IEnumerable[T])
            Modifies the current set so that it contains only elements that are present either in the 
             current set or in the specified collection, but not both.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def UnionWith(self, other):
        """
        UnionWith(self: ISet[T], other: IEnumerable[T])
            Modifies the current set so that it contains all elements that are present in both the current 
             set and in the specified collection.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
        """
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


class KeyNotFoundException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown when the key specified for accessing an element in a collection does not match any key in the collection.
    
    KeyNotFoundException()
    KeyNotFoundException(message: str)
    KeyNotFoundException(message: str, innerException: Exception)
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class KeyValuePair(object):
    """ KeyValuePair[TKey, TValue](key: TKey, value: TValue) """
    def ToString(self):
        """
        ToString(self: KeyValuePair[TKey, TValue]) -> str
        
            Returns a string representation of the System.Collections.Generic.KeyValuePair, using the string 
             representations of the key and value.
        
            Returns: A string representation of the System.Collections.Generic.KeyValuePair, which includes the 
             string representations of the key and value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, key, value):
        """
        __new__(cls: type, key: TKey, value: TValue)
        __new__[KeyValuePair`2]() -> KeyValuePair[TKey, TValue]
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key in the key/value pair.

Get: Key(self: KeyValuePair[TKey, TValue]) -> TKey

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value in the key/value pair.

Get: Value(self: KeyValuePair[TKey, TValue]) -> TValue

"""



class LinkedList(object, ICollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T], ISerializable, IDeserializationCallback):
    """
    LinkedList[T]()
    LinkedList[T](collection: IEnumerable[T])
    """
    def AddAfter(self, node, *__args):
        """
        AddAfter(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]
        
            Adds a new node containing the specified value after the specified existing node in the 
             System.Collections.Generic.LinkedList.
        
        
            node: The System.Collections.Generic.LinkedListNode after which to insert a new 
             System.Collections.Generic.LinkedListNode containing value.
        
            value: The value to add to the System.Collections.Generic.LinkedList.
            Returns: The new System.Collections.Generic.LinkedListNode containing value.
        AddAfter(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])
            Adds the specified new node after the specified existing node in the 
             System.Collections.Generic.LinkedList.
        
        
            node: The System.Collections.Generic.LinkedListNode after which to insert newNode.
            newNode: The new System.Collections.Generic.LinkedListNode to add to the 
             System.Collections.Generic.LinkedList.
        """
        pass

    def AddBefore(self, node, *__args):
        """
        AddBefore(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])
            Adds the specified new node before the specified existing node in the 
             System.Collections.Generic.LinkedList.
        
        
            node: The System.Collections.Generic.LinkedListNode before which to insert newNode.
            newNode: The new System.Collections.Generic.LinkedListNode to add to the 
             System.Collections.Generic.LinkedList.
        
        AddBefore(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]
        
            Adds a new node containing the specified value before the specified existing node in the 
             System.Collections.Generic.LinkedList.
        
        
            node: The System.Collections.Generic.LinkedListNode before which to insert a new 
             System.Collections.Generic.LinkedListNode containing value.
        
            value: The value to add to the System.Collections.Generic.LinkedList.
            Returns: The new System.Collections.Generic.LinkedListNode containing value.
        """
        pass

    def AddFirst(self, *__args):
        """
        AddFirst(self: LinkedList[T], node: LinkedListNode[T])
            Adds the specified new node at the start of the System.Collections.Generic.LinkedList.
        
            node: The new System.Collections.Generic.LinkedListNode to add at the start of the 
             System.Collections.Generic.LinkedList.
        
        AddFirst(self: LinkedList[T], value: T) -> LinkedListNode[T]
        
            Adds a new node containing the specified value at the start of the 
             System.Collections.Generic.LinkedList.
        
        
            value: The value to add at the start of the System.Collections.Generic.LinkedList.
            Returns: The new System.Collections.Generic.LinkedListNode containing value.
        """
        pass

    def AddLast(self, *__args):
        """
        AddLast(self: LinkedList[T], node: LinkedListNode[T])
            Adds the specified new node at the end of the System.Collections.Generic.LinkedList.
        
            node: The new System.Collections.Generic.LinkedListNode to add at the end of the 
             System.Collections.Generic.LinkedList.
        
        AddLast(self: LinkedList[T], value: T) -> LinkedListNode[T]
        
            Adds a new node containing the specified value at the end of the 
             System.Collections.Generic.LinkedList.
        
        
            value: The value to add at the end of the System.Collections.Generic.LinkedList.
            Returns: The new System.Collections.Generic.LinkedListNode containing value.
        """
        pass

    def Clear(self):
        """
        Clear(self: LinkedList[T])
            Removes all nodes from the System.Collections.Generic.LinkedList.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: LinkedList[T], value: T) -> bool
        
            Determines whether a value is in the System.Collections.Generic.LinkedList.
        
            value: The value to locate in the System.Collections.Generic.LinkedList. The value can be null for 
             reference types.
        
            Returns: true if value is found in the System.Collections.Generic.LinkedList; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: LinkedList[T], array: Array[T], index: int) """
        pass

    def Find(self, value):
        """
        Find(self: LinkedList[T], value: T) -> LinkedListNode[T]
        
            Finds the first node that contains the specified value.
        
            value: The value to locate in the System.Collections.Generic.LinkedList.
            Returns: The first System.Collections.Generic.LinkedListNode that contains the specified value, if found; 
             otherwise, null.
        """
        pass

    def FindLast(self, value):
        """
        FindLast(self: LinkedList[T], value: T) -> LinkedListNode[T]
        
            Finds the last node that contains the specified value.
        
            value: The value to locate in the System.Collections.Generic.LinkedList.
            Returns: The last System.Collections.Generic.LinkedListNode that contains the specified value, if found; 
             otherwise, null.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LinkedList[T]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.LinkedList.
            Returns: An System.Collections.Generic.LinkedList for the System.Collections.Generic.LinkedList.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: LinkedList[T], info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed 
             to serialize the System.Collections.Generic.LinkedList instance.
        
        
            info: A System.Runtime.Serialization.SerializationInfo object that contains the information required 
             to serialize the System.Collections.Generic.LinkedList instance.
        
            context: A System.Runtime.Serialization.StreamingContext object that contains the source and destination 
             of the serialized stream associated with the System.Collections.Generic.LinkedList instance.
        """
        pass

    def OnDeserialization(self, sender):
        """
        OnDeserialization(self: LinkedList[T], sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface and raises the 
             deserialization event when the deserialization is complete.
        
        
            sender: The source of the deserialization event.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: LinkedList[T], node: LinkedListNode[T])
            Removes the specified node from the System.Collections.Generic.LinkedList.
        
            node: The System.Collections.Generic.LinkedListNode to remove from the 
             System.Collections.Generic.LinkedList.
        
        Remove(self: LinkedList[T], value: T) -> bool
        
            Removes the first occurrence of the specified value from the 
             System.Collections.Generic.LinkedList.
        
        
            value: The value to remove from the System.Collections.Generic.LinkedList.
            Returns: true if the element containing value is successfully removed; otherwise, false.  This method 
             also returns false if value was not found in the original System.Collections.Generic.LinkedList.
        """
        pass

    def RemoveFirst(self):
        """
        RemoveFirst(self: LinkedList[T])
            Removes the node at the start of the System.Collections.Generic.LinkedList.
        """
        pass

    def RemoveLast(self):
        """
        RemoveLast(self: LinkedList[T])
            Removes the node at the end of the System.Collections.Generic.LinkedList.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[T])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of nodes actually contained in the System.Collections.Generic.LinkedList.

Get: Count(self: LinkedList[T]) -> int

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first node of the System.Collections.Generic.LinkedList.

Get: First(self: LinkedList[T]) -> LinkedListNode[T]

"""

    Last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last node of the System.Collections.Generic.LinkedList.

Get: Last(self: LinkedList[T]) -> LinkedListNode[T]

"""


    Enumerator = None


class LinkedListNode(object):
    """ LinkedListNode[T](value: T) """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: T) """
        pass

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.Generic.LinkedList that the System.Collections.Generic.LinkedListNode belongs to.

Get: List(self: LinkedListNode[T]) -> LinkedList[T]

"""

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the next node in the System.Collections.Generic.LinkedList.

Get: Next(self: LinkedListNode[T]) -> LinkedListNode[T]

"""

    Previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the previous node in the System.Collections.Generic.LinkedList.

Get: Previous(self: LinkedListNode[T]) -> LinkedListNode[T]

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value contained in the node.

Get: Value(self: LinkedListNode[T]) -> T

Set: Value(self: LinkedListNode[T]) = value
"""



class List(object, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
    """
    List[T]()
    List[T](capacity: int)
    List[T](collection: IEnumerable[T])
    """
    def Add(self, item):
        """
        Add(self: List[T], item: T)
            Adds an object to the end of the System.Collections.Generic.List.
        
            item: The object to be added to the end of the System.Collections.Generic.List. The value can be null 
             for reference types.
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: List[T], collection: IEnumerable[T])
            Adds the elements of the specified collection to the end of the System.Collections.Generic.List.
        
            collection: The collection whose elements should be added to the end of the System.Collections.Generic.List. 
             The collection itself cannot be null, but it can contain elements that are null, if type T is a 
             reference type.
        """
        pass

    def AsReadOnly(self):
        """
        AsReadOnly(self: List[T]) -> ReadOnlyCollection[T]
        
            Returns a read-only System.Collections.Generic.IList wrapper for the current collection.
            Returns: A System.Collections.ObjectModel.ReadOnlyCollection that acts as a read-only wrapper around the 
             current System.Collections.Generic.List.
        """
        pass

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: List[T], item: T, comparer: IComparer[T]) -> int
        
            Searches the entire sorted System.Collections.Generic.List for an element using the specified 
             comparer and returns the zero-based index of the element.
        
        
            item: The object to locate. The value can be null for reference types.
            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements.-or-null 
             to use the default comparer System.Collections.Generic.Comparer.
        
            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; 
             otherwise, a negative number that is the bitwise complement of the index of the next element 
             that is larger than item or, if there is no larger element, the bitwise complement of 
             System.Collections.Generic.List.
        
        BinarySearch(self: List[T], item: T) -> int
        
            Searches the entire sorted System.Collections.Generic.List for an element using the default 
             comparer and returns the zero-based index of the element.
        
        
            item: The object to locate. The value can be null for reference types.
            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; 
             otherwise, a negative number that is the bitwise complement of the index of the next element 
             that is larger than item or, if there is no larger element, the bitwise complement of 
             System.Collections.Generic.List.
        
        BinarySearch(self: List[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int
        
            Searches a range of elements in the sorted System.Collections.Generic.List for an element using 
             the specified comparer and returns the zero-based index of the element.
        
        
            index: The zero-based starting index of the range to search.
            count: The length of the range to search.
            item: The object to locate. The value can be null for reference types.
            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or null 
             to use the default comparer System.Collections.Generic.Comparer.
        
            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; 
             otherwise, a negative number that is the bitwise complement of the index of the next element 
             that is larger than item or, if there is no larger element, the bitwise complement of 
             System.Collections.Generic.List.
        """
        pass

    def Clear(self):
        """
        Clear(self: List[T])
            Removes all elements from the System.Collections.Generic.List.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: List[T], item: T) -> bool
        
            Determines whether an element is in the System.Collections.Generic.List.
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            Returns: true if item is found in the System.Collections.Generic.List; otherwise, false.
        """
        pass

    def ConvertAll(self, converter):
        """ ConvertAll[TOutput](self: List[T], converter: Converter[T, TOutput]) -> List[TOutput] """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: List[T], index: int, array: Array[T], arrayIndex: int, count: int)CopyTo(self: List[T], array: Array[T], arrayIndex: int)CopyTo(self: List[T], array: Array[T]) """
        pass

    def Exists(self, match):
        """
        Exists(self: List[T], match: Predicate[T]) -> bool
        
            Determines whether the System.Collections.Generic.List contains elements that match the 
             conditions defined by the specified predicate.
        
        
            match: The System.Predicate delegate that defines the conditions of the elements to search for.
            Returns: true if the System.Collections.Generic.List contains one or more elements that match the 
             conditions defined by the specified predicate; otherwise, false.
        """
        pass

    def Find(self, match):
        """
        Find(self: List[T], match: Predicate[T]) -> T
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the first occurrence within the entire System.Collections.Generic.List.
        
        
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The first element that matches the conditions defined by the specified predicate, if found; 
             otherwise, the default value for type T.
        """
        pass

    def FindAll(self, match):
        """
        FindAll(self: List[T], match: Predicate[T]) -> List[T]
        
            Retrieves all the elements that match the conditions defined by the specified predicate.
        
            match: The System.Predicate delegate that defines the conditions of the elements to search for.
            Returns: A System.Collections.Generic.List containing all the elements that match the conditions defined 
             by the specified predicate, if found; otherwise, an empty System.Collections.Generic.List.
        """
        pass

    def FindIndex(self, *__args):
        """
        FindIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the first occurrence within the range of elements in the 
             System.Collections.Generic.List that extends from the specified index to the last element.
        
        
            startIndex: The zero-based starting index of the search.
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that matches the conditions defined 
                
        FindIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the first occurrence within the range of elements in the 
             System.Collections.Generic.List that starts at the specified index and contains the specified 
             number of elements.
        
        
            startIndex: The zero-based starting index of the search.
            count: The number of elements in the section to search.
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that matches the conditions defined 
                
        FindIndex(self: List[T], match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the first occurrence within the entire 
             System.Collections.Generic.List.
        
        
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that matches the conditions defined 
                """
        pass

    def FindLast(self, match):
        """
        FindLast(self: List[T], match: Predicate[T]) -> T
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the last occurrence within the entire System.Collections.Generic.List.
        
        
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The last element that matches the conditions defined by the specified predicate, if found; 
             otherwise, the default value for type T.
        """
        pass

    def FindLastIndex(self, *__args):
        """
        FindLastIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the last occurrence within the range of elements in the 
             System.Collections.Generic.List that contains the specified number of elements and ends at the 
             specified index.
        
        
            startIndex: The zero-based starting index of the backward search.
            count: The number of elements in the section to search.
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches the conditions defined by 
                
        FindLastIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the last occurrence within the range of elements in the 
             System.Collections.Generic.List that extends from the first element to the specified index.
        
        
            startIndex: The zero-based starting index of the backward search.
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches the conditions defined by 
                
        FindLastIndex(self: List[T], match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, and 
             returns the zero-based index of the last occurrence within the entire 
             System.Collections.Generic.List.
        
        
            match: The System.Predicate delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches the conditions defined by 
                """
        pass

    def ForEach(self, action):
        """
        ForEach(self: List[T], action: Action[T])
            Performs the specified action on each element of the System.Collections.Generic.List.
        
            action: The System.Action delegate to perform on each element of the System.Collections.Generic.List.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: List[T]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.List.
            Returns: A System.Collections.Generic.List for the System.Collections.Generic.List.
        """
        pass

    def GetRange(self, index, count):
        """
        GetRange(self: List[T], index: int, count: int) -> List[T]
        
            Creates a shallow copy of a range of elements in the source System.Collections.Generic.List.
        
            index: The zero-based System.Collections.Generic.List index at which the range starts.
            count: The number of elements in the range.
            Returns: A shallow copy of a range of elements in the source System.Collections.Generic.List.
        """
        pass

    def IndexOf(self, item, index=None, count=None):
        """
        IndexOf(self: List[T], item: T, index: int, count: int) -> int
        
            Searches for the specified object and returns the zero-based index of the first occurrence 
             within the range of elements in the System.Collections.Generic.List that starts at the specified 
             index and contains the specified number of elements.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the first occurrence of item within the range of elements in the 
             System.Collections.Generic.List that starts at index and contains count number of elements, if 
                
        IndexOf(self: List[T], item: T, index: int) -> int
        
            Searches for the specified object and returns the zero-based index of the first occurrence 
             within the range of elements in the System.Collections.Generic.List that extends from the 
             specified index to the last element.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            Returns: The zero-based index of the first occurrence of item within the range of elements in the 
             System.Collections.Generic.List that extends from index to the last element, if found; 
                
        IndexOf(self: List[T], item: T) -> int
        
            Searches for the specified object and returns the zero-based index of the first occurrence 
             within the entire System.Collections.Generic.List.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            Returns: The zero-based index of the first occurrence of item within the entire 
                """
        pass

    def Insert(self, index, item):
        """
        Insert(self: List[T], index: int, item: T)
            Inserts an element into the System.Collections.Generic.List at the specified index.
        
            index: The zero-based index at which item should be inserted.
            item: The object to insert. The value can be null for reference types.
        """
        pass

    def InsertRange(self, index, collection):
        """
        InsertRange(self: List[T], index: int, collection: IEnumerable[T])
            Inserts the elements of a collection into the System.Collections.Generic.List at the specified 
             index.
        
        
            index: The zero-based index at which the new elements should be inserted.
            collection: The collection whose elements should be inserted into the System.Collections.Generic.List. The 
             collection itself cannot be null, but it can contain elements that are null, if type T is a 
             reference type.
        """
        pass

    def LastIndexOf(self, item, index=None, count=None):
        """
        LastIndexOf(self: List[T], item: T, index: int) -> int
        
            Searches for the specified object and returns the zero-based index of the last occurrence within 
             the range of elements in the System.Collections.Generic.List that extends from the first element 
             to the specified index.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            index: The zero-based starting index of the backward search.
            Returns: The zero-based index of the last occurrence of item within the range of elements in the 
             System.Collections.Generic.List that extends from the first element to index, if found; 
                
        LastIndexOf(self: List[T], item: T) -> int
        
            Searches for the specified object and returns the zero-based index of the last occurrence within 
             the entire System.Collections.Generic.List.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            Returns: The zero-based index of the last occurrence of item within the entire the 
                
        LastIndexOf(self: List[T], item: T, index: int, count: int) -> int
        
            Searches for the specified object and returns the zero-based index of the last occurrence within 
             the range of elements in the System.Collections.Generic.List that contains the specified number 
             of elements and ends at the specified index.
        
        
            item: The object to locate in the System.Collections.Generic.List. The value can be null for reference 
             types.
        
            index: The zero-based starting index of the backward search.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the last occurrence of item within the range of elements in the 
             System.Collections.Generic.List that contains count number of elements and ends at index, if 
                """
        pass

    def Remove(self, item):
        """
        Remove(self: List[T], item: T) -> bool
        
            Removes the first occurrence of a specific object from the System.Collections.Generic.List.
        
            item: The object to remove from the System.Collections.Generic.List. The value can be null for 
             reference types.
        
            Returns: true if item is successfully removed; otherwise, false.  This method also returns false if item 
             was not found in the System.Collections.Generic.List.
        """
        pass

    def RemoveAll(self, match):
        """
        RemoveAll(self: List[T], match: Predicate[T]) -> int
        
            Removes all the elements that match the conditions defined by the specified predicate.
        
            match: The System.Predicate delegate that defines the conditions of the elements to remove.
            Returns: The number of elements removed from the System.Collections.Generic.List .
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: List[T], index: int)
            Removes the element at the specified index of the System.Collections.Generic.List.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def RemoveRange(self, index, count):
        """
        RemoveRange(self: List[T], index: int, count: int)
            Removes a range of elements from the System.Collections.Generic.List.
        
            index: The zero-based starting index of the range of elements to remove.
            count: The number of elements to remove.
        """
        pass

    def Reverse(self, index=None, count=None):
        """
        Reverse(self: List[T], index: int, count: int)
            Reverses the order of the elements in the specified range.
        
            index: The zero-based starting index of the range to reverse.
            count: The number of elements in the range to reverse.
        Reverse(self: List[T])
            Reverses the order of the elements in the entire System.Collections.Generic.List.
        """
        pass

    def Sort(self, *__args):
        """
        Sort(self: List[T], index: int, count: int, comparer: IComparer[T])
            Sorts the elements in a range of elements in System.Collections.Generic.List using the specified 
             comparer.
        
        
            index: The zero-based starting index of the range to sort.
            count: The length of the range to sort.
            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or null 
             to use the default comparer System.Collections.Generic.Comparer.
        
        Sort(self: List[T], comparison: Comparison[T])
            Sorts the elements in the entire System.Collections.Generic.List using the specified 
             System.Comparison.
        
        
            comparison: The System.Comparison to use when comparing elements.
        Sort(self: List[T])
            Sorts the elements in the entire System.Collections.Generic.List using the default comparer.
        Sort(self: List[T], comparer: IComparer[T])
            Sorts the elements in the entire System.Collections.Generic.List using the specified comparer.
        
            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or null 
             to use the default comparer System.Collections.Generic.Comparer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: List[T]) -> Array[T]
        
            Copies the elements of the System.Collections.Generic.List to a new array.
            Returns: An array containing copies of the elements of the System.Collections.Generic.List.
        """
        pass

    def TrimExcess(self):
        """
        TrimExcess(self: List[T])
            Sets the capacity to the actual number of elements in the System.Collections.Generic.List, if 
             that number is less than a threshold value.
        """
        pass

    def TrueForAll(self, match):
        """
        TrueForAll(self: List[T], match: Predicate[T]) -> bool
        
            Determines whether every element in the System.Collections.Generic.List matches the conditions 
             defined by the specified predicate.
        
        
            match: The System.Predicate delegate that defines the conditions to check against the elements.
            Returns: true if every element in the System.Collections.Generic.List matches the conditions defined by 
             the specified predicate; otherwise, false. If the list has no elements, the return value is 
             true.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """
        __repr__(self: List[T]) -> str
        __repr__(self: List[T]) -> str
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the total number of elements the internal data structure can hold without resizing.

Get: Capacity(self: List[T]) -> int

Set: Capacity(self: List[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements actually contained in the System.Collections.Generic.List.

Get: Count(self: List[T]) -> int

"""


    Enumerator = None


class Queue(object, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """
    Queue[T]()
    Queue[T](capacity: int)
    Queue[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """
        Clear(self: Queue[T])
            Removes all objects from the System.Collections.Generic.Queue.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: Queue[T], item: T) -> bool
        
            Determines whether an element is in the System.Collections.Generic.Queue.
        
            item: The object to locate in the System.Collections.Generic.Queue. The value can be null for 
             reference types.
        
            Returns: true if item is found in the System.Collections.Generic.Queue; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: Queue[T], array: Array[T], arrayIndex: int) """
        pass

    def Dequeue(self):
        """
        Dequeue(self: Queue[T]) -> T
        
            Removes and returns the object at the beginning of the System.Collections.Generic.Queue.
            Returns: The object that is removed from the beginning of the System.Collections.Generic.Queue.
        """
        pass

    def Enqueue(self, item):
        """
        Enqueue(self: Queue[T], item: T)
            Adds an object to the end of the System.Collections.Generic.Queue.
        
            item: The object to add to the System.Collections.Generic.Queue. The value can be null for reference 
             types.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: Queue[T]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.Queue.
            Returns: An System.Collections.Generic.Queue for the System.Collections.Generic.Queue.
        """
        pass

    def Peek(self):
        """
        Peek(self: Queue[T]) -> T
        
            Returns the object at the beginning of the System.Collections.Generic.Queue without removing it.
            Returns: The object at the beginning of the System.Collections.Generic.Queue.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: Queue[T]) -> Array[T]
        
            Copies the System.Collections.Generic.Queue elements to a new array.
            Returns: A new array containing elements copied from the System.Collections.Generic.Queue.
        """
        pass

    def TrimExcess(self):
        """
        TrimExcess(self: Queue[T])
            Sets the capacity to the actual number of elements in the System.Collections.Generic.Queue, if 
             that number is less than 90 percent of current capacity.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
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
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Generic.Queue.

Get: Count(self: Queue[T]) -> int

"""


    Enumerator = None


class SortedDictionary(object, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    """
    SortedDictionary[TKey, TValue]()
    SortedDictionary[TKey, TValue](comparer: IComparer[TKey])
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    def Add(self, key, value):
        """
        Add(self: SortedDictionary[TKey, TValue], key: TKey, value: TValue)
            Adds an element with the specified key and value into the 
             System.Collections.Generic.SortedDictionary.
        
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be null for reference types.
        """
        pass

    def Clear(self):
        """
        Clear(self: SortedDictionary[TKey, TValue])
            Removes all elements from the System.Collections.Generic.SortedDictionary.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: SortedDictionary[TKey, TValue], key: TKey) -> bool
        
            Determines whether the System.Collections.Generic.SortedDictionary contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.Generic.SortedDictionary.
            Returns: true if the System.Collections.Generic.SortedDictionary contains an element with the specified 
             key; otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        """
        ContainsValue(self: SortedDictionary[TKey, TValue], value: TValue) -> bool
        
            Determines whether the System.Collections.Generic.SortedDictionary contains an element with the 
             specified value.
        
        
            value: The value to locate in the System.Collections.Generic.SortedDictionary. The value can be null 
             for reference types.
        
            Returns: true if the System.Collections.Generic.SortedDictionary contains an element with the specified 
             value; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: SortedDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], index: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SortedDictionary[TKey, TValue]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.SortedDictionary.
            Returns: A System.Collections.Generic.SortedDictionary for the 
             System.Collections.Generic.SortedDictionary.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: SortedDictionary[TKey, TValue], key: TKey) -> bool
        
            Removes the element with the specified key from the System.Collections.Generic.SortedDictionary.
        
            key: The key of the element to remove.
            Returns: true if the element is successfully removed; otherwise, false.  This method also returns false 
             if key is not found in the System.Collections.Generic.SortedDictionary.
        """
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
        
            Determines whether the System.Collections.Generic.IDictionary contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.Generic.IDictionary.
            Returns: true if the System.Collections.Generic.IDictionary contains an element with the key; otherwise, 
             false.
        
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
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
        __new__(cls: type, comparer: IComparer[TKey])
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

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.Generic.IComparer used to order the elements of the System.Collections.Generic.SortedDictionary.

Get: Comparer(self: SortedDictionary[TKey, TValue]) -> IComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Generic.SortedDictionary.

Get: Count(self: SortedDictionary[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the keys in the System.Collections.Generic.SortedDictionary.

Get: Keys(self: SortedDictionary[TKey, TValue]) -> KeyCollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the values in the System.Collections.Generic.SortedDictionary.

Get: Values(self: SortedDictionary[TKey, TValue]) -> ValueCollection

"""


    Enumerator = None
    KeyCollection = None
    ValueCollection = None


class SortedList(object, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    """
    SortedList[TKey, TValue]()
    SortedList[TKey, TValue](capacity: int)
    SortedList[TKey, TValue](comparer: IComparer[TKey])
    SortedList[TKey, TValue](capacity: int, comparer: IComparer[TKey])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    def Add(self, key, value):
        """
        Add(self: SortedList[TKey, TValue], key: TKey, value: TValue)
            Adds an element with the specified key and value into the System.Collections.Generic.SortedList.
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be null for reference types.
        """
        pass

    def Clear(self):
        """
        Clear(self: SortedList[TKey, TValue])
            Removes all elements from the System.Collections.Generic.SortedList.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: SortedList[TKey, TValue], key: TKey) -> bool
        
            Determines whether the System.Collections.Generic.SortedList contains a specific key.
        
            key: The key to locate in the System.Collections.Generic.SortedList.
            Returns: true if the System.Collections.Generic.SortedList contains an element with the specified key; 
             otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        """
        ContainsValue(self: SortedList[TKey, TValue], value: TValue) -> bool
        
            Determines whether the System.Collections.Generic.SortedList contains a specific value.
        
            value: The value to locate in the System.Collections.Generic.SortedList. The value can be null for 
             reference types.
        
            Returns: true if the System.Collections.Generic.SortedList contains an element with the specified value; 
             otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SortedList[TKey, TValue]) -> IEnumerator[KeyValuePair[TKey, TValue]]
        
            Returns an enumerator that iterates through the System.Collections.Generic.SortedList.
            Returns: An System.Collections.Generic.IEnumerator of type System.Collections.Generic.KeyValuePair for 
             the System.Collections.Generic.SortedList.
        """
        pass

    def IndexOfKey(self, key):
        """
        IndexOfKey(self: SortedList[TKey, TValue], key: TKey) -> int
        
            Searches for the specified key and returns the zero-based index within the entire 
             System.Collections.Generic.SortedList.
        
        
            key: The key to locate in the System.Collections.Generic.SortedList.
            Returns: The zero-based index of key within the entire System.Collections.Generic.SortedList, if found; 
             otherwise, -1.
        """
        pass

    def IndexOfValue(self, value):
        """
        IndexOfValue(self: SortedList[TKey, TValue], value: TValue) -> int
        
            Searches for the specified value and returns the zero-based index of the first occurrence within 
             the entire System.Collections.Generic.SortedList.
        
        
            value: The value to locate in the System.Collections.Generic.SortedList.  The value can be null for 
             reference types.
        
            Returns: The zero-based index of the first occurrence of value within the entire 
             System.Collections.Generic.SortedList, if found; otherwise, -1.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: SortedList[TKey, TValue], key: TKey) -> bool
        
            Removes the element with the specified key from the System.Collections.Generic.SortedList.
        
            key: The key of the element to remove.
            Returns: true if the element is successfully removed; otherwise, false.  This method also returns false 
             if key was not found in the original System.Collections.Generic.SortedList.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: SortedList[TKey, TValue], index: int)
            Removes the element at the specified index of the System.Collections.Generic.SortedList.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def TrimExcess(self):
        """
        TrimExcess(self: SortedList[TKey, TValue])
            Sets the capacity to the actual number of elements in the System.Collections.Generic.SortedList, 
             if that number is less than 90 percent of current capacity.
        """
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
        
            Determines whether the System.Collections.Generic.IDictionary contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.Generic.IDictionary.
            Returns: true if the System.Collections.Generic.IDictionary contains an element with the key; otherwise, 
             false.
        
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
        __new__(cls: type, capacity: int)
        __new__(cls: type, comparer: IComparer[TKey])
        __new__(cls: type, capacity: int, comparer: IComparer[TKey])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue])
        __new__(cls: type, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
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

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of elements that the System.Collections.Generic.SortedList can contain.

Get: Capacity(self: SortedList[TKey, TValue]) -> int

Set: Capacity(self: SortedList[TKey, TValue]) = value
"""

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.Generic.IComparer for the sorted list.

Get: Comparer(self: SortedList[TKey, TValue]) -> IComparer[TKey]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key/value pairs contained in the System.Collections.Generic.SortedList.

Get: Count(self: SortedList[TKey, TValue]) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the keys in the System.Collections.Generic.SortedList.

Get: Keys(self: SortedList[TKey, TValue]) -> IList[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the values in the System.Collections.Generic.SortedList.

Get: Values(self: SortedList[TKey, TValue]) -> IList[TValue]

"""



class SortedSet(object, ISet[T], ICollection[T], IEnumerable[T], IEnumerable, ICollection, ISerializable, IDeserializationCallback, IReadOnlyCollection[T]):
    """
    SortedSet[T]()
    SortedSet[T](collection: IEnumerable[T])
    SortedSet[T](collection: IEnumerable[T], comparer: IComparer[T])
    SortedSet[T](comparer: IComparer[T])
    """
    def Add(self, item):
        """
        Add(self: SortedSet[T], item: T) -> bool
        
            Adds an element to the set and returns a value that indicates if it was successfully added.
        
            item: The element to add to the set.
            Returns: true if item is added to the set; otherwise, false.
        """
        pass

    def Clear(self):
        """
        Clear(self: SortedSet[T])
            Removes all elements from the set.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: SortedSet[T], item: T) -> bool
        
            Determines whether the set contains a specific element.
        
            item: The element to locate in the set.
            Returns: true if the set contains item; otherwise, false.
        """
        pass

    def CopyTo(self, array, index=None, count=None):
        """ CopyTo(self: SortedSet[T], array: Array[T], index: int, count: int)CopyTo(self: SortedSet[T], array: Array[T], index: int)CopyTo(self: SortedSet[T], array: Array[T]) """
        pass

    @staticmethod
    def CreateSetComparer(memberEqualityComparer=None):
        """
        CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]
        
            Returns an System.Collections.IEqualityComparer object, according to a specified comparer, that 
             can be used to create a collection that contains individual sets.
        
        
            memberEqualityComparer: The comparer to use for creating the returned comparer.
            Returns: A comparer for creating a collection of sets.
        CreateSetComparer() -> IEqualityComparer[SortedSet[T]]
        
            Returns an System.Collections.IEqualityComparer object that can be used to create a collection 
             that contains individual sets.
        
            Returns: A comparer for creating a collection of sets.
        """
        pass

    def ExceptWith(self, other):
        """
        ExceptWith(self: SortedSet[T], other: IEnumerable[T])
            Removes all elements that are in a specified collection from the current 
             System.Collections.Generic.SortedSet object.
        
        
            other: The collection of items to remove from the System.Collections.Generic.SortedSet object.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SortedSet[T]) -> Enumerator
        
            Returns an enumerator that iterates through the System.Collections.Generic.SortedSet.
            Returns: An enumerator that iterates through the System.Collections.Generic.SortedSet.
        """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """
        GetObjectData(self: SortedSet[T], info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data that 
             you must have to serialize a System.Collections.Generic.SortedSet object.
        
        
            info: A System.Runtime.Serialization.SerializationInfo object that contains the information that is 
             required to serialize the System.Collections.Generic.SortedSet object.
        
            context: A System.Runtime.Serialization.StreamingContext structure that contains the source and 
             destination of the serialized stream associated with the System.Collections.Generic.SortedSet 
             object.
        """
        pass

    def GetViewBetween(self, lowerValue, upperValue):
        """
        GetViewBetween(self: SortedSet[T], lowerValue: T, upperValue: T) -> SortedSet[T]
        
            Returns a view of a subset in a System.Collections.Generic.SortedSet.
        
            lowerValue: The lowest desired value in the view.
            upperValue: The highest desired value in the view.
            Returns: A subset view that contains only the values in the specified range.
        """
        pass

    def IntersectWith(self, other):
        """
        IntersectWith(self: SortedSet[T], other: IEnumerable[T])
            Modifies the current System.Collections.Generic.SortedSet object so that it contains only 
             elements that are also in a specified collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
        """
        pass

    def IsProperSubsetOf(self, other):
        """
        IsProperSubsetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a System.Collections.Generic.SortedSet object is a proper subset of the 
             specified collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the System.Collections.Generic.SortedSet object is a proper subset of other; otherwise, 
             false.
        """
        pass

    def IsProperSupersetOf(self, other):
        """
        IsProperSupersetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a System.Collections.Generic.SortedSet object is a proper superset of the 
             specified collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the System.Collections.Generic.SortedSet object is a proper superset of other; 
             otherwise, false.
        """
        pass

    def IsSubsetOf(self, other):
        """
        IsSubsetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a System.Collections.Generic.SortedSet object is a subset of the specified 
             collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the current System.Collections.Generic.SortedSet object is a subset of other; otherwise, 
             false.
        """
        pass

    def IsSupersetOf(self, other):
        """
        IsSupersetOf(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a System.Collections.Generic.SortedSet object is a superset of the specified 
             collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the System.Collections.Generic.SortedSet object is a superset of other; otherwise, false.
        """
        pass

    def OnDeserialization(self, *args): #cannot find CLR method
        """
        OnDeserialization(self: SortedSet[T], sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface, and raises the 
             deserialization event when the deserialization is completed.
        
        
            sender: The source of the deserialization event.
        """
        pass

    def Overlaps(self, other):
        """
        Overlaps(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current System.Collections.Generic.SortedSet object and a specified 
             collection share common elements.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the System.Collections.Generic.SortedSet object and other share at least one common 
             element; otherwise, false.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: SortedSet[T], item: T) -> bool
        
            Removes a specified item from the System.Collections.Generic.SortedSet.
        
            item: The element to remove.
            Returns: true if the element is found and successfully removed; otherwise, false.
        """
        pass

    def RemoveWhere(self, match):
        """
        RemoveWhere(self: SortedSet[T], match: Predicate[T]) -> int
        
            Removes all elements that match the conditions defined by the specified predicate from a 
             System.Collections.Generic.SortedSet.
        
        
            match: The delegate that defines the conditions of the elements to remove.
            Returns: The number of elements that were removed from the System.Collections.Generic.SortedSet 
             collection..
        """
        pass

    def Reverse(self):
        """
        Reverse(self: SortedSet[T]) -> IEnumerable[T]
        
            Returns an System.Collections.Generic.IEnumerable that iterates over the 
             System.Collections.Generic.SortedSet in reverse order.
        
            Returns: An enumerator that iterates over the System.Collections.Generic.SortedSet in reverse order.
        """
        pass

    def SetEquals(self, other):
        """
        SetEquals(self: SortedSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current System.Collections.Generic.SortedSet object and the specified 
             collection contain the same elements.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
            Returns: true if the current System.Collections.Generic.SortedSet object is equal to other; otherwise, 
             false.
        """
        pass

    def SymmetricExceptWith(self, other):
        """
        SymmetricExceptWith(self: SortedSet[T], other: IEnumerable[T])
            Modifies the current System.Collections.Generic.SortedSet object so that it contains only 
             elements that are present either in the current object or in the specified collection, but not 
             both.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
        """
        pass

    def UnionWith(self, other):
        """
        UnionWith(self: SortedSet[T], other: IEnumerable[T])
            Modifies the current System.Collections.Generic.SortedSet object so that it contains all 
             elements that are present in both the current object and in the specified collection.
        
        
            other: The collection to compare to the current System.Collections.Generic.SortedSet object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, comparer: IComparer[T])
        __new__(cls: type, collection: IEnumerable[T])
        __new__(cls: type, collection: IEnumerable[T], comparer: IComparer[T])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.Generic.IEqualityComparer object that is used to determine equality for the values in the System.Collections.Generic.SortedSet.

Get: Comparer(self: SortedSet[T]) -> IComparer[T]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the System.Collections.Generic.SortedSet.

Get: Count(self: SortedSet[T]) -> int

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum value in the System.Collections.Generic.SortedSet, as defined by the comparer.

Get: Max(self: SortedSet[T]) -> T

"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum value in the System.Collections.Generic.SortedSet, as defined by the comparer.

Get: Min(self: SortedSet[T]) -> T

"""


    Enumerator = None


class Stack(object, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """
    Stack[T]()
    Stack[T](capacity: int)
    Stack[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """
        Clear(self: Stack[T])
            Removes all objects from the System.Collections.Generic.Stack.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: Stack[T], item: T) -> bool
        
            Determines whether an element is in the System.Collections.Generic.Stack.
        
            item: The object to locate in the System.Collections.Generic.Stack. The value can be null for 
             reference types.
        
            Returns: true if item is found in the System.Collections.Generic.Stack; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: Stack[T], array: Array[T], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: Stack[T]) -> Enumerator
        
            Returns an enumerator for the System.Collections.Generic.Stack.
            Returns: An System.Collections.Generic.Stack for the System.Collections.Generic.Stack.
        """
        pass

    def Peek(self):
        """
        Peek(self: Stack[T]) -> T
        
            Returns the object at the top of the System.Collections.Generic.Stack without removing it.
            Returns: The object at the top of the System.Collections.Generic.Stack.
        """
        pass

    def Pop(self):
        """
        Pop(self: Stack[T]) -> T
        
            Removes and returns the object at the top of the System.Collections.Generic.Stack.
            Returns: The object removed from the top of the System.Collections.Generic.Stack.
        """
        pass

    def Push(self, item):
        """
        Push(self: Stack[T], item: T)
            Inserts an object at the top of the System.Collections.Generic.Stack.
        
            item: The object to push onto the System.Collections.Generic.Stack. The value can be null for 
             reference types.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: Stack[T]) -> Array[T]
        
            Copies the System.Collections.Generic.Stack to a new array.
            Returns: A new array containing copies of the elements of the System.Collections.Generic.Stack.
        """
        pass

    def TrimExcess(self):
        """
        TrimExcess(self: Stack[T])
            Sets the capacity to the actual number of elements in the System.Collections.Generic.Stack, if 
             that number is less than 90 percent of current capacity.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
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
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Generic.Stack.

Get: Count(self: Stack[T]) -> int

"""


    Enumerator = None



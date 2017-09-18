# encoding: utf-8
# module System.Collections.Concurrent calls itself Concurrent
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def Partitioner(*args, **kwargs): # real signature unknown
    """ Provides common partitioning strategies for arrays, lists, and enumerables. """
    pass

# classes

class BlockingCollection(object, IEnumerable[T], IEnumerable, ICollection, IDisposable, IReadOnlyCollection[T]):
    """
    BlockingCollection[T]()
    BlockingCollection[T](boundedCapacity: int)
    BlockingCollection[T](collection: IProducerConsumerCollection[T], boundedCapacity: int)
    BlockingCollection[T](collection: IProducerConsumerCollection[T])
    """
    def Add(self, item, cancellationToken=None):
        """
        Add(self: BlockingCollection[T], item: T, cancellationToken: CancellationToken)
            Adds the item to the System.Collections.Concurrent.BlockingCollection.
        
            item: The item to be added to the collection. The value can be a null reference.
            cancellationToken: A cancellation token to observe.
        Add(self: BlockingCollection[T], item: T)
            Adds the item to the System.Collections.Concurrent.BlockingCollection.
        
            item: The item to be added to the collection. The value can be a null reference.
        """
        pass

    @staticmethod
    def AddToAny(collections, item, cancellationToken=None):
        """
        AddToAny(collections: Array[BlockingCollection[T]], item: T, cancellationToken: CancellationToken) -> int
        AddToAny(collections: Array[BlockingCollection[T]], item: T) -> int
        """
        pass

    def CompleteAdding(self):
        """
        CompleteAdding(self: BlockingCollection[T])
            Marks the System.Collections.Concurrent.BlockingCollection instances as not accepting any more 
             additions.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: BlockingCollection[T], array: Array[T], index: int) """
        pass

    def Dispose(self):
        """
        Dispose(self: BlockingCollection[T])
            Releases all resources used by the current instance of the 
             System.Collections.Concurrent.BlockingCollection class.
        """
        pass

    def GetConsumingEnumerable(self, cancellationToken=None):
        """
        GetConsumingEnumerable(self: BlockingCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]
        
            Provides a consuming System.Collections.Generics.IEnumerable for items in the collection.
        
            cancellationToken: A cancellation token to observe.
            Returns: An System.Collections.Generics.IEnumerable that removes and returns items from the collection.
        GetConsumingEnumerable(self: BlockingCollection[T]) -> IEnumerable[T]
        
            Provides a consuming System.Collections.Generics.IEnumerable for items in the collection.
            Returns: An System.Collections.Generics.IEnumerable that removes and returns items from the collection.
        """
        pass

    def Take(self, cancellationToken=None):
        """
        Take(self: BlockingCollection[T], cancellationToken: CancellationToken) -> T
        
            Takes an item from the System.Collections.Concurrent.BlockingCollection.
        
            cancellationToken: Object that can be used to cancel the take operation.
            Returns: The item removed from the collection.
        Take(self: BlockingCollection[T]) -> T
        
            Takes an item from the System.Collections.Concurrent.BlockingCollection.
            Returns: The item removed from the collection.
        """
        pass

    @staticmethod
    def TakeFromAny(collections, item, cancellationToken=None):
        """
        TakeFromAny(collections: Array[BlockingCollection[T]], cancellationToken: CancellationToken) -> (int, T)
        TakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)
        """
        pass

    def ToArray(self):
        """
        ToArray(self: BlockingCollection[T]) -> Array[T]
        
            Copies the items from the System.Collections.Concurrent.BlockingCollection instance into a new 
             array.
        
            Returns: An array containing copies of the elements of the collection.
        """
        pass

    def TryAdd(self, item, *__args):
        """
        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int) -> bool
        
            Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection 
             within the specified time period.
        
        
            item: The item to be added to the collection.
            millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait 
             indefinitely.
        
            Returns: true if the item could be added to the collection within the specified time; otherwise, false. 
             If the item is a duplicate, and the underlying collection does not accept duplicate items, then 
             an System.InvalidOperationException is thrown.
        
        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        
            Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection 
             within the specified time period, while observing a cancellation token.
        
        
            item: The item to be added to the collection.
            millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait 
             indefinitely.
        
            cancellationToken: A cancellation token to observe.
            Returns: true if the item could be added to the collection within the specified time; otherwise, false. 
             If the item is a duplicate, and the underlying collection does not accept duplicate items, then 
             an System.InvalidOperationException is thrown.
        
        TryAdd(self: BlockingCollection[T], item: T) -> bool
        
            Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection.
        
            item: The item to be added to the collection.
            Returns: true if item could be added; otherwise false. If the item is a duplicate, and the underlying 
             collection does not accept duplicate items, then an System.InvalidOperationException is thrown.
        
        TryAdd(self: BlockingCollection[T], item: T, timeout: TimeSpan) -> bool
        
            Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection.
        
            item: The item to be added to the collection.
            timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that 
             represents -1 milliseconds to wait indefinitely.
        
            Returns: true if the item could be added to the collection within the specified time span; otherwise, 
             false.
        """
        pass

    @staticmethod
    def TryAddToAny(collections, item, *__args):
        """
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan) -> int
        """
        pass

    def TryTake(self, item, *__args):
        """
        TryTake(self: BlockingCollection[T], millisecondsTimeout: int) -> (bool, T)
        TryTake(self: BlockingCollection[T], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (bool, T)
        TryTake(self: BlockingCollection[T]) -> (bool, T)
        TryTake(self: BlockingCollection[T], timeout: TimeSpan) -> (bool, T)
        """
        pass

    @staticmethod
    def TryTakeFromAny(collections, item, *__args):
        """
        TryTakeFromAny(collections: Array[BlockingCollection[T]], timeout: TimeSpan) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
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
        __new__(cls: type, boundedCapacity: int)
        __new__(cls: type, collection: IProducerConsumerCollection[T], boundedCapacity: int)
        __new__(cls: type, collection: IProducerConsumerCollection[T])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundedCapacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounded capacity of this System.Collections.Concurrent.BlockingCollection instance.

Get: BoundedCapacity(self: BlockingCollection[T]) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items contained in the System.Collections.Concurrent.BlockingCollection.

Get: Count(self: BlockingCollection[T]) -> int

"""

    IsAddingCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this System.Collections.Concurrent.BlockingCollection has been marked as complete for adding.

Get: IsAddingCompleted(self: BlockingCollection[T]) -> bool

"""

    IsCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this System.Collections.Concurrent.BlockingCollection has been marked as complete for adding and is empty.

Get: IsCompleted(self: BlockingCollection[T]) -> bool

"""



class ConcurrentBag(object, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """
    ConcurrentBag[T]()
    ConcurrentBag[T](collection: IEnumerable[T])
    """
    def Add(self, item):
        """
        Add(self: ConcurrentBag[T], item: T)
            Adds an object to the System.Collections.Concurrent.ConcurrentBag.
        
            item: The object to be added to the System.Collections.Concurrent.ConcurrentBag. The value can be a 
             null reference (Nothing in Visual Basic) for reference types.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: ConcurrentBag[T], array: Array[T], index: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentBag[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentBag.
            Returns: An enumerator for the contents of the System.Collections.Concurrent.ConcurrentBag.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: ConcurrentBag[T]) -> Array[T]
        
            Copies the System.Collections.Concurrent.ConcurrentBag elements to a new array.
            Returns: A new array containing a snapshot of elements copied from the 
             System.Collections.Concurrent.ConcurrentBag.
        """
        pass

    def TryPeek(self, result):
        """ TryPeek(self: ConcurrentBag[T]) -> (bool, T) """
        pass

    def TryTake(self, result):
        """ TryTake(self: ConcurrentBag[T]) -> (bool, T) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentBag.

Get: Count(self: ConcurrentBag[T]) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentBag is empty.

Get: IsEmpty(self: ConcurrentBag[T]) -> bool

"""



class ConcurrentDictionary(object, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    """
    ConcurrentDictionary[TKey, TValue]()
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int)
    ConcurrentDictionary[TKey, TValue](comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]])
    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
    """
    def AddOrUpdate(self, key, *__args):
        """
        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]) -> TValue
        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> TValue
        """
        pass

    def Clear(self):
        """
        Clear(self: ConcurrentDictionary[TKey, TValue])
            Removes all keys and values from the System.Collections.Concurrent.ConcurrentDictionary.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: ConcurrentDictionary[TKey, TValue], key: TKey) -> bool
        
            Determines whether the System.Collections.Concurrent.ConcurrentDictionary contains the specified 
             key.
        
        
            key: The key to locate in the System.Collections.Concurrent.ConcurrentDictionary.
            Returns: true if the System.Collections.Concurrent.ConcurrentDictionary contains an element with the 
             specified key; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentDictionary[TKey, TValue]) -> IEnumerator[KeyValuePair[TKey, TValue]]
        
            Returns an enumerator that iterates through the 
             System.Collections.Concurrent.ConcurrentDictionary.
        
            Returns: An enumerator for the System.Collections.Concurrent.ConcurrentDictionary.
        """
        pass

    def GetOrAdd(self, key, *__args):
        """
        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> TValue
        
            Adds a key/value pair to the System.Collections.Concurrent.ConcurrentDictionary if the key does 
             not already exist.
        
        
            key: The key of the element to add.
            value: the value to be added, if the key does not already exist
            Returns: The value for the key. This will be either the existing value for the key if the key is already 
             in the dictionary, or the new value if the key was not in the dictionary.
        
        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> TValue
        
            Adds a key/value pair to the System.Collections.Concurrent.ConcurrentDictionary if the key does 
             not already exist.
        
        
            key: The key of the element to add.
            valueFactory: The function used to generate a value for the key
            Returns: The value for the key. This will be either the existing value for the key if the key is already 
             in the dictionary, or the new value for the key as returned by valueFactory if the key was not 
             in the dictionary.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: ConcurrentDictionary[TKey, TValue]) -> Array[KeyValuePair[TKey, TValue]]
        
            Copies the key and value pairs stored in the System.Collections.Concurrent.ConcurrentDictionary 
             to a new array.
        
            Returns: A new array containing a snapshot of key and value pairs copied from the 
             System.Collections.Concurrent.ConcurrentDictionary.
        """
        pass

    def TryAdd(self, key, value):
        """
        TryAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> bool
        
            Attempts to add the specified key and value to the 
             System.Collections.Concurrent.ConcurrentDictionary.
        
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be a null reference (Nothing in Visual Basic) for 
             reference types.
        
            Returns: true if the key/value pair was added to the System.Collections.Concurrent.ConcurrentDictionary 
             successfully. If the key already exists, this method returns false.
        """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: ConcurrentDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def TryRemove(self, key, value):
        """ TryRemove(self: ConcurrentDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def TryUpdate(self, key, newValue, comparisonValue):
        """
        TryUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, newValue: TValue, comparisonValue: TValue) -> bool
        
            Compares the existing value for the specified key with a specified value, and if they are equal, 
             updates the key with a third value.
        
        
            key: The key whose value is compared with comparisonValue and possibly replaced.
            newValue: The value that replaces the value of the element with key if the comparison results in equality.
            comparisonValue: The value that is compared to the value of the element with key.
            Returns: true if the value with key was equal to comparisonValue and replaced with newValue; otherwise, 
             false.
        """
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
        __new__(cls: type, concurrencyLevel: int, capacity: int)
        __new__(cls: type, collection: IEnumerable[KeyValuePair[TKey, TValue]])
        __new__(cls: type, comparer: IEqualityComparer[TKey])
        __new__(cls: type, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
        __new__(cls: type, concurrencyLevel: int, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
        __new__(cls: type, concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey])
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
    """Gets the number of key/value pairs contained in the System.Collections.Concurrent.ConcurrentDictionary.

Get: Count(self: ConcurrentDictionary[TKey, TValue]) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentDictionary is empty.

Get: IsEmpty(self: ConcurrentDictionary[TKey, TValue]) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the keys in the System.Collections.Generic.Dictionary{TKey,TValue}.

Get: Keys(self: ConcurrentDictionary[TKey, TValue]) -> ICollection[TKey]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection containing the values in the System.Collections.Generic.Dictionary{TKey,TValue}.

Get: Values(self: ConcurrentDictionary[TKey, TValue]) -> ICollection[TValue]

"""



class ConcurrentQueue(object, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """
    ConcurrentQueue[T]()
    ConcurrentQueue[T](collection: IEnumerable[T])
    """
    def CopyTo(self, array, index):
        """ CopyTo(self: ConcurrentQueue[T], array: Array[T], index: int) """
        pass

    def Enqueue(self, item):
        """
        Enqueue(self: ConcurrentQueue[T], item: T)
            Adds an object to the end of the System.Collections.Concurrent.ConcurrentQueue.
        
            item: The object to add to the end of the System.Collections.Concurrent.ConcurrentQueue. The value can 
             be a null reference (Nothing in Visual Basic) for reference types.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentQueue[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentQueue.
            Returns: An enumerator for the contents of the System.Collections.Concurrent.ConcurrentQueue.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: ConcurrentQueue[T]) -> Array[T]
        
            Copies the elements stored in the System.Collections.Concurrent.ConcurrentQueue to a new array.
            Returns: A new array containing a snapshot of elements copied from the 
             System.Collections.Concurrent.ConcurrentQueue.
        """
        pass

    def TryDequeue(self, result):
        """ TryDequeue(self: ConcurrentQueue[T]) -> (bool, T) """
        pass

    def TryPeek(self, result):
        """ TryPeek(self: ConcurrentQueue[T]) -> (bool, T) """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentQueue.

Get: Count(self: ConcurrentQueue[T]) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentQueue is empty.

Get: IsEmpty(self: ConcurrentQueue[T]) -> bool

"""



class ConcurrentStack(object, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """
    ConcurrentStack[T]()
    ConcurrentStack[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """
        Clear(self: ConcurrentStack[T])
            Removes all objects from the System.Collections.Concurrent.ConcurrentStack.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: ConcurrentStack[T], array: Array[T], index: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentStack[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentStack.
            Returns: An enumerator for the System.Collections.Concurrent.ConcurrentStack.
        """
        pass

    def Push(self, item):
        """
        Push(self: ConcurrentStack[T], item: T)
            Inserts an object at the top of the System.Collections.Concurrent.ConcurrentStack.
        
            item: The object to push onto the System.Collections.Concurrent.ConcurrentStack. The value can be a 
             null reference (Nothing in Visual Basic) for reference types.
        """
        pass

    def PushRange(self, items, startIndex=None, count=None):
        """ PushRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int)PushRange(self: ConcurrentStack[T], items: Array[T]) """
        pass

    def ToArray(self):
        """
        ToArray(self: ConcurrentStack[T]) -> Array[T]
        
            Copies the items stored in the System.Collections.Concurrent.ConcurrentStack to a new array.
            Returns: A new array containing a snapshot of elements copied from the 
             System.Collections.Concurrent.ConcurrentStack.
        """
        pass

    def TryPeek(self, result):
        """ TryPeek(self: ConcurrentStack[T]) -> (bool, T) """
        pass

    def TryPop(self, result):
        """ TryPop(self: ConcurrentStack[T]) -> (bool, T) """
        pass

    def TryPopRange(self, items, startIndex=None, count=None):
        """
        TryPopRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int) -> int
        TryPopRange(self: ConcurrentStack[T], items: Array[T]) -> int
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentStack.

Get: Count(self: ConcurrentStack[T]) -> int

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentStack is empty.

Get: IsEmpty(self: ConcurrentStack[T]) -> bool

"""



class EnumerablePartitionerOptions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) EnumerablePartitionerOptions, values: NoBuffering (1), None (0) """
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

    NoBuffering = None
    None = None
    value__ = None


class IProducerConsumerCollection(IEnumerable[T], IEnumerable, ICollection):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: IProducerConsumerCollection[T], array: Array[T], index: int) """
        pass

    def ToArray(self):
        """
        ToArray(self: IProducerConsumerCollection[T]) -> Array[T]
        
            Copies the elements contained in the System.Collections.Concurrent.IProducerConsumerCollection 
             to a new array.
        
            Returns: A new array containing the elements copied from the 
             System.Collections.Concurrent.IProducerConsumerCollection.
        """
        pass

    def TryAdd(self, item):
        """
        TryAdd(self: IProducerConsumerCollection[T], item: T) -> bool
        
            Attempts to add an object to the System.Collections.Concurrent.IProducerConsumerCollection.
        
            item: The object to add to the System.Collections.Concurrent.IProducerConsumerCollection.
            Returns: true if the object was added successfully; otherwise, false.
        """
        pass

    def TryTake(self, item):
        """ TryTake(self: IProducerConsumerCollection[T]) -> (bool, T) """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass


class OrderablePartitioner(Partitioner[TSource]):
    # no doc
    def GetDynamicPartitions(self):
        """
        GetDynamicPartitions(self: OrderablePartitioner[TSource]) -> IEnumerable[TSource]
        
            Creates an object that can partition the underlying collection into a variable number of 
             partitions.
        
            Returns: An object that can create partitions over the underlying data source.
        """
        pass

    def GetOrderableDynamicPartitions(self):
        """
        GetOrderableDynamicPartitions(self: OrderablePartitioner[TSource]) -> IEnumerable[KeyValuePair[Int64, TSource]]
        
            Creates an object that can partition the underlying collection into a variable number of 
             partitions.
        
            Returns: An object that can create partitions over the underlying data source.
        """
        pass

    def GetOrderablePartitions(self, partitionCount):
        """
        GetOrderablePartitions(self: OrderablePartitioner[TSource], partitionCount: int) -> IList[IEnumerator[KeyValuePair[Int64, TSource]]]
        
            Partitions the underlying collection into the specified number of orderable partitions.
        
            partitionCount: The number of partitions to create.
            Returns: A list containing partitionCount enumerators.
        """
        pass

    def GetPartitions(self, partitionCount):
        """
        GetPartitions(self: OrderablePartitioner[TSource], partitionCount: int) -> IList[IEnumerator[TSource]]
        
            Partitions the underlying collection into the given number of ordered partitions.
        
            partitionCount: The number of partitions to create.
            Returns: A list containing partitionCount enumerators.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, keysOrderedInEachPartition: bool, keysOrderedAcrossPartitions: bool, keysNormalized: bool) """
        pass

    KeysNormalized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether order keys are normalized.

Get: KeysNormalized(self: OrderablePartitioner[TSource]) -> bool

"""

    KeysOrderedAcrossPartitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether elements in an earlier partition always come before elements in a later partition.

Get: KeysOrderedAcrossPartitions(self: OrderablePartitioner[TSource]) -> bool

"""

    KeysOrderedInEachPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether elements in each partition are yielded in the order of increasing keys.

Get: KeysOrderedInEachPartition(self: OrderablePartitioner[TSource]) -> bool

"""




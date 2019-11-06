# encoding: utf-8
# module System.Collections.ObjectModel calls itself ObjectModel
# from mscorlib,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089,System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no important

# no functions
# classes

class Collection(object):
 """
 Collection[T]()
 Collection[T](list: IList[T])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Collection()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,item):
  """
  Add(self: Collection[T],item: T)
   Adds an object to the end of the System.Collections.ObjectModel.Collection.
  
   item: The object to be added to the end of the System.Collections.ObjectModel.Collection. The value can be null for reference types.
  """
  pass
 def Clear(self):
  """
  Clear(self: Collection[T])
   Removes all elements from the System.Collections.ObjectModel.Collection.
  """
  pass
 def ClearItems(self,*args):
  """
  ClearItems(self: Collection[T])
   Removes all elements from the System.Collections.ObjectModel.Collection.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: Collection[T],item: T) -> bool
  
   Determines whether an element is in the System.Collections.ObjectModel.Collection.
  
   item: The object to locate in the System.Collections.ObjectModel.Collection. The value can be null for reference types.
   Returns: true if item is found in the System.Collections.ObjectModel.Collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """ CopyTo(self: Collection[T],array: Array[T],index: int) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: Collection[T]) -> IEnumerator[T]
  
   Returns an enumerator that iterates through the System.Collections.ObjectModel.Collection.
   Returns: An System.Collections.Generic.IEnumerator for the System.Collections.ObjectModel.Collection.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: Collection[T],item: T) -> int
  
   Searches for the specified object and returns the zero-based index of the first occurrence within the entire System.Collections.ObjectModel.Collection.
  
   item: The object to locate in the System.Collections.Generic.List. The value can be null for reference types.
   Returns: The zero-based index of the first occurrence of item within the entire System.Collections.ObjectModel.Collection,if found; otherwise,-1.
  """
  pass
 def Insert(self,index,item):
  """
  Insert(self: Collection[T],index: int,item: T)
   Inserts an element into the System.Collections.ObjectModel.Collection at the specified index.
  
   index: The zero-based index at which item should be inserted.
   item: The object to insert. The value can be null for reference types.
  """
  pass
 def InsertItem(self,*args):
  """
  InsertItem(self: Collection[T],index: int,item: T)
   Inserts an element into the System.Collections.ObjectModel.Collection at the specified index.
  
   index: The zero-based index at which item should be inserted.
   item: The object to insert. The value can be null for reference types.
  """
  pass
 def Remove(self,item):
  """
  Remove(self: Collection[T],item: T) -> bool
  
   Removes the first occurrence of a specific object from the System.Collections.ObjectModel.Collection.
  
   item: The object to remove from the System.Collections.ObjectModel.Collection. The value can be null for reference types.
   Returns: true if item is successfully removed; otherwise,false.  This method also returns false if item was not found in the original System.Collections.ObjectModel.Collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: Collection[T],index: int)
   Removes the element at the specified index of the System.Collections.ObjectModel.Collection.
  
   index: The zero-based index of the element to remove.
  """
  pass
 def RemoveItem(self,*args):
  """
  RemoveItem(self: Collection[T],index: int)
   Removes the element at the specified index of the System.Collections.ObjectModel.Collection.
  
   index: The zero-based index of the element to remove.
  """
  pass
 def SetItem(self,*args):
  """
  SetItem(self: Collection[T],index: int,item: T)
   Replaces the element at the specified index.
  
   index: The zero-based index of the element to replace.
   item: The new value for the element at the specified index. The value can be null for reference types.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[T],item: T) -> bool
  
   Determines whether the System.Collections.Generic.ICollection contains a specific value.
  
   item: The object to locate in the System.Collections.Generic.ICollection.
   Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise,false.
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,list=None):
  """
  __new__(cls: type)
  __new__(cls: type,list: IList[T])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of elements actually contained in the System.Collections.ObjectModel.Collection.

Get: Count(self: Collection[T]) -> int

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class KeyedCollection(Collection):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return KeyedCollection()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ChangeItemKey(self,*args):
  """
  ChangeItemKey(self: KeyedCollection[TKey,TItem],item: TItem,newKey: TKey)
   Changes the key associated with the specified element in the lookup dictionary.
  
   item: The element to change the key of.
   newKey: The new key for item.
  """
  pass
 def ClearItems(self,*args):
  """
  ClearItems(self: KeyedCollection[TKey,TItem])
   Removes all elements from the System.Collections.ObjectModel.KeyedCollection.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: KeyedCollection[TKey,TItem],key: TKey) -> bool
  
   Determines whether the collection contains an element with the specified key.
  
   key: The key to locate in the System.Collections.ObjectModel.KeyedCollection.
   Returns: true if the System.Collections.ObjectModel.KeyedCollection contains an element with the specified key; otherwise,false.
  """
  pass
 def GetKeyForItem(self,*args):
  """
  GetKeyForItem(self: KeyedCollection[TKey,TItem],item: TItem) -> TKey
  
   When implemented in a derived class,extracts the key from the specified element.
  
   item: The element from which to extract the key.
   Returns: The key for the specified element.
  """
  pass
 def InsertItem(self,*args):
  """
  InsertItem(self: KeyedCollection[TKey,TItem],index: int,item: TItem)
   Inserts an element into the System.Collections.ObjectModel.KeyedCollection at the specified index.
  
   index: The zero-based index at which item should be inserted.
   item: The object to insert.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: KeyedCollection[TKey,TItem],key: TKey) -> bool
  
   Removes the element with the specified key from the System.Collections.ObjectModel.KeyedCollection.
  
   key: The key of the element to remove.
   Returns: true if the element is successfully removed; otherwise,false.  This method also returns false if key is not found in the System.Collections.ObjectModel.KeyedCollection.
  """
  pass
 def RemoveItem(self,*args):
  """
  RemoveItem(self: KeyedCollection[TKey,TItem],index: int)
   Removes the element at the specified index of the System.Collections.ObjectModel.KeyedCollection.
  
   index: The index of the element to remove.
  """
  pass
 def SetItem(self,*args):
  """
  SetItem(self: KeyedCollection[TKey,TItem],index: int,item: TItem)
   Replaces the item at the specified index with the specified item.
  
   index: The zero-based index of the item to be replaced.
   item: The new item.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)
  __new__(cls: type,comparer: IEqualityComparer[TKey])
  __new__(cls: type,comparer: IEqualityComparer[TKey],dictionaryCreationThreshold: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Comparer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the generic equality comparer that is used to determine equality of keys in the collection.

Get: Comparer(self: KeyedCollection[TKey,TItem]) -> IEqualityComparer[TKey]

"""

 Dictionary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the lookup dictionary of the System.Collections.ObjectModel.KeyedCollection.

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class ObservableCollection(Collection):
 """
 ObservableCollection[T]()
 ObservableCollection[T](list: List[T])
 ObservableCollection[T](collection: IEnumerable[T])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ObservableCollection()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BlockReentrancy(self,*args):
  """
  BlockReentrancy(self: ObservableCollection[T]) -> IDisposable
  
   Disallows reentrant attempts to change this collection.
   Returns: An System.IDisposable object that can be used to dispose of the object.
  """
  pass
 def CheckReentrancy(self,*args):
  """
  CheckReentrancy(self: ObservableCollection[T])
   Checks for reentrant attempts to change this collection.
  """
  pass
 def ClearItems(self,*args):
  """
  ClearItems(self: ObservableCollection[T])
   Removes all items from the collection.
  """
  pass
 def InsertItem(self,*args):
  """
  InsertItem(self: ObservableCollection[T],index: int,item: T)
   Inserts an item into the collection at the specified index.
  
   index: The zero-based index at which item should be inserted.
   item: The object to insert.
  """
  pass
 def Move(self,oldIndex,newIndex):
  """
  Move(self: ObservableCollection[T],oldIndex: int,newIndex: int)
   Moves the item at the specified index to a new location in the collection.
  
   oldIndex: The zero-based index specifying the location of the item to be moved.
   newIndex: The zero-based index specifying the new location of the item.
  """
  pass
 def MoveItem(self,*args):
  """
  MoveItem(self: ObservableCollection[T],oldIndex: int,newIndex: int)
   Moves the item at the specified index to a new location in the collection.
  
   oldIndex: The zero-based index specifying the location of the item to be moved.
   newIndex: The zero-based index specifying the new location of the item.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: ObservableCollection[T],e: NotifyCollectionChangedEventArgs)
   Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
  
   e: Arguments of the event being raised.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: ObservableCollection[T],e: PropertyChangedEventArgs)
   Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
  
   e: Arguments of the event being raised.
  """
  pass
 def RemoveItem(self,*args):
  """
  RemoveItem(self: ObservableCollection[T],index: int)
   Removes the item at the specified index of the collection.
  
   index: The zero-based index of the element to remove.
  """
  pass
 def SetItem(self,*args):
  """
  SetItem(self: ObservableCollection[T],index: int,item: T)
   Replaces the element at the specified index.
  
   index: The zero-based index of the element to replace.
   item: The new value for the element at the specified index.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,list: List[T])
  __new__(cls: type,collection: IEnumerable[T])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


 CollectionChanged=None
 PropertyChanged=None


class ReadOnlyCollection(object):
 """ ReadOnlyCollection[T](list: IList[T]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReadOnlyCollection()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Contains(self,value):
  """
  Contains(self: ReadOnlyCollection[T],value: T) -> bool
  
   Determines whether an element is in the System.Collections.ObjectModel.ReadOnlyCollection.
  
   value: The object to locate in the System.Collections.ObjectModel.ReadOnlyCollection. The value can be null for reference types.
   Returns: true if value is found in the System.Collections.ObjectModel.ReadOnlyCollection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """ CopyTo(self: ReadOnlyCollection[T],array: Array[T],index: int) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ReadOnlyCollection[T]) -> IEnumerator[T]
  
   Returns an enumerator that iterates through the System.Collections.ObjectModel.ReadOnlyCollection.
   Returns: An System.Collections.Generic.IEnumerator for the System.Collections.ObjectModel.ReadOnlyCollection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: ReadOnlyCollection[T],value: T) -> int
  
   Searches for the specified object and returns the zero-based index of the first occurrence within the entire System.Collections.ObjectModel.ReadOnlyCollection.
  
   value: The object to locate in the System.Collections.Generic.List. The value can be null for reference types.
   Returns: The zero-based index of the first occurrence of item within the entire System.Collections.ObjectModel.ReadOnlyCollection,if found; otherwise,-1.
  """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[T],item: T) -> bool
  
   Determines whether the System.Collections.Generic.ICollection contains a specific value.
  
   item: The object to locate in the System.Collections.Generic.ICollection.
   Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise,false.
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,list):
  """ __new__(cls: type,list: IList[T]) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of elements contained in the System.Collections.ObjectModel.ReadOnlyCollection instance.

Get: Count(self: ReadOnlyCollection[T]) -> int

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""



class ReadOnlyDictionary(object):
 """ ReadOnlyDictionary[TKey,TValue](dictionary: IDictionary[TKey,TValue]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReadOnlyDictionary()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ContainsKey(self,key):
  """ ContainsKey(self: ReadOnlyDictionary[TKey,TValue],key: TKey) -> bool """
  pass
 def GetEnumerator(self):
  """ GetEnumerator(self: ReadOnlyDictionary[TKey,TValue]) -> IEnumerator[KeyValuePair[TKey,TValue]] """
  pass
 def TryGetValue(self,key,value):
  """ TryGetValue(self: ReadOnlyDictionary[TKey,TValue],key: TKey) -> (bool,TValue) """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IDictionary[TKey,TValue],key: TKey) -> bool
  
   Determines whether the System.Collections.Generic.IDictionary contains an element with the specified key.
  
   key: The key to locate in the System.Collections.Generic.IDictionary.
   Returns: true if the System.Collections.Generic.IDictionary contains an element with the key; otherwise,false.
  __contains__(self: IDictionary,key: object) -> bool
  
   Determines whether the System.Collections.IDictionary object contains an element with the specified key.
  
   key: The key to locate in the System.Collections.IDictionary object.
   Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise,false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,dictionary):
  """ __new__(cls: type,dictionary: IDictionary[TKey,TValue]) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: ReadOnlyDictionary[TKey,TValue]) -> int

"""

 Dictionary=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Keys(self: ReadOnlyDictionary[TKey,TValue]) -> KeyCollection

"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Values(self: ReadOnlyDictionary[TKey,TValue]) -> ValueCollection

"""


 KeyCollection=None
 ValueCollection=None


class ReadOnlyObservableCollection(ReadOnlyCollection):
 """ ReadOnlyObservableCollection[T](list: ObservableCollection[T]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReadOnlyObservableCollection()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: ReadOnlyObservableCollection[T],args: NotifyCollectionChangedEventArgs)
   Raises the System.Collections.ObjectModel.ReadOnlyObservableCollection event using the provided arguments.
  
   args: Arguments of the event being raised.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: ReadOnlyObservableCollection[T],args: PropertyChangedEventArgs)
   Raises the System.Collections.ObjectModel.ReadOnlyObservableCollection event using the provided arguments.
  
   args: Arguments of the event being raised.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,list):
  """ __new__(cls: type,list: ObservableCollection[T]) """
  pass
 def __reduce_ex__(self,*args):
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""


 CollectionChanged=None
 PropertyChanged=None



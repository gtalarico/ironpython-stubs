class TimelineCollection(Animatable,ISealable,IAnimatable,IResource,IList,ICollection,IEnumerable,IList[Timeline],ICollection[Timeline],IEnumerable[Timeline]):
 """
 Represents a collection of System.Windows.Media.Animation.Timeline objects.

 

 TimelineCollection()

 TimelineCollection(capacity: int)

 TimelineCollection(collection: IEnumerable[Timeline])
 """
 def Add(self,value):
  """
  Add(self: TimelineCollection,value: Timeline)

   Inserts a new System.Windows.Media.Animation.Timeline object into the 

    System.Windows.Media.Animation.TimelineCollection.

  

  

   value: The object to add.
  """
  pass
 def Clear(self):
  """
  Clear(self: TimelineCollection)

   Removes all items from the System.Windows.Media.Animation.TimelineCollection.
  """
  pass
 def Clone(self):
  """
  Clone(self: TimelineCollection) -> TimelineCollection

  

   Creates a modifiable clone of this System.Windows.Media.Animation.TimelineCollection,making 

    deep copies of this object's values. When copying dependency properties,this method copies 

    resource references and data bindings (but they might no longer resolve) but not animations or 

    their current values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """ CloneCore(self: TimelineCollection,source: Freezable) """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: TimelineCollection) -> TimelineCollection

  

   Creates a modifiable clone of this System.Windows.Media.Animation.TimelineCollection object,

    making deep copies of this object's current values. Resource references,data bindings,and 

    animations are not copied,but their current values are.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """ CloneCurrentValueCore(self: TimelineCollection,source: Freezable) """
  pass
 def Contains(self,value):
  """
  Contains(self: TimelineCollection,value: Timeline) -> bool

  

   Determines whether the System.Windows.Media.Animation.TimelineCollection contains the specified 

    System.Windows.Media.Animation.Timeline object.

  

  

   value: The object to locate.

   Returns: true if value is found; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: TimelineCollection,array: Array[Timeline],index: int)

   Copies the items of the System.Windows.Media.Animation.TimelineCollection to the passed Timeline 

    array,starting at the specified index position.

  

  

   array: The destination array.

   index: The zero-based index position where copying begins.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable

  

   Initializes a new instance of the System.Windows.Freezable class.

   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """ CreateInstanceCore(self: TimelineCollection) -> Freezable """
  pass
 def FreezeCore(self,*args):
  """ FreezeCore(self: TimelineCollection,isChecking: bool) -> bool """
  pass
 def GetAsFrozenCore(self,*args):
  """ GetAsFrozenCore(self: TimelineCollection,source: Freezable) """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """ GetCurrentValueAsFrozenCore(self: TimelineCollection,source: Freezable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TimelineCollection) -> Enumerator

  

   Gets an enumerator that can iterate the members of the collection.

   Returns: An object that can iterate the members of the collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: TimelineCollection,value: Timeline) -> int

  

   Gets the zero-based index position of a Timeline object in the 

    System.Windows.Media.Animation.TimelineCollection.

  

  

   value: The object to locate.

   Returns: The index position of value within this list.  If not found,-1 is returned.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: TimelineCollection,index: int,value: Timeline)

   Inserts the specified Timeline object into this 

    System.Windows.Media.Animation.TimelineCollection at the specified index position.

  

  

   index: The zero-based index position into which value is inserted.

   value: The object to insert.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Freezable)

   Called when the current System.Windows.Freezable object is modified.
  """
  pass
 def OnFreezablePropertyChanged(self,*args):
  """
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject,property: DependencyProperty)

   This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 

    intended to be used directly from your code.

  

  

   oldValue: The previous value of the data member.

   newValue: The current value of the data member.

   property: The property that changed.

  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject)

   Ensures that appropriate context pointers are established for a 

    System.Windows.DependencyObjectType data member that has just been set.

  

  

   oldValue: The previous value of the data member.

   newValue: The current value of the data member.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: Freezable,e: DependencyPropertyChangedEventArgs)

   Overrides the System.Windows.DependencyObject implementation of 

    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr

    gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 

    dependency property of type System.Windows.Freezable.

  

  

   e: Event data that contains information about which property changed,and its old and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)

   Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 

    System.Windows.Freezable must call this method at the beginning of any API that reads data 

    members that are not dependency properties.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: TimelineCollection,value: Timeline) -> bool

  

   Removes the first occurrence of a specified System.Windows.Media.Animation.Timeline from this 

    System.Windows.Media.Animation.TimelineCollection.

  

  

   value: The object to remove.

   Returns: true if the operation was successful; otherwise,false.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: TimelineCollection,index: int)

   Removes the System.Windows.Media.Animation.Timeline at the specified index position from this 

    System.Windows.Media.Animation.TimelineCollection.

  

  

   index: The zero-based index position of the item to remove.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)

   Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 

    its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 

    should call this method at the end of any API that modifies class members that are not stored as 

    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)

   Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 

    valid threading context. System.Windows.Freezable inheritors should call this method at the 

    beginning of any API that writes to data members that are not dependency properties.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[Timeline],item: Timeline) -> bool

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
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,capacity: int)

  __new__(cls: type,collection: IEnumerable[Timeline])
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items contained in this System.Windows.Media.Animation.TimelineCollection.



Get: Count(self: TimelineCollection) -> int



"""


 Enumerator=None


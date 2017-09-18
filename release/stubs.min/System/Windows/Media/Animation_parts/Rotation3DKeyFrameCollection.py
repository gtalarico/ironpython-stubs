class Rotation3DKeyFrameCollection(Freezable,ISealable,IList,ICollection,IEnumerable):
 """
 Represents a collection of System.Windows.Media.Animation.Rotation3DKeyFrame objects.

 

 Rotation3DKeyFrameCollection()
 """
 def Add(self,keyFrame):
  """
  Add(self: Rotation3DKeyFrameCollection,keyFrame: Rotation3DKeyFrame) -> int

  

   Adds a System.Windows.Media.Animation.Rotation3DKeyFrame to the end of the collection.

  

   keyFrame: The System.Windows.Media.Animation.Rotation3DKeyFrame to add to the end of the collection.

   Returns: The index at which the keyFrame was added.
  """
  pass
 def Clear(self):
  """
  Clear(self: Rotation3DKeyFrameCollection)

   Removes all System.Windows.Media.Animation.Rotation3DKeyFrame objects from the collection.
  """
  pass
 def Clone(self):
  """
  Clone(self: Rotation3DKeyFrameCollection) -> Rotation3DKeyFrameCollection

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Rotation3DKeyFrameCollection,

    making deep copies of this object's values. When copying dependency properties,this method 

    copies resource references and data bindings (but they might no longer resolve) but not 

    animations or their current values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: Rotation3DKeyFrameCollection,sourceFreezable: Freezable)

   Makes this instance a deep copy of the specified 

    System.Windows.Media.Animation.Rotation3DKeyFrameCollection. When copying dependency properties,

    this method copies resource references and data bindings (but they might no longer resolve) but 

    not animations or their current values.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Rotation3DKeyFrameCollection to clone.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: Rotation3DKeyFrameCollection,sourceFreezable: Freezable)

   Makes this instance a modifiable deep copy of the specified 

    System.Windows.Media.Animation.Rotation3DKeyFrameCollection using current property values. 

    Resource references,data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Rotation3DKeyFrameCollection to clone.
  """
  pass
 def Contains(self,keyFrame):
  """
  Contains(self: Rotation3DKeyFrameCollection,keyFrame: Rotation3DKeyFrame) -> bool

  

   Gets a value that indicates whether the collection contains the specified 

    System.Windows.Media.Animation.Rotation3DKeyFrame.

  

  

   keyFrame: The System.Windows.Media.Animation.Rotation3DKeyFrame to locate in the collection.

   Returns: true if the collection contains keyFrame; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: Rotation3DKeyFrameCollection,array: Array[Rotation3DKeyFrame],index: int)

   Copies all of the System.Windows.Media.Animation.Rotation3DKeyFrame objects in a collection to a 

    specified array.

  

  

   array: Identifies the array to which content is copied.

   index: Index position in the array to which the contents of the collection are copied.
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
  """
  CreateInstanceCore(self: Rotation3DKeyFrameCollection) -> Freezable

  

   Creates a new,frozen instance of System.Windows.Media.Animation.Rotation3DKeyFrameCollection.

   Returns: A frozen instance of System.Windows.Media.Animation.Rotation3DKeyFrameCollection.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Rotation3DKeyFrameCollection,isChecking: bool) -> bool

  

   Makes this instance of System.Windows.Media.Animation.Rotation3DKeyFrameCollection unmodifiable 

    or determines whether it can be made unmodifiable.

  

  

   isChecking: true to check if this instance can be frozen; false to freeze this instance.

   Returns: If isChecking is true,this method returns true if this instance can be made read-only,or false 

    if it cannot be made read-only. If isChecking is false,this method returns true if this 

    instance is now read-only,or false if it cannot be made read-only,with the side effect of 

    having begun to change the frozen status of this object.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: Rotation3DKeyFrameCollection,sourceFreezable: Freezable)

   Makes this instance a clone of the specified 

    System.Windows.Media.Animation.Rotation3DKeyFrameCollection object.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Rotation3DKeyFrameCollection object to clone.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Rotation3DKeyFrameCollection,sourceFreezable: Freezable)

   Makes this instance a frozen clone of the specified 

    System.Windows.Media.Animation.Rotation3DKeyFrameCollection. Resource references,data bindings,

    and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Rotation3DKeyFrameCollection to copy and freeze.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: Rotation3DKeyFrameCollection) -> IEnumerator

  

   Returns an enumerator that can iterate through the collection.

   Returns: An System.Collections.IEnumerator that can iterate through the collection.
  """
  pass
 def IndexOf(self,keyFrame):
  """
  IndexOf(self: Rotation3DKeyFrameCollection,keyFrame: Rotation3DKeyFrame) -> int

  

   Searches for the specified System.Windows.Media.Animation.Rotation3DKeyFrame and returns the 

    zero-based index of the first occurrence within the entire collection.

  

  

   keyFrame: The System.Windows.Media.Animation.Rotation3DKeyFrame to locate in the collection.

   Returns: The zero-based index of the first occurrence of keyFrame within the entire collection,if found; 

    otherwise,-1.
  """
  pass
 def Insert(self,index,keyFrame):
  """
  Insert(self: Rotation3DKeyFrameCollection,index: int,keyFrame: Rotation3DKeyFrame)

   Inserts a System.Windows.Media.Animation.Rotation3DKeyFrame into a specific location within the 

    collection.

  

  

   index: The index position at which the System.Windows.Media.Animation.Rotation3DKeyFrame is inserted.

   keyFrame: The System.Windows.Media.Animation.Rotation3DKeyFrame object to insert in the collection.
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
 def Remove(self,keyFrame):
  """
  Remove(self: Rotation3DKeyFrameCollection,keyFrame: Rotation3DKeyFrame)

   Removes a System.Windows.Media.Animation.Rotation3DKeyFrame object from the collection.

  

   keyFrame: Identifies the System.Windows.Media.Animation.Rotation3DKeyFrame to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: Rotation3DKeyFrameCollection,index: int)

   Removes the System.Windows.Media.Animation.Rotation3DKeyFrame at the specified index position 

    from the collection.

  

  

   index: Index position of the System.Windows.Media.Animation.Rotation3DKeyFrame to be removed.
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of key frames contained in the System.Windows.Media.Animation.Rotation3DKeyFrameCollection.



Get: Count(self: Rotation3DKeyFrameCollection) -> int



"""

 IsFixedSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates if the collection is frozen.



Get: IsFixedSize(self: Rotation3DKeyFrameCollection) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates if the collection is read-only.



Get: IsReadOnly(self: Rotation3DKeyFrameCollection) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to the collection is synchronized (thread-safe).



Get: IsSynchronized(self: Rotation3DKeyFrameCollection) -> bool



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the collection.



Get: SyncRoot(self: Rotation3DKeyFrameCollection) -> object



"""


 Empty=None


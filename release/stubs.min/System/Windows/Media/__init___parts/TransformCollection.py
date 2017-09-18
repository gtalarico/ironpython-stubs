class TransformCollection(Animatable,ISealable,IAnimatable,IResource,IList,ICollection,IEnumerable,IList[Transform],ICollection[Transform],IEnumerable[Transform]):
 """
 Represents a collection of System.Windows.Media.Transform objects that can be individually accessed by index.
 
 TransformCollection()
 TransformCollection(capacity: int)
 TransformCollection(collection: IEnumerable[Transform])
 """
 def Add(self,value):
  """
  Add(self: TransformCollection,value: Transform)
   Adds a System.Windows.Media.Transform to the end of the 
    System.Windows.Media.TransformCollection.
  
  
   value: The System.Windows.Media.Transform to add to the end of the 
    System.Windows.Media.TransformCollection.
  """
  pass
 def Clear(self):
  """
  Clear(self: TransformCollection)
   Removes all items from the System.Windows.Media.TransformCollection.
  """
  pass
 def Clone(self):
  """
  Clone(self: TransformCollection) -> TransformCollection
  
   Creates a modifiable clone of this System.Windows.Media.TransformCollection,
    making deep copies of this object's values. When copying dependency properties,
    this method copies resource references and data bindings (but they might no 
    longer resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """ CloneCore(self: TransformCollection,source: Freezable) """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: TransformCollection) -> TransformCollection
  
   Creates a modifiable clone of this System.Windows.Media.TransformCollection 
    object,making deep copies of this object's current values. Resource 
    references,data bindings,and animations are not copied,but their current 
    values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """ CloneCurrentValueCore(self: TransformCollection,source: Freezable) """
  pass
 def Contains(self,value):
  """
  Contains(self: TransformCollection,value: Transform) -> bool
  
   Determines whether the System.Windows.Media.TransformCollection contains the 
    specified System.Windows.Media.Transform.
  
  
   value: The System.Windows.Media.Transform to locate in the 
    System.Windows.Media.TransformCollection.
  
   Returns: true if the System.Windows.Media.Transform is found in the 
    System.Windows.Media.TransformCollection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: TransformCollection,array: Array[Transform],index: int)
   Copies the items of the System.Windows.Media.TransformCollection to an array,
    starting at the specified array index.
  
  
   array: The one-dimensional array that is the destination of the items copied from the 
    System.Windows.Media.TransformCollection. The array must have zero-based 
    indexing.
  
   index: The zero-based index in array at which copying begins.
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
  """ CreateInstanceCore(self: TransformCollection) -> Freezable """
  pass
 def FreezeCore(self,*args):
  """ FreezeCore(self: TransformCollection,isChecking: bool) -> bool """
  pass
 def GetAsFrozenCore(self,*args):
  """ GetAsFrozenCore(self: TransformCollection,source: Freezable) """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """ GetCurrentValueAsFrozenCore(self: TransformCollection,source: Freezable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TransformCollection) -> Enumerator
  
   Returns an enumerator that can iterate through the 
    System.Windows.Media.TransformCollection.
  
   Returns: A System.Windows.Media.TransformCollection.Enumerator that can be used to 
    iterate through the System.Windows.Media.TransformCollection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: TransformCollection,value: Transform) -> int
  
   Determines the index of the specified item in the 
    System.Windows.Media.TransformCollection.
  
  
   value: The System.Windows.Media.Transform to locate in the 
    System.Windows.Media.TransformCollection.
  
   Returns: The index of value if found in the System.Windows.Media.TransformCollection; 
    otherwise,-1.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: TransformCollection,index: int,value: Transform)
   Inserts a System.Windows.Media.Transform into the 
    System.Windows.Media.TransformCollection at the specified index.
  
  
   index: The zero-based index at which value should be inserted.
   value: The System.Windows.Media.Transform to insert into the 
    System.Windows.Media.TransformCollection.
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
   This member supports the Windows Presentation Foundation (WPF) infrastructure 
    and is not intended to be used directly from your code.
  
  
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
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
    handlers in response to a changing dependency property of type 
    System.Windows.Freezable.
  
  
   e: Event data that contains information about which property changed,and its old 
    and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)
   Ensures that the System.Windows.Freezable is being accessed from a valid 
    thread. Inheritors of System.Windows.Freezable must call this method at the 
    beginning of any API that reads data members that are not dependency 
    properties.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: TransformCollection,value: Transform) -> bool
  
   Removes the first occurrence of the specified System.Windows.Media.Transform 
    from the System.Windows.Media.TransformCollection.
  
  
   value: The System.Windows.Media.Transform to remove from the 
    System.Windows.Media.TransformCollection.
  
   Returns: true if value was removed from the System.Windows.Media.TransformCollection; 
    otherwise,false.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: TransformCollection,index: int)
   Removes the System.Windows.Media.Transform at the specified index.
  
   index: The zero-based index of the System.Windows.Media.Transform to remove.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)
   Raises the System.Windows.Freezable.Changed event for the 
    System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
    method. Classes that derive from System.Windows.Freezable should call this 
    method at the end of any API that modifies class members that are not stored as 
    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)
   Verifies that the System.Windows.Freezable is not frozen and that it is being 
    accessed from a valid threading context. System.Windows.Freezable inheritors 
    should call this method at the beginning of any API that writes to data members 
    that are not dependency properties.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[Transform],item: Transform) -> bool
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,
    false.
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
  __new__(cls: type,collection: IEnumerable[Transform])
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items contained in the System.Windows.Media.TransformCollection.

Get: Count(self: TransformCollection) -> int

"""


 Enumerator=None


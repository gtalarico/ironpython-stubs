class PathFigureCollection(Animatable,ISealable,IAnimatable,IResource,IFormattable,IList,ICollection,IEnumerable,IList[PathFigure],ICollection[PathFigure],IEnumerable[PathFigure]):
 """
 Represents a collection of System.Windows.Media.PathFigure objects that collectively make up the geometry of a System.Windows.Media.PathGeometry.
 
 PathFigureCollection()
 PathFigureCollection(capacity: int)
 PathFigureCollection(collection: IEnumerable[PathFigure])
 """
 def Add(self,value):
  """
  Add(self: PathFigureCollection,value: PathFigure)
   Adds a System.Windows.Media.PathFigure to the end of the collection.
  
   value: The System.Windows.Media.PathFigure to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: PathFigureCollection)
   Removes all items from the System.Windows.Media.PathFigureCollection.
  """
  pass
 def Clone(self):
  """
  Clone(self: PathFigureCollection) -> PathFigureCollection
  
   Creates a modifiable clone of this System.Windows.Media.PathFigureCollection,
    making deep copies of this object's values. When copying dependency properties,
    this method copies resource references and data bindings (but they might no 
    longer resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """ CloneCore(self: PathFigureCollection,source: Freezable) """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: PathFigureCollection) -> PathFigureCollection
  
   Creates a modifiable clone of this System.Windows.Media.PathFigureCollection 
    object,making deep copies of this object's current values. Resource 
    references,data bindings,and animations are not copied,but their current 
    values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """ CloneCurrentValueCore(self: PathFigureCollection,source: Freezable) """
  pass
 def Contains(self,value):
  """
  Contains(self: PathFigureCollection,value: PathFigure) -> bool
  
   Determines whether the collection contains the specified 
    System.Windows.Media.PathFigure.
  
  
   value: The System.Windows.Media.PathFigure being queried for.
   Returns: true if value is in the System.Windows.Media.PathFigureCollection; otherwise,
    false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: PathFigureCollection,array: Array[PathFigure],index: int)
   Copies the entire System.Windows.Media.PathFigureCollection to a 
    one-dimensional array of type System.Windows.Media.PathFigure,starting at the 
    specified index of the target array.
  
  
   array: The array into which the collection's items are to be copied.
   index: The index of array at which to start copying the contents of the 
    System.Windows.Media.PathFigureCollection.
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
  """ CreateInstanceCore(self: PathFigureCollection) -> Freezable """
  pass
 def FreezeCore(self,*args):
  """ FreezeCore(self: PathFigureCollection,isChecking: bool) -> bool """
  pass
 def GetAsFrozenCore(self,*args):
  """ GetAsFrozenCore(self: PathFigureCollection,source: Freezable) """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """ GetCurrentValueAsFrozenCore(self: PathFigureCollection,source: Freezable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PathFigureCollection) -> Enumerator
  
   Returns an enumerator that can iterate through the collection.
   Returns: An System.Windows.Media.PathFigureCollection.Enumerator that can iterate 
    through the collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: PathFigureCollection,value: PathFigure) -> int
  
   Searches for the specified System.Windows.Media.PathFigure and returns the 
    zero-based index of the first occurrence within the entire collection.
  
  
   value: The System.Windows.Media.PathFigure to locate in the collection.
   Returns: The index of value if found in the System.Windows.Media.PathFigureCollection; 
    otherwise,-1.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: PathFigureCollection,index: int,value: PathFigure)
   Inserts a System.Windows.Media.PathFigure into a specific location within the 
    collection.
  
  
   index: The index position at which the System.Windows.Media.PathFigure is inserted.
   value: The System.Windows.Media.PathFigure object to insert in the collection.
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
 @staticmethod
 def Parse(source):
  """
  Parse(source: str) -> PathFigureCollection
  
   Returns an instance of System.Windows.Media.PathFigureCollection created from a 
    specified string.
  
  
   source: The string that is converted to a System.Windows.Media.PathFigureCollection.
   Returns: An instance of System.Windows.Media.PathFigureCollection created from source.
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
  Remove(self: PathFigureCollection,value: PathFigure) -> bool
  
   Removes a System.Windows.Media.PathFigure object from the collection.
  
   value: Identifies the System.Windows.Media.PathFigure to remove from the collection.
   Returns: true if value was removed from the System.Windows.Media.PathFigureCollection; 
    otherwise,false.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: PathFigureCollection,index: int)
   Removes the System.Windows.Media.PathFigure at the specified index position 
    from the collection.
  
  
   index: Index position of the System.Windows.Media.PathFigure to be removed.
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
 def ToString(self,provider=None):
  """
  ToString(self: PathFigureCollection,provider: IFormatProvider) -> str
  
   Converts the current value of a System.Windows.Media.PathFigureCollection to a 
    System.String using the specified culture-specific formatting information.
  
  
   provider: Culture-specific formatting information.
   Returns: A string representation of the System.Windows.Media.PathFigureCollection.
  ToString(self: PathFigureCollection) -> str
  
   Converts the current value of a System.Windows.Media.PathFigureCollection to a 
    System.String.
  
   Returns: A string representation of the System.Windows.Media.PathFigureCollection.
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
  __contains__(self: ICollection[PathFigure],item: PathFigure) -> bool
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,
    false.
  """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
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
  __new__(cls: type,collection: IEnumerable[PathFigure])
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of path figures contained in the System.Windows.Media.PathFigureCollection.

Get: Count(self: PathFigureCollection) -> int

"""


 Enumerator=None


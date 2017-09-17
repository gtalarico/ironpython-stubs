class GroupDescription(object,INotifyPropertyChanged):
 """ Provides an abstract base class for types that describe how to divide the items in a collection into groups. """
 def add_PropertyChanged(self,*args):
  """ add_PropertyChanged(self: GroupDescription,value: PropertyChangedEventHandler) """
  pass
 def GroupNameFromItem(self,item,level,culture):
  """
  GroupNameFromItem(self: GroupDescription,item: object,level: int,culture: CultureInfo) -> object
  
   Returns the group name(s) for the given item.
  
   item: The item to return group names for.
   level: The level of grouping.
   culture: The System.Globalization.CultureInfo to supply to the converter.
   Returns: The group name(s) for the given item.
  """
  pass
 def NamesMatch(self,groupName,itemName):
  """
  NamesMatch(self: GroupDescription,groupName: object,itemName: object) -> bool
  
   Returns a value that indicates whether the group name and the item name match 
    such that the item belongs to the group.
  
  
   groupName: The name of the group to check.
   itemName: The name of the item to check.
   Returns: true if the names match and the item belongs to the group; otherwise,false.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: GroupDescription,e: PropertyChangedEventArgs)
   Raises the System.ComponentModel.GroupDescription.PropertyChanged event.
  
   e: Arguments of the event being raised.
  """
  pass
 def remove_PropertyChanged(self,*args):
  """ remove_PropertyChanged(self: GroupDescription,value: PropertyChangedEventHandler) """
  pass
 def ShouldSerializeGroupNames(self):
  """
  ShouldSerializeGroupNames(self: GroupDescription) -> bool
  
   Returns whether serialization processes should serialize the effective value of 
    the System.ComponentModel.GroupDescription.GroupNames property on instances of 
    this class.
  
   Returns: Returns true if the System.ComponentModel.GroupDescription.GroupNames property 
    value should be serialized; otherwise,false.
  """
  pass
 def ShouldSerializeSortDescriptions(self):
  """ ShouldSerializeSortDescriptions(self: GroupDescription) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CustomSort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomSort(self: GroupDescription) -> IComparer

Set: CustomSort(self: GroupDescription)=value
"""

 GroupNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of names that are used to initialize a group with a set of subgroups with the given names.

Get: GroupNames(self: GroupDescription) -> ObservableCollection[object]

"""

 SortDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SortDescriptions(self: GroupDescription) -> SortDescriptionCollection

"""



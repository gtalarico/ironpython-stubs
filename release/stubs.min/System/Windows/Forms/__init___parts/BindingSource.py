class BindingSource(Component,IComponent,IDisposable,IBindingListView,IBindingList,IList,ICollection,IEnumerable,ITypedList,ICancelAddNew,ISupportInitializeNotification,ISupportInitialize,ICurrencyManagerProvider):
 """
 Encapsulates the data source for a form.

 

 BindingSource()

 BindingSource(dataSource: object,dataMember: str)

 BindingSource(container: IContainer)
 """
 def Add(self,value):
  """
  Add(self: BindingSource,value: object) -> int

  

   Adds an existing item to the internal list.

  

   value: An System.Object to be added to the internal list.

   Returns: The zero-based index at which value was added to the underlying list represented by the 

    System.Windows.Forms.BindingSource.List property.
  """
  pass
 def AddNew(self):
  """
  AddNew(self: BindingSource) -> object

  

   Adds a new item to the underlying list.

   Returns: The System.Object that was created and added to the list.
  """
  pass
 def ApplySort(self,*__args):
  """
  ApplySort(self: BindingSource,sorts: ListSortDescriptionCollection)

   Sorts the data source with the specified sort descriptions.

  

   sorts: A System.ComponentModel.ListSortDescriptionCollection containing the sort descriptions to apply 

    to the data source.

  

  ApplySort(self: BindingSource,property: PropertyDescriptor,sort: ListSortDirection)

   Sorts the data source using the specified property descriptor and sort direction.

  

   property: A System.ComponentModel.PropertyDescriptor that describes the property by which to sort the data 

    source.

  

   sort: A System.ComponentModel.ListSortDirection indicating how the list should be sorted.
  """
  pass
 def CancelEdit(self):
  """
  CancelEdit(self: BindingSource)

   Cancels the current edit operation.
  """
  pass
 def Clear(self):
  """
  Clear(self: BindingSource)

   Removes all elements from the list.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: BindingSource,value: object) -> bool

  

   Determines whether an object is an item in the list.

  

   value: The System.Object to locate in the underlying list represented by the 

    System.Windows.Forms.BindingSource.List property. The value can be null.

  

   Returns: true if the value parameter is found in the System.Windows.Forms.BindingSource.List; otherwise,

    false.
  """
  pass
 def CopyTo(self,arr,index):
  """
  CopyTo(self: BindingSource,arr: Array,index: int)

   Copies the contents of the System.Windows.Forms.BindingSource.List to the specified array,

    starting at the specified index value.

  

  

   arr: The destination array.

   index: The index in the destination array at which to start the copy operation.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: BindingSource,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.BindingSource and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndEdit(self):
  """
  EndEdit(self: BindingSource)

   Applies pending changes to the underlying data source.
  """
  pass
 def Find(self,*__args):
  """
  Find(self: BindingSource,prop: PropertyDescriptor,key: object) -> int

  

   Searches for the index of the item that has the given property descriptor.

  

   prop: The System.ComponentModel.PropertyDescriptor to search for.

   key: The value of prop to match.

   Returns: The zero-based index of the item that has the given value for 

    System.ComponentModel.PropertyDescriptor.

  

  Find(self: BindingSource,propertyName: str,key: object) -> int

  

   Returns the index of the item in the list with the specified property name and value.

  

   propertyName: The name of the property to search for.

   key: The value of the item with the specified propertyName to find.

   Returns: The zero-based index of the item with the specified property name and value.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: BindingSource) -> IEnumerator

  

   Retrieves an enumerator for the System.Windows.Forms.BindingSource.List.

   Returns: An System.Collections.IEnumerator for the System.Windows.Forms.BindingSource.List.
  """
  pass
 def GetItemProperties(self,listAccessors):
  """
  GetItemProperties(self: BindingSource,listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection

  

   Retrieves an array of System.ComponentModel.PropertyDescriptor objects representing the bindable 

    properties of the data source list type.

  

  

   listAccessors: An array of System.ComponentModel.PropertyDescriptor objects to find in the list as bindable.

   Returns: An array of System.ComponentModel.PropertyDescriptor objects that represents the properties on 

    this list type used to bind data.
  """
  pass
 def GetListName(self,listAccessors):
  """
  GetListName(self: BindingSource,listAccessors: Array[PropertyDescriptor]) -> str

  

   Gets the name of the list supplying data for the binding.

  

   listAccessors: An array of System.ComponentModel.PropertyDescriptor objects to find in the list as bindable.

   Returns: The name of the list supplying the data for binding.
  """
  pass
 def GetRelatedCurrencyManager(self,dataMember):
  """
  GetRelatedCurrencyManager(self: BindingSource,dataMember: str) -> CurrencyManager

  

   Gets the related currency manager for the specified data member.

  

   dataMember: The name of column or list,within the data source to retrieve the currency manager for.

   Returns: The related System.Windows.Forms.CurrencyManager for the specified data member.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: BindingSource,value: object) -> int

  

   Searches for the specified object and returns the index of the first occurrence within the 

    entire list.

  

  

   value: The System.Object to locate in the underlying list represented by the 

    System.Windows.Forms.BindingSource.List property. The value can be null.

  

   Returns: The zero-based index of the first occurrence of the value parameter; otherwise,-1 if value is 

    not in the list.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: BindingSource,index: int,value: object)

   Inserts an item into the list at the specified index.

  

   index: The zero-based index at which value should be inserted.

   value: The System.Object to insert. The value can be null.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def MoveFirst(self):
  """
  MoveFirst(self: BindingSource)

   Moves to the first item in the list.
  """
  pass
 def MoveLast(self):
  """
  MoveLast(self: BindingSource)

   Moves to the last item in the list.
  """
  pass
 def MoveNext(self):
  """
  MoveNext(self: BindingSource)

   Moves to the next item in the list.
  """
  pass
 def MovePrevious(self):
  """
  MovePrevious(self: BindingSource)

   Moves to the previous item in the list.
  """
  pass
 def OnAddingNew(self,*args):
  """
  OnAddingNew(self: BindingSource,e: AddingNewEventArgs)

   Raises the System.Windows.Forms.BindingSource.AddingNew event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBindingComplete(self,*args):
  """
  OnBindingComplete(self: BindingSource,e: BindingCompleteEventArgs)

   Raises the System.Windows.Forms.BindingSource.BindingComplete event.

  

   e: A System.Windows.Forms.BindingCompleteEventArgs  that contains the event data.
  """
  pass
 def OnCurrentChanged(self,*args):
  """
  OnCurrentChanged(self: BindingSource,e: EventArgs)

   Raises the System.Windows.Forms.BindingSource.CurrentChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCurrentItemChanged(self,*args):
  """
  OnCurrentItemChanged(self: BindingSource,e: EventArgs)

   Raises the System.Windows.Forms.BindingSource.CurrentItemChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataError(self,*args):
  """
  OnDataError(self: BindingSource,e: BindingManagerDataErrorEventArgs)

   Raises the System.Windows.Forms.BindingSource.DataError event.

  

   e: A System.Windows.Forms.BindingManagerDataErrorEventArgs that contains the event data.
  """
  pass
 def OnDataMemberChanged(self,*args):
  """
  OnDataMemberChanged(self: BindingSource,e: EventArgs)

   Raises the System.Windows.Forms.BindingSource.DataMemberChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataSourceChanged(self,*args):
  """
  OnDataSourceChanged(self: BindingSource,e: EventArgs)

   Raises the System.Windows.Forms.BindingSource.DataSourceChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnListChanged(self,*args):
  """
  OnListChanged(self: BindingSource,e: ListChangedEventArgs)

   Raises the System.Windows.Forms.BindingSource.ListChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPositionChanged(self,*args):
  """
  OnPositionChanged(self: BindingSource,e: EventArgs)

   Raises the System.Windows.Forms.BindingSource.PositionChanged event.

  

   e: A System.ComponentModel.ListChangedEventArgs that contains the event data.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: BindingSource,value: object)

   Removes the specified item from the list.

  

   value: The item to remove from the underlying list represented by the 

    System.Windows.Forms.BindingSource.List property.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: BindingSource,index: int)

   Removes the item at the specified index in the list.

  

   index: The zero-based index of the item to remove.
  """
  pass
 def RemoveCurrent(self):
  """
  RemoveCurrent(self: BindingSource)

   Removes the current item from the list.
  """
  pass
 def RemoveFilter(self):
  """
  RemoveFilter(self: BindingSource)

   Removes the filter associated with the System.Windows.Forms.BindingSource.
  """
  pass
 def RemoveSort(self):
  """
  RemoveSort(self: BindingSource)

   Removes the sort associated with the System.Windows.Forms.BindingSource.
  """
  pass
 def ResetAllowNew(self):
  """
  ResetAllowNew(self: BindingSource)

   Reinitializes the System.Windows.Forms.BindingSource.AllowNew property.
  """
  pass
 def ResetBindings(self,metadataChanged):
  """
  ResetBindings(self: BindingSource,metadataChanged: bool)

   Causes a control bound to the System.Windows.Forms.BindingSource to reread all the items in the 

    list and refresh their displayed values.

  

  

   metadataChanged: true if the data schema has changed; false if only values have changed.
  """
  pass
 def ResetCurrentItem(self):
  """
  ResetCurrentItem(self: BindingSource)

   Causes a control bound to the System.Windows.Forms.BindingSource to reread the currently 

    selected item and refresh its displayed value.
  """
  pass
 def ResetItem(self,itemIndex):
  """
  ResetItem(self: BindingSource,itemIndex: int)

   Causes a control bound to the System.Windows.Forms.BindingSource to reread the item at the 

    specified index,and refresh its displayed value.

  

  

   itemIndex: The zero-based index of the item that has changed.
  """
  pass
 def ResumeBinding(self):
  """
  ResumeBinding(self: BindingSource)

   Resumes data binding.
  """
  pass
 def SuspendBinding(self):
  """
  SuspendBinding(self: BindingSource)

   Suspends data binding to prevent changes from updating the bound data source.
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
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
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

  __new__(cls: type,dataSource: object,dataMember: str)

  __new__(cls: type,container: IContainer)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 AllowEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items in the underlying list can be edited.



Get: AllowEdit(self: BindingSource) -> bool



"""

 AllowNew=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.BindingSource.AddNew method can be used to add items to the list.



Get: AllowNew(self: BindingSource) -> bool



Set: AllowNew(self: BindingSource)=value

"""

 AllowRemove=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items can be removed from the underlying list.



Get: AllowRemove(self: BindingSource) -> bool



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of items in the underlying list,taking the current System.Windows.Forms.BindingSource.Filter value into consideration.



Get: Count(self: BindingSource) -> int



"""

 CurrencyManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the currency manager associated with this System.Windows.Forms.BindingSource.



Get: CurrencyManager(self: BindingSource) -> CurrencyManager



"""

 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current item in the list.



Get: Current(self: BindingSource) -> object



"""

 DataMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the specific list in the data source to which the connector currently binds to.



Get: DataMember(self: BindingSource) -> str



Set: DataMember(self: BindingSource)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data source that the connector binds to.



Get: DataSource(self: BindingSource) -> object



Set: DataSource(self: BindingSource)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the expression used to filter which rows are viewed.



Get: Filter(self: BindingSource) -> str



Set: Filter(self: BindingSource)=value

"""

 IsBindingSuspended=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the list binding is suspended.



Get: IsBindingSuspended(self: BindingSource) -> bool



"""

 IsFixedSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the underlying list has a fixed size.



Get: IsFixedSize(self: BindingSource) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the underlying list is read-only.



Get: IsReadOnly(self: BindingSource) -> bool



"""

 IsSorted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the items in the underlying list are sorted.



Get: IsSorted(self: BindingSource) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether access to the collection is synchronized (thread safe).



Get: IsSynchronized(self: BindingSource) -> bool



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list that the connector is bound to.



Get: List(self: BindingSource) -> IList



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the current item in the underlying list.



Get: Position(self: BindingSource) -> int



Set: Position(self: BindingSource)=value

"""

 RaiseListChangedEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether System.Windows.Forms.BindingSource.ListChanged events should be raised.



Get: RaiseListChangedEvents(self: BindingSource) -> bool



Set: RaiseListChangedEvents(self: BindingSource)=value

"""

 Sort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column names used for sorting,and the sort order for viewing the rows in the data source.



Get: Sort(self: BindingSource) -> str



Set: Sort(self: BindingSource)=value

"""

 SortDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of sort descriptions applied to the data source.



Get: SortDescriptions(self: BindingSource) -> ListSortDescriptionCollection



"""

 SortDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction the items in the list are sorted.



Get: SortDirection(self: BindingSource) -> ListSortDirection



"""

 SortProperty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.ComponentModel.PropertyDescriptor that is being used for sorting the list.



Get: SortProperty(self: BindingSource) -> PropertyDescriptor



"""

 SupportsAdvancedSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports multi-column sorting.



Get: SupportsAdvancedSorting(self: BindingSource) -> bool



"""

 SupportsChangeNotification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports change notification.



Get: SupportsChangeNotification(self: BindingSource) -> bool



"""

 SupportsFiltering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports filtering.



Get: SupportsFiltering(self: BindingSource) -> bool



"""

 SupportsSearching=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports searching with the System.Windows.Forms.BindingSource.Find(System.ComponentModel.PropertyDescriptor,System.Object) method.



Get: SupportsSearching(self: BindingSource) -> bool



"""

 SupportsSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports sorting.



Get: SupportsSorting(self: BindingSource) -> bool



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the underlying list.



Get: SyncRoot(self: BindingSource) -> object



"""


 AddingNew=None
 BindingComplete=None
 CurrentChanged=None
 CurrentItemChanged=None
 DataError=None
 DataMemberChanged=None
 DataSourceChanged=None
 ListChanged=None
 PositionChanged=None


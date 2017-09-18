class ControlBindingsCollection(BindingsCollection,ICollection,IEnumerable):
 """
 Represents the collection of data bindings for a control.

 

 ControlBindingsCollection(control: IBindableComponent)
 """
 def Add(self,*__args):
  """
  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,updateMode: DataSourceUpdateMode,nullValue: object) -> Binding

  

   Creates a binding that binds the specified control property to the specified data member of the 

    specified data source,optionally enabling formatting,propagating values to the data source 

    based on the specified update setting,setting the property to the specified value when 

    System.DBNull is returned from the data source,and adding the binding to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object representing the data source.

   dataMember: The property or list to bind to.

   formattingEnabled: true to format the displayed data; otherwise,false.

   updateMode: One of the System.Windows.Forms.DataSourceUpdateMode values.

   nullValue: The System.Object to be applied to the bound control property if the data source value is 

    System.DBNull.

  

   Returns: The newly created System.Windows.Forms.Binding

  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,updateMode: DataSourceUpdateMode,nullValue: object,formatString: str) -> Binding

  

   Creates a binding that binds the specified control property to the specified data member of the 

    specified data source,optionally enabling formatting with the specified format string,

    propagating values to the data source based on the specified update setting,setting the 

    property to the specified value when System.DBNull is returned from the data source,and adding 

    the binding to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object representing the data source.

   dataMember: The property or list to bind to.

   formattingEnabled: true to format the displayed data; otherwise,false.

   updateMode: One of the System.Windows.Forms.DataSourceUpdateMode values.

   nullValue: The System.Object to be applied to the bound control property if the data source value is 

    System.DBNull.

  

   formatString: One or more format specifier characters that indicate how a value is to be displayed.

   Returns: The newly created System.Windows.Forms.Binding

  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,updateMode: DataSourceUpdateMode,nullValue: object,formatString: str,formatInfo: IFormatProvider) -> Binding

  

   Creates a binding that binds the specified control property to the specified data member of the 

    specified data source,optionally enabling formatting with the specified format string,

    propagating values to the data source based on the specified update setting,setting the 

    property to the specified value when System.DBNull is returned from the data source,setting the 

    specified format provider,and adding the binding to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object representing the data source.

   dataMember: The property or list to bind to.

   formattingEnabled: true to format the displayed data; otherwise,false.

   updateMode: One of the System.Windows.Forms.DataSourceUpdateMode values.

   nullValue: The System.Object to be applied to the bound control property if the data source value is 

    System.DBNull.

  

   formatString: One or more format specifier characters that indicate how a value is to be displayed

   formatInfo: An implementation of System.IFormatProvider to override default formatting behavior.

   Returns: The newly created System.Windows.Forms.Binding.

  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,updateMode: DataSourceUpdateMode) -> Binding

  

   Creates a binding that binds the specified control property to the specified data member of the 

    specified data source,optionally enabling formatting,propagating values to the data source 

    based on the specified update setting,and adding the binding to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object representing the data source.

   dataMember: The property or list to bind to.

   formattingEnabled: true to format the displayed data; otherwise,false.

   updateMode: One of the System.Windows.Forms.DataSourceUpdateMode values.

   Returns: The newly created System.Windows.Forms.Binding.

  Add(self: ControlBindingsCollection,binding: Binding)

   Adds the specified System.Windows.Forms.Binding to the collection.

  

   binding: The System.Windows.Forms.Binding to add.

  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str) -> Binding

  

   Creates a System.Windows.Forms.Binding using the specified control property name,data source,

    and data member,and adds it to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object that represents the data source.

   dataMember: The property or list to bind to.

   Returns: The newly created System.Windows.Forms.Binding.

  Add(self: ControlBindingsCollection,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool) -> Binding

  

   Creates a binding with the specified control property name,data source,data member,and 

    information about whether formatting is enabled,and adds the binding to the collection.

  

  

   propertyName: The name of the control property to bind.

   dataSource: An System.Object representing the data source.

   dataMember: The property or list to bind to.

   formattingEnabled: true to format the displayed data; otherwise,false

   Returns: The newly created System.Windows.Forms.Binding.
  """
  pass
 def AddCore(self,*args):
  """
  AddCore(self: ControlBindingsCollection,dataBinding: Binding)

   Adds a binding to the collection.

  

   dataBinding: The System.Windows.Forms.Binding to add.
  """
  pass
 def Clear(self):
  """
  Clear(self: ControlBindingsCollection)

   Clears the collection of any bindings.
  """
  pass
 def ClearCore(self,*args):
  """
  ClearCore(self: ControlBindingsCollection)

   Clears the bindings in the collection.
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
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: BindingsCollection,ccevent: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.BindingsCollection.CollectionChanged event.

  

   ccevent: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def OnCollectionChanging(self,*args):
  """
  OnCollectionChanging(self: BindingsCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.BindingsCollection.CollectionChanging event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains event data.
  """
  pass
 def Remove(self,binding):
  """
  Remove(self: ControlBindingsCollection,binding: Binding)

   Deletes the specified System.Windows.Forms.Binding from the collection.

  

   binding: The System.Windows.Forms.Binding to remove.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: ControlBindingsCollection,index: int)

   Deletes the System.Windows.Forms.Binding at the specified index.

  

   index: The zero-based index of the item to remove.
  """
  pass
 def RemoveCore(self,*args):
  """
  RemoveCore(self: ControlBindingsCollection,dataBinding: Binding)

   Removes the specified binding from the collection.

  

   dataBinding: The System.Windows.Forms.Binding to remove from the collection.
  """
  pass
 def ShouldSerializeMyAll(self,*args):
  """
  ShouldSerializeMyAll(self: BindingsCollection) -> bool

  

   Gets a value that indicates whether the collection should be serialized.

   Returns: true if the collection count is greater than zero; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 def __new__(self,control):
  """ __new__(cls: type,control: IBindableComponent) """
  pass
 BindableComponent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.IBindableComponent the binding collection belongs to.



Get: BindableComponent(self: ControlBindingsCollection) -> IBindableComponent



"""

 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control that the collection belongs to.



Get: Control(self: ControlBindingsCollection) -> Control



"""

 DefaultDataSourceUpdateMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default System.Windows.Forms.Binding.DataSourceUpdateMode for a System.Windows.Forms.Binding in the collection.



Get: DefaultDataSourceUpdateMode(self: ControlBindingsCollection) -> DataSourceUpdateMode



Set: DefaultDataSourceUpdateMode(self: ControlBindingsCollection)=value

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bindings in the collection as an object.



"""



class BindingManagerBase(object):
 """
 Manages all System.Windows.Forms.Binding objects that are bound to the same data source and data member. This class is abstract.

 

 BindingManagerBase()
 """
 def AddNew(self):
  """
  AddNew(self: BindingManagerBase)

   When overridden in a derived class,adds a new item to the underlying list.
  """
  pass
 def CancelCurrentEdit(self):
  """
  CancelCurrentEdit(self: BindingManagerBase)

   When overridden in a derived class,cancels the current edit.
  """
  pass
 def EndCurrentEdit(self):
  """
  EndCurrentEdit(self: BindingManagerBase)

   When overridden in a derived class,ends the current edit.
  """
  pass
 def GetItemProperties(self):
  """
  GetItemProperties(self: BindingManagerBase) -> PropertyDescriptorCollection

  

   When overridden in a derived class,gets the collection of property descriptors for the binding.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the property descriptors 

    for the binding.
  """
  pass
 def GetListName(self,*args):
  """
  GetListName(self: BindingManagerBase,listAccessors: ArrayList) -> str

  

   When overridden in a derived class,gets the name of the list supplying the data for the binding.

  

   listAccessors: An System.Collections.ArrayList containing the table's bound properties.

   Returns: The name of the list supplying the data for the binding.
  """
  pass
 def OnBindingComplete(self,*args):
  """
  OnBindingComplete(self: BindingManagerBase,args: BindingCompleteEventArgs)

   Raises the System.Windows.Forms.BindingManagerBase.BindingComplete event.

  

   args: A System.Windows.Forms.BindingCompleteEventArgs  that contains the event data.
  """
  pass
 def OnCurrentChanged(self,*args):
  """
  OnCurrentChanged(self: BindingManagerBase,e: EventArgs)

   Raises the System.Windows.Forms.BindingManagerBase.CurrentChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnCurrentItemChanged(self,*args):
  """
  OnCurrentItemChanged(self: BindingManagerBase,e: EventArgs)

   Raises the System.Windows.Forms.BindingManagerBase.CurrentItemChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnDataError(self,*args):
  """
  OnDataError(self: BindingManagerBase,e: Exception)

   Raises the System.Windows.Forms.BindingManagerBase.DataError event.

  

   e: An System.Exception that caused the System.Windows.Forms.BindingManagerBase.DataError event to 

    occur.
  """
  pass
 def PullData(self,*args):
  """
  PullData(self: BindingManagerBase)

   Pulls data from the data-bound control into the data source,returning no information.
  """
  pass
 def PushData(self,*args):
  """
  PushData(self: BindingManagerBase)

   Pushes data from the data source into the data-bound control,returning no information.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: BindingManagerBase,index: int)

   When overridden in a derived class,deletes the row at the specified index from the underlying 

    list.

  

  

   index: The index of the row to delete.
  """
  pass
 def ResumeBinding(self):
  """
  ResumeBinding(self: BindingManagerBase)

   When overridden in a derived class,resumes data binding.
  """
  pass
 def SuspendBinding(self):
  """
  SuspendBinding(self: BindingManagerBase)

   When overridden in a derived class,suspends data binding.
  """
  pass
 def UpdateIsBinding(self,*args):
  """
  UpdateIsBinding(self: BindingManagerBase)

   When overridden in a derived class,updates the binding.
  """
  pass
 Bindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of bindings being managed.



Get: Bindings(self: BindingManagerBase) -> BindingsCollection



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the number of rows managed by the System.Windows.Forms.BindingManagerBase.



Get: Count(self: BindingManagerBase) -> int



"""

 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the current object.



Get: Current(self: BindingManagerBase) -> object



"""

 IsBindingSuspended=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether binding is suspended.



Get: IsBindingSuspended(self: BindingManagerBase) -> bool



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets or sets the position in the underlying list that controls bound to this data source point to.



Get: Position(self: BindingManagerBase) -> int



Set: Position(self: BindingManagerBase)=value

"""


 BindingComplete=None
 CurrentChanged=None
 CurrentItemChanged=None
 DataError=None
 onCurrentChangedHandler=None
 onPositionChangedHandler=None
 PositionChanged=None


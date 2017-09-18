class CurrencyManager(BindingManagerBase):
 """ Manages a list of System.Windows.Forms.Binding objects. """
 def AddNew(self):
  """
  AddNew(self: CurrencyManager)

   Adds a new item to the underlying list.
  """
  pass
 def CancelCurrentEdit(self):
  """
  CancelCurrentEdit(self: CurrencyManager)

   Cancels the current edit operation.
  """
  pass
 def CheckEmpty(self,*args):
  """
  CheckEmpty(self: CurrencyManager)

   Throws an exception if there is no list,or the list is empty.
  """
  pass
 def EndCurrentEdit(self):
  """
  EndCurrentEdit(self: CurrencyManager)

   Ends the current edit operation.
  """
  pass
 def GetItemProperties(self):
  """
  GetItemProperties(self: CurrencyManager) -> PropertyDescriptorCollection

  

   Gets the property descriptor collection for the underlying list.

   Returns: A System.ComponentModel.PropertyDescriptorCollection for the list.
  """
  pass
 def OnItemChanged(self,*args):
  """
  OnItemChanged(self: CurrencyManager,e: ItemChangedEventArgs)

   Raises the System.Windows.Forms.CurrencyManager.ItemChanged event.

  

   e: An System.Windows.Forms.ItemChangedEventArgs that contains the event data.
  """
  pass
 def OnMetaDataChanged(self,*args):
  """
  OnMetaDataChanged(self: CurrencyManager,e: EventArgs)

   Raises the System.Windows.Forms.CurrencyManager.MetaDataChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPositionChanged(self,*args):
  """
  OnPositionChanged(self: CurrencyManager,e: EventArgs)

   Raises the System.Windows.Forms.BindingManagerBase.PositionChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: CurrencyManager)

   Forces a repopulation of the data-bound list.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: CurrencyManager,index: int)

   Removes the item at the specified index.

  

   index: The index of the item to remove from the list.
  """
  pass
 def ResumeBinding(self):
  """
  ResumeBinding(self: CurrencyManager)

   Resumes data binding.
  """
  pass
 def SuspendBinding(self):
  """
  SuspendBinding(self: CurrencyManager)

   Suspends data binding to prevents changes from updating the bound data source.
  """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items in the list.



Get: Count(self: CurrencyManager) -> int



"""

 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current item in the list.



Get: Current(self: CurrencyManager) -> object



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list for this System.Windows.Forms.CurrencyManager.



Get: List(self: CurrencyManager) -> IList



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position you are at within the list.



Get: Position(self: CurrencyManager) -> int



Set: Position(self: CurrencyManager)=value

"""


 finalType=None
 ItemChanged=None
 ListChanged=None
 listposition=None
 MetaDataChanged=None
 onCurrentChangedHandler=None
 onPositionChangedHandler=None


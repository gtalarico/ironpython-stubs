class PropertyManager(BindingManagerBase):
 """
 Maintains a System.Windows.Forms.Binding between an object's property and a data-bound control property.

 

 PropertyManager()
 """
 def AddNew(self):
  """ AddNew(self: PropertyManager) """
  pass
 def CancelCurrentEdit(self):
  """ CancelCurrentEdit(self: PropertyManager) """
  pass
 def EndCurrentEdit(self):
  """ EndCurrentEdit(self: PropertyManager) """
  pass
 def GetItemProperties(self):
  """
  GetItemProperties(self: BindingManagerBase,listType: Type,offset: int,dataSources: ArrayList,listAccessors: ArrayList) -> PropertyDescriptorCollection

  

   Gets the list of properties of the items managed by this System.Windows.Forms.BindingManagerBase.

  

   listType: The System.Type of the bound list.

   offset: A counter used to recursively call the method.

   dataSources: An System.Collections.ArrayList containing the data sources.

   listAccessors: An System.Collections.ArrayList containing the table's bound properties.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the property descriptors 

    for the binding.

  

  GetItemProperties(self: BindingManagerBase,dataSources: ArrayList,listAccessors: ArrayList) -> PropertyDescriptorCollection

  

   Gets the collection of property descriptors for the binding using the specified 

    System.Collections.ArrayList.

  

  

   dataSources: An System.Collections.ArrayList containing the data sources.

   listAccessors: An System.Collections.ArrayList containing the table's bound properties.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the property descriptors 

    for the binding.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: PropertyManager,index: int)

   index: The index of the row to delete.
  """
  pass
 def ResumeBinding(self):
  """ ResumeBinding(self: PropertyManager) """
  pass
 def SuspendBinding(self):
  """
  SuspendBinding(self: PropertyManager)

   Suspends the data binding between a data source and a data-bound property.
  """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: PropertyManager) -> int



"""

 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object to which the data-bound property belongs.



Get: Current(self: PropertyManager) -> object



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Position(self: PropertyManager) -> int



Set: Position(self: PropertyManager)=value

"""


 onCurrentChangedHandler=None
 onPositionChangedHandler=None


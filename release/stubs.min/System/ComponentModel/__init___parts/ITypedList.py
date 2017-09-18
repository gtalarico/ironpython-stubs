class ITypedList:
 """ Provides functionality to discover the schema for a bindable list,where the properties available for binding differ from the public properties of the object to bind to. """
 def GetItemProperties(self,listAccessors):
  """
  GetItemProperties(self: ITypedList,listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection

  

   Returns the System.ComponentModel.PropertyDescriptorCollection that represents the properties on 

    each item used to bind data.

  

  

   listAccessors: An array of System.ComponentModel.PropertyDescriptor objects to find in the collection as 

    bindable. This can be null.

  

   Returns: The System.ComponentModel.PropertyDescriptorCollection that represents the properties on each 

    item used to bind data.
  """
  pass
 def GetListName(self,listAccessors):
  """
  GetListName(self: ITypedList,listAccessors: Array[PropertyDescriptor]) -> str

  

   Returns the name of the list.

  

   listAccessors: An array of System.ComponentModel.PropertyDescriptor objects,for which the list name is 

    returned. This can be null.

  

   Returns: The name of the list.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

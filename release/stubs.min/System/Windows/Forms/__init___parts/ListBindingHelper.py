class ListBindingHelper(object):
 """ Provides functionality to discover a bindable list and the properties of the items contained in the list when they differ from the public properties of the object to which they bind. """
 @staticmethod
 def GetList(*__args):
  """
  GetList(dataSource: object,dataMember: str) -> object

  

   Returns an object,typically a list,from the evaluation of a specified data source and optional 

    data member.

  

  

   dataSource: The data source from which to find the list.

   dataMember: The name of the data source property that contains the list. This can be null.

   Returns: An System.Object representing the underlying list if it was found; otherwise,dataSource.

  GetList(list: object) -> object

  

   Returns a list associated with the specified data source.

  

   list: The data source to examine for its underlying list.

   Returns: An System.Object representing the underlying list if it exists; otherwise,the original data 

    source specified by list.
  """
  pass
 @staticmethod
 def GetListItemProperties(*__args):
  """
  GetListItemProperties(dataSource: object,dataMember: str,listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection

  

   Returns the System.ComponentModel.PropertyDescriptorCollection that describes the properties of 

    an item type contained in the specified data member of a data source. Uses the specified 

    System.ComponentModel.PropertyDescriptor array to indicate which properties to examine.

  

  

   dataSource: The data source to be examined for property information.

   dataMember: The optional data member to be examined for property information. This can be null.

   listAccessors: The System.ComponentModel.PropertyDescriptor array describing which properties of the data 

    member to examine. This can be null.

  

   Returns: The System.ComponentModel.PropertyDescriptorCollection describing the properties of an item type 

    contained in a collection property of the specified data source.

  

  GetListItemProperties(list: object,listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection

  

   Returns the System.ComponentModel.PropertyDescriptorCollection that describes the properties of 

    an item type contained in a collection property of a data source. Uses the specified 

    System.ComponentModel.PropertyDescriptor array to indicate which properties to examine.

  

  

   list: The data source to be examined for property information.

   listAccessors: The System.ComponentModel.PropertyDescriptor array describing which properties of the data 

    source to examine. This can be null.

  

   Returns: The System.ComponentModel.PropertyDescriptorCollection describing the properties of the item 

    type contained in a collection property of the data source.

  

  GetListItemProperties(list: object) -> PropertyDescriptorCollection

  

   Returns the System.ComponentModel.PropertyDescriptorCollection that describes the properties of 

    an item type contained in a specified data source,or properties of the specified data source.

  

  

   list: The data source to examine for property information.

   Returns: The System.ComponentModel.PropertyDescriptorCollection containing the properties of the items 

    contained in list,or properties of list.
  """
  pass
 @staticmethod
 def GetListItemType(*__args):
  """
  GetListItemType(dataSource: object,dataMember: str) -> Type

  

   Returns the data type of the items in the specified data source.

  

   dataSource: The data source to examine for items.

   dataMember: The optional name of the property on the data source that is to be used as the data member. This 

    can be null.

  

   Returns: For complex data binding,the System.Type of the items represented by the dataMember in the data 

    source; otherwise,the System.Type of the item in the list itself.

  

  GetListItemType(list: object) -> Type

  

   Returns the data type of the items in the specified list.

  

   list: The list to be examined for type information.

   Returns: The System.Type of the items contained in the list.
  """
  pass
 @staticmethod
 def GetListName(list,listAccessors):
  """
  GetListName(list: object,listAccessors: Array[PropertyDescriptor]) -> str

  

   Returns the name of an underlying list,given a data source and optional 

    System.ComponentModel.PropertyDescriptor array.

  

  

   list: The data source to examine for the list name.

   listAccessors: An array of System.ComponentModel.PropertyDescriptor objects to find in the data source. This 

    can be null.

  

   Returns: The name of the list in the data source,as described by listAccessors,orthe name of the data 

    source type.
  """
  pass
 __all__=[
  'GetList',
  'GetListItemProperties',
  'GetListItemType',
  'GetListName',
 ]


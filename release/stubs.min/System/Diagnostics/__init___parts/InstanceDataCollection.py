class InstanceDataCollection(DictionaryBase,IDictionary,ICollection,IEnumerable):
 """
 Provides a strongly typed collection of System.Diagnostics.InstanceData objects.

 

 InstanceDataCollection(counterName: str)
 """
 def Contains(self,instanceName):
  """
  Contains(self: InstanceDataCollection,instanceName: str) -> bool

  

   Determines whether a performance instance with a specified name (identified by one of the 

    indexed System.Diagnostics.InstanceData objects) exists in the collection.

  

  

   instanceName: The name of the instance to find in this collection.

   Returns: true if the instance exists in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,*__args):
  """
  CopyTo(self: InstanceDataCollection,instances: Array[InstanceData],index: int)

   Copies the items in the collection to the specified one-dimensional array at the specified index.

  

   instances: The one-dimensional System.Array that is the destination of the values copied from the 

    collection.

  

   index: The zero-based index value at which to add the new instances.
  """
  pass
 def OnClear(self,*args):
  """
  OnClear(self: DictionaryBase)

   Performs additional custom processes before clearing the contents of the 

    System.Collections.DictionaryBase instance.
  """
  pass
 def OnClearComplete(self,*args):
  """
  OnClearComplete(self: DictionaryBase)

   Performs additional custom processes after clearing the contents of the 

    System.Collections.DictionaryBase instance.
  """
  pass
 def OnGet(self,*args):
  """
  OnGet(self: DictionaryBase,key: object,currentValue: object) -> object

  

   Gets the element with the specified key and value in the System.Collections.DictionaryBase 

    instance.

  

  

   key: The key of the element to get.

   currentValue: The current value of the element associated with key.

   Returns: An System.Object containing the element with the specified key and value.
  """
  pass
 def OnInsert(self,*args):
  """
  OnInsert(self: DictionaryBase,key: object,value: object)

   Performs additional custom processes before inserting a new element into the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to insert.

   value: The value of the element to insert.
  """
  pass
 def OnInsertComplete(self,*args):
  """
  OnInsertComplete(self: DictionaryBase,key: object,value: object)

   Performs additional custom processes after inserting a new element into the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to insert.

   value: The value of the element to insert.
  """
  pass
 def OnRemove(self,*args):
  """
  OnRemove(self: DictionaryBase,key: object,value: object)

   Performs additional custom processes before removing an element from the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to remove.

   value: The value of the element to remove.
  """
  pass
 def OnRemoveComplete(self,*args):
  """
  OnRemoveComplete(self: DictionaryBase,key: object,value: object)

   Performs additional custom processes after removing an element from the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to remove.

   value: The value of the element to remove.
  """
  pass
 def OnSet(self,*args):
  """
  OnSet(self: DictionaryBase,key: object,oldValue: object,newValue: object)

   Performs additional custom processes before setting a value in the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to locate.

   oldValue: The old value of the element associated with key.

   newValue: The new value of the element associated with key.
  """
  pass
 def OnSetComplete(self,*args):
  """
  OnSetComplete(self: DictionaryBase,key: object,oldValue: object,newValue: object)

   Performs additional custom processes after setting a value in the 

    System.Collections.DictionaryBase instance.

  

  

   key: The key of the element to locate.

   oldValue: The old value of the element associated with key.

   newValue: The new value of the element associated with key.
  """
  pass
 def OnValidate(self,*args):
  """
  OnValidate(self: DictionaryBase,key: object,value: object)

   Performs additional custom processes when validating the element with the specified key and 

    value.

  

  

   key: The key of the element to validate.

   value: The value of the element to validate.
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
 @staticmethod
 def __new__(self,counterName):
  """ __new__(cls: type,counterName: str) """
  pass
 CounterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the performance counter whose instance data you want to get.



Get: CounterName(self: InstanceDataCollection) -> str



"""

 Dictionary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.DictionaryBase instance.



"""

 InnerHashtable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.DictionaryBase instance.



"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object and counter registry keys for the objects associated with this instance data.



Get: Keys(self: InstanceDataCollection) -> ICollection



"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw counter values that comprise the instance data for the counter.



Get: Values(self: InstanceDataCollection) -> ICollection



"""



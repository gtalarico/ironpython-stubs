class InstanceDataCollectionCollection(DictionaryBase,IDictionary,ICollection,IEnumerable):
 """
 Provides a strongly typed collection of System.Diagnostics.InstanceDataCollection objects.

 

 InstanceDataCollectionCollection()
 """
 def Contains(self,counterName):
  """
  Contains(self: InstanceDataCollectionCollection,counterName: str) -> bool

  

   Determines whether an instance data collection for the specified counter (identified by one of 

    the indexed System.Diagnostics.InstanceDataCollection objects) exists in the collection.

  

  

   counterName: The name of the performance counter.

   Returns: true if an instance data collection containing the specified counter exists in the collection; 

    otherwise,false.
  """
  pass
 def CopyTo(self,*__args):
  """
  CopyTo(self: InstanceDataCollectionCollection,counters: Array[InstanceDataCollection],index: int)

   Copies an array of System.Diagnostics.InstanceDataCollection instances to the collection,at the 

    specified index.

  

  

   counters: An array of System.Diagnostics.InstanceDataCollection instances (identified by the counters they 

    contain) to add to the collection.

  

   index: The location at which to add the new instances.
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
 Dictionary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.DictionaryBase instance.



"""

 InnerHashtable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.DictionaryBase instance.



"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object and counter registry keys for the objects associated with this instance data collection.



Get: Keys(self: InstanceDataCollectionCollection) -> ICollection



"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the instance data values that comprise the collection of instances for the counter.



Get: Values(self: InstanceDataCollectionCollection) -> ICollection



"""



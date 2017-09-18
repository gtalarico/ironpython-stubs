class TextElementCollection(object,IList,ICollection,IEnumerable,ICollection[TextElementType],IEnumerable[TextElementType]):
 # no doc
 def Add(self,item):
  """
  Add(self: TextElementCollection[TextElementType],item: TextElementType)
   Appends a specified item to the collection.
  
   item: An item to append to the collection.
  """
  pass
 def AddRange(self,range):
  """
  AddRange(self: TextElementCollection[TextElementType],range: IEnumerable)
   Appends a specified range of items to the collection.
  
   range: An object that implements the System.Collections.IEnumerable interface,and 
    that specifies a range of items to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: TextElementCollection[TextElementType])
   Clears all items from the collection.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: TextElementCollection[TextElementType],item: TextElementType) -> bool
  
   Queries for the presence of a specified item in the collection.
  
   item: An item to query for the presence of in the collection.
   Returns: true if the specified item is present in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,arrayIndex):
  """ CopyTo(self: TextElementCollection[TextElementType],array: Array[TextElementType],arrayIndex: int) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TextElementCollection[TextElementType]) -> IEnumerator[TextElementType]
  
   Returns an enumerator for the contents of the collection.
   Returns: An enumerator for the contents of the collection.
  """
  pass
 def InsertAfter(self,previousSibling,newItem):
  """
  InsertAfter(self: TextElementCollection[TextElementType],previousSibling: TextElementType,newItem: TextElementType)
   Inserts a specified item in the collection after a specified collection item.
  
   previousSibling: An item in the collection after which the new item will be inserted.
   newItem: An item to insert into the collection.
  """
  pass
 def InsertBefore(self,nextSibling,newItem):
  """
  InsertBefore(self: TextElementCollection[TextElementType],nextSibling: TextElementType,newItem: TextElementType)
   Inserts a specified item in the collection before a specified collection item.
  
   nextSibling: An item in the collection before which the new item will be inserted.
   newItem: An item to insert into the collection.
  """
  pass
 def Remove(self,item):
  """
  Remove(self: TextElementCollection[TextElementType],item: TextElementType) -> bool
  
   Removes a specified item from the collection.
  
   item: An item to be removed fro the collection.
   Returns: true if the specified item was found and removed; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[TextElementType],item: TextElementType) -> bool
  
   Determines whether the System.Collections.Generic.ICollection contains a 
    specific value.
  
  
   item: The object to locate in the System.Collections.Generic.ICollection.
   Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise,
    false.
  
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,
    false.
  """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items currently in the collection.

Get: Count(self: TextElementCollection[TextElementType]) -> int

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether or not the collection is read-only.

Get: IsReadOnly(self: TextElementCollection[TextElementType]) -> bool

"""



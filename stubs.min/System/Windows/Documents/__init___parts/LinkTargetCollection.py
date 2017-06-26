class LinkTargetCollection(CollectionBase,IList,ICollection,IEnumerable):
 """
 Provides a collection of all of the System.Windows.Documents.LinkTarget elements in a System.IO.Packaging.Package.
 
 LinkTargetCollection()
 """
 def Add(self,value):
  """
  Add(self: LinkTargetCollection,value: LinkTarget) -> int
  
   Adds a specified System.Windows.Documents.LinkTarget to the collection.
  
   value: The link target that is added.
   Returns: The zero-based index in the collection of the value added.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: LinkTargetCollection,value: LinkTarget) -> bool
  
   Specifies a value that indicates whether a particular 
    System.Windows.Documents.LinkTarget is in the collection.
  
  
   value: The link to test for.
   Returns: true if value is present; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: LinkTargetCollection,array: Array[LinkTarget],index: int)
   Copies the items in the collection to the specified array beginning at the 
    specified index.
  
  
   array: The target array.
   index: The zero-based index of the array position where the first item is copied.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: LinkTargetCollection,value: LinkTarget) -> int
  
   Gets the index of the specified item.
  
   value: The object to locate in the collection.
   Returns: The index of value if found in the collection; otherwise,-1.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: LinkTargetCollection,index: int,value: LinkTarget)
   Inserts the specified item into the collection at the specified index.
  
   index: The point where the link target is inserted.
   value: The target to insert.
  """
  pass
 def OnClear(self,*args):
  """
  OnClear(self: CollectionBase)
   Performs additional custom processes when clearing the contents of the 
    System.Collections.CollectionBase instance.
  """
  pass
 def OnClearComplete(self,*args):
  """
  OnClearComplete(self: CollectionBase)
   Performs additional custom processes after clearing the contents of the 
    System.Collections.CollectionBase instance.
  """
  pass
 def OnInsert(self,*args):
  """
  OnInsert(self: CollectionBase,index: int,value: object)
   Performs additional custom processes before inserting a new element into the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which to insert value.
   value: The new value of the element at index.
  """
  pass
 def OnInsertComplete(self,*args):
  """
  OnInsertComplete(self: CollectionBase,index: int,value: object)
   Performs additional custom processes after inserting a new element into the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which to insert value.
   value: The new value of the element at index.
  """
  pass
 def OnRemove(self,*args):
  """
  OnRemove(self: CollectionBase,index: int,value: object)
   Performs additional custom processes when removing an element from the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which value can be found.
   value: The value of the element to remove from index.
  """
  pass
 def OnRemoveComplete(self,*args):
  """
  OnRemoveComplete(self: CollectionBase,index: int,value: object)
   Performs additional custom processes after removing an element from the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which value can be found.
   value: The value of the element to remove from index.
  """
  pass
 def OnSet(self,*args):
  """
  OnSet(self: CollectionBase,index: int,oldValue: object,newValue: object)
   Performs additional custom processes before setting a value in the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which oldValue can be found.
   oldValue: The value to replace with newValue.
   newValue: The new value of the element at index.
  """
  pass
 def OnSetComplete(self,*args):
  """
  OnSetComplete(self: CollectionBase,index: int,oldValue: object,newValue: object)
   Performs additional custom processes after setting a value in the 
    System.Collections.CollectionBase instance.
  
  
   index: The zero-based index at which oldValue can be found.
   oldValue: The value to replace with newValue.
   newValue: The new value of the element at index.
  """
  pass
 def OnValidate(self,*args):
  """
  OnValidate(self: CollectionBase,value: object)
   Performs additional custom processes when validating a value.
  
   value: The object to validate.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: LinkTargetCollection,value: LinkTarget)
   Removes the first occurrence of a specific object from the 
    System.Collections.Generic.ICollection.
  
  
   value: The link target to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



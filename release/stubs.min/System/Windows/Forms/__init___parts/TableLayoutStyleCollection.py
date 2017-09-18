class TableLayoutStyleCollection(object,IList,ICollection,IEnumerable):
 """ Implements the basic functionality for a collection of table layout styles. """
 def Add(self,style):
  """
  Add(self: TableLayoutStyleCollection,style: TableLayoutStyle) -> int

  

   Adds a new System.Windows.Forms.TableLayoutStyle to the end of the current collection.

  

   style: The System.Windows.Forms.TableLayoutStyle to add to the 

    System.Windows.Forms.TableLayoutStyleCollection.

  

   Returns: The position into which the new element was inserted.
  """
  pass
 def Clear(self):
  """
  Clear(self: TableLayoutStyleCollection)

   Disassociates the collection from its associated System.Windows.Forms.TableLayoutPanel and 

    empties the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: TableLayoutStyleCollection,index: int)

   Removes the style at the specified index of the collection.

  

   index: The zero-based index of the System.Windows.Forms.TableLayoutStyle to be removed.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of styles actually contained in the System.Windows.Forms.TableLayoutStyleCollection.



Get: Count(self: TableLayoutStyleCollection) -> int



"""



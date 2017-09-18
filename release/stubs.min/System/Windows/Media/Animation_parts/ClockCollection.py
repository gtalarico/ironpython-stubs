class ClockCollection(object,ICollection[Clock],IEnumerable[Clock],IEnumerable):
 """ Represents an ordered collection of System.Windows.Media.Animation.Clock objects. """
 def Add(self,item):
  """
  Add(self: ClockCollection,item: Clock)

   Adds a new System.Windows.Media.Animation.Clock object to the end of this 

    System.Windows.Media.Animation.ClockCollection.

  

  

   item: The object to add.
  """
  pass
 def Clear(self):
  """
  Clear(self: ClockCollection)

   Removes all items from this System.Windows.Media.Animation.ClockCollection.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: ClockCollection,item: Clock) -> bool

  

   Indicates whether the System.Windows.Media.Animation.ClockCollection contains the specified 

    System.Windows.Media.Animation.Clock object.

  

  

   item: The object to locate.

   Returns: true if item is found; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ClockCollection,array: Array[Clock],index: int)

   Copies the System.Windows.Media.Animation.Clock objects of this 

    System.Windows.Media.Animation.ClockCollection to an array of Clocks,starting at the specified 

    index position.

  

  

   array: The destination array.

   index: The zero-based index position where copying begins.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(objA: ClockCollection,objB: ClockCollection) -> bool

  

   Indicates whether the two specified System.Windows.Media.Animation.ClockCollection collections 

    are equal.

  

  

   objA: The first value to compare.

   objB: The second value to compare.

   Returns: true if objA and objB are equal; otherwise,false.

  Equals(self: ClockCollection,obj: object) -> bool

  

   Indicates whether this instance is equal to the specified object.

  

   obj: The object to compare with this instance.

   Returns: true if obj is equal to this instance; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ClockCollection) -> int

  

   Returns a 32-bit signed integer hash code representing this instance.

   Returns: A 32-bit signed integer.
  """
  pass
 def Remove(self,item):
  """
  Remove(self: ClockCollection,item: Clock) -> bool

  

   Removes the specified System.Windows.Media.Animation.Clock from the 

    System.Windows.Media.Animation.ClockCollection.

  

  

   item: The object to remove.

   Returns: true if item was successfully removed; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__(self: ICollection[Clock],item: Clock) -> bool """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
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
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items contained in this System.Windows.Media.Animation.ClockCollection.



Get: Count(self: ClockCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Media.Animation.ClockCollection is read-only.



Get: IsReadOnly(self: ClockCollection) -> bool



"""



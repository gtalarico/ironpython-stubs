class GroundConductorSizeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains GroundConductorSizes.

 

 GroundConductorSizeSet()
 """
 def Clear(self):
  """
  Clear(self: GroundConductorSizeSet)

   Removes every GroundConductorSize from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: GroundConductorSizeSet,item: GroundConductorSize) -> bool

  

   Tests for the existence of a GroundConductorSize within the set.

  

   item: The GroundConductorSize to be searched for.

   Returns: The Contains method returns True if the GroundConductorSize is within the set,

    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: GroundConductorSizeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: GroundConductorSizeSet,item: GroundConductorSize) -> int

  

   Removes a specified GroundConductorSize from the set.

  

   item: The GroundConductorSize to be erased.

   Returns: The number of GroundConductorSizes that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: GroundConductorSizeSet) -> GroundConductorSizeSetIterator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GroundConductorSizeSet) -> IEnumerator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: GroundConductorSizeSet,item: GroundConductorSize) -> bool

  

   Insert the specified GroundConductorSize into the set.

  

   item: The GroundConductorSize to be inserted into the set.

   Returns: Returns whether the GroundConductorSize was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GroundConductorSizeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: GroundConductorSizeSet) -> GroundConductorSizeSetIterator

  

   Retrieve a backward moving iterator to the set.

   Returns: Returns a backward moving iterator to the set.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Test to see if the set is empty.



Get: IsEmpty(self: GroundConductorSizeSet) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of GroundConductorSizes that are in the set.



Get: Size(self: GroundConductorSizeSet) -> int



"""



class ParameterSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains parameters.

 

 ParameterSet()
 """
 def Clear(self):
  """
  Clear(self: ParameterSet)

   Removes every parameter from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: ParameterSet,item: Parameter) -> bool

  

   Tests for the existence of a parameter within the set.

  

   item: The parameter to be searched for.

   Returns: The Contains method returns True if the parameter is within the set,otherwise 

    False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ParameterSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: ParameterSet,item: Parameter) -> int

  

   Removes a specified parameter from the set.

  

   item: The parameter to be erased.

   Returns: The number of parameters that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: ParameterSet) -> ParameterSetIterator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ParameterSet) -> IEnumerator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: ParameterSet,item: Parameter) -> bool

  

   Insert the specified parameter into the set.

  

   item: The parameter to be inserted into the set.

   Returns: Returns whether the parameter was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ParameterSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: ParameterSet) -> ParameterSetIterator

  

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



Get: IsEmpty(self: ParameterSet) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of parameters that are in the set.



Get: Size(self: ParameterSet) -> int



"""



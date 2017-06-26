class CharacterMetricsDictionary(object,IDictionary[int,CharacterMetrics],ICollection[KeyValuePair[int,CharacterMetrics]],IEnumerable[KeyValuePair[int,CharacterMetrics]],IEnumerable,IDictionary,ICollection):
 """ Represents a dictionary of System.Windows.Media.CharacterMetrics objects for a device font that is indexed by Unicode scalar values. """
 def Add(self,*__args):
  """
  Add(self: CharacterMetricsDictionary,key: int,value: CharacterMetrics)
   Adds a character code and associated System.Windows.Media.CharacterMetrics 
    value to the collection.
  
  
   key: A value of type System.Int32 representing the character code.
   value: A value of type System.Windows.Media.CharacterMetrics.
  Add(self: CharacterMetricsDictionary,item: KeyValuePair[int,CharacterMetrics])
  """
  pass
 def Clear(self):
  """
  Clear(self: CharacterMetricsDictionary)
   Removes all elements from the collection.
  """
  pass
 def Contains(self,item):
  """ Contains(self: CharacterMetricsDictionary,item: KeyValuePair[int,CharacterMetrics]) -> bool """
  pass
 def ContainsKey(self,key):
  """
  ContainsKey(self: CharacterMetricsDictionary,key: int) -> bool
  
   Determines whether the collection contains the specified character code.
  
   key: A value of type System.Int32 representing the character code.
   Returns: true if the dictionary contains key; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """ CopyTo(self: CharacterMetricsDictionary,array: Array[KeyValuePair[int,CharacterMetrics]],index: int) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CharacterMetricsDictionary) -> IEnumerator[KeyValuePair[int,CharacterMetrics]]
  
   Returns an enumerator that iterates through the collection.
   Returns: An enumerator that iterates through the collection.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: CharacterMetricsDictionary,key: int) -> bool
  
   Removes the element from System.Windows.Media.CharacterMetricsDictionary based 
    on the specified character code.
  
  
   key: A value of type System.Int32 representing the character code.
   Returns: true if the System.Windows.Media.CharacterMetrics item was successfully 
    deleted; otherwise false.
  
  Remove(self: CharacterMetricsDictionary,item: KeyValuePair[int,CharacterMetrics]) -> bool
  """
  pass
 def TryGetValue(self,key,value):
  """
  TryGetValue(self: CharacterMetricsDictionary,key: int) -> (bool,CharacterMetrics)
  
   Retrieves the System.Windows.Media.CharacterMetrics value in the dictionary for 
    a specified character code value.
  
  
   key: A value of type System.Int32.
   Returns: true if the dictionary contains an entry for key; otherwise false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IDictionary[int,CharacterMetrics],key: int) -> bool
  __contains__(self: IDictionary,key: object) -> bool
  
   Determines whether the System.Collections.IDictionary object contains an 
    element with the specified key.
  
  
   key: The key to locate in the System.Collections.IDictionary object.
   Returns: true if the System.Collections.IDictionary contains an element with the key; 
    otherwise,false.
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
 """Gets the number of elements in the collection.

Get: Count(self: CharacterMetricsDictionary) -> int

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Media.CharacterMetricsDictionary is read-only.

Get: IsReadOnly(self: CharacterMetricsDictionary) -> bool

"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of character codes from System.Windows.Media.CharacterMetricsDictionary.

Get: Keys(self: CharacterMetricsDictionary) -> ICollection[int]

"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.Media.CharacterMetrics values in the System.Windows.Media.CharacterMetricsDictionary.

Get: Values(self: CharacterMetricsDictionary) -> ICollection[CharacterMetrics]

"""



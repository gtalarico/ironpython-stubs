class HttpListenerPrefixCollection(object,ICollection[str],IEnumerable[str],IEnumerable):
 """ Represents the collection used to store Uniform Resource Identifier (URI) prefixes for System.Net.HttpListener objects. """
 def Add(self,uriPrefix):
  """
  Add(self: HttpListenerPrefixCollection,uriPrefix: str)

   Adds a Uniform Resource Identifier (URI) prefix to the collection.

  

   uriPrefix: A System.String that identifies the URI information that is compared in incoming requests. The 

    prefix must be terminated with a forward slash ("/").
  """
  pass
 def Clear(self):
  """
  Clear(self: HttpListenerPrefixCollection)

   Removes all the Uniform Resource Identifier (URI) prefixes from the collection.
  """
  pass
 def Contains(self,uriPrefix):
  """
  Contains(self: HttpListenerPrefixCollection,uriPrefix: str) -> bool

  

   Returns a System.Boolean value that indicates whether the specified prefix is contained in the 

    collection.

  

  

   uriPrefix: A System.String that contains the Uniform Resource Identifier (URI) prefix to test.

   Returns: true if this collection contains the prefix specified by uriPrefix; otherwise,false.
  """
  pass
 def CopyTo(self,array,offset):
  """
  CopyTo(self: HttpListenerPrefixCollection,array: Array[str],offset: int)

   Copies the contents of an System.Net.HttpListenerPrefixCollection to the specified string array.

  

   array: The one dimensional string array that receives the Uniform Resource Identifier (URI) prefix 

    strings in this collection.

  

   offset: The zero-based index in array at which copying begins.

  CopyTo(self: HttpListenerPrefixCollection,array: Array,offset: int)

   Copies the contents of an System.Net.HttpListenerPrefixCollection to the specified array.

  

   array: The one dimensional System.Array that receives the Uniform Resource Identifier (URI) prefix 

    strings in this collection.

  

   offset: The zero-based index in array at which copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: HttpListenerPrefixCollection) -> IEnumerator[str]

  

   Returns an object that can be used to iterate through the collection.

   Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 

    the strings in this collection.
  """
  pass
 def Remove(self,uriPrefix):
  """
  Remove(self: HttpListenerPrefixCollection,uriPrefix: str) -> bool

  

   Removes the specified Uniform Resource Identifier (URI) from the list of prefixes handled by the 

    System.Net.HttpListener object.

  

  

   uriPrefix: A System.String that contains the URI prefix to remove.

   Returns: true if the uriPrefix was found in the System.Net.HttpListenerPrefixCollection and removed; 

    otherwise false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__(self: ICollection[str],item: str) -> bool """
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
 """Gets the number of prefixes contained in the collection.



Get: Count(self: HttpListenerPrefixCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to the collection is read-only.



Get: IsReadOnly(self: HttpListenerPrefixCollection) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to the collection is synchronized (thread-safe).



Get: IsSynchronized(self: HttpListenerPrefixCollection) -> bool



"""



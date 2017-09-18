class WebHeaderCollection(NameValueCollection,ICollection,IEnumerable,ISerializable,IDeserializationCallback):
 """
 Contains protocol headers associated with a request or response.

 

 WebHeaderCollection()
 """
 def Add(self,*__args):
  """
  Add(self: WebHeaderCollection,header: HttpResponseHeader,value: str)

   Inserts the specified header with the specified value into the collection.

  

   header: The header to add to the collection.

   value: The content of the header.

  Add(self: WebHeaderCollection,header: str)

   Inserts the specified header into the collection.

  

   header: The header to add,with the name and value separated by a colon.

  Add(self: WebHeaderCollection,name: str,value: str)

   Inserts a header with the specified name and value into the collection.

  

   name: The header to add to the collection.

   value: The content of the header.

  Add(self: WebHeaderCollection,header: HttpRequestHeader,value: str)

   Inserts the specified header with the specified value into the collection.

  

   header: The header to add to the collection.

   value: The content of the header.
  """
  pass
 def AddWithoutValidate(self,*args):
  """
  AddWithoutValidate(self: WebHeaderCollection,headerName: str,headerValue: str)

   Inserts a header into the collection without checking whether the header is on the restricted 

    header list.

  

  

   headerName: The header to add to the collection.

   headerValue: The content of the header.
  """
  pass
 def BaseAdd(self,*args):
  """
  BaseAdd(self: NameObjectCollectionBase,name: str,value: object)

   Adds an entry with the specified key and value into the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   name: The System.String key of the entry to add. The key can be null.

   value: The System.Object value of the entry to add. The value can be null.
  """
  pass
 def BaseClear(self,*args):
  """
  BaseClear(self: NameObjectCollectionBase)

   Removes all entries from the System.Collections.Specialized.NameObjectCollectionBase instance.
  """
  pass
 def BaseGet(self,*args):
  """
  BaseGet(self: NameObjectCollectionBase,index: int) -> object

  

   Gets the value of the entry at the specified index of the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   index: The zero-based index of the value to get.

   Returns: An System.Object that represents the value of the entry at the specified index.

  BaseGet(self: NameObjectCollectionBase,name: str) -> object

  

   Gets the value of the first entry with the specified key from the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   name: The System.String key of the entry to get. The key can be null.

   Returns: An System.Object that represents the value of the first entry with the specified key,if found; 

    otherwise,null.
  """
  pass
 def BaseGetAllKeys(self,*args):
  """
  BaseGetAllKeys(self: NameObjectCollectionBase) -> Array[str]

  

   Returns a System.String array that contains all the keys in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

   Returns: A System.String array that contains all the keys in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.
  """
  pass
 def BaseGetAllValues(self,*args):
  """
  BaseGetAllValues(self: NameObjectCollectionBase,type: Type) -> Array[object]

  

   Returns an array of the specified type that contains all the values in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   type: A System.Type that represents the type of array to return.

   Returns: An array of the specified type that contains all the values in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  BaseGetAllValues(self: NameObjectCollectionBase) -> Array[object]

  

   Returns an System.Object array that contains all the values in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

   Returns: An System.Object array that contains all the values in the 

    System.Collections.Specialized.NameObjectCollectionBase instance.
  """
  pass
 def BaseGetKey(self,*args):
  """
  BaseGetKey(self: NameObjectCollectionBase,index: int) -> str

  

   Gets the key of the entry at the specified index of the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   index: The zero-based index of the key to get.

   Returns: A System.String that represents the key of the entry at the specified index.
  """
  pass
 def BaseHasKeys(self,*args):
  """
  BaseHasKeys(self: NameObjectCollectionBase) -> bool

  

   Gets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase 

    instance contains entries whose keys are not null.

  

   Returns: true if the System.Collections.Specialized.NameObjectCollectionBase instance contains entries 

    whose keys are not null; otherwise,false.
  """
  pass
 def BaseRemove(self,*args):
  """
  BaseRemove(self: NameObjectCollectionBase,name: str)

   Removes the entries with the specified key from the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   name: The System.String key of the entries to remove. The key can be null.
  """
  pass
 def BaseRemoveAt(self,*args):
  """
  BaseRemoveAt(self: NameObjectCollectionBase,index: int)

   Removes the entry at the specified index of the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   index: The zero-based index of the entry to remove.
  """
  pass
 def BaseSet(self,*args):
  """
  BaseSet(self: NameObjectCollectionBase,index: int,value: object)

   Sets the value of the entry at the specified index of the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   index: The zero-based index of the entry to set.

   value: The System.Object that represents the new value of the entry to set. The value can be null.

  BaseSet(self: NameObjectCollectionBase,name: str,value: object)

   Sets the value of the first entry with the specified key in the 

    System.Collections.Specialized.NameObjectCollectionBase instance,if found; otherwise,adds an 

    entry with the specified key and value into the 

    System.Collections.Specialized.NameObjectCollectionBase instance.

  

  

   name: The System.String key of the entry to set. The key can be null.

   value: The System.Object that represents the new value of the entry to set. The value can be null.
  """
  pass
 def Clear(self):
  """
  Clear(self: WebHeaderCollection)

   Removes all headers from the collection.
  """
  pass
 def Get(self,*__args):
  """
  Get(self: WebHeaderCollection,index: int) -> str

  

   Get the value of a particular header in the collection,specified by an index into the 

    collection.

  

  

   index: The zero-based index of the key to get from the collection.

   Returns: A System.String containing the value of the specified header.

  Get(self: WebHeaderCollection,name: str) -> str

  

   Get the value of a particular header in the collection,specified by the name of the header.

  

   name: The name of the Web header.

   Returns: A System.String holding the value of the specified header.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: WebHeaderCollection) -> IEnumerator

  

   Returns an enumerator that can iterate through the System.Net.WebHeaderCollection instance.

   Returns: An System.Collections.IEnumerator for the System.Net.WebHeaderCollection.
  """
  pass
 def GetKey(self,index):
  """
  GetKey(self: WebHeaderCollection,index: int) -> str

  

   Get the header name at the specified position in the collection.

  

   index: The zero-based index of the key to get from the collection.

   Returns: A System.String holding the header name.
  """
  pass
 def GetObjectData(self,serializationInfo,streamingContext):
  """
  GetObjectData(self: WebHeaderCollection,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 

    serialization.
  """
  pass
 def GetValues(self,*__args):
  """
  GetValues(self: WebHeaderCollection,index: int) -> Array[str]

  

   Gets an array of header values stored in the index position of the header collection.

  

   index: The header index to return.

   Returns: An array of header strings.

  GetValues(self: WebHeaderCollection,header: str) -> Array[str]

  

   Gets an array of header values stored in a header.

  

   header: The header to return.

   Returns: An array of header strings.
  """
  pass
 def InvalidateCachedArrays(self,*args):
  """
  InvalidateCachedArrays(self: NameValueCollection)

   Resets the cached arrays of the collection to null.
  """
  pass
 @staticmethod
 def IsRestricted(headerName,response=None):
  """
  IsRestricted(headerName: str,response: bool) -> bool

  

   Tests whether the specified HTTP header can be set for the request or the response.

  

   headerName: The header to test.

   response: Does the Framework test the response or the request?

   Returns: true if the header is restricted; otherwise,false.

  IsRestricted(headerName: str) -> bool

  

   Tests whether the specified HTTP header can be set for the request.

  

   headerName: The header to test.

   Returns: true if the header is restricted; otherwise false.
  """
  pass
 def OnDeserialization(self,sender):
  """
  OnDeserialization(self: WebHeaderCollection,sender: object)

   Implements the System.Runtime.Serialization.ISerializable interface and raises the 

    deserialization event when the deserialization is complete.

  

  

   sender: The source of the deserialization event.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: WebHeaderCollection,name: str)

   Removes the specified header from the collection.

  

   name: The name of the header to remove from the collection.

  Remove(self: WebHeaderCollection,header: HttpResponseHeader)

   Removes the specified header from the collection.

  

   header: The System.Net.HttpResponseHeader instance to remove from the collection.

  Remove(self: WebHeaderCollection,header: HttpRequestHeader)

   Removes the specified header from the collection.

  

   header: The System.Net.HttpRequestHeader instance to remove from the collection.
  """
  pass
 def Set(self,*__args):
  """
  Set(self: WebHeaderCollection,header: HttpResponseHeader,value: str)

   Sets the specified header to the specified value.

  

   header: The System.Net.HttpResponseHeader value to set.

   value: The content of the header to set.

  Set(self: WebHeaderCollection,name: str,value: str)

   Sets the specified header to the specified value.

  

   name: The header to set.

   value: The content of the header to set.

  Set(self: WebHeaderCollection,header: HttpRequestHeader,value: str)

   Sets the specified header to the specified value.

  

   header: The System.Net.HttpRequestHeader value to set.

   value: The content of the header to set.
  """
  pass
 def ToByteArray(self):
  """
  ToByteArray(self: WebHeaderCollection) -> Array[Byte]

  

   Converts the System.Net.WebHeaderCollection to a byte array..

   Returns: A System.Byte array holding the header collection.
  """
  pass
 def ToString(self):
  """
  ToString(self: WebHeaderCollection) -> str

  

   This method is obsolete.

   Returns: The System.String representation of the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 AllKeys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all header names (keys) in the collection.



Get: AllKeys(self: WebHeaderCollection) -> Array[str]



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of headers in the collection.



Get: Count(self: WebHeaderCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase instance is read-only.



"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of header names (keys) in the collection.



Get: Keys(self: WebHeaderCollection) -> KeysCollection



"""



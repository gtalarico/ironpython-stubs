class DocumentReferenceCollection(object,IEnumerable[DocumentReference],IEnumerable,INotifyCollectionChanged):
 """ Defines an ordered list of System.Windows.Documents.DocumentReference elements. """
 def Add(self,item):
  """
  Add(self: DocumentReferenceCollection,item: DocumentReference)
   Adds an element to the end of the collection.
  
   item: The element to add to the end of the collection.
  """
  pass
 def CopyTo(self,array,arrayIndex):
  """
  CopyTo(self: DocumentReferenceCollection,array: Array[DocumentReference],arrayIndex: int)
   Copies the whole collection to an array that starts at a given array index.
  
   array: The destination array to which the elements from the collection should be 
    copied.
  
   arrayIndex: The zero-based starting index within the array where the collection elements 
    are to be copied.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: DocumentReferenceCollection) -> IEnumerator[DocumentReference]
  
   Returns an enumerator for iterating through the collection.
   Returns: An enumerator that you can use to iterate through the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[DocumentReference](enumerable: IEnumerable[DocumentReference],value: DocumentReference) -> bool """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of elements that are in the collection.

Get: Count(self: DocumentReferenceCollection) -> int

"""


 CollectionChanged=None


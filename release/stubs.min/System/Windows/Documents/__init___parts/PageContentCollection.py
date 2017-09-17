class PageContentCollection(object,IEnumerable[PageContent],IEnumerable):
 """ Provides collection support for a collection of document pages. """
 def Add(self,newPageContent):
  """
  Add(self: PageContentCollection,newPageContent: PageContent) -> int
  
   Adds a new page to the page collection.
  
   newPageContent: The new page to add to the collection.
   Returns: The zero-based index within the collection where the page was added.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PageContentCollection) -> IEnumerator[PageContent]
  
   Returns an enumerator for iterating through the page collection.
   Returns: An enumerator that can be used to iterate through the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[PageContent](enumerable: IEnumerable[PageContent],value: PageContent) -> bool """
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
 """Gets the number of elements contained in the page collection.

Get: Count(self: PageContentCollection) -> int

"""



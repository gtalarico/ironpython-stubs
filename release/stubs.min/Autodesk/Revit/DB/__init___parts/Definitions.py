class Definitions(object,IEnumerable[Definition],IEnumerable,IDisposable):
 """
 A base class that supports the addition of new parameter definitions.

 

 Definitions()
 """
 def Contains(self,definition):
  """
  Contains(self: Definitions,definition: Definition) -> bool

  

   Tests for the existence of a definition within the set.

  

   definition: The definition to look for.

   Returns: True if the definition was found,false otherwise.
  """
  pass
 def Create(self,option):
  """
  Create(self: Definitions,option: ExternalDefinitionCreationOptions) -> Definition

  

   Creates a new parameter definition using specified options.

  

   option: The options used to create the new parameter definition.

   Returns: If successful a reference to the new parameter definition is returned,

    otherwise ll.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Definitions) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: Definitions) -> IEnumerator[Definition]

  

   Retrieves an enumerator to the collection.

   Returns: The enumerator.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Definition](enumerable: IEnumerable[Definition],value: Definition) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
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
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the definitions collection is empty.



Get: IsEmpty(self: Definitions) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of definitions in the collection.



Get: Size(self: Definitions) -> int



"""



class DefinitionGroups(object,IEnumerable[DefinitionGroup],IEnumerable,IDisposable):
 """ A specialized set of definition groups that allows creation of new groups. """
 def Contains(self,definitionGroup):
  """
  Contains(self: DefinitionGroups,definitionGroup: DefinitionGroup) -> bool

  

   Tests for the existence of a definition group within the collection.

  

   definitionGroup: The definition group to look for.

   Returns: True if the definition group was found,false otherwise.
  """
  pass
 def Create(self,name):
  """
  Create(self: DefinitionGroups,name: str) -> DefinitionGroup

  

   Create a new parameter definition group using the name provided.

  

   name: The name of the group to be created.

   Returns: If successful a reference to the new parameter group is returned,otherwise ll.
  """
  pass
 def Dispose(self):
  """ Dispose(self: DefinitionGroups) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: DefinitionGroups) -> IEnumerator[DefinitionGroup]

  

   Retrieves an enumerator to the collection.

   Returns: The enumerator.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[DefinitionGroup](enumerable: IEnumerable[DefinitionGroup],value: DefinitionGroup) -> bool """
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
 """Identifies if the definition groups collection is empty.



Get: IsEmpty(self: DefinitionGroups) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of definition groups in the collection.



Get: Size(self: DefinitionGroups) -> int



"""



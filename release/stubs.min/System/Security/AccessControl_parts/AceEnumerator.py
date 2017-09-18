class AceEnumerator(object,IEnumerator):
 """ Provides the ability to iterate through the access control entries (ACEs) in an access control list (ACL). """
 def MoveNext(self):
  """
  MoveNext(self: AceEnumerator) -> bool

  

   Advances the enumerator to the next element of the System.Security.AccessControl.GenericAce 

    collection.

  

   Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 

    has passed the end of the collection.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def Reset(self):
  """
  Reset(self: AceEnumerator)

   Sets the enumerator to its initial position,which is before the first element in the 

    System.Security.AccessControl.GenericAce collection.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerator) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current element in the System.Security.AccessControl.GenericAce collection. This property gets the type-friendly version of the object.



Get: Current(self: AceEnumerator) -> GenericAce



"""



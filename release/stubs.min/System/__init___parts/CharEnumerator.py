class CharEnumerator(object,IEnumerator,ICloneable,IEnumerator[Char],IDisposable):
 """ Supports iterating over a System.String object and reading its individual characters. This class cannot be inherited. """
 def Clone(self):
  """
  Clone(self: CharEnumerator) -> object

  

   Creates a copy of the current System.CharEnumerator object.

   Returns: An System.Object that is a copy of the current System.CharEnumerator object.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CharEnumerator)

   Releases all resources used by the current instance of the System.CharEnumerator class.
  """
  pass
 def MoveNext(self):
  """
  MoveNext(self: CharEnumerator) -> bool

  

   Increments the internal index of the current System.CharEnumerator object to the next character 

    of the enumerated string.

  

   Returns: true if the index is successfully incremented and within the enumerated string; otherwise,false.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def Reset(self):
  """
  Reset(self: CharEnumerator)

   Initializes the index to a position logically before the first character of the enumerated 

    string.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Char](enumerator: IEnumerator[Char],value: Char) -> bool """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerator) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the currently referenced character in the string enumerated by this System.CharEnumerator object.



Get: Current(self: CharEnumerator) -> Char



"""



class FilterRule(object,IDisposable):
 """ Defines a boolean operation that can be used to cull elements from a document. """
 def Dispose(self):
  """ Dispose(self: FilterRule) """
  pass
 def ElementPasses(self,element):
  """
  ElementPasses(self: FilterRule,element: Element) -> bool

  

   Derived classes override this method to implement the test that determines

     

    whether the given element passes this rule or not.

  

  

   element: The element to test against the rule.

   Returns: True if the element satisfies the rule,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterRule,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FilterRule) -> bool



"""



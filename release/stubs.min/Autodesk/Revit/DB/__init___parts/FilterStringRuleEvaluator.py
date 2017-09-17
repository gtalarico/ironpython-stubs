class FilterStringRuleEvaluator(object,IDisposable):
 """ Base for all classes that compare string values from Revit to a user-supplied filter value """
 def Dispose(self):
  """ Dispose(self: FilterStringRuleEvaluator) """
  pass
 def Evaluate(self,lhs,rhs,caseSensitive):
  """
  Evaluate(self: FilterStringRuleEvaluator,lhs: str,rhs: str,caseSensitive: bool) -> bool
  
   Derived classes override this method to implement the test that determines
     
    whether the two given string values satisfy the desired condition or not.
  
  
   lhs: A value from an element in the document.
   rhs: The user-supplied value against which values from the document are tested.
   caseSensitive: If true,string comparisons are done case-sensitively.
   Returns: True if the given arguments satisfy the condition,otherwise false.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterStringRuleEvaluator,disposing: bool) """
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

Get: IsValidObject(self: FilterStringRuleEvaluator) -> bool

"""



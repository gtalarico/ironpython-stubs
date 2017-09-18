class FilterNumericRuleEvaluator(object,IDisposable):
 """ Base for all classes that compare numeric values from Revit to a user-supplied filter value. """
 def Dispose(self):
  """ Dispose(self: FilterNumericRuleEvaluator) """
  pass
 def Evaluate(self,lhs,rhs,epsilon=None):
  """
  Evaluate(self: FilterNumericRuleEvaluator,lhs: float,rhs: float,epsilon: float) -> bool

  

   Derived classes override this method to implement the test that determines

     

    whether the two given double-precision values satisfy the desired condition or 

    not.

  

  

   lhs: A value from an element in the document.

   rhs: The user-supplied value against which values from the document are tested.

   epsilon: Defines the tolerance within which two values may be considered equal.

   Returns: True if the given arguments satisfy the condition,otherwise false.

  Evaluate(self: FilterNumericRuleEvaluator,lhs: int,rhs: int) -> bool

  

   Derived classes should override this method to implement the desired test.

  

   lhs: A value from an element in the document.

   rhs: The user-supplied value against which values from the document are tested.

   Returns: True if lhs,rhs satisfy the condition implemented by this evaluator.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterNumericRuleEvaluator,disposing: bool) """
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



Get: IsValidObject(self: FilterNumericRuleEvaluator) -> bool



"""



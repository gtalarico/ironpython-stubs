class SharedParameterApplicableRule(FilterRule,IDisposable):
 """
 Tests whether an element supports a shared parameter.

 

 SharedParameterApplicableRule(parameterName: str)
 """
 def Dispose(self):
  """ Dispose(self: FilterRule,A_0: bool) """
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
 @staticmethod
 def __new__(self,parameterName):
  """ __new__(cls: type,parameterName: str) """
  pass
 ParameterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the parameter that an element must support to pass this rule.



Get: ParameterName(self: SharedParameterApplicableRule) -> str



Set: ParameterName(self: SharedParameterApplicableRule)=value

"""



class ParameterValueProvider(FilterableValueProvider,IDisposable):
 """
 Gets the value of a parameter from any element passed to getStringValue,

    getDoubleValue,getIntegerValue,or getElementIdValue.

 

 ParameterValueProvider(parameter: ElementId)
 """
 def Dispose(self):
  """ Dispose(self: FilterableValueProvider,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterableValueProvider,disposing: bool) """
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
 def __new__(self,parameter):
  """ __new__(cls: type,parameter: ElementId) """
  pass
 Parameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The parameter used to provide a string,integer,double-precision,or ElementId

   value on request for a given element.



Get: Parameter(self: ParameterValueProvider) -> ElementId



Set: Parameter(self: ParameterValueProvider)=value

"""



class ElementParameterFilter(ElementSlowFilter,IDisposable):
 """
 A filter used to match elements by one or more parameter filter rules.
 
 ElementParameterFilter(filterRules: IList[FilterRule],inverted: bool)
 ElementParameterFilter(filterRules: IList[FilterRule])
 ElementParameterFilter(filterRule: FilterRule,inverted: bool)
 ElementParameterFilter(filterRule: FilterRule)
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def GetRules(self):
  """
  GetRules(self: ElementParameterFilter) -> IList[FilterRule]
  
   Returns the set of rules contained in this filter.
   Returns: A copy of the set of rules.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementFilter,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,filterRules: IList[FilterRule],inverted: bool)
  __new__(cls: type,filterRules: IList[FilterRule])
  __new__(cls: type,filterRule: FilterRule,inverted: bool)
  __new__(cls: type,filterRule: FilterRule)
  """
  pass

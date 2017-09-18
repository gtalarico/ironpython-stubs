class FilterableValueProvider(object,IDisposable):
 """
 Defines the interface for classes that extract values from elements

    in a Revit project for testing against filter rules.
 """
 def Dispose(self):
  """ Dispose(self: FilterableValueProvider) """
  pass
 def GetAssociatedGlobalParameterValue(self,element):
  """
  GetAssociatedGlobalParameterValue(self: FilterableValueProvider,element: Element) -> ElementId

  

   Gets a global parameter value associated with a parameter from the given 

    element.

  

  

   element: The element to query.

   Returns: The associated global parameter.
  """
  pass
 def GetDoubleValue(self,element):
  """
  GetDoubleValue(self: FilterableValueProvider,element: Element) -> float

  

   Gets a double-precision numeric value from the given element.

  

   element: The element to query.

   Returns: The double-precision numeric value from the element.
  """
  pass
 def GetElementIdValue(self,element):
  """
  GetElementIdValue(self: FilterableValueProvider,element: Element) -> ElementId

  

   Gets an ElementId value from the given element.

  

   element: The element to query.

   Returns: The ElementId value from the element.
  """
  pass
 def GetIntegerValue(self,element):
  """
  GetIntegerValue(self: FilterableValueProvider,element: Element) -> int

  

   Gets an integer value from the given element.

  

   element: The element to query.

   Returns: The integer value from the element.
  """
  pass
 def GetStringValue(self,element):
  """
  GetStringValue(self: FilterableValueProvider,element: Element) -> str

  

   Gets a string value from the given element.

  

   element: The element to query.

   Returns: The string value from the element.
  """
  pass
 def IsDoubleValueSupported(self,element):
  """
  IsDoubleValueSupported(self: FilterableValueProvider,element: Element) -> bool

  

   Determines whether the provide can provide a double-precision numeric value for 

    the given element.

  

  

   element: The element to query.

   Returns: True if the provider can return a double-precision numeric value for the given 

    element,false otherwise.
  """
  pass
 def IsElementIdValueSupported(self,element):
  """
  IsElementIdValueSupported(self: FilterableValueProvider,element: Element) -> bool

  

   Determines whether the provide can provide an ElementId value for the given 

    element.

  

  

   element: The element to query.

   Returns: True if the provider can return an ElementId value for the given element,false 

    otherwise.
  """
  pass
 def IsIntegerValueSupported(self,element):
  """
  IsIntegerValueSupported(self: FilterableValueProvider,element: Element) -> bool

  

   Determines whether the provide can provide an integer value for the given 

    element.

  

  

   element: The element to query.

   Returns: True if the provider can return an integer value for the given element,false 

    otherwise.
  """
  pass
 def IsStringValueSupported(self,element):
  """
  IsStringValueSupported(self: FilterableValueProvider,element: Element) -> bool

  

   Determines whether the provide can provide a string value for the given element.

  

   element: The element to query.

   Returns: True if the provider can return a string value for the given element,false 

    otherwise.
  """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FilterableValueProvider) -> bool



"""



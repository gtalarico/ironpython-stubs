class ResourceKey(MarkupExtension):
 """ Provides an abstract base class for various resource keys. """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: ResourceKey,serviceProvider: IServiceProvider) -> object
  
   Returns this System.Windows.ResourceKey. Instances of this class are typically 
    used as a key in a dictionary.
  
  
   serviceProvider: A service implementation that provides the desired value.
   Returns: Calling this method always returns the instance itself.
  """
  pass
 Assembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an assembly object that indicates which assembly's dictionary to look in for the value associated with this key.

Get: Assembly(self: ResourceKey) -> Assembly

"""



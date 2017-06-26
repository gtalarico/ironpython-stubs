class DynamicResourceExtension(MarkupExtension):
 """
 Implements a markup extension that supports dynamic resource references made from XAML.
 
 DynamicResourceExtension(resourceKey: object)
 DynamicResourceExtension()
 """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: DynamicResourceExtension,serviceProvider: IServiceProvider) -> object
  
   Returns an object that should be set on the property where this extension is 
    applied. For System.Windows.DynamicResourceExtension,this is the object found 
    in a resource dictionary in the current parent chain that is keyed by the 
    System.Windows.DynamicResourceExtension.ResourceKey.
  
  
   serviceProvider: Object that can provide services for the markup extension.
   Returns: The object to set on the property where the extension is applied. Rather than 
    the actual value,this will be an expression that will be evaluated at a later 
    time.
  """
  pass
 @staticmethod
 def __new__(self,resourceKey=None):
  """
  __new__(cls: type)
  __new__(cls: type,resourceKey: object)
  """
  pass
 ResourceKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key specified by this dynamic resource reference. The key is used to lookup a resource in resource dictionaries,by means of an intermediate expression.

Get: ResourceKey(self: DynamicResourceExtension) -> object

Set: ResourceKey(self: DynamicResourceExtension)=value
"""



class StaticResourceExtension(MarkupExtension):
 """
 Implements a markup extension that supports static (XAML load time) resource references made from XAML.
 
 StaticResourceExtension(resourceKey: object)
 StaticResourceExtension()
 """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: StaticResourceExtension,serviceProvider: IServiceProvider) -> object
  
   Returns an object that should be set on the property where this extension is 
    applied. For System.Windows.StaticResourceExtension,this is the object found 
    in a resource dictionary,where the object to find is identified by the 
    System.Windows.StaticResourceExtension.ResourceKey.
  
  
   serviceProvider: Object that can provide services for the markup extension.
   Returns: The object value to set on the property where the markup extension provided 
    value is evaluated.
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
 """Gets or sets the key value passed by this static resource reference. They key is used  to return the object matching that key in resource dictionaries.

Get: ResourceKey(self: StaticResourceExtension) -> object

Set: ResourceKey(self: StaticResourceExtension)=value
"""



class ThemeDictionaryExtension(MarkupExtension):
 """
 Implements a markup extension that enables application authors to customize control styles based on the current system theme.
 
 ThemeDictionaryExtension()
 ThemeDictionaryExtension(assemblyName: str)
 """
 def ProvideValue(self,serviceProvider):
  """
  ProvideValue(self: ThemeDictionaryExtension,serviceProvider: IServiceProvider) -> object
  
   Returns an object that should be set on the property where this extension is 
    applied. For System.Windows.ThemeDictionaryExtension,this is the URI value for 
    a particular theme dictionary extension.
  
  
   serviceProvider: An object that can provide services for the markup extension. This service is 
    expected to provide results for System.Windows.Markup.IXamlTypeResolver.
  
   Returns: The object value to set on the property where the extension is applied.
  """
  pass
 @staticmethod
 def __new__(self,assemblyName=None):
  """
  __new__(cls: type)
  __new__(cls: type,assemblyName: str)
  """
  pass
 AssemblyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string setting a particular naming convention to identify which dictionary applies for a particular theme.

Get: AssemblyName(self: ThemeDictionaryExtension) -> str

Set: AssemblyName(self: ThemeDictionaryExtension)=value
"""



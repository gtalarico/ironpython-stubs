class ComponentResourceManager(ResourceManager):
 """
 Provides simple functionality for enumerating resources for a component or object. The System.ComponentModel.ComponentResourceManager class is a System.Resources.ResourceManager.

 

 ComponentResourceManager()

 ComponentResourceManager(t: Type)
 """
 def ApplyResources(self,value,objectName,culture=None):
  """
  ApplyResources(self: ComponentResourceManager,value: object,objectName: str,culture: CultureInfo)

   Applies a resource's value to the corresponding property of the object.

  

   value: An System.Object that contains the property value to be applied.

   objectName: A System.String that contains the name of the object to look up in the resources.

   culture: The culture for which to apply resources.

  ApplyResources(self: ComponentResourceManager,value: object,objectName: str)

   Applies a resource's value to the corresponding property of the object.

  

   value: An System.Object that contains the property value to be applied.

   objectName: A System.String that contains the name of the object to look up in the resources.
  """
  pass
 @staticmethod
 def __new__(self,t=None):
  """
  __new__(cls: type)

  __new__(cls: type,t: Type)
  """
  pass
 FallbackLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location from which to retrieve neutral fallback resources.



"""


 BaseNameField=None
 MainAssembly=None
 ResourceSets=None


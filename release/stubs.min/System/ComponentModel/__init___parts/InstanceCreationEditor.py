class InstanceCreationEditor(object):
 """ Creates an instance of a particular type of property from a drop-down box within the System.Windows.Forms.PropertyGrid. """
 def CreateInstance(self,context,instanceType):
  """
  CreateInstance(self: InstanceCreationEditor,context: ITypeDescriptorContext,instanceType: Type) -> object

  

   When overridden in a derived class,returns an instance of the specified type.

  

   context: The context information.

   instanceType: The specified type.

   Returns: An instance of the specified type or null.
  """
  pass
 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the specified text.



Get: Text(self: InstanceCreationEditor) -> str



"""



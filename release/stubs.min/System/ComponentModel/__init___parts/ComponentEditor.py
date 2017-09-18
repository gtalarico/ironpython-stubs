class ComponentEditor(object):
 """ Provides the base class for a custom component editor. """
 def EditComponent(self,*__args):
  """
  EditComponent(self: ComponentEditor,context: ITypeDescriptorContext,component: object) -> bool

  

   Edits the component and returns a value indicating whether the component was modified based upon 

    a given context.

  

  

   context: An optional context object that can be used to obtain further information about the edit.

   component: The component to be edited.

   Returns: true if the component was modified; otherwise,false.

  EditComponent(self: ComponentEditor,component: object) -> bool

  

   Edits the component and returns a value indicating whether the component was modified.

  

   component: The component to be edited.

   Returns: true if the component was modified; otherwise,false.
  """
  pass

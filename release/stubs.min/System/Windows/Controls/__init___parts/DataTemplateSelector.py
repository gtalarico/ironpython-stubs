class DataTemplateSelector(object):
 """
 Provides a way to choose a System.Windows.DataTemplate based on the data object and the data-bound element.

 

 DataTemplateSelector()
 """
 def SelectTemplate(self,item,container):
  """
  SelectTemplate(self: DataTemplateSelector,item: object,container: DependencyObject) -> DataTemplate

  

   When overridden in a derived class,returns a System.Windows.DataTemplate based on custom logic.

  

   item: The data object for which to select the template.

   container: The data-bound object.

   Returns: Returns a System.Windows.DataTemplate or null. The default value is null.
  """
  pass

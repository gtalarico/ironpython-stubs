class HierarchicalDataTemplate(DataTemplate,INameScope,ISealable,IHaveResources,IQueryAmbient):
 """
 Represents a System.Windows.DataTemplate that supports System.Windows.Controls.HeaderedItemsControl,such as System.Windows.Controls.TreeViewItem or System.Windows.Controls.MenuItem.
 
 HierarchicalDataTemplate()
 HierarchicalDataTemplate(dataType: object)
 """
 def ValidateTemplatedParent(self,*args):
  """
  ValidateTemplatedParent(self: DataTemplate,templatedParent: FrameworkElement)
   Checks the templated parent against a set of rules.
  
   templatedParent: The element this template is applied to.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dataType=None):
  """
  __new__(cls: type)
  __new__(cls: type,dataType: object)
  """
  pass
 AlternationCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of alternating item containers for the child items.

Get: AlternationCount(self: HierarchicalDataTemplate) -> int

Set: AlternationCount(self: HierarchicalDataTemplate)=value
"""

 ItemBindingGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Data.BindingGroup that is copied to each child item.

Get: ItemBindingGroup(self: HierarchicalDataTemplate) -> BindingGroup

Set: ItemBindingGroup(self: HierarchicalDataTemplate)=value
"""

 ItemContainerStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Style that is applied to the item container for each child item.

Get: ItemContainerStyle(self: HierarchicalDataTemplate) -> Style

Set: ItemContainerStyle(self: HierarchicalDataTemplate)=value
"""

 ItemContainerStyleSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets custom style-selection logic for a style that can be applied to each item container.

Get: ItemContainerStyleSelector(self: HierarchicalDataTemplate) -> StyleSelector

Set: ItemContainerStyleSelector(self: HierarchicalDataTemplate)=value
"""

 ItemsSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding for this data template,which indicates where to find the collection that represents the next level in the data hierarchy.

Get: ItemsSource(self: HierarchicalDataTemplate) -> BindingBase

Set: ItemsSource(self: HierarchicalDataTemplate)=value
"""

 ItemStringFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a composite string that specifies how to format the items in the next level in the data hierarchy if they are displayed as strings.

Get: ItemStringFormat(self: HierarchicalDataTemplate) -> str

Set: ItemStringFormat(self: HierarchicalDataTemplate)=value
"""

 ItemTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.DataTemplate to apply to the System.Windows.Controls.ItemsControl.ItemTemplate property on a generated System.Windows.Controls.HeaderedItemsControl (such as a System.Windows.Controls.MenuItem or a System.Windows.Controls.TreeViewItem),to indicate how to display items from the next level in the data hierarchy.

Get: ItemTemplate(self: HierarchicalDataTemplate) -> DataTemplate

Set: ItemTemplate(self: HierarchicalDataTemplate)=value
"""

 ItemTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Controls.DataTemplateSelector to apply to the System.Windows.Controls.ItemsControl.ItemTemplateSelector property on a generated System.Windows.Controls.HeaderedItemsControl (such as a System.Windows.Controls.MenuItem or a System.Windows.Controls.TreeViewItem),to indicate how to select a template to display items from the next level in the data hierarchy.

Get: ItemTemplateSelector(self: HierarchicalDataTemplate) -> DataTemplateSelector

Set: ItemTemplateSelector(self: HierarchicalDataTemplate)=value
"""



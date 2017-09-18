class GridViewColumn(DependencyObject,INotifyPropertyChanged):
 """
 Represents a column that displays data.

 

 GridViewColumn()
 """
 def OnHeaderStringFormatChanged(self,*args):
  """
  OnHeaderStringFormatChanged(self: GridViewColumn,oldHeaderStringFormat: str,newHeaderStringFormat: str)

   Occurs when the System.Windows.Controls.GridViewColumn.HeaderStringFormat property changes.

  

   oldHeaderStringFormat: The old value of the System.Windows.Controls.GridViewColumn.HeaderStringFormat property.

   newHeaderStringFormat: The new value of the System.Windows.Controls.GridViewColumn.HeaderStringFormat property.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: GridViewColumn,e: PropertyChangedEventArgs)

   Raises the 

    System.Windows.Controls.GridViewColumn.System#ComponentModel#INotifyPropertyChanged#PropertyChang

    ed event.

  

  

   e: The event data.

  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)

   Invoked whenever the effective value of any dependency property on this 

    System.Windows.DependencyObject has been updated. The specific dependency property that changed 

    is reported in the event data.

  

  

   e: Event data that will contain the dependency property identifier of interest,the property 

    metadata for the type,and old and new values.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: GridViewColumn) -> str

  

   Creates a string representation of the System.Windows.Controls.GridViewColumn.

   Returns: A string that identifies the object as a System.Windows.Controls.GridViewColumn object and 

    displays the value of the System.Windows.Controls.GridViewColumn.Header property.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 ActualWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the actual width of a System.Windows.Controls.GridViewColumn.



Get: ActualWidth(self: GridViewColumn) -> float



"""

 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template to use to display the contents of a column cell.



Get: CellTemplate(self: GridViewColumn) -> DataTemplate



Set: CellTemplate(self: GridViewColumn)=value

"""

 CellTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Controls.DataTemplateSelector that determines the template to use to display cells in a column.



Get: CellTemplateSelector(self: GridViewColumn) -> DataTemplateSelector



Set: CellTemplateSelector(self: GridViewColumn)=value

"""

 DisplayMemberBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data item to bind to for this column.



Get: DisplayMemberBinding(self: GridViewColumn) -> BindingBase



Set: DisplayMemberBinding(self: GridViewColumn)=value

"""

 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the content of the header of a System.Windows.Controls.GridViewColumn.



Get: Header(self: GridViewColumn) -> object



Set: Header(self: GridViewColumn)=value

"""

 HeaderContainerStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style to use for the header of the System.Windows.Controls.GridViewColumn.



Get: HeaderContainerStyle(self: GridViewColumn) -> Style



Set: HeaderContainerStyle(self: GridViewColumn)=value

"""

 HeaderStringFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a composite string that specifies how to format the System.Windows.Controls.GridViewColumn.Header property if it is displayed as a string.



Get: HeaderStringFormat(self: GridViewColumn) -> str



Set: HeaderStringFormat(self: GridViewColumn)=value

"""

 HeaderTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template to use to display the content of the column header.



Get: HeaderTemplate(self: GridViewColumn) -> DataTemplate



Set: HeaderTemplate(self: GridViewColumn)=value

"""

 HeaderTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Controls.DataTemplateSelector that provides logic to select the template to use to display the column header.



Get: HeaderTemplateSelector(self: GridViewColumn) -> DataTemplateSelector



Set: HeaderTemplateSelector(self: GridViewColumn)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the column.



Get: Width(self: GridViewColumn) -> float



Set: Width(self: GridViewColumn)=value

"""


 CellTemplateProperty=None
 CellTemplateSelectorProperty=None
 HeaderContainerStyleProperty=None
 HeaderProperty=None
 HeaderStringFormatProperty=None
 HeaderTemplateProperty=None
 HeaderTemplateSelectorProperty=None
 WidthProperty=None


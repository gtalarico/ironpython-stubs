class GridView(ViewBase,IAddChild):
 """
 Represents a view mode that displays data items in columns for a System.Windows.Controls.ListView control.

 

 GridView()
 """
 def AddChild(self,*args):
  """
  AddChild(self: GridView,column: object)

   Adds a System.Windows.Controls.GridViewColumn object to a System.Windows.Controls.GridView.

  

   column: The column to add
  """
  pass
 def AddText(self,*args):
  """
  AddText(self: GridView,text: str)

   Not supported.

  

   text: Text string
  """
  pass
 def ClearItem(self,*args):
  """
  ClearItem(self: GridView,item: ListViewItem)

   Removes all settings,bindings,and styling from a System.Windows.Controls.ListViewItem.

  

   item: The System.Windows.Controls.ListViewItem to clear.
  """
  pass
 def GetAutomationPeer(self,*args):
  """
  GetAutomationPeer(self: GridView,parent: ListView) -> IViewAutomationPeer

  

   Gets the System.Windows.Automation.Peers.AutomationPeer implementation for this 

    System.Windows.Controls.GridView object.

  

  

   parent: The System.Windows.Controls.ListView control that implements this 

    System.Windows.Controls.GridView view.

  

   Returns: A System.Windows.Automation.Peers.GridViewAutomationPeer for this 

    System.Windows.Controls.GridView.
  """
  pass
 @staticmethod
 def GetColumnCollection(element):
  """
  GetColumnCollection(element: DependencyObject) -> GridViewColumnCollection

  

   Gets the contents of the System.Windows.Controls.GridView.ColumnCollection�attached property.

  

   element: The System.Windows.DependencyObject that is associated with the collection.

   Returns: The System.Windows.Controls.GridView.ColumnCollection of the specified 

    System.Windows.DependencyObject.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)

   Invoked whenever the effective value of any dependency property on this 

    System.Windows.DependencyObject has been updated. The specific dependency property that changed 

    is reported in the event data.

  

  

   e: Event data that will contain the dependency property identifier of interest,the property 

    metadata for the type,and old and new values.
  """
  pass
 def PrepareItem(self,*args):
  """
  PrepareItem(self: GridView,item: ListViewItem)

   Prepares a System.Windows.Controls.ListViewItem for display according to the definition of this 

    System.Windows.Controls.GridView object.

  

  

   item: The System.Windows.Controls.ListViewItem to display.
  """
  pass
 @staticmethod
 def SetColumnCollection(element,collection):
  """
  SetColumnCollection(element: DependencyObject,collection: GridViewColumnCollection)

   Sets the contents of the System.Windows.Controls.GridView.ColumnCollection�attached property.

  

   element: The System.Windows.Controls.GridView object.

   collection: The System.Windows.Controls.GridViewColumnCollection object to assign.
  """
  pass
 @staticmethod
 def ShouldSerializeColumnCollection(obj):
  """
  ShouldSerializeColumnCollection(obj: DependencyObject) -> bool

  

   Determines whether to serialize the System.Windows.Controls.GridView.ColumnCollection�attached 

    property.

  

  

   obj: The object on which the System.Windows.Controls.GridView.ColumnCollection is set.

   Returns: true if the System.Windows.Controls.GridView.ColumnCollection must be serialized; otherwise,

    false.
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
  ToString(self: GridView) -> str

  

   Returns the string representation of the System.Windows.Controls.GridView object.

   Returns: A string that indicates the number of columns in the System.Windows.Controls.GridView.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AllowsColumnReorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether columns in a System.Windows.Controls.GridView can be reordered by a drag-and-drop operation.



Get: AllowsColumnReorder(self: GridView) -> bool



Set: AllowsColumnReorder(self: GridView)=value

"""

 ColumnHeaderContainerStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style to apply to column headers.



Get: ColumnHeaderContainerStyle(self: GridView) -> Style



Set: ColumnHeaderContainerStyle(self: GridView)=value

"""

 ColumnHeaderContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Controls.ContextMenu for the System.Windows.Controls.GridView.



Get: ColumnHeaderContextMenu(self: GridView) -> ContextMenu



Set: ColumnHeaderContextMenu(self: GridView)=value

"""

 ColumnHeaderStringFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a composite string that specifies how to format the column headers of the System.Windows.Controls.GridView if they are displayed as strings.



Get: ColumnHeaderStringFormat(self: GridView) -> str



Set: ColumnHeaderStringFormat(self: GridView)=value

"""

 ColumnHeaderTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a template to use to display the column headers.



Get: ColumnHeaderTemplate(self: GridView) -> DataTemplate



Set: ColumnHeaderTemplate(self: GridView)=value

"""

 ColumnHeaderTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the selector object that provides logic for selecting a template to use for each column header.



Get: ColumnHeaderTemplateSelector(self: GridView) -> DataTemplateSelector



Set: ColumnHeaderTemplateSelector(self: GridView)=value

"""

 ColumnHeaderToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the content of a tooltip that appears when the mouse pointer pauses over one of the column headers.



Get: ColumnHeaderToolTip(self: GridView) -> object



Set: ColumnHeaderToolTip(self: GridView)=value

"""

 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.Controls.GridViewColumn objects that is defined for this System.Windows.Controls.GridView.



Get: Columns(self: GridView) -> GridViewColumnCollection



"""

 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the reference for the default style for the System.Windows.Controls.GridView.



"""

 ItemContainerDefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the reference to the default style for the container of the data items in the System.Windows.Controls.GridView.



"""


 AllowsColumnReorderProperty=None
 ColumnCollectionProperty=None
 ColumnHeaderContainerStyleProperty=None
 ColumnHeaderContextMenuProperty=None
 ColumnHeaderStringFormatProperty=None
 ColumnHeaderTemplateProperty=None
 ColumnHeaderTemplateSelectorProperty=None
 ColumnHeaderToolTipProperty=None
 GridViewItemContainerStyleKey=None
 GridViewScrollViewerStyleKey=None
 GridViewStyleKey=None


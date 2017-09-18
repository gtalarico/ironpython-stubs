class DataGridColumn(DependencyObject):
 """ Represents a System.Windows.Controls.DataGrid column. """
 def CancelCellEdit(self,*args):
  """
  CancelCellEdit(self: DataGridColumn,editingElement: FrameworkElement,uneditedValue: object)

   Causes the cell being edited to revert to the original,unedited value.

  

   editingElement: The element that the column displays for a cell in editing mode.

   uneditedValue: The original,unedited value in the cell being edited.
  """
  pass
 def CommitCellEdit(self,*args):
  """
  CommitCellEdit(self: DataGridColumn,editingElement: FrameworkElement) -> bool

  

   Performs any required validation before exiting cell editing mode.

  

   editingElement: The element that the column displays for a cell in editing mode.

   Returns: true if no validation errors are found; otherwise,false.
  """
  pass
 def GenerateEditingElement(self,*args):
  """
  GenerateEditingElement(self: DataGridColumn,cell: DataGridCell,dataItem: object) -> FrameworkElement

  

   When overridden in a derived class,gets an editing element that is bound to the 

    System.Windows.Controls.DataGridBoundColumn.Binding property value of the column.

  

  

   cell: The cell that will contain the generated element.

   dataItem: The data item that is represented by the row that contains the intended cell.

   Returns: A new editing element that is bound to the System.Windows.Controls.DataGridBoundColumn.Binding 

    property value of the column.
  """
  pass
 def GenerateElement(self,*args):
  """
  GenerateElement(self: DataGridColumn,cell: DataGridCell,dataItem: object) -> FrameworkElement

  

   When overridden in a derived class,gets a read-only element that is bound to the 

    System.Windows.Controls.DataGridBoundColumn.Binding property value of the column.

  

  

   cell: The cell that will contain the generated element.

   dataItem: The data item that is represented by the row that contains the intended cell.

   Returns: A new read-only element that is bound to the System.Windows.Controls.DataGridBoundColumn.Binding 

    property value of the column.
  """
  pass
 def GetCellContent(self,*__args):
  """
  GetCellContent(self: DataGridColumn,dataGridRow: DataGridRow) -> FrameworkElement

  

   Retrieves the System.Windows.Controls.ContentControl.Content property value for the cell at the 

    intersection of this column and the specified row.

  

  

   dataGridRow: The row that contains the intended cell.

   Returns: The cell content; or null,if the cell is not found.

  GetCellContent(self: DataGridColumn,dataItem: object) -> FrameworkElement

  

   Gets the System.Windows.Controls.ContentControl.Content property value for the cell at the 

    intersection of this column and the row that represents the specified data item.

  

  

   dataItem: The data item that is represented by the row that contains the intended cell.

   Returns: The cell content; or null,if the cell is not found.
  """
  pass
 def NotifyPropertyChanged(self,*args):
  """
  NotifyPropertyChanged(self: DataGridColumn,propertyName: str)

   Notifies the System.Windows.Controls.DataGrid that contains this column that a column property 

    has changed.

  

  

   propertyName: The name of the column property that changed.
  """
  pass
 def OnCoerceIsReadOnly(self,*args):
  """
  OnCoerceIsReadOnly(self: DataGridColumn,baseValue: bool) -> bool

  

   Determines the value of the System.Windows.Controls.DataGridColumn.IsReadOnly property based on 

    the property rules of the System.Windows.Controls.DataGrid that contains this column.

  

  

   baseValue: The value that was passed to the delegate.

   Returns: true if cells in the column cannot be edited based on rules from the 

    System.Windows.Controls.DataGrid; otherwise,false.
  """
  pass
 def OnCopyingCellClipboardContent(self,item):
  """
  OnCopyingCellClipboardContent(self: DataGridColumn,item: object) -> object

  

   Raises the System.Windows.Controls.DataGridColumn.CopyingCellClipboardContent event.

  

   item: The data context for the selected element.

   Returns: An object that represents the content of the cell.
  """
  pass
 def OnPastingCellClipboardContent(self,item,cellContent):
  """
  OnPastingCellClipboardContent(self: DataGridColumn,item: object,cellContent: object)

   Raises the System.Windows.Controls.DataGridColumn.PastingCellClipboardContent event.

  

   item: The data context for the selected element.

   cellContent: The content to paste into the cell.
  """
  pass
 def PrepareCellForEdit(self,*args):
  """
  PrepareCellForEdit(self: DataGridColumn,editingElement: FrameworkElement,editingEventArgs: RoutedEventArgs) -> object

  

   When overridden in a derived class,sets cell content as needed for editing.

  

   editingElement: The element that the column displays for a cell in editing mode.

   editingEventArgs: Information about the user gesture that is causing a cell to enter editing mode.

   Returns: When returned by a derived class,the unedited cell value. This implementation returns null in 

    all cases.
  """
  pass
 def RefreshCellContent(self,*args):
  """
  RefreshCellContent(self: DataGridColumn,element: FrameworkElement,propertyName: str)

   When overridden in a derived class,updates the contents of a cell in the column in response to 

    a column property value that changed.

  

  

   element: The cell to update.

   propertyName: The name of the column property that changed.
  """
  pass
 ActualWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current width of the column,in device-independent units (1/96th inch per unit).



Get: ActualWidth(self: DataGridColumn) -> float



"""

 CanUserReorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can change the column display position by dragging the column header.



Get: CanUserReorder(self: DataGridColumn) -> bool



Set: CanUserReorder(self: DataGridColumn)=value

"""

 CanUserResize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can adjust the column width by using the mouse.



Get: CanUserResize(self: DataGridColumn) -> bool



Set: CanUserResize(self: DataGridColumn)=value

"""

 CanUserSort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can sort the column by clicking the column header.



Get: CanUserSort(self: DataGridColumn) -> bool



Set: CanUserSort(self: DataGridColumn)=value

"""

 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used to render cells in the column.



Get: CellStyle(self: DataGridColumn) -> Style



Set: CellStyle(self: DataGridColumn)=value

"""

 ClipboardContentBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding object to use when getting or setting cell content for the clipboard.



Get: ClipboardContentBinding(self: DataGridColumn) -> BindingBase



Set: ClipboardContentBinding(self: DataGridColumn)=value

"""

 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""

 DisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display position of the column relative to the other columns in the System.Windows.Controls.DataGrid.



Get: DisplayIndex(self: DataGridColumn) -> int



Set: DisplayIndex(self: DataGridColumn)=value

"""

 DragIndicatorStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style object to apply to the column header during a drag operation.



Get: DragIndicatorStyle(self: DataGridColumn) -> Style



Set: DragIndicatorStyle(self: DataGridColumn)=value

"""

 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the content of the column header.



Get: Header(self: DataGridColumn) -> object



Set: Header(self: DataGridColumn)=value

"""

 HeaderStringFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the format pattern to apply to the content of the column header.



Get: HeaderStringFormat(self: DataGridColumn) -> str



Set: HeaderStringFormat(self: DataGridColumn)=value

"""

 HeaderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the column header.



Get: HeaderStyle(self: DataGridColumn) -> Style



Set: HeaderStyle(self: DataGridColumn)=value

"""

 HeaderTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template that defines the visual representation of the column header.



Get: HeaderTemplate(self: DataGridColumn) -> DataTemplate



Set: HeaderTemplate(self: DataGridColumn)=value

"""

 HeaderTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that selects which template to use for the column header.



Get: HeaderTemplateSelector(self: DataGridColumn) -> DataTemplateSelector



Set: HeaderTemplateSelector(self: DataGridColumn)=value

"""

 IsAutoGenerated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the column is auto-generated.



Get: IsAutoGenerated(self: DataGridColumn) -> bool



"""

 IsFrozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the column is prevented from scrolling horizontally.



Get: IsFrozen(self: DataGridColumn) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether cells in the column can be edited.



Get: IsReadOnly(self: DataGridColumn) -> bool



Set: IsReadOnly(self: DataGridColumn)=value

"""

 MaxWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum width constraint of the column.



Get: MaxWidth(self: DataGridColumn) -> float



Set: MaxWidth(self: DataGridColumn)=value

"""

 MinWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum width constraint of the column.



Get: MinWidth(self: DataGridColumn) -> float



Set: MinWidth(self: DataGridColumn)=value

"""

 SortDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sort direction (ascending or descending) of the column.



Get: SortDirection(self: DataGridColumn) -> Nullable[ListSortDirection]



Set: SortDirection(self: DataGridColumn)=value

"""

 SortMemberPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a property name,or a period-delimited hierarchy of property names,that indicates the member to sort by.



Get: SortMemberPath(self: DataGridColumn) -> str



Set: SortMemberPath(self: DataGridColumn)=value

"""

 Visibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the visibility of the column.



Get: Visibility(self: DataGridColumn) -> Visibility



Set: Visibility(self: DataGridColumn)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column width or automatic sizing mode.



Get: Width(self: DataGridColumn) -> DataGridLength



Set: Width(self: DataGridColumn)=value

"""


 ActualWidthProperty=None
 CanUserReorderProperty=None
 CanUserResizeProperty=None
 CanUserSortProperty=None
 CellStyleProperty=None
 CopyingCellClipboardContent=None
 DisplayIndexProperty=None
 DragIndicatorStyleProperty=None
 HeaderProperty=None
 HeaderStringFormatProperty=None
 HeaderStyleProperty=None
 HeaderTemplateProperty=None
 HeaderTemplateSelectorProperty=None
 IsAutoGeneratedProperty=None
 IsFrozenProperty=None
 IsReadOnlyProperty=None
 MaxWidthProperty=None
 MinWidthProperty=None
 PastingCellClipboardContent=None
 SortDirectionProperty=None
 SortMemberPathProperty=None
 VisibilityProperty=None
 WidthProperty=None


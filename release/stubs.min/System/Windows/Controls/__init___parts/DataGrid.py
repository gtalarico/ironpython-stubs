class DataGrid(MultiSelector,IResource,IAnimatable,IInputElement,IFrameworkInputElement,ISupportInitialize,IHaveResources,IQueryAmbient,IAddChild,IGeneratorHost,IContainItemStorage):
 """
 Represents a control that displays data in a customizable grid.
 
 DataGrid()
 """
 def AddChild(self,*args):
  """
  AddChild(self: ItemsControl,value: object)
   Adds the specified object as the child of the 
    System.Windows.Controls.ItemsControl object.
  
  
   value: The object to add as a child.
  AddChild(self: ComboBox_21$22,value: object)
  """
  pass
 def AddLogicalChild(self,*args):
  """
  AddLogicalChild(self: FrameworkElement,child: object)
   Adds the provided object to the logical tree of this element.
  
   child: Child element to be added.
  AddLogicalChild(self: Window_16$17,child: object)AddLogicalChild(self: Label_17$18,child: object)AddLogicalChild(self: TextBox_18$19,child: object)AddLogicalChild(self: Button_19$20,child: object)AddLogicalChild(self: CheckBox_20$21,child: object)AddLogicalChild(self: ComboBox_21$22,child: object)AddLogicalChild(self: Separator_22$23,child: object)
  """
  pass
 def AddText(self,*args):
  """
  AddText(self: ItemsControl,text: str)
   Adds the specified text string to the System.Windows.Controls.ItemsControl 
    object.
  
  
   text: The string to add.
  AddText(self: ComboBox_21$22,text: str)
  """
  pass
 def AddVisualChild(self,*args):
  """
  AddVisualChild(self: Visual,child: Visual)
   Defines the parent-child relationship between two visuals.
  
   child: The child visual object to add to parent visual.
  AddVisualChild(self: Window_16$17,child: Window_16$17)AddVisualChild(self: Label_17$18,child: Label_17$18)AddVisualChild(self: TextBox_18$19,child: TextBox_18$19)AddVisualChild(self: Button_19$20,child: Button_19$20)AddVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)AddVisualChild(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def ArrangeCore(self,*args):
  """
  ArrangeCore(self: FrameworkElement,finalRect: Rect)
   Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
    as virtual in System.Windows.UIElement) and seals the implementation.
  
  
   finalRect: The final area within the parent that this element should use to arrange itself 
    and its children.
  
  ArrangeCore(self: Window_16$17,finalRect: Rect)ArrangeCore(self: Label_17$18,finalRect: Rect)ArrangeCore(self: TextBox_18$19,finalRect: Rect)ArrangeCore(self: Button_19$20,finalRect: Rect)ArrangeCore(self: CheckBox_20$21,finalRect: Rect)ArrangeCore(self: ComboBox_21$22,finalRect: Rect)ArrangeCore(self: Separator_22$23,finalRect: Rect)
  """
  pass
 def ArrangeOverride(self,*args):
  """
  ArrangeOverride(self: Control,arrangeBounds: Size) -> Size
  
   Called to arrange and size the content of a System.Windows.Controls.Control 
    object.
  
  
   arrangeBounds: The computed size that is used to arrange the content.
   Returns: The size of the control.
  ArrangeOverride(self: Window_16$17,arrangeBounds: Size) -> Size
  ArrangeOverride(self: Label_17$18,arrangeBounds: Size) -> Size
  ArrangeOverride(self: TextBox_18$19,arrangeBounds: Size) -> Size
  ArrangeOverride(self: Button_19$20,arrangeBounds: Size) -> Size
  ArrangeOverride(self: CheckBox_20$21,arrangeBounds: Size) -> Size
  ArrangeOverride(self: ComboBox_21$22,arrangeBounds: Size) -> Size
  ArrangeOverride(self: Separator_22$23,arrangeBounds: Size) -> Size
  """
  pass
 def BeginEdit(self,editingEventArgs=None):
  """
  BeginEdit(self: DataGrid,editingEventArgs: RoutedEventArgs) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.BeginEdit command,which will 
    place the current cell or row into edit mode.
  
  
   editingEventArgs: If called from an event handler,the event arguments. May be null.
   Returns: true if the current cell or row enters edit mode; otherwise,false.
  BeginEdit(self: DataGrid) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.BeginEdit command,which will 
    place the current cell or row into edit mode.
  
   Returns: true if the current cell or row enters edit mode; otherwise,false.
  """
  pass
 def BeginUpdateSelectedItems(self,*args):
  """
  BeginUpdateSelectedItems(self: MultiSelector)
   Starts a new selection transaction.
  """
  pass
 def CancelEdit(self,editingUnit=None):
  """
  CancelEdit(self: DataGrid,editingUnit: DataGridEditingUnit) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.CancelEditCommand command for the 
    specified cell or row in edit mode.
  
  
   editingUnit: One of the enumeration values that specifies whether to cancel row or cell 
    edits.
  
   Returns: true if the current cell or row exits edit mode; otherwise,false.
  CancelEdit(self: DataGrid) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.CancelEditCommand command for the 
    cell or row currently in edit mode.
  
   Returns: true if the current cell or row exits edit mode,or if no cells or rows are in 
    edit mode; otherwise,false.
  """
  pass
 def ClearContainerForItemOverride(self,*args):
  """
  ClearContainerForItemOverride(self: DataGrid,element: DependencyObject,item: object)
   Unloads the row for the specified item.
  
   element: The System.Windows.Controls.DataGridRow to clear.
   item: The data item that the row contains.
  """
  pass
 def ClearDetailsVisibilityForItem(self,item):
  """
  ClearDetailsVisibilityForItem(self: DataGrid,item: object)
   Clears the System.Windows.Controls.DataGridRow.DetailsVisibility property for 
    the System.Windows.Controls.DataGridRow that represents the specified data 
    item.
  
  
   item: The data item in the row for which 
    System.Windows.Controls.DataGridRow.DetailsVisibility is cleared.
  """
  pass
 def ColumnFromDisplayIndex(self,displayIndex):
  """
  ColumnFromDisplayIndex(self: DataGrid,displayIndex: int) -> DataGridColumn
  
   Gets the System.Windows.Controls.DataGridColumn at the specified index.
  
   displayIndex: The zero-based index of the column to retrieve.
   Returns: The System.Windows.Controls.DataGridColumn at the specified 
    System.Windows.Controls.DataGridColumn.DisplayIndex.
  """
  pass
 def CommitEdit(self,editingUnit=None,exitEditingMode=None):
  """
  CommitEdit(self: DataGrid,editingUnit: DataGridEditingUnit,exitEditingMode: bool) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.CommitEditCommand command for the 
    specified cell or row currently in edit mode.
  
  
   editingUnit: One of the enumeration values that specifies whether to commit row or cell 
    edits.
  
   exitEditingMode: true to exit edit mode; otherwise,false.
   Returns: true if the current cell or row exits edit mode; otherwise,false.
  CommitEdit(self: DataGrid) -> bool
  
   Invokes the System.Windows.Controls.DataGrid.CommitEditCommand command for the 
    cell or row currently in edit mode.
  
   Returns: true if the current cell or row exits edit mode,or if no cells or rows are in 
    edit mode; otherwise,false.
  """
  pass
 def EndUpdateSelectedItems(self,*args):
  """
  EndUpdateSelectedItems(self: MultiSelector)
   Commits the selected items to the 
    System.Windows.Controls.Primitives.MultiSelector.
  """
  pass
 @staticmethod
 def GenerateColumns(itemProperties):
  """
  GenerateColumns(itemProperties: IItemProperties) -> Collection[DataGridColumn]
  
   Generates columns for the specified properties of an object.
  
   itemProperties: The properties of the object to be in the columns.
   Returns: The collection of columns for the properties of the object.
  """
  pass
 def GetContainerForItemOverride(self,*args):
  """
  GetContainerForItemOverride(self: DataGrid) -> DependencyObject
  
   Instantiates a new System.Windows.Controls.DataGridRow.
   Returns: The row that is the container.
  """
  pass
 def GetDetailsVisibilityForItem(self,item):
  """
  GetDetailsVisibilityForItem(self: DataGrid,item: object) -> Visibility
  
   Gets the System.Windows.Controls.DataGridRow.DetailsVisibility property for the 
    System.Windows.Controls.DataGridRow that represents the specified data item.
  
  
   item: The data item in the row for which 
    System.Windows.Controls.DataGridRow.DetailsVisibility is returned.
  
   Returns: The visibility for the row that contains the item.
  """
  pass
 def GetLayoutClip(self,*args):
  """
  GetLayoutClip(self: FrameworkElement,layoutSlotSize: Size) -> Geometry
  
   Returns a geometry for a clipping mask. The mask applies if the layout system 
    attempts to arrange an element that is larger than the available display space.
  
  
   layoutSlotSize: The size of the part of the element that does visual presentation.
   Returns: The clipping geometry.
  GetLayoutClip(self: Window_16$17,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Label_17$18,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: TextBox_18$19,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Button_19$20,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: CheckBox_20$21,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: ComboBox_21$22,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Separator_22$23,layoutSlotSize: Size) -> Geometry
  """
  pass
 def GetTemplateChild(self,*args):
  """
  GetTemplateChild(self: FrameworkElement,childName: str) -> DependencyObject
  
   Returns the named element in the visual tree of an instantiated 
    System.Windows.Controls.ControlTemplate.
  
  
   childName: Name of the child to find.
   Returns: The requested element. May be null if no element of the requested name exists.
  GetTemplateChild(self: Window_16$17,childName: str) -> DependencyObject
  GetTemplateChild(self: Label_17$18,childName: str) -> DependencyObject
  GetTemplateChild(self: TextBox_18$19,childName: str) -> DependencyObject
  GetTemplateChild(self: Button_19$20,childName: str) -> DependencyObject
  GetTemplateChild(self: CheckBox_20$21,childName: str) -> DependencyObject
  GetTemplateChild(self: ComboBox_21$22,childName: str) -> DependencyObject
  GetTemplateChild(self: Separator_22$23,childName: str) -> DependencyObject
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: FrameworkElement) -> DependencyObject
  
   Returns an alternative logical parent for this element if there is no visual 
    parent.
  
   Returns: Returns something other than null whenever a WPF framework-level implementation 
    of this method has a non-visual parent connection.
  
  GetUIParentCore(self: Window_16$17) -> DependencyObject
  GetUIParentCore(self: Label_17$18) -> DependencyObject
  GetUIParentCore(self: TextBox_18$19) -> DependencyObject
  GetUIParentCore(self: Button_19$20) -> DependencyObject
  GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
  GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
  GetUIParentCore(self: Separator_22$23) -> DependencyObject
  """
  pass
 def GetVisualChild(self,*args):
  """
  GetVisualChild(self: FrameworkElement,index: int) -> Visual
  
   Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32),and returns 
    a child at the specified index from a collection of child elements.
  
  
   index: The zero-based index of the requested child element in the collection.
   Returns: The requested child element. This should not return null; if the provided index 
    is out of range,an exception is thrown.
  
  GetVisualChild(self: Window_16$17,index: int) -> Visual
  GetVisualChild(self: Label_17$18,index: int) -> Visual
  GetVisualChild(self: TextBox_18$19,index: int) -> Visual
  GetVisualChild(self: Button_19$20,index: int) -> Visual
  GetVisualChild(self: CheckBox_20$21,index: int) -> Visual
  GetVisualChild(self: ComboBox_21$22,index: int) -> Visual
  GetVisualChild(self: Separator_22$23,index: int) -> Visual
  """
  pass
 def HitTestCore(self,*args):
  """
  HitTestCore(self: UIElement,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  
   Implements 
    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
    meters) to supply base element hit testing behavior (returning 
    System.Windows.Media.GeometryHitTestResult).
  
  
   hitTestParameters: Describes the hit test to perform,including the initial hit point.
   Returns: Results of the test,including the evaluated geometry.
  HitTestCore(self: UIElement,hitTestParameters: PointHitTestParameters) -> HitTestResult
  
   Implements 
    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
    ers) to supply base element hit testing behavior (returning 
    System.Windows.Media.HitTestResult).
  
  
   hitTestParameters: Describes the hit test to perform,including the initial hit point.
   Returns: Results of the test,including the evaluated point.
  HitTestCore(self: Window_16$17,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Window_16$17,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  """
  pass
 def IsItemItsOwnContainerOverride(self,*args):
  """
  IsItemItsOwnContainerOverride(self: DataGrid,item: object) -> bool
  
   Determines if an item is a System.Windows.Controls.DataGridRow.
  
   item: The item to test.
   Returns: true if the item is a System.Windows.Controls.DataGridRow; otherwise,false.
  """
  pass
 def MeasureCore(self,*args):
  """
  MeasureCore(self: FrameworkElement,availableSize: Size) -> Size
  
   Implements basic measure-pass layout system behavior for 
    System.Windows.FrameworkElement.
  
  
   availableSize: The available size that the parent element can give to the child elements.
   Returns: The desired size of this element in layout.
  MeasureCore(self: Window_16$17,availableSize: Size) -> Size
  MeasureCore(self: Label_17$18,availableSize: Size) -> Size
  MeasureCore(self: TextBox_18$19,availableSize: Size) -> Size
  MeasureCore(self: Button_19$20,availableSize: Size) -> Size
  MeasureCore(self: CheckBox_20$21,availableSize: Size) -> Size
  MeasureCore(self: ComboBox_21$22,availableSize: Size) -> Size
  MeasureCore(self: Separator_22$23,availableSize: Size) -> Size
  """
  pass
 def MeasureOverride(self,*args):
  """
  MeasureOverride(self: DataGrid,availableSize: Size) -> Size
  
   Determines the desired size of the System.Windows.Controls.DataGrid.
  
   availableSize: The maximum size that the System.Windows.Controls.DataGrid can occupy.
   Returns: The desired size of the System.Windows.Controls.DataGrid.
  """
  pass
 def OnAccessKey(self,*args):
  """
  OnAccessKey(self: UIElement,e: AccessKeyEventArgs)
   Provides class handling for when an access key that is meaningful for this 
    element is invoked.
  
  
   e: The event data to the access key event. The event data reports which key was 
    invoked,and indicate whether the System.Windows.Input.AccessKeyManager object 
    that controls the sending of these events also sent this access key invocation 
    to other elements.
  
  OnAccessKey(self: Window_16$17,e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18,e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19,e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20,e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21,e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22,e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23,e: AccessKeyEventArgs)
  """
  pass
 def OnAddingNewItem(self,*args):
  """ OnAddingNewItem(self: DataGrid,e: AddingNewItemEventArgs) """
  pass
 def OnAlternationCountChanged(self,*args):
  """
  OnAlternationCountChanged(self: ItemsControl,oldAlternationCount: int,newAlternationCount: int)
   Invoked when the System.Windows.Controls.ItemsControl.AlternationCount property 
    changes.
  
  
   oldAlternationCount: The old value of System.Windows.Controls.ItemsControl.AlternationCount.
   newAlternationCount: The new value of System.Windows.Controls.ItemsControl.AlternationCount.
  OnAlternationCountChanged(self: ComboBox_21$22,oldAlternationCount: int,newAlternationCount: int)
  """
  pass
 def OnApplyTemplate(self):
  """ OnApplyTemplate(self: DataGrid) """
  pass
 def OnAutoGeneratedColumns(self,*args):
  """
  OnAutoGeneratedColumns(self: DataGrid,e: EventArgs)
   Raises the System.Windows.Controls.DataGrid.AutoGeneratedColumns event.
  
   e: The data for the event.
  """
  pass
 def OnAutoGeneratingColumn(self,*args):
  """
  OnAutoGeneratingColumn(self: DataGrid,e: DataGridAutoGeneratingColumnEventArgs)
   Raises the System.Windows.Controls.DataGrid.AutoGeneratingColumn event.
  
   e: The data for the event.
  """
  pass
 def OnBeginningEdit(self,*args):
  """
  OnBeginningEdit(self: DataGrid,e: DataGridBeginningEditEventArgs)
   Raises the System.Windows.Controls.DataGrid.BeginningEdit event.
  
   e: The data for the event.
  """
  pass
 def OnCanExecuteBeginEdit(self,*args):
  """
  OnCanExecuteBeginEdit(self: DataGrid,e: CanExecuteRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event 
    associated with the System.Windows.Controls.DataGrid.BeginEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnCanExecuteCancelEdit(self,*args):
  """
  OnCanExecuteCancelEdit(self: DataGrid,e: CanExecuteRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event 
    associated with the System.Windows.Controls.DataGrid.CancelEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnCanExecuteCommitEdit(self,*args):
  """
  OnCanExecuteCommitEdit(self: DataGrid,e: CanExecuteRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event 
    associated with the System.Windows.Controls.DataGrid.CommitEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnCanExecuteCopy(self,*args):
  """
  OnCanExecuteCopy(self: DataGrid,args: CanExecuteRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event 
    associated with the System.Windows.Input.ApplicationCommands.Copy command.
  
  
   args: The data for the event.
  """
  pass
 def OnCanExecuteDelete(self,*args):
  """
  OnCanExecuteDelete(self: DataGrid,e: CanExecuteRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event 
    associated with the System.Windows.Controls.DataGrid.DeleteCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnCellEditEnding(self,*args):
  """
  OnCellEditEnding(self: DataGrid,e: DataGridCellEditEndingEventArgs)
   Raises the System.Windows.Controls.DataGrid.CellEditEnding event.
  
   e: The data for the event.
  """
  pass
 def OnChildDesiredSizeChanged(self,*args):
  """
  OnChildDesiredSizeChanged(self: UIElement,child: UIElement)
   Supports layout behavior when a child element is resized.
  
   child: The child element that is being resized.
  OnChildDesiredSizeChanged(self: Window_16$17,child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18,child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19,child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20,child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21,child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22,child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def OnColumnDisplayIndexChanged(self,*args):
  """
  OnColumnDisplayIndexChanged(self: DataGrid,e: DataGridColumnEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnDisplayIndexChanged event.
  
   e: The data for the event.
  """
  pass
 def OnColumnHeaderDragCompleted(self,*args):
  """
  OnColumnHeaderDragCompleted(self: DataGrid,e: DragCompletedEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnHeaderDragCompleted event.
  
   e: The data for the event.
  """
  pass
 def OnColumnHeaderDragDelta(self,*args):
  """
  OnColumnHeaderDragDelta(self: DataGrid,e: DragDeltaEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnHeaderDragDelta event.
  
   e: The data for the event.
  """
  pass
 def OnColumnHeaderDragStarted(self,*args):
  """
  OnColumnHeaderDragStarted(self: DataGrid,e: DragStartedEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnHeaderDragStarted event.
  
   e: The data for the event.
  """
  pass
 def OnColumnReordered(self,*args):
  """
  OnColumnReordered(self: DataGrid,e: DataGridColumnEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnReordered event.
  
   e: The data for the event.
  """
  pass
 def OnColumnReordering(self,*args):
  """
  OnColumnReordering(self: DataGrid,e: DataGridColumnReorderingEventArgs)
   Raises the System.Windows.Controls.DataGrid.ColumnReordering event.
  
   e: The data for the event.
  """
  pass
 def OnContextMenuClosing(self,*args):
  """
  OnContextMenuClosing(self: FrameworkElement,e: ContextMenuEventArgs)
   Invoked whenever an unhandled 
    System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
    class in its route. Implement this method to add class handling for this event.
  
  
   e: Provides data about the event.
  OnContextMenuClosing(self: Window_16$17,e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18,e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19,e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20,e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21,e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22,e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23,e: ContextMenuEventArgs)
  """
  pass
 def OnContextMenuOpening(self,*args):
  """
  OnContextMenuOpening(self: DataGrid,e: ContextMenuEventArgs)
   Selects a cell if its context menu is opened.
  
   e: The item whose context menu was opened.
  """
  pass
 def OnCopyingRowClipboardContent(self,*args):
  """
  OnCopyingRowClipboardContent(self: DataGrid,args: DataGridRowClipboardEventArgs)
   Raises the System.Windows.Controls.DataGrid.CopyingRowClipboardContent event.
  
   args: The data for the event.
  """
  pass
 def OnCreateAutomationPeer(self,*args):
  """
  OnCreateAutomationPeer(self: DataGrid) -> AutomationPeer
  
   Returns the automation peer for this System.Windows.Controls.DataGrid.
   Returns: The automation peer for this System.Windows.Controls.DataGrid.
  """
  pass
 def OnCurrentCellChanged(self,*args):
  """
  OnCurrentCellChanged(self: DataGrid,e: EventArgs)
   Raises the System.Windows.Controls.DataGrid.CurrentCellChanged event.
  
   e: The data for the event.
  """
  pass
 def OnDisplayMemberPathChanged(self,*args):
  """
  OnDisplayMemberPathChanged(self: ItemsControl,oldDisplayMemberPath: str,newDisplayMemberPath: str)
   Invoked when the System.Windows.Controls.ItemsControl.DisplayMemberPath 
    property changes.
  
  
   oldDisplayMemberPath: The old value of the System.Windows.Controls.ItemsControl.DisplayMemberPath 
    property.
  
   newDisplayMemberPath: New value of the System.Windows.Controls.ItemsControl.DisplayMemberPath 
    property.
  
  OnDisplayMemberPathChanged(self: ComboBox_21$22,oldDisplayMemberPath: str,newDisplayMemberPath: str)
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Window_16$17,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Label_17$18,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Button_19$20,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Separator_22$23,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragEnter(self: Window_16$17,e: DragEventArgs)OnDragEnter(self: Label_17$18,e: DragEventArgs)OnDragEnter(self: TextBox_18$19,e: DragEventArgs)OnDragEnter(self: Button_19$20,e: DragEventArgs)OnDragEnter(self: CheckBox_20$21,e: DragEventArgs)OnDragEnter(self: ComboBox_21$22,e: DragEventArgs)OnDragEnter(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragLeave(self: Window_16$17,e: DragEventArgs)OnDragLeave(self: Label_17$18,e: DragEventArgs)OnDragLeave(self: TextBox_18$19,e: DragEventArgs)OnDragLeave(self: Button_19$20,e: DragEventArgs)OnDragLeave(self: CheckBox_20$21,e: DragEventArgs)OnDragLeave(self: ComboBox_21$22,e: DragEventArgs)OnDragLeave(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragOver(self: Window_16$17,e: DragEventArgs)OnDragOver(self: Label_17$18,e: DragEventArgs)OnDragOver(self: TextBox_18$19,e: DragEventArgs)OnDragOver(self: Button_19$20,e: DragEventArgs)OnDragOver(self: CheckBox_20$21,e: DragEventArgs)OnDragOver(self: ComboBox_21$22,e: DragEventArgs)OnDragOver(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDrop(self: Window_16$17,e: DragEventArgs)OnDrop(self: Label_17$18,e: DragEventArgs)OnDrop(self: TextBox_18$19,e: DragEventArgs)OnDrop(self: Button_19$20,e: DragEventArgs)OnDrop(self: CheckBox_20$21,e: DragEventArgs)OnDrop(self: ComboBox_21$22,e: DragEventArgs)OnDrop(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnExecutedBeginEdit(self,*args):
  """
  OnExecutedBeginEdit(self: DataGrid,e: ExecutedRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.Executed event 
    associated with the System.Windows.Controls.DataGrid.BeginEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnExecutedCancelEdit(self,*args):
  """
  OnExecutedCancelEdit(self: DataGrid,e: ExecutedRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.Executed event 
    associated with the System.Windows.Controls.DataGrid.CancelEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnExecutedCommitEdit(self,*args):
  """
  OnExecutedCommitEdit(self: DataGrid,e: ExecutedRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.Executed event 
    associated with the System.Windows.Controls.DataGrid.CommitEditCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnExecutedCopy(self,*args):
  """
  OnExecutedCopy(self: DataGrid,args: ExecutedRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.Executed event 
    associated with the System.Windows.Input.ApplicationCommands.Copy command.
  
  
   args: The data for the event.
  """
  pass
 def OnExecutedDelete(self,*args):
  """
  OnExecutedDelete(self: DataGrid,e: ExecutedRoutedEventArgs)
   Provides handling for the System.Windows.Input.CommandBinding.Executed event 
    associated with the System.Windows.Controls.DataGrid.DeleteCommand command.
  
  
   e: The data for the event.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  OnGiveFeedback(self: Window_16$17,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18,e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20,e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21,e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23,e: GiveFeedbackEventArgs)
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: FrameworkElement,e: RoutedEventArgs)
   Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
    this element in its route.
  
  
   e: The System.Windows.RoutedEventArgs that contains the event data.
  OnGotFocus(self: Window_16$17,e: RoutedEventArgs)OnGotFocus(self: Label_17$18,e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19,e: RoutedEventArgs)OnGotFocus(self: Button_19$20,e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21,e: RoutedEventArgs)OnGotFocus(self: Separator_22$23,e: RoutedEventArgs)
  """
  pass
 def OnGotKeyboardFocus(self,*args):
  """
  OnGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnGotKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnGotMouseCapture(self,*args):
  """
  OnGotMouseCapture(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnGotMouseCapture(self: Window_16$17,e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18,e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19,e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20,e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21,e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22,e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnGotStylusCapture(self,*args):
  """
  OnGotStylusCapture(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnGotStylusCapture(self: Window_16$17,e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18,e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19,e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20,e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21,e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22,e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnGotTouchCapture(self,*args):
  """
  OnGotTouchCapture(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
    event that occurs when a touch is captured to this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnGotTouchCapture(self: Window_16$17,e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18,e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19,e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20,e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21,e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22,e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnGroupStyleSelectorChanged(self,*args):
  """
  OnGroupStyleSelectorChanged(self: ItemsControl,oldGroupStyleSelector: GroupStyleSelector,newGroupStyleSelector: GroupStyleSelector)
   Invoked when the System.Windows.Controls.ItemsControl.GroupStyleSelector 
    property changes.
  
  
   oldGroupStyleSelector: Old value of the System.Windows.Controls.ItemsControl.GroupStyleSelector 
    property.
  
   newGroupStyleSelector: New value of the System.Windows.Controls.ItemsControl.GroupStyleSelector 
    property.
  
  OnGroupStyleSelectorChanged(self: ComboBox_21$22,oldGroupStyleSelector: GroupStyleSelector,newGroupStyleSelector: GroupStyleSelector)
  """
  pass
 def OnInitialized(self,*args):
  """
  OnInitialized(self: Selector,e: EventArgs)
   Raises the System.Windows.FrameworkElement.Initialized event. This method is 
    invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
    internally.
  
  
   e: The System.Windows.RoutedEventArgs that contains the event data.
  OnInitialized(self: ComboBox_21$22,e: EventArgs)
  """
  pass
 def OnInitializingNewItem(self,*args):
  """
  OnInitializingNewItem(self: DataGrid,e: InitializingNewItemEventArgs)
   Raises the System.Windows.Controls.DataGrid.InitializingNewItem event.
  
   e: The data for the event.
  """
  pass
 def OnIsKeyboardFocusedChanged(self,*args):
  """
  OnIsKeyboardFocusedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsKeyboardFocusedChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsKeyboardFocusWithinChanged(self,*args):
  """
  OnIsKeyboardFocusWithinChanged(self: Selector,e: DependencyPropertyChangedEventArgs)
   Called when the System.Windows.UIElement.IsKeyboardFocusWithin property has 
    changed.
  
  
   e: The event data.
  OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsMouseCapturedChanged(self,*args):
  """
  OnIsMouseCapturedChanged(self: DataGrid,e: DependencyPropertyChangedEventArgs)
   Called when the System.Windows.UIElement.IsMouseCaptured property changes on 
    this element.
  
  
   e: The data for the event.
  """
  pass
 def OnIsMouseCaptureWithinChanged(self,*args):
  """
  OnIsMouseCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsMouseCaptureWithinChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsMouseDirectlyOverChanged(self,*args):
  """
  OnIsMouseDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsMouseDirectlyOverChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusCapturedChanged(self,*args):
  """
  OnIsStylusCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusCapturedChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusCaptureWithinChanged(self,*args):
  """
  OnIsStylusCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusCaptureWithinChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusDirectlyOverChanged(self,*args):
  """
  OnIsStylusDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusDirectlyOverChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnItemBindingGroupChanged(self,*args):
  """
  OnItemBindingGroupChanged(self: ItemsControl,oldItemBindingGroup: BindingGroup,newItemBindingGroup: BindingGroup)
   Invoked when the System.Windows.Controls.ItemsControl.ItemBindingGroup property 
    changes.
  
  
   oldItemBindingGroup: The old value of the System.Windows.Controls.ItemsControl.ItemBindingGroup.
   newItemBindingGroup: The new value of the System.Windows.Controls.ItemsControl.ItemBindingGroup.
  OnItemBindingGroupChanged(self: ComboBox_21$22,oldItemBindingGroup: BindingGroup,newItemBindingGroup: BindingGroup)
  """
  pass
 def OnItemContainerStyleChanged(self,*args):
  """
  OnItemContainerStyleChanged(self: ItemsControl,oldItemContainerStyle: Style,newItemContainerStyle: Style)
   Invoked when the System.Windows.Controls.ItemsControl.ItemContainerStyle 
    property changes.
  
  
   oldItemContainerStyle: Old value of the System.Windows.Controls.ItemsControl.ItemContainerStyle 
    property.
  
   newItemContainerStyle: New value of the System.Windows.Controls.ItemsControl.ItemContainerStyle 
    property.
  
  OnItemContainerStyleChanged(self: ComboBox_21$22,oldItemContainerStyle: Style,newItemContainerStyle: Style)
  """
  pass
 def OnItemContainerStyleSelectorChanged(self,*args):
  """
  OnItemContainerStyleSelectorChanged(self: ItemsControl,oldItemContainerStyleSelector: StyleSelector,newItemContainerStyleSelector: StyleSelector)
   Invoked when the 
    System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property 
    changes.
  
  
   oldItemContainerStyleSelector: Old value of the 
    System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property.
  
   newItemContainerStyleSelector: New value of the 
    System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property.
  
  OnItemContainerStyleSelectorChanged(self: ComboBox_21$22,oldItemContainerStyleSelector: StyleSelector,newItemContainerStyleSelector: StyleSelector)
  """
  pass
 def OnItemsChanged(self,*args):
  """
  OnItemsChanged(self: DataGrid,e: NotifyCollectionChangedEventArgs)
   Performs column auto generation and updates validation flags when items change.
  
   e: The data for the event.
  """
  pass
 def OnItemsPanelChanged(self,*args):
  """
  OnItemsPanelChanged(self: ItemsControl,oldItemsPanel: ItemsPanelTemplate,newItemsPanel: ItemsPanelTemplate)
   Invoked when the System.Windows.Controls.ItemsControl.ItemsPanel property 
    changes.
  
  
   oldItemsPanel: Old value of the System.Windows.Controls.ItemsControl.ItemsPanel property.
   newItemsPanel: New value of the System.Windows.Controls.ItemsControl.ItemsPanel property.
  OnItemsPanelChanged(self: ComboBox_21$22,oldItemsPanel: ItemsPanelTemplate,newItemsPanel: ItemsPanelTemplate)
  """
  pass
 def OnItemsSourceChanged(self,*args):
  """
  OnItemsSourceChanged(self: DataGrid,oldValue: IEnumerable,newValue: IEnumerable)
   Invoked when the System.Windows.Controls.ItemsControl.ItemsSource property 
    changes.
  
  
   oldValue: The old source.
   newValue: The new source.
  """
  pass
 def OnItemStringFormatChanged(self,*args):
  """
  OnItemStringFormatChanged(self: ItemsControl,oldItemStringFormat: str,newItemStringFormat: str)
   Invoked when the System.Windows.Controls.ItemsControl.ItemStringFormat property 
    changes.
  
  
   oldItemStringFormat: The old value of the System.Windows.Controls.ItemsControl.ItemStringFormat 
    property.
  
   newItemStringFormat: The new value of the System.Windows.Controls.ItemsControl.ItemStringFormat 
    property.
  
  OnItemStringFormatChanged(self: ComboBox_21$22,oldItemStringFormat: str,newItemStringFormat: str)
  """
  pass
 def OnItemTemplateChanged(self,*args):
  """
  OnItemTemplateChanged(self: ItemsControl,oldItemTemplate: DataTemplate,newItemTemplate: DataTemplate)
   Invoked when the System.Windows.Controls.ItemsControl.ItemTemplate property 
    changes.
  
  
   oldItemTemplate: The old System.Windows.Controls.ItemsControl.ItemTemplate property value.
   newItemTemplate: The new System.Windows.Controls.ItemsControl.ItemTemplate property value.
  OnItemTemplateChanged(self: ComboBox_21$22,oldItemTemplate: DataTemplate,newItemTemplate: DataTemplate)
  """
  pass
 def OnItemTemplateSelectorChanged(self,*args):
  """
  OnItemTemplateSelectorChanged(self: ItemsControl,oldItemTemplateSelector: DataTemplateSelector,newItemTemplateSelector: DataTemplateSelector)
   Invoked when the System.Windows.Controls.ItemsControl.ItemTemplateSelector 
    property changes.
  
  
   oldItemTemplateSelector: Old value of the System.Windows.Controls.ItemsControl.ItemTemplateSelector 
    property.
  
   newItemTemplateSelector: New value of the System.Windows.Controls.ItemsControl.ItemTemplateSelector 
    property.
  
  OnItemTemplateSelectorChanged(self: ComboBox_21$22,oldItemTemplateSelector: DataTemplateSelector,newItemTemplateSelector: DataTemplateSelector)
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: DataGrid,e: KeyEventArgs)
   e: The keyboard data that specifies which keys are pressed.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnKeyUp(self: Window_16$17,e: KeyEventArgs)OnKeyUp(self: Label_17$18,e: KeyEventArgs)OnKeyUp(self: TextBox_18$19,e: KeyEventArgs)OnKeyUp(self: Button_19$20,e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21,e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22,e: KeyEventArgs)OnKeyUp(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnLoadingRow(self,*args):
  """
  OnLoadingRow(self: DataGrid,e: DataGridRowEventArgs)
   Raises the System.Windows.Controls.DataGrid.LoadingRow event.
  
   e: The data for the event.
  """
  pass
 def OnLoadingRowDetails(self,*args):
  """
  OnLoadingRowDetails(self: DataGrid,e: DataGridRowDetailsEventArgs)
   Raises the System.Windows.Controls.DataGrid.LoadingRowDetails event.
  
   e: The data for the event.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: UIElement,e: RoutedEventArgs)
   Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
    data that is provided.
  
  
   e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
    contain the identifier for the System.Windows.UIElement.LostFocus event.
  
  OnLostFocus(self: Window_16$17,e: RoutedEventArgs)OnLostFocus(self: Label_17$18,e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19,e: RoutedEventArgs)OnLostFocus(self: Button_19$20,e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21,e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22,e: RoutedEventArgs)OnLostFocus(self: Separator_22$23,e: RoutedEventArgs)
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
  OnLostKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnLostMouseCapture(self,*args):
  """
  OnLostMouseCapture(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains event data.
  OnLostMouseCapture(self: Window_16$17,e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18,e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19,e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20,e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21,e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnLostStylusCapture(self,*args):
  """
  OnLostStylusCapture(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains event data.
  OnLostStylusCapture(self: Window_16$17,e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18,e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19,e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20,e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21,e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22,e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnLostTouchCapture(self,*args):
  """
  OnLostTouchCapture(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.LostTouchCapture 
    routed event that occurs when this element loses a touch capture.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnLostTouchCapture(self: Window_16$17,e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18,e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19,e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20,e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21,e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22,e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnManipulationBoundaryFeedback(self,*args):
  """
  OnManipulationBoundaryFeedback(self: UIElement,e: ManipulationBoundaryFeedbackEventArgs)
   Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
    occurs.
  
  
   e: The data for the event.
  OnManipulationBoundaryFeedback(self: Window_16$17,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23,e: ManipulationBoundaryFeedbackEventArgs)
  """
  pass
 def OnManipulationCompleted(self,*args):
  """
  OnManipulationCompleted(self: UIElement,e: ManipulationCompletedEventArgs)
   Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
  
   e: The data for the event.
  OnManipulationCompleted(self: Window_16$17,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23,e: ManipulationCompletedEventArgs)
  """
  pass
 def OnManipulationDelta(self,*args):
  """
  OnManipulationDelta(self: UIElement,e: ManipulationDeltaEventArgs)
   Called when the System.Windows.UIElement.ManipulationDelta event occurs.
  
   e: The data for the event.
  OnManipulationDelta(self: Window_16$17,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23,e: ManipulationDeltaEventArgs)
  """
  pass
 def OnManipulationInertiaStarting(self,*args):
  """
  OnManipulationInertiaStarting(self: UIElement,e: ManipulationInertiaStartingEventArgs)
   Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
    occurs.
  
  
   e: The data for the event.
  OnManipulationInertiaStarting(self: Window_16$17,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23,e: ManipulationInertiaStartingEventArgs)
  """
  pass
 def OnManipulationStarted(self,*args):
  """
  OnManipulationStarted(self: UIElement,e: ManipulationStartedEventArgs)
   Called when the System.Windows.UIElement.ManipulationStarted event occurs.
  
   e: The data for the event.
  OnManipulationStarted(self: Window_16$17,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18,e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20,e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21,e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23,e: ManipulationStartedEventArgs)
  """
  pass
 def OnManipulationStarting(self,*args):
  """
  OnManipulationStarting(self: UIElement,e: ManipulationStartingEventArgs)
   Provides class handling for the System.Windows.UIElement.ManipulationStarting 
    routed event that occurs when the manipulation processor is first created.
  
  
   e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
    data.
  
  OnManipulationStarting(self: Window_16$17,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18,e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20,e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21,e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23,e: ManipulationStartingEventArgs)
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: Control,e: MouseButtonEventArgs)
   Raises the System.Windows.Controls.Control.MouseDoubleClick routed event.
  
   e: The event data.
  OnMouseDoubleClick(self: Window_16$17,e: MouseButtonEventArgs)OnMouseDoubleClick(self: Label_17$18,e: MouseButtonEventArgs)OnMouseDoubleClick(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseDoubleClick(self: Button_19$20,e: MouseButtonEventArgs)OnMouseDoubleClick(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseDoubleClick(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseDoubleClick(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
    This event data reports details about the mouse button that was pressed and the 
    handled state.
  
  OnMouseDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnMouseEnter(self: Window_16$17,e: MouseEventArgs)OnMouseEnter(self: Label_17$18,e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19,e: MouseEventArgs)OnMouseEnter(self: Button_19$20,e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21,e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22,e: MouseEventArgs)OnMouseEnter(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnMouseLeave(self: Window_16$17,e: MouseEventArgs)OnMouseLeave(self: Label_17$18,e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19,e: MouseEventArgs)OnMouseLeave(self: Button_19$20,e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21,e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22,e: MouseEventArgs)OnMouseLeave(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnMouseLeftButtonDown(self,*args):
  """
  OnMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  
  OnMouseLeftButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseLeftButtonUp(self,*args):
  """
  OnMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  
  OnMouseLeftButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGrid,e: MouseEventArgs)
   Updates the collection of items that are selected due to the user dragging the 
    mouse in the System.Windows.Controls.DataGrid.
  
  
   e: The mouse data.
  """
  pass
 def OnMouseRightButtonDown(self,*args):
  """
  OnMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  
  OnMouseRightButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseRightButtonUp(self,*args):
  """
  OnMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  
  OnMouseRightButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the mouse button was released.
  
  OnMouseUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: UIElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  OnMouseWheel(self: Window_16$17,e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18,e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19,e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20,e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21,e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23,e: MouseWheelEventArgs)
  """
  pass
 def OnPreparingCellForEdit(self,*args):
  """
  OnPreparingCellForEdit(self: DataGrid,e: DataGridPreparingCellForEditEventArgs)
   Raises the System.Windows.Controls.DataGrid.PreparingCellForEdit event.
  
   e: The data for the event.
  """
  pass
 def OnPreviewDragEnter(self,*args):
  """
  OnPreviewDragEnter(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragEnter(self: Window_16$17,e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18,e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20,e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDragLeave(self,*args):
  """
  OnPreviewDragLeave(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragLeave(self: Window_16$17,e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18,e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20,e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDragOver(self,*args):
  """
  OnPreviewDragOver(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragOver(self: Window_16$17,e: DragEventArgs)OnPreviewDragOver(self: Label_17$18,e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragOver(self: Button_19$20,e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDrop(self,*args):
  """
  OnPreviewDrop(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDrop(self: Window_16$17,e: DragEventArgs)OnPreviewDrop(self: Label_17$18,e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19,e: DragEventArgs)OnPreviewDrop(self: Button_19$20,e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDrop(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewGiveFeedback(self,*args):
  """
  OnPreviewGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  OnPreviewGiveFeedback(self: Window_16$17,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23,e: GiveFeedbackEventArgs)
  """
  pass
 def OnPreviewGotKeyboardFocus(self,*args):
  """
  OnPreviewGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnPreviewGotKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnPreviewKeyDown(self: Window_16$17,e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18,e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19,e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20,e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21,e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22,e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnPreviewKeyUp(self,*args):
  """
  OnPreviewKeyUp(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnPreviewKeyUp(self: Window_16$17,e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18,e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19,e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20,e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21,e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22,e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnPreviewLostKeyboardFocus(self,*args):
  """
  OnPreviewLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnPreviewLostKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnPreviewMouseDoubleClick(self,*args):
  """
  OnPreviewMouseDoubleClick(self: Control,e: MouseButtonEventArgs)
   Raises the System.Windows.Controls.Control.PreviewMouseDoubleClick routed event.
  
   e: The event data.
  OnPreviewMouseDoubleClick(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseDoubleClick(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseDown(self,*args):
  """
  OnPreviewMouseDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were pressed.
  
  OnPreviewMouseDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseLeftButtonDown(self,*args):
  """
  OnPreviewMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  
  OnPreviewMouseLeftButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseLeftButtonUp(self,*args):
  """
  OnPreviewMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  
  OnPreviewMouseLeftButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseMove(self,*args):
  """
  OnPreviewMouseMove(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnPreviewMouseMove(self: Window_16$17,e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18,e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19,e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20,e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21,e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22,e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnPreviewMouseRightButtonDown(self,*args):
  """
  OnPreviewMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  
  OnPreviewMouseRightButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseRightButtonUp(self,*args):
  """
  OnPreviewMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  
  OnPreviewMouseRightButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseUp(self,*args):
  """
  OnPreviewMouseUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were released.
  
  OnPreviewMouseUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseWheel(self,*args):
  """
  OnPreviewMouseWheel(self: UIElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  OnPreviewMouseWheel(self: Window_16$17,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23,e: MouseWheelEventArgs)
  """
  pass
 def OnPreviewQueryContinueDrag(self,*args):
  """
  OnPreviewQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  OnPreviewQueryContinueDrag(self: Window_16$17,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23,e: QueryContinueDragEventArgs)
  """
  pass
 def OnPreviewStylusButtonDown(self,*args):
  """
  OnPreviewStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnPreviewStylusButtonDown(self: Window_16$17,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnPreviewStylusButtonUp(self,*args):
  """
  OnPreviewStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnPreviewStylusButtonUp(self: Window_16$17,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnPreviewStylusDown(self,*args):
  """
  OnPreviewStylusDown(self: UIElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  OnPreviewStylusDown(self: Window_16$17,e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18,e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19,e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20,e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21,e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22,e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23,e: StylusDownEventArgs)
  """
  pass
 def OnPreviewStylusInAirMove(self,*args):
  """
  OnPreviewStylusInAirMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusInAirMove(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusInRange(self,*args):
  """
  OnPreviewStylusInRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusInRange(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusMove(self,*args):
  """
  OnPreviewStylusMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusMove(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusOutOfRange(self,*args):
  """
  OnPreviewStylusOutOfRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusOutOfRange(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusSystemGesture(self,*args):
  """
  OnPreviewStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
    an element in its route that is derived from this class. Implement this method 
    to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  
  OnPreviewStylusSystemGesture(self: Window_16$17,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23,e: StylusSystemGestureEventArgs)
  """
  pass
 def OnPreviewStylusUp(self,*args):
  """
  OnPreviewStylusUp(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusUp(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewTextInput(self,*args):
  """
  OnPreviewTextInput(self: UIElement,e: TextCompositionEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  OnPreviewTextInput(self: Window_16$17,e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18,e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19,e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20,e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21,e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22,e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23,e: TextCompositionEventArgs)
  """
  pass
 def OnPreviewTouchDown(self,*args):
  """
  OnPreviewTouchDown(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
    routed event that occurs when a touch presses this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchDown(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnPreviewTouchMove(self,*args):
  """
  OnPreviewTouchMove(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
    routed event that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchMove(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnPreviewTouchUp(self,*args):
  """
  OnPreviewTouchUp(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
    event that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchUp(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: FrameworkElement,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.FrameworkElement has been updated. The specific dependency 
    property that changed is reported in the arguments parameter. Overrides 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs).
  
  
   e: The event data that describes the property that changed,as well as old and new 
    values.
  
  OnPropertyChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  OnQueryContinueDrag(self: Window_16$17,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23,e: QueryContinueDragEventArgs)
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: UIElement,e: QueryCursorEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
  OnQueryCursor(self: Window_16$17,e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18,e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19,e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20,e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21,e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22,e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23,e: QueryCursorEventArgs)
  """
  pass
 def OnRender(self,*args):
  """
  OnRender(self: UIElement,drawingContext: DrawingContext)
   When overridden in a derived class,participates in rendering operations that 
    are directed by the layout system. The rendering instructions for this element 
    are not used directly when this method is invoked,and are instead preserved 
    for later asynchronous use by layout and drawing.
  
  
   drawingContext: The drawing instructions for a specific element. This context is provided to 
    the layout system.
  
  OnRender(self: Window_16$17,drawingContext: DrawingContext)OnRender(self: Label_17$18,drawingContext: DrawingContext)OnRender(self: TextBox_18$19,drawingContext: DrawingContext)OnRender(self: Button_19$20,drawingContext: DrawingContext)OnRender(self: CheckBox_20$21,drawingContext: DrawingContext)OnRender(self: ComboBox_21$22,drawingContext: DrawingContext)OnRender(self: Separator_22$23,drawingContext: DrawingContext)
  """
  pass
 def OnRenderSizeChanged(self,*args):
  """
  OnRenderSizeChanged(self: FrameworkElement,sizeInfo: SizeChangedInfo)
   Raises the System.Windows.FrameworkElement.SizeChanged event,using the 
    specified information as part of the eventual event data.
  
  
   sizeInfo: Details of the old and new size involved in the change.
  OnRenderSizeChanged(self: Window_16$17,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23,sizeInfo: SizeChangedInfo)
  """
  pass
 def OnRowDetailsVisibilityChanged(self,*args):
  """
  OnRowDetailsVisibilityChanged(self: DataGrid,e: DataGridRowDetailsEventArgs)
   Raises the System.Windows.Controls.DataGrid.RowDetailsVisibilityChanged event.
  
   e: The data for the event.
  """
  pass
 def OnRowEditEnding(self,*args):
  """
  OnRowEditEnding(self: DataGrid,e: DataGridRowEditEndingEventArgs)
   Raises the System.Windows.Controls.DataGrid.RowEditEnding event.
  
   e: The data for the event.
  """
  pass
 def OnSelectedCellsChanged(self,*args):
  """
  OnSelectedCellsChanged(self: DataGrid,e: SelectedCellsChangedEventArgs)
   Raises the System.Windows.Controls.DataGrid.SelectedCellsChanged event.
  
   e: The data for the event.
  """
  pass
 def OnSelectionChanged(self,*args):
  """
  OnSelectionChanged(self: DataGrid,e: SelectionChangedEventArgs)
   Invoked when the selection changes.
  
   e: The data for the event.
  """
  pass
 def OnSorting(self,*args):
  """
  OnSorting(self: DataGrid,eventArgs: DataGridSortingEventArgs)
   Raises the System.Windows.Controls.DataGrid.Sorting event.
  
   eventArgs: The data for the event.
  """
  pass
 def OnStyleChanged(self,*args):
  """
  OnStyleChanged(self: FrameworkElement,oldStyle: Style,newStyle: Style)
   Invoked when the style in use on this element changes,which will invalidate 
    the layout.
  
  
   oldStyle: The old style.
   newStyle: The new style.
  OnStyleChanged(self: Window_16$17,oldStyle: Style,newStyle: Style)OnStyleChanged(self: Label_17$18,oldStyle: Style,newStyle: Style)OnStyleChanged(self: TextBox_18$19,oldStyle: Style,newStyle: Style)OnStyleChanged(self: Button_19$20,oldStyle: Style,newStyle: Style)OnStyleChanged(self: CheckBox_20$21,oldStyle: Style,newStyle: Style)OnStyleChanged(self: ComboBox_21$22,oldStyle: Style,newStyle: Style)OnStyleChanged(self: Separator_22$23,oldStyle: Style,newStyle: Style)
  """
  pass
 def OnStylusButtonDown(self,*args):
  """
  OnStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnStylusButtonDown(self: Window_16$17,e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18,e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19,e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20,e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21,e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22,e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnStylusButtonUp(self,*args):
  """
  OnStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnStylusButtonUp(self: Window_16$17,e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18,e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19,e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20,e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21,e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22,e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnStylusDown(self,*args):
  """
  OnStylusDown(self: UIElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  OnStylusDown(self: Window_16$17,e: StylusDownEventArgs)OnStylusDown(self: Label_17$18,e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19,e: StylusDownEventArgs)OnStylusDown(self: Button_19$20,e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21,e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22,e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23,e: StylusDownEventArgs)
  """
  pass
 def OnStylusEnter(self,*args):
  """
  OnStylusEnter(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusEnter(self: Window_16$17,e: StylusEventArgs)OnStylusEnter(self: Label_17$18,e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19,e: StylusEventArgs)OnStylusEnter(self: Button_19$20,e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21,e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22,e: StylusEventArgs)OnStylusEnter(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusInAirMove(self,*args):
  """
  OnStylusInAirMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusInAirMove(self: Window_16$17,e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18,e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19,e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20,e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21,e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22,e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusInRange(self,*args):
  """
  OnStylusInRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusInRange(self: Window_16$17,e: StylusEventArgs)OnStylusInRange(self: Label_17$18,e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19,e: StylusEventArgs)OnStylusInRange(self: Button_19$20,e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21,e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22,e: StylusEventArgs)OnStylusInRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusLeave(self,*args):
  """
  OnStylusLeave(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusLeave(self: Window_16$17,e: StylusEventArgs)OnStylusLeave(self: Label_17$18,e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19,e: StylusEventArgs)OnStylusLeave(self: Button_19$20,e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21,e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22,e: StylusEventArgs)OnStylusLeave(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusMove(self,*args):
  """
  OnStylusMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusMove(self: Window_16$17,e: StylusEventArgs)OnStylusMove(self: Label_17$18,e: StylusEventArgs)OnStylusMove(self: TextBox_18$19,e: StylusEventArgs)OnStylusMove(self: Button_19$20,e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21,e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22,e: StylusEventArgs)OnStylusMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusOutOfRange(self,*args):
  """
  OnStylusOutOfRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusOutOfRange(self: Window_16$17,e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18,e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19,e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20,e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21,e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22,e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusSystemGesture(self,*args):
  """
  OnStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  
  OnStylusSystemGesture(self: Window_16$17,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23,e: StylusSystemGestureEventArgs)
  """
  pass
 def OnStylusUp(self,*args):
  """
  OnStylusUp(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusUp(self: Window_16$17,e: StylusEventArgs)OnStylusUp(self: Label_17$18,e: StylusEventArgs)OnStylusUp(self: TextBox_18$19,e: StylusEventArgs)OnStylusUp(self: Button_19$20,e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21,e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22,e: StylusEventArgs)OnStylusUp(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnTemplateChanged(self,*args):
  """
  OnTemplateChanged(self: DataGrid,oldTemplate: ControlTemplate,newTemplate: ControlTemplate)
   Called whenever the template of the System.Windows.Controls.DataGrid changes.
  
   oldTemplate: The old template.
   newTemplate: The new template.
  """
  pass
 def OnTextInput(self,*args):
  """ OnTextInput(self: DataGrid,e: TextCompositionEventArgs) """
  pass
 def OnToolTipClosing(self,*args):
  """
  OnToolTipClosing(self: FrameworkElement,e: ToolTipEventArgs)
   Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
    routed event reaches this class in its route. Implement this method to add 
    class handling for this event.
  
  
   e: Provides data about the event.
  OnToolTipClosing(self: Window_16$17,e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18,e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19,e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20,e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21,e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22,e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23,e: ToolTipEventArgs)
  """
  pass
 def OnToolTipOpening(self,*args):
  """
  OnToolTipOpening(self: FrameworkElement,e: ToolTipEventArgs)
   Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
    event reaches this class in its route. Implement this method to add class 
    handling for this event.
  
  
   e: Provides data about the event.
  OnToolTipOpening(self: Window_16$17,e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18,e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19,e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20,e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21,e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22,e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23,e: ToolTipEventArgs)
  """
  pass
 def OnTouchDown(self,*args):
  """
  OnTouchDown(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchDown routed event 
    that occurs when a touch presses inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchDown(self: Window_16$17,e: TouchEventArgs)OnTouchDown(self: Label_17$18,e: TouchEventArgs)OnTouchDown(self: TextBox_18$19,e: TouchEventArgs)OnTouchDown(self: Button_19$20,e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21,e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22,e: TouchEventArgs)OnTouchDown(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchEnter(self,*args):
  """
  OnTouchEnter(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchEnter routed 
    event that occurs when a touch moves from outside to inside the bounds of this 
    element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchEnter(self: Window_16$17,e: TouchEventArgs)OnTouchEnter(self: Label_17$18,e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19,e: TouchEventArgs)OnTouchEnter(self: Button_19$20,e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21,e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22,e: TouchEventArgs)OnTouchEnter(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchLeave(self,*args):
  """
  OnTouchLeave(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchLeave routed 
    event that occurs when a touch moves from inside to outside the bounds of this 
    System.Windows.UIElement.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchLeave(self: Window_16$17,e: TouchEventArgs)OnTouchLeave(self: Label_17$18,e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19,e: TouchEventArgs)OnTouchLeave(self: Button_19$20,e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21,e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22,e: TouchEventArgs)OnTouchLeave(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchMove(self,*args):
  """
  OnTouchMove(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchMove routed event 
    that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchMove(self: Window_16$17,e: TouchEventArgs)OnTouchMove(self: Label_17$18,e: TouchEventArgs)OnTouchMove(self: TextBox_18$19,e: TouchEventArgs)OnTouchMove(self: Button_19$20,e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21,e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22,e: TouchEventArgs)OnTouchMove(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchUp(self,*args):
  """
  OnTouchUp(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchUp routed event 
    that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchUp(self: Window_16$17,e: TouchEventArgs)OnTouchUp(self: Label_17$18,e: TouchEventArgs)OnTouchUp(self: TextBox_18$19,e: TouchEventArgs)OnTouchUp(self: Button_19$20,e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21,e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22,e: TouchEventArgs)OnTouchUp(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnUnloadingRow(self,*args):
  """
  OnUnloadingRow(self: DataGrid,e: DataGridRowEventArgs)
   Raises the System.Windows.Controls.DataGrid.UnloadingRow event.
  
   e: The data for the event.
  """
  pass
 def OnUnloadingRowDetails(self,*args):
  """
  OnUnloadingRowDetails(self: DataGrid,e: DataGridRowDetailsEventArgs)
   Raises the System.Windows.Controls.DataGrid.UnloadingRowDetails event.
  
   e: The data for the event.
  """
  pass
 def OnVisualChildrenChanged(self,*args):
  """
  OnVisualChildrenChanged(self: Visual,visualAdded: DependencyObject,visualRemoved: DependencyObject)
   Called when the System.Windows.Media.VisualCollection of the visual object is 
    modified.
  
  
   visualAdded: The System.Windows.Media.Visual that was added to the collection
   visualRemoved: The System.Windows.Media.Visual that was removed from the collection
  OnVisualChildrenChanged(self: Window_16$17,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23,visualAdded: DependencyObject,visualRemoved: DependencyObject)
  """
  pass
 def OnVisualParentChanged(self,*args):
  """
  OnVisualParentChanged(self: FrameworkElement,oldParent: DependencyObject)
   Invoked when the parent of this element in the visual tree is changed. 
    Overrides 
    System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
  
  
   oldParent: The old parent element. May be null to indicate that the element did not have a 
    visual parent previously.
  
  OnVisualParentChanged(self: Window_16$17,oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18,oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19,oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20,oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21,oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22,oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23,oldParent: DependencyObject)
  """
  pass
 def ParentLayoutInvalidated(self,*args):
  """
  ParentLayoutInvalidated(self: FrameworkElement,child: UIElement)
   Supports incremental layout implementations in specialized subclasses of 
    System.Windows.FrameworkElement. 
    System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
    )  is invoked when a child element has invalidated a property that is marked in 
    metadata as affecting the parent's measure or arrange passes during layout.
  
  
   child: The child element reporting the change.
  ParentLayoutInvalidated(self: Window_16$17,child: UIElement)ParentLayoutInvalidated(self: Label_17$18,child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19,child: UIElement)ParentLayoutInvalidated(self: Button_19$20,child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21,child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22,child: UIElement)ParentLayoutInvalidated(self: Separator_22$23,child: UIElement)
  """
  pass
 def PrepareContainerForItemOverride(self,*args):
  """
  PrepareContainerForItemOverride(self: DataGrid,element: DependencyObject,item: object)
   Prepares a new row for the specified item.
  
   element: The new System.Windows.Controls.DataGridRow.
   item: The data item that the row contains.
  """
  pass
 def RemoveLogicalChild(self,*args):
  """
  RemoveLogicalChild(self: FrameworkElement,child: object)
   Removes the provided object from this element's logical tree. 
    System.Windows.FrameworkElement updates the affected logical tree parent 
    pointers to keep in sync with this deletion.
  
  
   child: The element to remove.
  RemoveLogicalChild(self: Window_16$17,child: object)RemoveLogicalChild(self: Label_17$18,child: object)RemoveLogicalChild(self: TextBox_18$19,child: object)RemoveLogicalChild(self: Button_19$20,child: object)RemoveLogicalChild(self: CheckBox_20$21,child: object)RemoveLogicalChild(self: ComboBox_21$22,child: object)RemoveLogicalChild(self: Separator_22$23,child: object)
  """
  pass
 def RemoveVisualChild(self,*args):
  """
  RemoveVisualChild(self: Visual,child: Visual)
   Removes the parent-child relationship between two visuals.
  
   child: The child visual object to remove from the parent visual.
  RemoveVisualChild(self: Window_16$17,child: Window_16$17)RemoveVisualChild(self: Label_17$18,child: Label_17$18)RemoveVisualChild(self: TextBox_18$19,child: TextBox_18$19)RemoveVisualChild(self: Button_19$20,child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def ScrollIntoView(self,item,column=None):
  """
  ScrollIntoView(self: DataGrid,item: object,column: DataGridColumn)
   Scrolls the System.Windows.Controls.DataGrid vertically and horizontally to 
    display a cell for the specified data item and column.
  
  
   item: The data item to bring into view.
   column: The column to bring into view.
  ScrollIntoView(self: DataGrid,item: object)
   Scrolls the System.Windows.Controls.DataGrid vertically to display the row for 
    the specified data item.
  
  
   item: The data item to bring into view.
  """
  pass
 def SelectAllCells(self):
  """
  SelectAllCells(self: DataGrid)
   Selects all the cells in the System.Windows.Controls.DataGrid.
  """
  pass
 def SetDetailsVisibilityForItem(self,item,detailsVisibility):
  """
  SetDetailsVisibilityForItem(self: DataGrid,item: object,detailsVisibility: Visibility)
   Sets the value of the System.Windows.Controls.DataGridRow.DetailsVisibility 
    property for the System.Windows.Controls.DataGridRow that contains the 
    specified object.
  
  
   item: The object in the row for which 
    System.Windows.Controls.DataGridRow.DetailsVisibility is being set.
  
   detailsVisibility: The System.Windows.Visibility to set for the row that contains the item.
  """
  pass
 def ShouldApplyItemContainerStyle(self,*args):
  """
  ShouldApplyItemContainerStyle(self: ItemsControl,container: DependencyObject,item: object) -> bool
  
   Returns a value that indicates whether to apply the style from the 
    System.Windows.Controls.ItemsControl.ItemContainerStyle or 
    System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property to the 
    container element of the specified item.
  
  
   container: The container element.
   item: The item of interest.
   Returns: Always true for the base implementation.
  ShouldApplyItemContainerStyle(self: ComboBox_21$22,container: DependencyObject,item: object) -> bool
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def UnselectAllCells(self):
  """
  UnselectAllCells(self: DataGrid)
   Unselects all the cells in the System.Windows.Controls.DataGrid.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AlternatingRowBackground=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background brush for use on alternating rows.

Get: AlternatingRowBackground(self: DataGrid) -> Brush

Set: AlternatingRowBackground(self: DataGrid)=value
"""

 AreRowDetailsFrozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the row details can scroll horizontally.

Get: AreRowDetailsFrozen(self: DataGrid) -> bool

Set: AreRowDetailsFrozen(self: DataGrid)=value
"""

 AutoGenerateColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the columns are created automatically.

Get: AutoGenerateColumns(self: DataGrid) -> bool

Set: AutoGenerateColumns(self: DataGrid)=value
"""

 CanSelectMultipleItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the multiple items in the System.Windows.Controls.Primitives.MultiSelector can be selected at a time.

"""

 CanUserAddRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can add new rows to the System.Windows.Controls.DataGrid.

Get: CanUserAddRows(self: DataGrid) -> bool

Set: CanUserAddRows(self: DataGrid)=value
"""

 CanUserDeleteRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can delete rows from the System.Windows.Controls.DataGrid.

Get: CanUserDeleteRows(self: DataGrid) -> bool

Set: CanUserDeleteRows(self: DataGrid)=value
"""

 CanUserReorderColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can change the column display order by dragging column headers with the mouse.

Get: CanUserReorderColumns(self: DataGrid) -> bool

Set: CanUserReorderColumns(self: DataGrid)=value
"""

 CanUserResizeColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can adjust the width of columns by using the mouse.

Get: CanUserResizeColumns(self: DataGrid) -> bool

Set: CanUserResizeColumns(self: DataGrid)=value
"""

 CanUserResizeRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can adjust the height of rows by using the mouse.

Get: CanUserResizeRows(self: DataGrid) -> bool

Set: CanUserResizeRows(self: DataGrid)=value
"""

 CanUserSortColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can sort columns by clicking the column header.

Get: CanUserSortColumns(self: DataGrid) -> bool

Set: CanUserSortColumns(self: DataGrid)=value
"""

 CellsPanelHorizontalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal offset for the System.Windows.Controls.DataGridCellsPanel.

Get: CellsPanelHorizontalOffset(self: DataGrid) -> float

"""

 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style applied to all cells in the System.Windows.Controls.DataGrid.

Get: CellStyle(self: DataGrid) -> Style

Set: CellStyle(self: DataGrid)=value
"""

 ClipboardCopyMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how content is copied to the clipboard.

Get: ClipboardCopyMode(self: DataGrid) -> DataGridClipboardCopyMode

Set: ClipboardCopyMode(self: DataGrid)=value
"""

 ColumnHeaderHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the column headers row.

Get: ColumnHeaderHeight(self: DataGrid) -> float

Set: ColumnHeaderHeight(self: DataGrid)=value
"""

 ColumnHeaderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style applied to all column headers in the System.Windows.Controls.DataGrid.

Get: ColumnHeaderStyle(self: DataGrid) -> Style

Set: ColumnHeaderStyle(self: DataGrid)=value
"""

 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection that contains all the columns in the System.Windows.Controls.DataGrid.

Get: Columns(self: DataGrid) -> ObservableCollection[DataGridColumn]

"""

 ColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the standard width and sizing mode of columns and headers in the System.Windows.Controls.DataGrid.

Get: ColumnWidth(self: DataGrid) -> DataGridLength

Set: ColumnWidth(self: DataGrid)=value
"""

 CurrentCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cell that has focus.

Get: CurrentCell(self: DataGrid) -> DataGridCellInfo

Set: CurrentCell(self: DataGrid)=value
"""

 CurrentColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column that contains the current cell.

Get: CurrentColumn(self: DataGrid) -> DataGridColumn

Set: CurrentColumn(self: DataGrid)=value
"""

 CurrentItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data item bound to the row that contains the current cell.

Get: CurrentItem(self: DataGrid) -> object

Set: CurrentItem(self: DataGrid)=value
"""

 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key to use to reference the style for this control,when theme styles are used or defined.

"""

 DragIndicatorStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the drag indicator that is displayed while dragging a column header.

Get: DragIndicatorStyle(self: DataGrid) -> Style

Set: DragIndicatorStyle(self: DataGrid)=value
"""

 DropLocationIndicatorStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is applied to indicate the drop location when dragging a column header.

Get: DropLocationIndicatorStyle(self: DataGrid) -> Style

Set: DropLocationIndicatorStyle(self: DataGrid)=value
"""

 EnableColumnVirtualization=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether column virtualization is enabled.

Get: EnableColumnVirtualization(self: DataGrid) -> bool

Set: EnableColumnVirtualization(self: DataGrid)=value
"""

 EnableRowVirtualization=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether row virtualization is enabled.

Get: EnableRowVirtualization(self: DataGrid) -> bool

Set: EnableRowVirtualization(self: DataGrid)=value
"""

 FrozenColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of non-scrolling columns.

Get: FrozenColumnCount(self: DataGrid) -> int

Set: FrozenColumnCount(self: DataGrid)=value
"""

 GridLinesVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates which grid lines are shown.

Get: GridLinesVisibility(self: DataGrid) -> DataGridGridLinesVisibility

Set: GridLinesVisibility(self: DataGrid)=value
"""

 HandlesScrolling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Controls.DataGrid supports custom keyboard scrolling.

"""

 HasEffectiveKeyboardFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)

 HeadersVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value that specifies the visibility of the row and column headers.

Get: HeadersVisibility(self: DataGrid) -> DataGridHeadersVisibility

Set: HeadersVisibility(self: DataGrid)=value
"""

 HorizontalGridLinesBrush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush that is used to draw the horizontal grid lines.

Get: HorizontalGridLinesBrush(self: DataGrid) -> Brush

Set: HorizontalGridLinesBrush(self: DataGrid)=value
"""

 HorizontalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how horizontal scroll bars are displayed in the System.Windows.Controls.DataGrid.

Get: HorizontalScrollBarVisibility(self: DataGrid) -> ScrollBarVisibility

Set: HorizontalScrollBarVisibility(self: DataGrid)=value
"""

 InheritanceBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scope limits for property value inheritance,resource key lookup,and RelativeSource FindAncestor lookup.

"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the user can edit values in the System.Windows.Controls.DataGrid.

Get: IsReadOnly(self: DataGrid) -> bool

Set: IsReadOnly(self: DataGrid)=value
"""

 IsUpdatingSelectedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Controls.Primitives.MultiSelector is currently performing a bulk update to the System.Windows.Controls.Primitives.MultiSelector.SelectedItems collection.

"""

 LogicalChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an enumerator for the logical child objects of the System.Windows.Controls.ItemsControl object.

"""

 MaxColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum width constraint of the columns and headers in the System.Windows.Controls.DataGrid.

Get: MaxColumnWidth(self: DataGrid) -> float

Set: MaxColumnWidth(self: DataGrid)=value
"""

 MinColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum width constraint of the columns and headers in the System.Windows.Controls.DataGrid.

Get: MinColumnWidth(self: DataGrid) -> float

Set: MinColumnWidth(self: DataGrid)=value
"""

 MinRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum height constraint of the rows and headers in the System.Windows.Controls.DataGrid.

Get: MinRowHeight(self: DataGrid) -> float

Set: MinRowHeight(self: DataGrid)=value
"""

 NewItemMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewItemMargin(self: DataGrid) -> Thickness

"""

 NonFrozenColumnsViewportHorizontalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal offset of the scrollable columns in the view port.

Get: NonFrozenColumnsViewportHorizontalOffset(self: DataGrid) -> float

"""

 RowBackground=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default brush for the row background.

Get: RowBackground(self: DataGrid) -> Brush

Set: RowBackground(self: DataGrid)=value
"""

 RowDetailsTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template that is used to display the row details.

Get: RowDetailsTemplate(self: DataGrid) -> DataTemplate

Set: RowDetailsTemplate(self: DataGrid)=value
"""

 RowDetailsTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template selector that is used for the row details.

Get: RowDetailsTemplateSelector(self: DataGrid) -> DataTemplateSelector

Set: RowDetailsTemplateSelector(self: DataGrid)=value
"""

 RowDetailsVisibilityMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates when the details section of a row is displayed.

Get: RowDetailsVisibilityMode(self: DataGrid) -> DataGridRowDetailsVisibilityMode

Set: RowDetailsVisibilityMode(self: DataGrid)=value
"""

 RowHeaderActualWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rendered width of the row headers column.

Get: RowHeaderActualWidth(self: DataGrid) -> float

"""

 RowHeaderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style applied to all row headers.

Get: RowHeaderStyle(self: DataGrid) -> Style

Set: RowHeaderStyle(self: DataGrid)=value
"""

 RowHeaderTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or set the template for the row headers.

Get: RowHeaderTemplate(self: DataGrid) -> DataTemplate

Set: RowHeaderTemplate(self: DataGrid)=value
"""

 RowHeaderTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template selector for row headers.

Get: RowHeaderTemplateSelector(self: DataGrid) -> DataTemplateSelector

Set: RowHeaderTemplateSelector(self: DataGrid)=value
"""

 RowHeaderWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the row header column.

Get: RowHeaderWidth(self: DataGrid) -> float

Set: RowHeaderWidth(self: DataGrid)=value
"""

 RowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the suggested height for all rows.

Get: RowHeight(self: DataGrid) -> float

Set: RowHeight(self: DataGrid)=value
"""

 RowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style applied to all rows.

Get: RowStyle(self: DataGrid) -> Style

Set: RowStyle(self: DataGrid)=value
"""

 RowStyleSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style selector for the rows.

Get: RowStyleSelector(self: DataGrid) -> StyleSelector

Set: RowStyleSelector(self: DataGrid)=value
"""

 RowValidationErrorTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template that is used to visually indicate an error in row validation.

Get: RowValidationErrorTemplate(self: DataGrid) -> ControlTemplate

Set: RowValidationErrorTemplate(self: DataGrid)=value
"""

 RowValidationRules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rules that are used to validate the data in each row.

Get: RowValidationRules(self: DataGrid) -> ObservableCollection[ValidationRule]

"""

 SelectedCells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of cells that are currently selected.

Get: SelectedCells(self: DataGrid) -> IList[DataGridCellInfo]

"""

 SelectionMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how rows and cells are selected in the System.Windows.Controls.DataGrid.

Get: SelectionMode(self: DataGrid) -> DataGridSelectionMode

Set: SelectionMode(self: DataGrid)=value
"""

 SelectionUnit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether rows,cells,or both can be selected in the System.Windows.Controls.DataGrid.

Get: SelectionUnit(self: DataGrid) -> DataGridSelectionUnit

Set: SelectionUnit(self: DataGrid)=value
"""

 StylusPlugIns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

 VerticalGridLinesBrush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush that is used to draw the vertical grid lines.

Get: VerticalGridLinesBrush(self: DataGrid) -> Brush

Set: VerticalGridLinesBrush(self: DataGrid)=value
"""

 VerticalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how vertical scroll bars are displayed in the System.Windows.Controls.DataGrid.

Get: VerticalScrollBarVisibility(self: DataGrid) -> ScrollBarVisibility

Set: VerticalScrollBarVisibility(self: DataGrid)=value
"""

 VisualBitmapEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

 VisualBitmapEffectInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

 VisualBitmapScalingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

 VisualCacheMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

 VisualChildrenCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of visual child elements within this element.

"""

 VisualClearTypeHint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

 VisualClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

 VisualEdgeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

 VisualEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

 VisualOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the offset value of the visual object.

"""

 VisualOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

 VisualOpacityMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

 VisualParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the visual tree parent of the visual object.

"""

 VisualScrollableAreaClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

 VisualTextHintingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

 VisualTextRenderingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

 VisualTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

 VisualXSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate (vertical) guideline collection.

"""

 VisualYSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


 AddingNewItem=None
 AlternatingRowBackgroundProperty=None
 AreRowDetailsFrozenProperty=None
 AutoGenerateColumnsProperty=None
 AutoGeneratedColumns=None
 AutoGeneratingColumn=None
 BeginEditCommand=None
 BeginningEdit=None
 CancelEditCommand=None
 CanUserAddRowsProperty=None
 CanUserDeleteRowsProperty=None
 CanUserReorderColumnsProperty=None
 CanUserResizeColumnsProperty=None
 CanUserResizeRowsProperty=None
 CanUserSortColumnsProperty=None
 CellEditEnding=None
 CellsPanelHorizontalOffsetProperty=None
 CellStyleProperty=None
 ClipboardCopyModeProperty=None
 ColumnDisplayIndexChanged=None
 ColumnHeaderDragCompleted=None
 ColumnHeaderDragDelta=None
 ColumnHeaderDragStarted=None
 ColumnHeaderHeightProperty=None
 ColumnHeaderStyleProperty=None
 ColumnReordered=None
 ColumnReordering=None
 ColumnWidthProperty=None
 CommitEditCommand=None
 CopyingRowClipboardContent=None
 CurrentCellChanged=None
 CurrentCellProperty=None
 CurrentColumnProperty=None
 CurrentItemProperty=None
 DeleteCommand=None
 DragIndicatorStyleProperty=None
 DropLocationIndicatorStyleProperty=None
 EnableColumnVirtualizationProperty=None
 EnableRowVirtualizationProperty=None
 FocusBorderBrushKey=None
 FrozenColumnCountProperty=None
 GridLinesVisibilityProperty=None
 HeadersVisibilityConverter=None
 HeadersVisibilityProperty=None
 HorizontalGridLinesBrushProperty=None
 HorizontalScrollBarVisibilityProperty=None
 InitializingNewItem=None
 IsReadOnlyProperty=None
 LoadingRow=None
 LoadingRowDetails=None
 MaxColumnWidthProperty=None
 MinColumnWidthProperty=None
 MinRowHeightProperty=None
 NewItemMarginProperty=None
 NonFrozenColumnsViewportHorizontalOffsetProperty=None
 PreparingCellForEdit=None
 RowBackgroundProperty=None
 RowDetailsScrollingConverter=None
 RowDetailsTemplateProperty=None
 RowDetailsTemplateSelectorProperty=None
 RowDetailsVisibilityChanged=None
 RowDetailsVisibilityModeProperty=None
 RowEditEnding=None
 RowHeaderActualWidthProperty=None
 RowHeaderStyleProperty=None
 RowHeaderTemplateProperty=None
 RowHeaderTemplateSelectorProperty=None
 RowHeaderWidthProperty=None
 RowHeightProperty=None
 RowStyleProperty=None
 RowStyleSelectorProperty=None
 RowValidationErrorTemplateProperty=None
 SelectAllCommand=None
 SelectedCellsChanged=None
 SelectionModeProperty=None
 SelectionUnitProperty=None
 Sorting=None
 UnloadingRow=None
 UnloadingRowDetails=None
 VerticalGridLinesBrushProperty=None
 VerticalScrollBarVisibilityProperty=None


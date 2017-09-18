class DataGrid(MultiSelector,IResource,IAnimatable,IInputElement,IFrameworkInputElement,ISupportInitialize,IHaveResources,IQueryAmbient,IAddChild,IGeneratorHost,IContainItemStorage):
 """
 Represents a control that displays data in a customizable grid.

 

 DataGrid()
 """
 def AddChild(self,*args):
  """
  AddChild(self: ItemsControl,value: object)

   Adds the specified object as the child of the System.Windows.Controls.ItemsControl object.

  

   value: The object to add as a child.
  """
  pass
 def AddLogicalChild(self,*args):
  """
  AddLogicalChild(self: FrameworkElement,child: object)

   Adds the provided object to the logical tree of this element.

  

   child: Child element to be added.
  """
  pass
 def AddText(self,*args):
  """
  AddText(self: ItemsControl,text: str)

   Adds the specified text string to the System.Windows.Controls.ItemsControl object.

  

   text: The string to add.
  """
  pass
 def AddVisualChild(self,*args):
  """
  AddVisualChild(self: Visual,child: Visual)

   Defines the parent-child relationship between two visuals.

  

   child: The child visual object to add to parent visual.
  """
  pass
 def ArrangeCore(self,*args):
  """
  ArrangeCore(self: FrameworkElement,finalRect: Rect)

   Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined as virtual in 

    System.Windows.UIElement) and seals the implementation.

  

  

   finalRect: The final area within the parent that this element should use to arrange itself and its children.
  """
  pass
 def ArrangeOverride(self,*args):
  """
  ArrangeOverride(self: Control,arrangeBounds: Size) -> Size

  

   Called to arrange and size the content of a System.Windows.Controls.Control object.

  

   arrangeBounds: The computed size that is used to arrange the content.

   Returns: The size of the control.
  """
  pass
 def BeginEdit(self,editingEventArgs=None):
  """
  BeginEdit(self: DataGrid,editingEventArgs: RoutedEventArgs) -> bool

  

   Invokes the System.Windows.Controls.DataGrid.BeginEdit command,which will place the current 

    cell or row into edit mode.

  

  

   editingEventArgs: If called from an event handler,the event arguments. May be null.

   Returns: true if the current cell or row enters edit mode; otherwise,false.

  BeginEdit(self: DataGrid) -> bool

  

   Invokes the System.Windows.Controls.DataGrid.BeginEdit command,which will place the current 

    cell or row into edit mode.

  

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

  

   Invokes the System.Windows.Controls.DataGrid.CancelEditCommand command for the specified cell or 

    row in edit mode.

  

  

   editingUnit: One of the enumeration values that specifies whether to cancel row or cell edits.

   Returns: true if the current cell or row exits edit mode; otherwise,false.

  CancelEdit(self: DataGrid) -> bool

  

   Invokes the System.Windows.Controls.DataGrid.CancelEditCommand command for the cell or row 

    currently in edit mode.

  

   Returns: true if the current cell or row exits edit mode,or if no cells or rows are in edit mode; 

    otherwise,false.
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

   Clears the System.Windows.Controls.DataGridRow.DetailsVisibility property for the 

    System.Windows.Controls.DataGridRow that represents the specified data item.

  

  

   item: The data item in the row for which System.Windows.Controls.DataGridRow.DetailsVisibility is 

    cleared.
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

  

   Invokes the System.Windows.Controls.DataGrid.CommitEditCommand command for the specified cell or 

    row currently in edit mode.

  

  

   editingUnit: One of the enumeration values that specifies whether to commit row or cell edits.

   exitEditingMode: true to exit edit mode; otherwise,false.

   Returns: true if the current cell or row exits edit mode; otherwise,false.

  CommitEdit(self: DataGrid) -> bool

  

   Invokes the System.Windows.Controls.DataGrid.CommitEditCommand command for the cell or row 

    currently in edit mode.

  

   Returns: true if the current cell or row exits edit mode,or if no cells or rows are in edit mode; 

    otherwise,false.
  """
  pass
 def EndUpdateSelectedItems(self,*args):
  """
  EndUpdateSelectedItems(self: MultiSelector)

   Commits the selected items to the System.Windows.Controls.Primitives.MultiSelector.
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

  

  

   item: The data item in the row for which System.Windows.Controls.DataGridRow.DetailsVisibility is 

    returned.

  

   Returns: The visibility for the row that contains the item.
  """
  pass
 def GetLayoutClip(self,*args):
  """
  GetLayoutClip(self: FrameworkElement,layoutSlotSize: Size) -> Geometry

  

   Returns a geometry for a clipping mask. The mask applies if the layout system attempts to 

    arrange an element that is larger than the available display space.

  

  

   layoutSlotSize: The size of the part of the element that does visual presentation.

   Returns: The clipping geometry.
  """
  pass
 def GetTemplateChild(self,*args):
  """
  GetTemplateChild(self: FrameworkElement,childName: str) -> DependencyObject

  

   Returns the named element in the visual tree of an instantiated 

    System.Windows.Controls.ControlTemplate.

  

  

   childName: Name of the child to find.

   Returns: The requested element. May be null if no element of the requested name exists.
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: FrameworkElement) -> DependencyObject

  

   Returns an alternative logical parent for this element if there is no visual parent.

   Returns: Returns something other than null whenever a WPF framework-level implementation of this method 

    has a non-visual parent connection.
  """
  pass
 def GetVisualChild(self,*args):
  """
  GetVisualChild(self: FrameworkElement,index: int) -> Visual

  

   Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32),and returns a child at the 

    specified index from a collection of child elements.

  

  

   index: The zero-based index of the requested child element in the collection.

   Returns: The requested child element. This should not return null; if the provided index is out of range,

    an exception is thrown.
  """
  pass
 def HitTestCore(self,*args):
  """
  HitTestCore(self: UIElement,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult

  

   Implements 

    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestParameters) to 

    supply base element hit testing behavior (returning System.Windows.Media.GeometryHitTestResult).

  

  

   hitTestParameters: Describes the hit test to perform,including the initial hit point.

   Returns: Results of the test,including the evaluated geometry.

  HitTestCore(self: UIElement,hitTestParameters: PointHitTestParameters) -> HitTestResult

  

   Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParameters) 

    to supply base element hit testing behavior (returning System.Windows.Media.HitTestResult).

  

  

   hitTestParameters: Describes the hit test to perform,including the initial hit point.

   Returns: Results of the test,including the evaluated point.
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

  

   Implements basic measure-pass layout system behavior for System.Windows.FrameworkElement.

  

   availableSize: The available size that the parent element can give to the child elements.

   Returns: The desired size of this element in layout.
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

   Provides class handling for when an access key that is meaningful for this element is invoked.

  

   e: The event data to the access key event. The event data reports which key was invoked,and 

    indicate whether the System.Windows.Input.AccessKeyManager object that controls the sending of 

    these events also sent this access key invocation to other elements.
  """
  pass
 def OnAddingNewItem(self,*args):
  """ OnAddingNewItem(self: DataGrid,e: AddingNewItemEventArgs) """
  pass
 def OnAlternationCountChanged(self,*args):
  """
  OnAlternationCountChanged(self: ItemsControl,oldAlternationCount: int,newAlternationCount: int)

   Invoked when the System.Windows.Controls.ItemsControl.AlternationCount property changes.

  

   oldAlternationCount: The old value of System.Windows.Controls.ItemsControl.AlternationCount.

   newAlternationCount: The new value of System.Windows.Controls.ItemsControl.AlternationCount.
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

   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event associated with 

    the System.Windows.Controls.DataGrid.BeginEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnCanExecuteCancelEdit(self,*args):
  """
  OnCanExecuteCancelEdit(self: DataGrid,e: CanExecuteRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event associated with 

    the System.Windows.Controls.DataGrid.CancelEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnCanExecuteCommitEdit(self,*args):
  """
  OnCanExecuteCommitEdit(self: DataGrid,e: CanExecuteRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event associated with 

    the System.Windows.Controls.DataGrid.CommitEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnCanExecuteCopy(self,*args):
  """
  OnCanExecuteCopy(self: DataGrid,args: CanExecuteRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event associated with 

    the System.Windows.Input.ApplicationCommands.Copy command.

  

  

   args: The data for the event.
  """
  pass
 def OnCanExecuteDelete(self,*args):
  """
  OnCanExecuteDelete(self: DataGrid,e: CanExecuteRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.CanExecute event associated with 

    the System.Windows.Controls.DataGrid.DeleteCommand command.

  

  

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

   Invoked whenever an unhandled System.Windows.FrameworkElement.ContextMenuClosing routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
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

   Invoked when the System.Windows.Controls.ItemsControl.DisplayMemberPath property changes.

  

   oldDisplayMemberPath: The old value of the System.Windows.Controls.ItemsControl.DisplayMemberPath property.

   newDisplayMemberPath: New value of the System.Windows.Controls.ItemsControl.DisplayMemberPath property.
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnExecutedBeginEdit(self,*args):
  """
  OnExecutedBeginEdit(self: DataGrid,e: ExecutedRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.Executed event associated with the 

    System.Windows.Controls.DataGrid.BeginEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnExecutedCancelEdit(self,*args):
  """
  OnExecutedCancelEdit(self: DataGrid,e: ExecutedRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.Executed event associated with the 

    System.Windows.Controls.DataGrid.CancelEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnExecutedCommitEdit(self,*args):
  """
  OnExecutedCommitEdit(self: DataGrid,e: ExecutedRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.Executed event associated with the 

    System.Windows.Controls.DataGrid.CommitEditCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnExecutedCopy(self,*args):
  """
  OnExecutedCopy(self: DataGrid,args: ExecutedRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.Executed event associated with the 

    System.Windows.Input.ApplicationCommands.Copy command.

  

  

   args: The data for the event.
  """
  pass
 def OnExecutedDelete(self,*args):
  """
  OnExecutedDelete(self: DataGrid,e: ExecutedRoutedEventArgs)

   Provides handling for the System.Windows.Input.CommandBinding.Executed event associated with the 

    System.Windows.Controls.DataGrid.DeleteCommand command.

  

  

   e: The data for the event.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: FrameworkElement,e: RoutedEventArgs)

   Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches this element in 

    its route.

  

  

   e: The System.Windows.RoutedEventArgs that contains the event data.
  """
  pass
 def OnGotKeyboardFocus(self,*args):
  """
  OnGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
  """
  pass
 def OnGotMouseCapture(self,*args):
  """
  OnGotMouseCapture(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnGotStylusCapture(self,*args):
  """
  OnGotStylusCapture(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnGotTouchCapture(self,*args):
  """
  OnGotTouchCapture(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.GotTouchCapture routed event that 

    occurs when a touch is captured to this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnGroupStyleSelectorChanged(self,*args):
  """
  OnGroupStyleSelectorChanged(self: ItemsControl,oldGroupStyleSelector: GroupStyleSelector,newGroupStyleSelector: GroupStyleSelector)

   Invoked when the System.Windows.Controls.ItemsControl.GroupStyleSelector property changes.

  

   oldGroupStyleSelector: Old value of the System.Windows.Controls.ItemsControl.GroupStyleSelector property.

   newGroupStyleSelector: New value of the System.Windows.Controls.ItemsControl.GroupStyleSelector property.
  """
  pass
 def OnInitialized(self,*args):
  """
  OnInitialized(self: Selector,e: EventArgs)

   Raises the System.Windows.FrameworkElement.Initialized event. This method is invoked whenever 

    System.Windows.FrameworkElement.IsInitialized is set to true internally.

  

  

   e: The System.Windows.RoutedEventArgs that contains the event data.
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

   Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsKeyboardFocusWithinChanged(self,*args):
  """
  OnIsKeyboardFocusWithinChanged(self: Selector,e: DependencyPropertyChangedEventArgs)

   Called when the System.Windows.UIElement.IsKeyboardFocusWithin property has changed.

  

   e: The event data.
  """
  pass
 def OnIsMouseCapturedChanged(self,*args):
  """
  OnIsMouseCapturedChanged(self: DataGrid,e: DependencyPropertyChangedEventArgs)

   Called when the System.Windows.UIElement.IsMouseCaptured property changes on this element.

  

   e: The data for the event.
  """
  pass
 def OnIsMouseCaptureWithinChanged(self,*args):
  """
  OnIsMouseCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsMouseDirectlyOverChanged(self,*args):
  """
  OnIsMouseDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusCapturedChanged(self,*args):
  """
  OnIsStylusCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusCaptureWithinChanged(self,*args):
  """
  OnIsStylusCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusDirectlyOverChanged(self,*args):
  """
  OnIsStylusDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnItemBindingGroupChanged(self,*args):
  """
  OnItemBindingGroupChanged(self: ItemsControl,oldItemBindingGroup: BindingGroup,newItemBindingGroup: BindingGroup)

   Invoked when the System.Windows.Controls.ItemsControl.ItemBindingGroup property changes.

  

   oldItemBindingGroup: The old value of the System.Windows.Controls.ItemsControl.ItemBindingGroup.

   newItemBindingGroup: The new value of the System.Windows.Controls.ItemsControl.ItemBindingGroup.
  """
  pass
 def OnItemContainerStyleChanged(self,*args):
  """
  OnItemContainerStyleChanged(self: ItemsControl,oldItemContainerStyle: Style,newItemContainerStyle: Style)

   Invoked when the System.Windows.Controls.ItemsControl.ItemContainerStyle property changes.

  

   oldItemContainerStyle: Old value of the System.Windows.Controls.ItemsControl.ItemContainerStyle property.

   newItemContainerStyle: New value of the System.Windows.Controls.ItemsControl.ItemContainerStyle property.
  """
  pass
 def OnItemContainerStyleSelectorChanged(self,*args):
  """
  OnItemContainerStyleSelectorChanged(self: ItemsControl,oldItemContainerStyleSelector: StyleSelector,newItemContainerStyleSelector: StyleSelector)

   Invoked when the System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property 

    changes.

  

  

   oldItemContainerStyleSelector: Old value of the System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property.

   newItemContainerStyleSelector: New value of the System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property.
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

   Invoked when the System.Windows.Controls.ItemsControl.ItemsPanel property changes.

  

   oldItemsPanel: Old value of the System.Windows.Controls.ItemsControl.ItemsPanel property.

   newItemsPanel: New value of the System.Windows.Controls.ItemsControl.ItemsPanel property.
  """
  pass
 def OnItemsSourceChanged(self,*args):
  """
  OnItemsSourceChanged(self: DataGrid,oldValue: IEnumerable,newValue: IEnumerable)

   Invoked when the System.Windows.Controls.ItemsControl.ItemsSource property changes.

  

   oldValue: The old source.

   newValue: The new source.
  """
  pass
 def OnItemStringFormatChanged(self,*args):
  """
  OnItemStringFormatChanged(self: ItemsControl,oldItemStringFormat: str,newItemStringFormat: str)

   Invoked when the System.Windows.Controls.ItemsControl.ItemStringFormat property changes.

  

   oldItemStringFormat: The old value of the System.Windows.Controls.ItemsControl.ItemStringFormat property.

   newItemStringFormat: The new value of the System.Windows.Controls.ItemsControl.ItemStringFormat property.
  """
  pass
 def OnItemTemplateChanged(self,*args):
  """
  OnItemTemplateChanged(self: ItemsControl,oldItemTemplate: DataTemplate,newItemTemplate: DataTemplate)

   Invoked when the System.Windows.Controls.ItemsControl.ItemTemplate property changes.

  

   oldItemTemplate: The old System.Windows.Controls.ItemsControl.ItemTemplate property value.

   newItemTemplate: The new System.Windows.Controls.ItemsControl.ItemTemplate property value.
  """
  pass
 def OnItemTemplateSelectorChanged(self,*args):
  """
  OnItemTemplateSelectorChanged(self: ItemsControl,oldItemTemplateSelector: DataTemplateSelector,newItemTemplateSelector: DataTemplateSelector)

   Invoked when the System.Windows.Controls.ItemsControl.ItemTemplateSelector property changes.

  

   oldItemTemplateSelector: Old value of the System.Windows.Controls.ItemsControl.ItemTemplateSelector property.

   newItemTemplateSelector: New value of the System.Windows.Controls.ItemsControl.ItemTemplateSelector property.
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

   Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
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

   Raises the System.Windows.UIElement.LostFocus�routed event by using the event data that is 

    provided.

  

  

   e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the 

    identifier for the System.Windows.UIElement.LostFocus event.
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
  """
  pass
 def OnLostMouseCapture(self,*args):
  """
  OnLostMouseCapture(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains event data.
  """
  pass
 def OnLostStylusCapture(self,*args):
  """
  OnLostStylusCapture(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains event data.
  """
  pass
 def OnLostTouchCapture(self,*args):
  """
  OnLostTouchCapture(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.LostTouchCapture routed event that 

    occurs when this element loses a touch capture.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnManipulationBoundaryFeedback(self,*args):
  """
  OnManipulationBoundaryFeedback(self: UIElement,e: ManipulationBoundaryFeedbackEventArgs)

   Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationCompleted(self,*args):
  """
  OnManipulationCompleted(self: UIElement,e: ManipulationCompletedEventArgs)

   Called when the System.Windows.UIElement.ManipulationCompleted event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationDelta(self,*args):
  """
  OnManipulationDelta(self: UIElement,e: ManipulationDeltaEventArgs)

   Called when the System.Windows.UIElement.ManipulationDelta event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationInertiaStarting(self,*args):
  """
  OnManipulationInertiaStarting(self: UIElement,e: ManipulationInertiaStartingEventArgs)

   Called when the System.Windows.UIElement.ManipulationInertiaStarting event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationStarted(self,*args):
  """
  OnManipulationStarted(self: UIElement,e: ManipulationStartedEventArgs)

   Called when the System.Windows.UIElement.ManipulationStarted event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationStarting(self,*args):
  """
  OnManipulationStarting(self: UIElement,e: ManipulationStartingEventArgs)

   Provides class handling for the System.Windows.UIElement.ManipulationStarting routed event that 

    occurs when the manipulation processor is first created.

  

  

   e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: Control,e: MouseButtonEventArgs)

   Raises the System.Windows.Controls.Control.MouseDoubleClick routed event.

  

   e: The event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data 

    reports details about the mouse button that was pressed and the handled state.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this 

    element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this 

    element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeftButtonDown(self,*args):
  """
  OnMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was pressed.
  """
  pass
 def OnMouseLeftButtonUp(self,*args):
  """
  OnMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was released.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGrid,e: MouseEventArgs)

   Updates the collection of items that are selected due to the user dragging the mouse in the 

    System.Windows.Controls.DataGrid.

  

  

   e: The mouse data.
  """
  pass
 def OnMouseRightButtonDown(self,*args):
  """
  OnMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was pressed.
  """
  pass
 def OnMouseRightButtonUp(self,*args):
  """
  OnMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was released.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the mouse button was released.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: UIElement,e: MouseWheelEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
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

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragLeave(self,*args):
  """
  OnPreviewDragLeave(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragOver(self,*args):
  """
  OnPreviewDragOver(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDrop(self,*args):
  """
  OnPreviewDrop(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewGiveFeedback(self,*args):
  """
  OnPreviewGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnPreviewGotKeyboardFocus(self,*args):
  """
  OnPreviewGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: UIElement,e: KeyEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyUp(self,*args):
  """
  OnPreviewKeyUp(self: UIElement,e: KeyEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnPreviewLostKeyboardFocus(self,*args):
  """
  OnPreviewLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
  """
  pass
 def OnPreviewMouseDoubleClick(self,*args):
  """
  OnPreviewMouseDoubleClick(self: Control,e: MouseButtonEventArgs)

   Raises the System.Windows.Controls.Control.PreviewMouseDoubleClick routed event.

  

   e: The event data.
  """
  pass
 def OnPreviewMouseDown(self,*args):
  """
  OnPreviewMouseDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that one or more mouse buttons were pressed.
  """
  pass
 def OnPreviewMouseLeftButtonDown(self,*args):
  """
  OnPreviewMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was pressed.
  """
  pass
 def OnPreviewMouseLeftButtonUp(self,*args):
  """
  OnPreviewMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�routed event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was released.
  """
  pass
 def OnPreviewMouseMove(self,*args):
  """
  OnPreviewMouseMove(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnPreviewMouseRightButtonDown(self,*args):
  """
  OnPreviewMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was pressed.
  """
  pass
 def OnPreviewMouseRightButtonUp(self,*args):
  """
  OnPreviewMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was released.
  """
  pass
 def OnPreviewMouseUp(self,*args):
  """
  OnPreviewMouseUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that one or more mouse buttons were released.
  """
  pass
 def OnPreviewMouseWheel(self,*args):
  """
  OnPreviewMouseWheel(self: UIElement,e: MouseWheelEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  """
  pass
 def OnPreviewQueryContinueDrag(self,*args):
  """
  OnPreviewQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonDown(self,*args):
  """
  OnPreviewStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonUp(self,*args):
  """
  OnPreviewStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusDown(self,*args):
  """
  OnPreviewStylusDown(self: UIElement,e: StylusDownEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInAirMove(self,*args):
  """
  OnPreviewStylusInAirMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInRange(self,*args):
  """
  OnPreviewStylusInRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusMove(self,*args):
  """
  OnPreviewStylusMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusOutOfRange(self,*args):
  """
  OnPreviewStylusOutOfRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusSystemGesture(self,*args):
  """
  OnPreviewStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusUp(self,*args):
  """
  OnPreviewStylusUp(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewTextInput(self,*args):
  """
  OnPreviewTextInput(self: UIElement,e: TextCompositionEventArgs)

   Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached 

    event reaches an element in its route that is derived from this class. Implement this method to 

    add class handling for this event.

  

  

   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchDown(self,*args):
  """
  OnPreviewTouchDown(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchDown routed event that 

    occurs when a touch presses this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchMove(self,*args):
  """
  OnPreviewTouchMove(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchMove routed event that 

    occurs when a touch moves while inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchUp(self,*args):
  """
  OnPreviewTouchUp(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed event that occurs 

    when a touch is released inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: FrameworkElement,e: DependencyPropertyChangedEventArgs)

   Invoked whenever the effective value of any dependency property on this 

    System.Windows.FrameworkElement has been updated. The specific dependency property that changed 

    is reported in the arguments parameter. Overrides 

    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr

    gs).

  

  

   e: The event data that describes the property that changed,as well as old and new values.
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: UIElement,e: QueryCursorEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
  """
  pass
 def OnRender(self,*args):
  """
  OnRender(self: UIElement,drawingContext: DrawingContext)

   When overridden in a derived class,participates in rendering operations that are directed by 

    the layout system. The rendering instructions for this element are not used directly when this 

    method is invoked,and are instead preserved for later asynchronous use by layout and drawing.

  

  

   drawingContext: The drawing instructions for a specific element. This context is provided to the layout system.
  """
  pass
 def OnRenderSizeChanged(self,*args):
  """
  OnRenderSizeChanged(self: FrameworkElement,sizeInfo: SizeChangedInfo)

   Raises the System.Windows.FrameworkElement.SizeChanged event,using the specified information as 

    part of the eventual event data.

  

  

   sizeInfo: Details of the old and new size involved in the change.
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

   Invoked when the style in use on this element changes,which will invalidate the layout.

  

   oldStyle: The old style.

   newStyle: The new style.
  """
  pass
 def OnStylusButtonDown(self,*args):
  """
  OnStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusButtonUp(self,*args):
  """
  OnStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusDown(self,*args):
  """
  OnStylusDown(self: UIElement,e: StylusDownEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnStylusEnter(self,*args):
  """
  OnStylusEnter(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInAirMove(self,*args):
  """
  OnStylusInAirMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInRange(self,*args):
  """
  OnStylusInRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusLeave(self,*args):
  """
  OnStylusLeave(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusMove(self,*args):
  """
  OnStylusMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusOutOfRange(self,*args):
  """
  OnStylusOutOfRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusSystemGesture(self,*args):
  """
  OnStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
  """
  pass
 def OnStylusUp(self,*args):
  """
  OnStylusUp(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
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

   Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnToolTipOpening(self,*args):
  """
  OnToolTipOpening(self: FrameworkElement,e: ToolTipEventArgs)

   Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed event reaches this 

    class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnTouchDown(self,*args):
  """
  OnTouchDown(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchDown routed event that occurs when 

    a touch presses inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchEnter(self,*args):
  """
  OnTouchEnter(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchEnter routed event that occurs 

    when a touch moves from outside to inside the bounds of this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchLeave(self,*args):
  """
  OnTouchLeave(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchLeave routed event that occurs 

    when a touch moves from inside to outside the bounds of this System.Windows.UIElement.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchMove(self,*args):
  """
  OnTouchMove(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchMove routed event that occurs when 

    a touch moves while inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchUp(self,*args):
  """
  OnTouchUp(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchUp routed event that occurs when a 

    touch is released inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
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

   Called when the System.Windows.Media.VisualCollection of the visual object is modified.

  

   visualAdded: The System.Windows.Media.Visual that was added to the collection

   visualRemoved: The System.Windows.Media.Visual that was removed from the collection
  """
  pass
 def OnVisualParentChanged(self,*args):
  """
  OnVisualParentChanged(self: FrameworkElement,oldParent: DependencyObject)

   Invoked when the parent of this element in the visual tree is changed. Overrides 

    System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).

  

  

   oldParent: The old parent element. May be null to indicate that the element did not have a visual parent 

    previously.
  """
  pass
 def ParentLayoutInvalidated(self,*args):
  """
  ParentLayoutInvalidated(self: FrameworkElement,child: UIElement)

   Supports incremental layout implementations in specialized subclasses of 

    System.Windows.FrameworkElement. 

    System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement)  is invoked 

    when a child element has invalidated a property that is marked in metadata as affecting the 

    parent's measure or arrange passes during layout.

  

  

   child: The child element reporting the change.
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

   Removes the provided object from this element's logical tree. System.Windows.FrameworkElement 

    updates the affected logical tree parent pointers to keep in sync with this deletion.

  

  

   child: The element to remove.
  """
  pass
 def RemoveVisualChild(self,*args):
  """
  RemoveVisualChild(self: Visual,child: Visual)

   Removes the parent-child relationship between two visuals.

  

   child: The child visual object to remove from the parent visual.
  """
  pass
 def ScrollIntoView(self,item,column=None):
  """
  ScrollIntoView(self: DataGrid,item: object,column: DataGridColumn)

   Scrolls the System.Windows.Controls.DataGrid vertically and horizontally to display a cell for 

    the specified data item and column.

  

  

   item: The data item to bring into view.

   column: The column to bring into view.

  ScrollIntoView(self: DataGrid,item: object)

   Scrolls the System.Windows.Controls.DataGrid vertically to display the row for the specified 

    data item.

  

  

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

   Sets the value of the System.Windows.Controls.DataGridRow.DetailsVisibility property for the 

    System.Windows.Controls.DataGridRow that contains the specified object.

  

  

   item: The object in the row for which System.Windows.Controls.DataGridRow.DetailsVisibility is being 

    set.

  

   detailsVisibility: The System.Windows.Visibility to set for the row that contains the item.
  """
  pass
 def ShouldApplyItemContainerStyle(self,*args):
  """
  ShouldApplyItemContainerStyle(self: ItemsControl,container: DependencyObject,item: object) -> bool

  

   Returns a value that indicates whether to apply the style from the 

    System.Windows.Controls.ItemsControl.ItemContainerStyle or 

    System.Windows.Controls.ItemsControl.ItemContainerStyleSelector property to the container 

    element of the specified item.

  

  

   container: The container element.

   item: The item of interest.

   Returns: Always true for the base implementation.
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


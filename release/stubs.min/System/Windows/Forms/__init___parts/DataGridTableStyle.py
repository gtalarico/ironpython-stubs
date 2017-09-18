class DataGridTableStyle(Component,IComponent,IDisposable,IDataGridEditingService):
 """
 Represents the table drawn by the System.Windows.Forms.DataGrid control at run time.

 

 DataGridTableStyle(isDefaultTableStyle: bool)

 DataGridTableStyle()

 DataGridTableStyle(listManager: CurrencyManager)
 """
 def BeginEdit(self,gridColumn,rowNumber):
  """
  BeginEdit(self: DataGridTableStyle,gridColumn: DataGridColumnStyle,rowNumber: int) -> bool

  

   Requests an edit operation.

  

   gridColumn: The System.Windows.Forms.DataGridColumnStyle to edit.

   rowNumber: The number of the edited row.

   Returns: true,if the operation succeeds; otherwise,false.
  """
  pass
 def CreateGridColumn(self,*args):
  """
  CreateGridColumn(self: DataGridTableStyle,prop: PropertyDescriptor,isDefault: bool) -> DataGridColumnStyle

  

   Creates a System.Windows.Forms.DataGridColumnStyle using the specified property descriptor. 

    Specifies whether the System.Windows.Forms.DataGridColumnStyle is a default column style.

  

  

   prop: The System.ComponentModel.PropertyDescriptor used to create the column style object.

   isDefault: Specifies whether the System.Windows.Forms.DataGridColumnStyle is a default column style. This 

    parameter is read-only.

  

   Returns: The newly created System.Windows.Forms.DataGridColumnStyle.

  CreateGridColumn(self: DataGridTableStyle,prop: PropertyDescriptor) -> DataGridColumnStyle

  

   Creates a System.Windows.Forms.DataGridColumnStyle,using the specified property descriptor.

  

   prop: The System.ComponentModel.PropertyDescriptor used to create the column style object.

   Returns: The newly created System.Windows.Forms.DataGridColumnStyle.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridTableStyle,disposing: bool)

   Disposes of the resources (other than memory) used by the 

    System.Windows.Forms.DataGridTableStyle.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndEdit(self,gridColumn,rowNumber,shouldAbort):
  """
  EndEdit(self: DataGridTableStyle,gridColumn: DataGridColumnStyle,rowNumber: int,shouldAbort: bool) -> bool

  

   Requests an end to an edit operation.

  

   gridColumn: The System.Windows.Forms.DataGridColumnStyle to edit.

   rowNumber: The number of the edited row.

   shouldAbort: A value indicating whether the operation should be stopped; true if it should stop; otherwise,

    false.

  

   Returns: true if the edit operation ends successfully; otherwise,false.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnAllowSortingChanged(self,*args):
  """
  OnAllowSortingChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.AllowSortingChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAlternatingBackColorChanged(self,*args):
  """
  OnAlternatingBackColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.AlternatingBackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnColumnHeadersVisibleChanged(self,*args):
  """
  OnColumnHeadersVisibleChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.ColumnHeadersVisibleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.ForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGridLineColorChanged(self,*args):
  """
  OnGridLineColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.GridLineColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGridLineStyleChanged(self,*args):
  """
  OnGridLineStyleChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.GridLineStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHeaderBackColorChanged(self,*args):
  """
  OnHeaderBackColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.HeaderBackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHeaderFontChanged(self,*args):
  """
  OnHeaderFontChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.HeaderFontChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHeaderForeColorChanged(self,*args):
  """
  OnHeaderForeColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.HeaderForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLinkColorChanged(self,*args):
  """
  OnLinkColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.LinkColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLinkHoverColorChanged(self,*args):
  """
  OnLinkHoverColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the LinkHoverColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMappingNameChanged(self,*args):
  """
  OnMappingNameChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.MappingNameChanged event

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPreferredColumnWidthChanged(self,*args):
  """
  OnPreferredColumnWidthChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.PreferredColumnWidthChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPreferredRowHeightChanged(self,*args):
  """
  OnPreferredRowHeightChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.PreferredRowHeightChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnReadOnlyChanged(self,*args):
  """
  OnReadOnlyChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.ReadOnlyChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeadersVisibleChanged(self,*args):
  """
  OnRowHeadersVisibleChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.RowHeadersVisibleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeaderWidthChanged(self,*args):
  """
  OnRowHeaderWidthChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.RowHeaderWidthChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSelectionBackColorChanged(self,*args):
  """
  OnSelectionBackColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.SelectionBackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSelectionForeColorChanged(self,*args):
  """
  OnSelectionForeColorChanged(self: DataGridTableStyle,e: EventArgs)

   Raises the System.Windows.Forms.DataGridTableStyle.SelectionForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def ResetAlternatingBackColor(self):
  """
  ResetAlternatingBackColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.AlternatingBackColor property to its default 

    value.
  """
  pass
 def ResetBackColor(self):
  """
  ResetBackColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.BackColor property to its default value.
  """
  pass
 def ResetForeColor(self):
  """
  ResetForeColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.ForeColor property to its default value.
  """
  pass
 def ResetGridLineColor(self):
  """
  ResetGridLineColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.GridLineColor property to its default value.
  """
  pass
 def ResetHeaderBackColor(self):
  """
  ResetHeaderBackColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.HeaderBackColor property to its default value.
  """
  pass
 def ResetHeaderFont(self):
  """
  ResetHeaderFont(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.HeaderFont property to its default value.
  """
  pass
 def ResetHeaderForeColor(self):
  """
  ResetHeaderForeColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.HeaderForeColor property to its default value.
  """
  pass
 def ResetLinkColor(self):
  """
  ResetLinkColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.LinkColor property to its default value.
  """
  pass
 def ResetLinkHoverColor(self):
  """
  ResetLinkHoverColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.LinkHoverColor property to its default value.
  """
  pass
 def ResetSelectionBackColor(self):
  """
  ResetSelectionBackColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.SelectionBackColor property to its default 

    value.
  """
  pass
 def ResetSelectionForeColor(self):
  """
  ResetSelectionForeColor(self: DataGridTableStyle)

   Resets the System.Windows.Forms.DataGridTableStyle.SelectionForeColor property to its default 

    value.
  """
  pass
 def ShouldSerializeAlternatingBackColor(self,*args):
  """
  ShouldSerializeAlternatingBackColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.AlternatingBackColor property 

    should be persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeBackColor(self,*args):
  """
  ShouldSerializeBackColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.BackColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeForeColor(self,*args):
  """
  ShouldSerializeForeColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.ForeColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeGridLineColor(self,*args):
  """
  ShouldSerializeGridLineColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.GridLineColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeHeaderBackColor(self,*args):
  """
  ShouldSerializeHeaderBackColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.HeaderBackColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeHeaderForeColor(self,*args):
  """
  ShouldSerializeHeaderForeColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.HeaderForeColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeLinkColor(self,*args):
  """
  ShouldSerializeLinkColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.LinkColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeLinkHoverColor(self,*args):
  """
  ShouldSerializeLinkHoverColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.LinkHoverColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializePreferredRowHeight(self,*args):
  """
  ShouldSerializePreferredRowHeight(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.PreferredRowHeight property should 

    be persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeSelectionBackColor(self,*args):
  """
  ShouldSerializeSelectionBackColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.SelectionBackColor property should 

    be persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeSelectionForeColor(self,*args):
  """
  ShouldSerializeSelectionForeColor(self: DataGridTableStyle) -> bool

  

   Indicates whether the System.Windows.Forms.DataGridTableStyle.SelectionForeColor property should 

    be persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,isDefaultTableStyle: bool)

  __new__(cls: type)

  __new__(cls: type,listManager: CurrencyManager)
  """
  pass
 def __str__(self,*args):
  pass
 AllowSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether sorting is allowed on the grid table when this System.Windows.Forms.DataGridTableStyle is used.



Get: AllowSorting(self: DataGridTableStyle) -> bool



Set: AllowSorting(self: DataGridTableStyle)=value

"""

 AlternatingBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of odd-numbered rows of the grid.



Get: AlternatingBackColor(self: DataGridTableStyle) -> Color



Set: AlternatingBackColor(self: DataGridTableStyle)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of even-numbered rows of the grid.



Get: BackColor(self: DataGridTableStyle) -> Color



Set: BackColor(self: DataGridTableStyle)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 ColumnHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether column headers are visible.



Get: ColumnHeadersVisible(self: DataGridTableStyle) -> bool



Set: ColumnHeadersVisible(self: DataGridTableStyle)=value

"""

 DataGrid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.DataGrid control for the drawn table.



Get: DataGrid(self: DataGridTableStyle) -> DataGrid



Set: DataGrid(self: DataGridTableStyle)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the grid table.



Get: ForeColor(self: DataGridTableStyle) -> Color



Set: ForeColor(self: DataGridTableStyle)=value

"""

 GridColumnStyles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of columns drawn for this table.



Get: GridColumnStyles(self: DataGridTableStyle) -> GridColumnStylesCollection



"""

 GridLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of grid lines.



Get: GridLineColor(self: DataGridTableStyle) -> Color



Set: GridLineColor(self: DataGridTableStyle)=value

"""

 GridLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style of grid lines.



Get: GridLineStyle(self: DataGridTableStyle) -> DataGridLineStyle



Set: GridLineStyle(self: DataGridTableStyle)=value

"""

 HeaderBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of headers.



Get: HeaderBackColor(self: DataGridTableStyle) -> Color



Set: HeaderBackColor(self: DataGridTableStyle)=value

"""

 HeaderFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font used for header captions.



Get: HeaderFont(self: DataGridTableStyle) -> Font



Set: HeaderFont(self: DataGridTableStyle)=value

"""

 HeaderForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of headers.



Get: HeaderForeColor(self: DataGridTableStyle) -> Color



Set: HeaderForeColor(self: DataGridTableStyle)=value

"""

 LinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of link text.



Get: LinkColor(self: DataGridTableStyle) -> Color



Set: LinkColor(self: DataGridTableStyle)=value

"""

 LinkHoverColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color displayed when hovering over link text.



Get: LinkHoverColor(self: DataGridTableStyle) -> Color



Set: LinkHoverColor(self: DataGridTableStyle)=value

"""

 MappingName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name used to map this table to a specific data source.



Get: MappingName(self: DataGridTableStyle) -> str



Set: MappingName(self: DataGridTableStyle)=value

"""

 PreferredColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width used to create columns when a new grid is displayed.



Get: PreferredColumnWidth(self: DataGridTableStyle) -> int



Set: PreferredColumnWidth(self: DataGridTableStyle)=value

"""

 PreferredRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height used to create a row when a new grid is displayed.



Get: PreferredRowHeight(self: DataGridTableStyle) -> int



Set: PreferredRowHeight(self: DataGridTableStyle)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether columns can be edited.



Get: ReadOnly(self: DataGridTableStyle) -> bool



Set: ReadOnly(self: DataGridTableStyle)=value

"""

 RowHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether row headers are visible.



Get: RowHeadersVisible(self: DataGridTableStyle) -> bool



Set: RowHeadersVisible(self: DataGridTableStyle)=value

"""

 RowHeaderWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of row headers.



Get: RowHeaderWidth(self: DataGridTableStyle) -> int



Set: RowHeaderWidth(self: DataGridTableStyle)=value

"""

 SelectionBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of selected cells.



Get: SelectionBackColor(self: DataGridTableStyle) -> Color



Set: SelectionBackColor(self: DataGridTableStyle)=value

"""

 SelectionForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of selected cells.



Get: SelectionForeColor(self: DataGridTableStyle) -> Color



Set: SelectionForeColor(self: DataGridTableStyle)=value

"""


 AllowSortingChanged=None
 AlternatingBackColorChanged=None
 BackColorChanged=None
 ColumnHeadersVisibleChanged=None
 DefaultTableStyle=None
 ForeColorChanged=None
 GridLineColorChanged=None
 GridLineStyleChanged=None
 HeaderBackColorChanged=None
 HeaderFontChanged=None
 HeaderForeColorChanged=None
 LinkColorChanged=None
 LinkHoverColorChanged=None
 MappingNameChanged=None
 PreferredColumnWidthChanged=None
 PreferredRowHeightChanged=None
 ReadOnlyChanged=None
 RowHeadersVisibleChanged=None
 RowHeaderWidthChanged=None
 SelectionBackColorChanged=None
 SelectionForeColorChanged=None


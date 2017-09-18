class DataGridBoolColumn(DataGridColumnStyle,IComponent,IDisposable,IDataGridColumnStyleEditingNotificationService):
 """
 Specifies a column in which each cell contains a check box for representing a Boolean value.

 

 DataGridBoolColumn()

 DataGridBoolColumn(prop: PropertyDescriptor)

 DataGridBoolColumn(prop: PropertyDescriptor,isDefault: bool)
 """
 def Abort(self,*args):
  """
  Abort(self: DataGridBoolColumn,rowNum: int)

   Initiates a request to interrupt an edit procedure.

  

   rowNum: The number of the row in which an operation is being interrupted.
  """
  pass
 def BeginUpdate(self,*args):
  """
  BeginUpdate(self: DataGridColumnStyle)

   Suspends the painting of the column until the System.Windows.Forms.DataGridColumnStyle.EndUpdate 

    method is called.
  """
  pass
 def CheckValidDataSource(self,*args):
  """
  CheckValidDataSource(self: DataGridColumnStyle,value: CurrencyManager)

   Throws an exception if the System.Windows.Forms.DataGrid does not have a valid data source,or 

    if this column is not mapped to a valid property in the data source.

  

  

   value: A System.Windows.Forms.CurrencyManager to check.
  """
  pass
 def ColumnStartedEditing(self,*args):
  """
  ColumnStartedEditing(self: DataGridColumnStyle,editingControl: Control)

   Informs the System.Windows.Forms.DataGrid that the user has begun editing the column.

  

   editingControl: The System.Windows.Forms.Control that hosted by the column.
  """
  pass
 def Commit(self,*args):
  """
  Commit(self: DataGridBoolColumn,dataSource: CurrencyManager,rowNum: int) -> bool

  

   Initiates a request to complete an editing procedure.

  

   dataSource: The System.Data.DataView of the edited column.

   rowNum: The number of the edited row.

   Returns: true if the editing procedure committed successfully; otherwise,false.
  """
  pass
 def ConcedeFocus(self,*args):
  """ ConcedeFocus(self: DataGridBoolColumn) """
  pass
 def CreateHeaderAccessibleObject(self,*args):
  """
  CreateHeaderAccessibleObject(self: DataGridColumnStyle) -> AccessibleObject

  

   Gets the System.Windows.Forms.AccessibleObject for the column.

   Returns: An System.Windows.Forms.AccessibleObject for the column.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)

   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def Edit(self,*args):
  """
  Edit(self: DataGridBoolColumn,source: CurrencyManager,rowNum: int,bounds: Rectangle,readOnly: bool,displayText: str,cellIsVisible: bool)

   Prepares the cell for editing a value.

  

   source: The System.Data.DataView of the edited cell.

   rowNum: The row number of the edited cell.

   bounds: The System.Drawing.Rectangle in which the control is to be sited.

   readOnly: true if the value is read only; otherwise,false.

   displayText: The text to display in the cell.

   cellIsVisible: true to show the cell; otherwise,false.

  Edit(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int,bounds: Rectangle,readOnly: bool,displayText: str)

   Prepares the cell for editing using the specified System.Windows.Forms.CurrencyManager,row 

    number,and System.Drawing.Rectangle parameters.

  

  

   source: The System.Windows.Forms.CurrencyManager for the System.Windows.Forms.DataGridColumnStyle.

   rowNum: The row number in this column which is being edited.

   bounds: The System.Drawing.Rectangle in which the control is to be sited.

   readOnly: A value indicating whether the column is a read-only. true if the value is read-only; otherwise,

    false.

  

   displayText: The text to display in the control.

  Edit(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int,bounds: Rectangle,readOnly: bool)

   Prepares a cell for editing.

  

   source: The System.Windows.Forms.CurrencyManager for the System.Windows.Forms.DataGridColumnStyle.

   rowNum: The row number to edit.

   bounds: The bounding System.Drawing.Rectangle in which the control is to be sited.

   readOnly: A value indicating whether the column is a read-only. true if the value is read-only; otherwise,

    false.
  """
  pass
 def EndUpdate(self,*args):
  """
  EndUpdate(self: DataGridColumnStyle)

   Resumes the painting of columns suspended by calling the 

    System.Windows.Forms.DataGridColumnStyle.BeginUpdate method.
  """
  pass
 def EnterNullValue(self,*args):
  """
  EnterNullValue(self: DataGridBoolColumn)

   Enters a System.DBNull.Value into the column.
  """
  pass
 def GetColumnValueAtRow(self,*args):
  """
  GetColumnValueAtRow(self: DataGridBoolColumn,lm: CurrencyManager,row: int) -> object

  

   Gets the value at the specified row.

  

   lm: The System.Windows.Forms.CurrencyManager for the column.

   row: The row number.

   Returns: The value,typed as System.Object.
  """
  pass
 def GetMinimumHeight(self,*args):
  """
  GetMinimumHeight(self: DataGridBoolColumn) -> int

  

   Gets the height of a cell in a column.

   Returns: The height of the column. The default is 16.
  """
  pass
 def GetPreferredHeight(self,*args):
  """
  GetPreferredHeight(self: DataGridBoolColumn,g: Graphics,value: object) -> int

  

   Gets the height used when resizing columns.

  

   g: A System.Drawing.Graphics that draws on the screen.

   value: An System.Object that contains the value to be drawn to the screen.

   Returns: The height used to automatically resize cells in a column.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridBoolColumn,g: Graphics,value: object) -> Size

  

   Gets the optimum width and height of a cell given a specific value to contain.

  

   g: A System.Drawing.Graphics that draws the cell.

   value: The value that must fit in the cell.

   Returns: A System.Drawing.Size that contains the drawing information for the cell.
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
 def Invalidate(self,*args):
  """
  Invalidate(self: DataGridColumnStyle)

   Redraws the column and causes a paint message to be sent to the control.
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
 def Paint(self,*args):
  """
  Paint(self: DataGridBoolColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,backBrush: Brush,foreBrush: Brush,alignToRight: bool)

   Draws the System.Windows.Forms.DataGridBoolColumn with the given System.Drawing.Graphics,

    System.Drawing.Rectangle,row number,System.Drawing.Brush,and System.Drawing.Color.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the column.

   rowNum: The number of the row in the underlying data table being referred to.

   backBrush: A System.Drawing.Brush used to paint the background color.

   foreBrush: A System.Drawing.Color used to paint the foreground color.

   alignToRight: A value indicating whether to align the content to the right. true if the content is aligned to 

    the right,otherwise,false.

  

  Paint(self: DataGridBoolColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,alignToRight: bool)

   Draws the System.Windows.Forms.DataGridBoolColumn with the given System.Drawing.Graphics,

    System.Drawing.Rectangle,row number,and alignment settings.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the column.

   rowNum: The number of the row in the underlying data table being referred to.

   alignToRight: A value indicating whether to align the content to the right. true if the content is aligned to 

    the right,otherwise,false.

  

  Paint(self: DataGridBoolColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int)

   Draws the System.Windows.Forms.DataGridBoolColumn with the given System.Drawing.Graphics,

    System.Drawing.Rectangle and row number.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the column.

   rowNum: The number of the row referred to in the underlying data.
  """
  pass
 def ReleaseHostedControl(self,*args):
  """
  ReleaseHostedControl(self: DataGridColumnStyle)

   Allows the column to free resources when the control it hosts is not needed.
  """
  pass
 def SetColumnValueAtRow(self,*args):
  """
  SetColumnValueAtRow(self: DataGridBoolColumn,lm: CurrencyManager,row: int,value: object)

   Sets the value of a specified row.

  

   lm: The System.Windows.Forms.CurrencyManager for the column.

   row: The row number.

   value: The value to set,typed as System.Object.
  """
  pass
 def SetDataGrid(self,*args):
  """
  SetDataGrid(self: DataGridColumnStyle,value: DataGrid)

   Sets the System.Windows.Forms.DataGrid control that this column belongs to.

  

   value: The System.Windows.Forms.DataGrid control that this column belongs to.
  """
  pass
 def SetDataGridInColumn(self,*args):
  """
  SetDataGridInColumn(self: DataGridColumnStyle,value: DataGrid)

   Sets the System.Windows.Forms.DataGrid for the column.

  

   value: A System.Windows.Forms.DataGrid.
  """
  pass
 def UpdateUI(self,*args):
  """
  UpdateUI(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int,displayText: str)

   Updates the value of a specified row with the given text.

  

   source: The System.Windows.Forms.CurrencyManager associated with the 

    System.Windows.Forms.DataGridColumnStyle.

  

   rowNum: The row to update.

   displayText: The new value.
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
 def __new__(self,prop=None,isDefault=None):
  """
  __new__(cls: type)

  __new__(cls: type,prop: PropertyDescriptor)

  __new__(cls: type,prop: PropertyDescriptor,isDefault: bool)
  """
  pass
 def __str__(self,*args):
  pass
 AllowNull=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether null values are allowed.



Get: AllowNull(self: DataGridBoolColumn) -> bool



Set: AllowNull(self: DataGridBoolColumn)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FalseValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the actual value used when setting the value of the column to false.



Get: FalseValue(self: DataGridBoolColumn) -> object



Set: FalseValue(self: DataGridBoolColumn)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the column's font.



"""

 NullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the actual value used when setting the value of the column to System.DBNull.Value.



Get: NullValue(self: DataGridBoolColumn) -> object



Set: NullValue(self: DataGridBoolColumn)=value

"""

 TrueValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the actual value used when setting the value of the column to true.



Get: TrueValue(self: DataGridBoolColumn) -> object



Set: TrueValue(self: DataGridBoolColumn)=value

"""


 AllowNullChanged=None
 FalseValueChanged=None
 TrueValueChanged=None


class DataGridTextBoxColumn(DataGridColumnStyle,IComponent,IDisposable,IDataGridColumnStyleEditingNotificationService):
 """
 Hosts a System.Windows.Forms.TextBox control in a cell of a System.Windows.Forms.DataGridColumnStyle for editing strings.

 

 DataGridTextBoxColumn()

 DataGridTextBoxColumn(prop: PropertyDescriptor)

 DataGridTextBoxColumn(prop: PropertyDescriptor,format: str)

 DataGridTextBoxColumn(prop: PropertyDescriptor,format: str,isDefault: bool)

 DataGridTextBoxColumn(prop: PropertyDescriptor,isDefault: bool)
 """
 def Abort(self,*args):
  """
  Abort(self: DataGridTextBoxColumn,rowNum: int)

   Initiates a request to interrupt an edit procedure.

  

   rowNum: The number of the row in which an edit operation is being interrupted.
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
  Commit(self: DataGridTextBoxColumn,dataSource: CurrencyManager,rowNum: int) -> bool

  

   Inititates a request to complete an editing procedure.

  

   dataSource: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid control the column 

    belongs to.

  

   rowNum: The number of the edited row.

   Returns: true if the value was successfully committed; otherwise,false.
  """
  pass
 def ConcedeFocus(self,*args):
  """
  ConcedeFocus(self: DataGridTextBoxColumn)

   Informs the column that the focus is being conceded.
  """
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
  Edit(self: DataGridTextBoxColumn,source: CurrencyManager,rowNum: int,bounds: Rectangle,readOnly: bool,displayText: str,cellIsVisible: bool)

   Prepares a cell for editing.

  

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid control the column 

    belongs to.

  

   rowNum: The row number in this column being edited.

   bounds: The bounding System.Drawing.Rectangle in which the control is to be sited.

   readOnly: A value indicating whether the column is a read-only. true if the value is read-only; otherwise,

    false.

  

   displayText: The text to display in the control.

   cellIsVisible: A value indicating whether the cell is visible. true if the cell is visible; otherwise,false.

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
 def EndEdit(self,*args):
  """
  EndEdit(self: DataGridTextBoxColumn)

   Ends an edit operation on the System.Windows.Forms.DataGridColumnStyle.
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
  EnterNullValue(self: DataGridTextBoxColumn)

   Enters a System.DBNull.Value in the column.
  """
  pass
 def GetColumnValueAtRow(self,*args):
  """
  GetColumnValueAtRow(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int) -> object

  

   Gets the value in the specified row from the specified System.Windows.Forms.CurrencyManager.

  

   source: The System.Windows.Forms.CurrencyManager containing the data.

   rowNum: The row number containing the data.

   Returns: An System.Object containing the value.
  """
  pass
 def GetMinimumHeight(self,*args):
  """
  GetMinimumHeight(self: DataGridTextBoxColumn) -> int

  

   Gets the height of a cell in a System.Windows.Forms.DataGridColumnStyle.

   Returns: The height of a cell.
  """
  pass
 def GetPreferredHeight(self,*args):
  """
  GetPreferredHeight(self: DataGridTextBoxColumn,g: Graphics,value: object) -> int

  

   Gets the height to be used in for automatically resizing columns.

  

   g: A System.Drawing.Graphics object used to draw shapes on the screen.

   value: The value to draw.

   Returns: The height the cells automatically resize to.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridTextBoxColumn,g: Graphics,value: object) -> Size

  

   Returns the optimum width and height of the cell in a specified row relative to the specified 

    value.

  

  

   g: A System.Drawing.Graphics object used to draw shapes on the screen.

   value: The value to draw.

   Returns: A System.Drawing.Size that contains the dimensions of the cell.
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
 def HideEditBox(self,*args):
  """
  HideEditBox(self: DataGridTextBoxColumn)

   Hides the System.Windows.Forms.DataGridTextBox control and moves the focus to the 

    System.Windows.Forms.DataGrid control.
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
  Paint(self: DataGridTextBoxColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,backBrush: Brush,foreBrush: Brush,alignToRight: bool)

   Paints a System.Windows.Forms.DataGridColumnStyle with the specified System.Drawing.Graphics,

    System.Drawing.Rectangle,System.Windows.Forms.CurrencyManager,row number,

    System.Drawing.Brush,and foreground color.

  

  

   g: The System.Drawing.Graphics object to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid the that contains 

    the column.

  

   rowNum: The number of the row in the underlying data table.

   backBrush: A System.Drawing.Brush that paints the background.

   foreBrush: A System.Drawing.Brush that paints the foreground color.

   alignToRight: A value indicating whether to align the column's content to the right. true if the content 

    should be aligned to the right; otherwise,false.

  

  Paint(self: DataGridTextBoxColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,alignToRight: bool)

   Paints a System.Windows.Forms.DataGridColumnStyle with the specified System.Drawing.Graphics,

    System.Drawing.Rectangle,System.Windows.Forms.CurrencyManager,row number,and alignment.

  

  

   g: The System.Drawing.Graphics object to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid the that contains 

    the column.

  

   rowNum: The number of the row in the underlying data table.

   alignToRight: A value indicating whether to align the column's content to the right. true if the content 

    should be aligned to the right; otherwise,false.

  

  Paint(self: DataGridTextBoxColumn,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int)

   Paints the a System.Windows.Forms.DataGridColumnStyle with the specified 

    System.Drawing.Graphics,System.Drawing.Rectangle,System.Windows.Forms.CurrencyManager,and row 

    number.

  

  

   g: The System.Drawing.Graphics object to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid the that contains 

    the column.

  

   rowNum: The number of the row in the underlying data table.
  """
  pass
 def PaintText(self,*args):
  """
  PaintText(self: DataGridTextBoxColumn,g: Graphics,textBounds: Rectangle,text: str,backBrush: Brush,foreBrush: Brush,alignToRight: bool)

   Draws the text and rectangle at the specified location with the specified colors and alignment.

  

   g: A System.Drawing.Graphics object used to draw the string.

   textBounds: A System.Drawing.Rectangle which contains the boundary data of the rectangle.

   text: The string to be drawn to the screen.

   backBrush: A System.Drawing.Brush that determines the rectangle's background color

   foreBrush: A System.Drawing.Brush that determines the rectangles foreground color.

   alignToRight: A value indicating whether the text is right-aligned.

  PaintText(self: DataGridTextBoxColumn,g: Graphics,bounds: Rectangle,text: str,alignToRight: bool)

   Draws the text and rectangle at the given location with the specified alignment.

  

   g: A System.Drawing.Graphics object used to draw the string.

   bounds: A System.Drawing.Rectangle which contains the boundary data of the rectangle.

   text: The string to be drawn to the screen.

   alignToRight: A value indicating whether the text is right-aligned.
  """
  pass
 def ReleaseHostedControl(self,*args):
  """
  ReleaseHostedControl(self: DataGridTextBoxColumn)

   Removes the reference that the System.Windows.Forms.DataGrid holds to the control used to edit 

    data.
  """
  pass
 def SetColumnValueAtRow(self,*args):
  """
  SetColumnValueAtRow(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int,value: object)

   Sets the value in a specified row with the value from a specified 

    System.Windows.Forms.CurrencyManager.

  

  

   source: A System.Windows.Forms.CurrencyManager associated with the 

    System.Windows.Forms.DataGridColumnStyle.

  

   rowNum: The number of the row.

   value: The value to set.
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
  SetDataGridInColumn(self: DataGridTextBoxColumn,value: DataGrid)

   Adds a System.Windows.Forms.TextBox control to the System.Windows.Forms.DataGrid control's 

    System.Windows.Forms.Control.ControlCollection.

  

  

   value: The System.Windows.Forms.DataGrid control the System.Windows.Forms.TextBox control is added to.
  """
  pass
 def UpdateUI(self,*args):
  """
  UpdateUI(self: DataGridTextBoxColumn,source: CurrencyManager,rowNum: int,displayText: str)

   Updates the user interface.

  

   source: The System.Windows.Forms.CurrencyManager that supplies the data.

   rowNum: The index of the row to update.

   displayText: The text that will be displayed in the cell.
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
 def __new__(self,prop=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,prop: PropertyDescriptor)

  __new__(cls: type,prop: PropertyDescriptor,format: str)

  __new__(cls: type,prop: PropertyDescriptor,format: str,isDefault: bool)

  __new__(cls: type,prop: PropertyDescriptor,isDefault: bool)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the column's font.



"""

 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character(s) that specify how text is formatted.



Get: Format(self: DataGridTextBoxColumn) -> str



Set: Format(self: DataGridTextBoxColumn)=value

"""

 FormatInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the culture specific information used to determine how values are formatted.



Get: FormatInfo(self: DataGridTextBoxColumn) -> IFormatProvider



Set: FormatInfo(self: DataGridTextBoxColumn)=value

"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.ComponentModel.PropertyDescriptor for the System.Windows.Forms.DataGridTextBoxColumn.



Set: PropertyDescriptor(self: DataGridTextBoxColumn)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets a value indicating whether the text box column is read-only.



Get: ReadOnly(self: DataGridTextBoxColumn) -> bool



Set: ReadOnly(self: DataGridTextBoxColumn)=value

"""

 TextBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hosted System.Windows.Forms.TextBox control.



Get: TextBox(self: DataGridTextBoxColumn) -> TextBox



"""



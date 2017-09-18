class DataGridColumnStyle(Component,IComponent,IDisposable,IDataGridColumnStyleEditingNotificationService):
 """
 Specifies the appearance,text formatting,and behavior of a System.Windows.Forms.DataGrid control column. This class is abstract.

 

 DataGridColumnStyle()

 DataGridColumnStyle(prop: PropertyDescriptor)
 """
 def Abort(self,*args):
  """
  Abort(self: DataGridColumnStyle,rowNum: int)

   When overridden in a derived class,initiates a request to interrupt an edit procedure.

  

   rowNum: The row number upon which an operation is being interrupted.
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
  Commit(self: DataGridColumnStyle,dataSource: CurrencyManager,rowNum: int) -> bool

  

   When overridden in a derived class,initiates a request to complete an editing procedure.

  

   dataSource: The System.Windows.Forms.CurrencyManager for the System.Windows.Forms.DataGridColumnStyle.

   rowNum: The number of the row being edited.

   Returns: true if the editing procedure committed successfully; otherwise,false.
  """
  pass
 def ConcedeFocus(self,*args):
  """
  ConcedeFocus(self: DataGridColumnStyle)

   Notifies a column that it must relinquish the focus to the control it is hosting.
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
  Edit(self: DataGridColumnStyle,source: CurrencyManager,rowNum: int,bounds: Rectangle,readOnly: bool,displayText: str,cellIsVisible: bool)

   When overridden in a deriving class,prepares a cell for editing.

  

   source: The System.Windows.Forms.CurrencyManager for the System.Windows.Forms.DataGridColumnStyle.

   rowNum: The row number in this column which is being edited.

   bounds: The System.Drawing.Rectangle in which the control is to be sited.

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
 def EndUpdate(self,*args):
  """
  EndUpdate(self: DataGridColumnStyle)

   Resumes the painting of columns suspended by calling the 

    System.Windows.Forms.DataGridColumnStyle.BeginUpdate method.
  """
  pass
 def EnterNullValue(self,*args):
  """
  EnterNullValue(self: DataGridColumnStyle)

   Enters a System.DBNull.Value into the column.
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
  GetMinimumHeight(self: DataGridColumnStyle) -> int

  

   When overridden in a derived class,gets the minimum height of a row.

   Returns: The minimum height of a row.
  """
  pass
 def GetPreferredHeight(self,*args):
  """
  GetPreferredHeight(self: DataGridColumnStyle,g: Graphics,value: object) -> int

  

   When overridden in a derived class,gets the height used for automatically resizing columns.

  

   g: A System.Drawing.Graphics object.

   value: An object value for which you want to know the screen height and width.

   Returns: The height used for auto resizing a cell.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridColumnStyle,g: Graphics,value: object) -> Size

  

   When overridden in a derived class,gets the width and height of the specified value. The width 

    and height are used when the user navigates to System.Windows.Forms.DataGridTableStyle using the 

    System.Windows.Forms.DataGridColumnStyle.

  

  

   g: A System.Drawing.Graphics object.

   value: An object value for which you want to know the screen height and width.

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
  Paint(self: DataGridColumnStyle,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,backBrush: Brush,foreBrush: Brush,alignToRight: bool)

   Paints a System.Windows.Forms.DataGridColumnStyle with the specified System.Drawing.Graphics,

    System.Drawing.Rectangle,System.Windows.Forms.CurrencyManager,row number,background color,

    foreground color,and alignment.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid control the column 

    belongs to.

  

   rowNum: The number of the row in the underlying data table being referred to.

   backBrush: A System.Drawing.Brush used to paint the background color.

   foreBrush: A System.Drawing.Color used to paint the foreground color.

   alignToRight: A value indicating whether to align the content to the right. true if the content is aligned to 

    the right,otherwise,false.

  

  Paint(self: DataGridColumnStyle,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int,alignToRight: bool)

   When overridden in a derived class,paints a System.Windows.Forms.DataGridColumnStyle with the 

    specified System.Drawing.Graphics,System.Drawing.Rectangle,

    System.Windows.Forms.CurrencyManager,row number,and alignment.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid control the column 

    belongs to.

  

   rowNum: The number of the row in the underlying data being referred to.

   alignToRight: A value indicating whether to align the column's content to the right. true if the content 

    should be aligned to the right; otherwise false.

  

  Paint(self: DataGridColumnStyle,g: Graphics,bounds: Rectangle,source: CurrencyManager,rowNum: int)

   Paints the System.Windows.Forms.DataGridColumnStyle with the specified System.Drawing.Graphics,

    System.Drawing.Rectangle,System.Windows.Forms.CurrencyManager,and row number.

  

  

   g: The System.Drawing.Graphics to draw to.

   bounds: The bounding System.Drawing.Rectangle to paint into.

   source: The System.Windows.Forms.CurrencyManager of the System.Windows.Forms.DataGrid control the column 

    belongs to.

  

   rowNum: The number of the row in the underlying data being referred to.
  """
  pass
 def ReleaseHostedControl(self,*args):
  """
  ReleaseHostedControl(self: DataGridColumnStyle)

   Allows the column to free resources when the control it hosts is not needed.
  """
  pass
 def ResetHeaderText(self):
  """
  ResetHeaderText(self: DataGridColumnStyle)

   Resets the System.Windows.Forms.DataGridColumnStyle.HeaderText to its default value,null.
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
 def __new__(self,prop=None):
  """
  __new__(cls: type)

  __new__(cls: type,prop: PropertyDescriptor)
  """
  pass
 def __str__(self,*args):
  pass
 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of text in a column.



Get: Alignment(self: DataGridColumnStyle) -> HorizontalAlignment



Set: Alignment(self: DataGridColumnStyle)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DataGridTableStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridTableStyle for the column.



Get: DataGridTableStyle(self: DataGridColumnStyle) -> DataGridTableStyle



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

 HeaderAccessibleObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.AccessibleObject for the column.



Get: HeaderAccessibleObject(self: DataGridColumnStyle) -> AccessibleObject



"""

 HeaderText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the column header.



Get: HeaderText(self: DataGridColumnStyle) -> str



Set: HeaderText(self: DataGridColumnStyle)=value

"""

 MappingName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the data member to map the column style to.



Get: MappingName(self: DataGridColumnStyle) -> str



Set: MappingName(self: DataGridColumnStyle)=value

"""

 NullText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that is displayed when the column contains null.



Get: NullText(self: DataGridColumnStyle) -> str



Set: NullText(self: DataGridColumnStyle)=value

"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.ComponentModel.PropertyDescriptor that determines the attributes of data displayed by the System.Windows.Forms.DataGridColumnStyle.



Get: PropertyDescriptor(self: DataGridColumnStyle) -> PropertyDescriptor



Set: PropertyDescriptor(self: DataGridColumnStyle)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the data in the column can be edited.



Get: ReadOnly(self: DataGridColumnStyle) -> bool



Set: ReadOnly(self: DataGridColumnStyle)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the column.



Get: Width(self: DataGridColumnStyle) -> int



Set: Width(self: DataGridColumnStyle)=value

"""


 AlignmentChanged=None
 CompModSwitches=None
 DataGridColumnHeaderAccessibleObject=None
 FontChanged=None
 HeaderTextChanged=None
 MappingNameChanged=None
 NullTextChanged=None
 PropertyDescriptorChanged=None
 ReadOnlyChanged=None
 WidthChanged=None


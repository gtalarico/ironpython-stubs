class DataGridViewCellStyle(object,ICloneable):
 """
 Represents the formatting and style information applied to individual cells within a System.Windows.Forms.DataGridView control.

 

 DataGridViewCellStyle()

 DataGridViewCellStyle(dataGridViewCellStyle: DataGridViewCellStyle)
 """
 def ApplyStyle(self,dataGridViewCellStyle):
  """
  ApplyStyle(self: DataGridViewCellStyle,dataGridViewCellStyle: DataGridViewCellStyle)

   Applies the specified System.Windows.Forms.DataGridViewCellStyle to the current 

    System.Windows.Forms.DataGridViewCellStyle.

  

  

   dataGridViewCellStyle: The System.Windows.Forms.DataGridViewCellStyle to apply to the current 

    System.Windows.Forms.DataGridViewCellStyle.
  """
  pass
 def Clone(self):
  """
  Clone(self: DataGridViewCellStyle) -> DataGridViewCellStyle

  

   Creates an exact copy of this System.Windows.Forms.DataGridViewCellStyle.

   Returns: A System.Windows.Forms.DataGridViewCellStyle that represents an exact copy of this cell style.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: DataGridViewCellStyle,o: object) -> bool

  

   Returns a value indicating whether this instance is equivalent to the specified object.

  

   o: An object to compare with this instance,or null.

   Returns: true if o is a System.Windows.Forms.DataGridViewCellStyle and has the same property values as 

    this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridViewCellStyle) -> int

   Returns: A hash code for the current System.Object.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewCellStyle) -> str

  

   Returns a string indicating the current property settings of the 

    System.Windows.Forms.DataGridViewCellStyle.

  

   Returns: A string indicating the current property settings of the 

    System.Windows.Forms.DataGridViewCellStyle.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dataGridViewCellStyle=None):
  """
  __new__(cls: type)

  __new__(cls: type,dataGridViewCellStyle: DataGridViewCellStyle)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the position of the cell content within a System.Windows.Forms.DataGridView cell.



Get: Alignment(self: DataGridViewCellStyle) -> DataGridViewContentAlignment



Set: Alignment(self: DataGridViewCellStyle)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of a System.Windows.Forms.DataGridView cell.



Get: BackColor(self: DataGridViewCellStyle) -> Color



Set: BackColor(self: DataGridViewCellStyle)=value

"""

 DataSourceNullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value saved to the data source when the user enters a null value into a cell.



Get: DataSourceNullValue(self: DataGridViewCellStyle) -> object



Set: DataSourceNullValue(self: DataGridViewCellStyle)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font applied to the textual content of a System.Windows.Forms.DataGridView cell.



Get: Font(self: DataGridViewCellStyle) -> Font



Set: Font(self: DataGridViewCellStyle)=value

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of a System.Windows.Forms.DataGridView cell.



Get: ForeColor(self: DataGridViewCellStyle) -> Color



Set: ForeColor(self: DataGridViewCellStyle)=value

"""

 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the format string applied to the textual content of a System.Windows.Forms.DataGridView cell.



Get: Format(self: DataGridViewCellStyle) -> str



Set: Format(self: DataGridViewCellStyle)=value

"""

 FormatProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object used to provide culture-specific formatting of System.Windows.Forms.DataGridView cell values.



Get: FormatProvider(self: DataGridViewCellStyle) -> IFormatProvider



Set: FormatProvider(self: DataGridViewCellStyle)=value

"""

 IsDataSourceNullValueDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.DataGridViewCellStyle.DataSourceNullValue property has been set.



Get: IsDataSourceNullValueDefault(self: DataGridViewCellStyle) -> bool



"""

 IsFormatProviderDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Forms.DataGridViewCellStyle.FormatProvider property has been set.



Get: IsFormatProviderDefault(self: DataGridViewCellStyle) -> bool



"""

 IsNullValueDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.DataGridViewCellStyle.NullValue property has been set.



Get: IsNullValueDefault(self: DataGridViewCellStyle) -> bool



"""

 NullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.DataGridView cell display value corresponding to a cell value of System.DBNull.Value or null.



Get: NullValue(self: DataGridViewCellStyle) -> object



Set: NullValue(self: DataGridViewCellStyle)=value

"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between the edge of a System.Windows.Forms.DataGridViewCell and its content.



Get: Padding(self: DataGridViewCellStyle) -> Padding



Set: Padding(self: DataGridViewCellStyle)=value

"""

 SelectionBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color used by a System.Windows.Forms.DataGridView cell when it is selected.



Get: SelectionBackColor(self: DataGridViewCellStyle) -> Color



Set: SelectionBackColor(self: DataGridViewCellStyle)=value

"""

 SelectionForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color used by a System.Windows.Forms.DataGridView cell when it is selected.



Get: SelectionForeColor(self: DataGridViewCellStyle) -> Color



Set: SelectionForeColor(self: DataGridViewCellStyle)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains additional data related to the System.Windows.Forms.DataGridViewCellStyle.



Get: Tag(self: DataGridViewCellStyle) -> object



Set: Tag(self: DataGridViewCellStyle)=value

"""

 WrapMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether textual content in a System.Windows.Forms.DataGridView cell is wrapped to subsequent lines or truncated when it is too long to fit on a single line.



Get: WrapMode(self: DataGridViewCellStyle) -> DataGridViewTriState



Set: WrapMode(self: DataGridViewCellStyle)=value

"""



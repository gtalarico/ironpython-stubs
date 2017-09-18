class TableCellStyle(object,IDisposable):
 """
 The TableCellStyle class contains the appearance settings for a given table cell,column,or table.

 

 TableCellStyle(other: TableCellStyle)

 TableCellStyle()
 """
 def Dispose(self):
  """ Dispose(self: TableCellStyle) """
  pass
 def GetCellStyleOverrideOptions(self):
  """
  GetCellStyleOverrideOptions(self: TableCellStyle) -> TableCellStyleOverrideOptions

  

   Gets cell style override options of this cell.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TableCellStyle,disposing: bool) """
  pass
 def ResetOverride(self):
  """
  ResetOverride(self: TableCellStyle)

   Resets any overrides applied to this cell.
  """
  pass
 def SetCellStyleOverrideOptions(self,helper):
  """
  SetCellStyleOverrideOptions(self: TableCellStyle,helper: TableCellStyleOverrideOptions)

   Sets cell style override options of this cell.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,other=None):
  """
  __new__(cls: type,other: TableCellStyle)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The background color of this cell in the grid view.



Get: BackgroundColor(self: TableCellStyle) -> Color



Set: BackgroundColor(self: TableCellStyle)=value

"""

 BorderBottomLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id (GraphicsStyle element) for the bottom line of the cell border.



Get: BorderBottomLineStyle(self: TableCellStyle) -> ElementId



Set: BorderBottomLineStyle(self: TableCellStyle)=value

"""

 BorderLeftLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id (GraphicsStyle element) for the left line of the cell border.



Get: BorderLeftLineStyle(self: TableCellStyle) -> ElementId



Set: BorderLeftLineStyle(self: TableCellStyle)=value

"""

 BorderRightLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id (GraphicsStyle element) for the right line of the cell border.



Get: BorderRightLineStyle(self: TableCellStyle) -> ElementId



Set: BorderRightLineStyle(self: TableCellStyle)=value

"""

 BorderTopLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id (GraphicsStyle element) for the top line of the cell border.



Get: BorderTopLineStyle(self: TableCellStyle) -> ElementId



Set: BorderTopLineStyle(self: TableCellStyle)=value

"""

 FontHorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The horizontal alignment style of text font.



Get: FontHorizontalAlignment(self: TableCellStyle) -> HorizontalAlignmentStyle



Set: FontHorizontalAlignment(self: TableCellStyle)=value

"""

 FontName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The font used for this style



Get: FontName(self: TableCellStyle) -> str



Set: FontName(self: TableCellStyle)=value

"""

 FontVerticalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vertical alignment style of text font.



Get: FontVerticalAlignment(self: TableCellStyle) -> VerticalAlignmentStyle



Set: FontVerticalAlignment(self: TableCellStyle)=value

"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the status whether this cell is enabled.



Get: IsEnabled(self: TableCellStyle) -> bool



Set: IsEnabled(self: TableCellStyle)=value

"""

 IsFontBold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the text font is set to bold of this cell.



Get: IsFontBold(self: TableCellStyle) -> bool



Set: IsFontBold(self: TableCellStyle)=value

"""

 IsFontItalic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the text font is set to italic of this cell.



Get: IsFontItalic(self: TableCellStyle) -> bool



Set: IsFontItalic(self: TableCellStyle)=value

"""

 IsFontUnderline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the text font is set to Underline of this cell.



Get: IsFontUnderline(self: TableCellStyle) -> bool



Set: IsFontUnderline(self: TableCellStyle)=value

"""

 IsInactivePhaseload=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether this is an inactive phase load cell.



Get: IsInactivePhaseload(self: TableCellStyle) -> bool



Set: IsInactivePhaseload(self: TableCellStyle)=value

"""

 IsOverridden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the cell is overridden or not.



Get: IsOverridden(self: TableCellStyle) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether this cell is read only.



Get: IsReadOnly(self: TableCellStyle) -> bool



Set: IsReadOnly(self: TableCellStyle)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TableCellStyle) -> bool



"""

 SheetBackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The background color of this cell in the sheet view.



Get: SheetBackgroundColor(self: TableCellStyle) -> Color



"""

 TextColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text color of this cell.



Get: TextColor(self: TableCellStyle) -> Color



Set: TextColor(self: TableCellStyle)=value

"""

 TextOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The orientation of the cell (for vertical/horizontal text) with input in degrees multiplied by 10



Get: TextOrientation(self: TableCellStyle) -> int



Set: TextOrientation(self: TableCellStyle)=value

"""

 TextSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text size.



Get: TextSize(self: TableCellStyle) -> float



Set: TextSize(self: TableCellStyle)=value

"""



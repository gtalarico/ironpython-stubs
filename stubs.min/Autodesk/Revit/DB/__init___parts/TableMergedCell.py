class TableMergedCell(object,IDisposable):
 """
 The TableMergedCell class defines a merged area of the upper-left and lower-right of a table grid.
 
 TableMergedCell(top: int,left: int,bottom: int,right: int)
 TableMergedCell()
 """
 def Dispose(self):
  """ Dispose(self: TableMergedCell) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TableMergedCell,disposing: bool) """
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
 def __new__(self,top=None,left=None,bottom=None,right=None):
  """
  __new__(cls: type,top: int,left: int,bottom: int,right: int)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the row index of the bottom-right corner of a table grid.

Get: Bottom(self: TableMergedCell) -> int

Set: Bottom(self: TableMergedCell)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TableMergedCell) -> bool

"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the column index of the top-left corner of a table grid.

Get: Left(self: TableMergedCell) -> int

Set: Left(self: TableMergedCell)=value
"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the column index of the bottom-right corner of a table grid.

Get: Right(self: TableMergedCell) -> int

Set: Right(self: TableMergedCell)=value
"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the row index of the top-left corner of a table grid.

Get: Top(self: TableMergedCell) -> int

Set: Top(self: TableMergedCell)=value
"""



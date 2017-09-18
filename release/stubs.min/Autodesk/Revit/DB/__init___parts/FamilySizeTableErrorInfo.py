class FamilySizeTableErrorInfo(object,IDisposable):
 """
 Error information generated from the CSV file import of a FamilySizeTable.

 

 FamilySizeTableErrorInfo()
 """
 def Dispose(self):
  """ Dispose(self: FamilySizeTableErrorInfo) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FamilySizeTableErrorInfo,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FamilySizeTableErrorType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The error type.



Get: FamilySizeTableErrorType(self: FamilySizeTableErrorInfo) -> FamilySizeTableErrorType



"""

 FilePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path of the imported CSV file.



Get: FilePath(self: FamilySizeTableErrorInfo) -> str



"""

 InvalidColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the invalid column.



Get: InvalidColumnIndex(self: FamilySizeTableErrorInfo) -> int



"""

 InvalidHeaderText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The invalid header text.



Get: InvalidHeaderText(self: FamilySizeTableErrorInfo) -> str



"""

 InvalidRowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the invalid row.



Get: InvalidRowIndex(self: FamilySizeTableErrorInfo) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FamilySizeTableErrorInfo) -> bool



"""



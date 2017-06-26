class ViewScheduleExportOptions(object,IDisposable):
 """
 The export options used to export schedule views.
 
 ViewScheduleExportOptions()
 ViewScheduleExportOptions(other: ViewScheduleExportOptions)
 """
 def Dispose(self):
  """ Dispose(self: ViewScheduleExportOptions) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ViewScheduleExportOptions,disposing: bool) """
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
  __new__(cls: type)
  __new__(cls: type,other: ViewScheduleExportOptions)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ColumnHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How to export column headers. Default is MultipleRows.

Get: ColumnHeaders(self: ViewScheduleExportOptions) -> ExportColumnHeaders

Set: ColumnHeaders(self: ViewScheduleExportOptions)=value
"""

 FieldDelimiter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How to delimit fields. Default is Tab.

Get: FieldDelimiter(self: ViewScheduleExportOptions) -> str

Set: FieldDelimiter(self: ViewScheduleExportOptions)=value
"""

 HeadersFootersBlanks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether to export group headers,footers,and blank lines. Default is true.

Get: HeadersFootersBlanks(self: ViewScheduleExportOptions) -> bool

Set: HeadersFootersBlanks(self: ViewScheduleExportOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ViewScheduleExportOptions) -> bool

"""

 TextQualifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How to qualify text fields. Default is DoubleQuote.

Get: TextQualifier(self: ViewScheduleExportOptions) -> ExportTextQualifier

Set: TextQualifier(self: ViewScheduleExportOptions)=value
"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to export the schedule title. Default is true.

Get: Title(self: ViewScheduleExportOptions) -> bool

Set: Title(self: ViewScheduleExportOptions)=value
"""



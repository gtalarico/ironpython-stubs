class DWFImportOptions(object,IDisposable):
 """
 The import options used by importing DWF or DWFx format file.

 

 DWFImportOptions(option: DWFImportOptions)

 DWFImportOptions(views: IList[ElementId])
 """
 def Dispose(self):
  """ Dispose(self: DWFImportOptions) """
  pass
 def GetSheetViews(self):
  """
  GetSheetViews(self: DWFImportOptions) -> IList[ElementId]

  

   Get sheet views where DWF markups are imported.

   Returns: An array of sheet views
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DWFImportOptions,disposing: bool) """
  pass
 def SetSheetViews(self,sheetViews):
  """ SetSheetViews(self: DWFImportOptions,sheetViews: IList[ElementId]) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,option: DWFImportOptions)

  __new__(cls: type,views: IList[ElementId])
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: DWFImportOptions) -> bool



"""



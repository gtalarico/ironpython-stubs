class ExportLayerKey(object,IDisposable):
 """
 A key used to represent an item stored in an Autodesk.Revit.DB.ExportLayerTable.
 
 ExportLayerKey(categoryName: str,subCategoryName: str,num: SpecialType)
 ExportLayerKey()
 """
 def Dispose(self):
  """ Dispose(self: ExportLayerKey) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportLayerKey,disposing: bool) """
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
 def __new__(self,categoryName=None,subCategoryName=None,num=None):
  """
  __new__(cls: type,categoryName: str,subCategoryName: str,num: SpecialType)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The category name.

Get: CategoryName(self: ExportLayerKey) -> str

Set: CategoryName(self: ExportLayerKey)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLayerKey) -> bool

"""

 SpecialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The special type for layer key.

Get: SpecialType(self: ExportLayerKey) -> SpecialType

Set: SpecialType(self: ExportLayerKey)=value
"""

 SubCategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The subcategrory Name.

Get: SubCategoryName(self: ExportLayerKey) -> str

Set: SubCategoryName(self: ExportLayerKey)=value
"""



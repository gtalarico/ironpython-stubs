class FamilySizeTableManager(object,IDisposable):
 """ Manages importing,exporting,and querying size data through the FamilySizeTable class. """
 @staticmethod
 def CreateFamilySizeTableManager(document,familyId):
  """
  CreateFamilySizeTableManager(document: Document,familyId: ElementId) -> bool
  
   Adds FamilySizeTableManager to a Family.
     A FamilySizeTableManager and 
    FamilySizeTables are only needed when
     importing,exporting,or removing 
    size data previously stored in CSV files.
  
  
   document: Family owned document or project document.
   familyId: ElementId of the Family.
   Returns: True if successful,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FamilySizeTableManager) """
  pass
 def ExportSizeTable(self,tableName,filePath):
  """
  ExportSizeTable(self: FamilySizeTableManager,tableName: str,filePath: str) -> bool
  
   Exports the size table to  aCSV file.
  
   tableName: The bool name to export.
   filePath: The CSV file to export to.
   Returns: True if successful,false otherwise..
  """
  pass
 def GetAllSizeTableNames(self):
  """
  GetAllSizeTableNames(self: FamilySizeTableManager) -> IList[str]
  
   Get the FamilySizeTable names in a family.
   Returns: Array of size table names.
  """
  pass
 @staticmethod
 def GetFamilySizeTableManager(document,familyId):
  """
  GetFamilySizeTableManager(document: Document,familyId: ElementId) -> FamilySizeTableManager
  
   Gets a FamilySizeTableManager from a Family
  
   document: Family owned document or a project document
   familyId: ElementId of the  Family.
   Returns: The FamilySizeTableManager of the Family.
  """
  pass
 def GetSizeTable(self,tableName):
  """
  GetSizeTable(self: FamilySizeTableManager,tableName: str) -> FamilySizeTable
  
   Get a FamilySizeTable by name.
  
   tableName: The FamilySizeTable name.
   Returns: The FamilySizeTable of a given name.
  """
  pass
 def HasSizeTable(self,tableName):
  """
  HasSizeTable(self: FamilySizeTableManager,tableName: str) -> bool
  
   Checks if a FamilySizeTable of a given name exists.
  
   tableName: The name of the FamilySizeTable.
   Returns: True if the FamilySizeTable exists,false otherwise.
  """
  pass
 def ImportSizeTable(self,document,filePath,errorInfo):
  """
  ImportSizeTable(self: FamilySizeTableManager,document: Document,filePath: str,errorInfo: FamilySizeTableErrorInfo) -> bool
  
   Imports a FamilySizeTable from a CSV file.
  
   document: Family owned document or project document.
   filePath: The CSV file path.
   errorInfo: An error object to be written to if errors occur.
   Returns: True if successful,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FamilySizeTableManager,disposing: bool) """
  pass
 def RemoveSizeTable(self,tableName):
  """
  RemoveSizeTable(self: FamilySizeTableManager,tableName: str) -> bool
  
   Removes the FamilySizeTable of a given name.
  
   tableName: The FamilySizeTable name.
   Returns: True if successful,false otherwise.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilySizeTableManager) -> bool

"""

 NumberOfSizeTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of FamilySizeTables in a family.

Get: NumberOfSizeTables(self: FamilySizeTableManager) -> int

"""



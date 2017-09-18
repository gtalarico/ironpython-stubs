class BaseExportOptions(object,IDisposable):
 """ The base class for options used to export DWG,DXF and DGN format files. """
 def Dispose(self):
  """ Dispose(self: BaseExportOptions) """
  pass
 def GetExportFontTable(self):
  """
  GetExportFontTable(self: BaseExportOptions) -> ExportFontTable

  

   Gets font table.
  """
  pass
 def GetExportLayerTable(self):
  """
  GetExportLayerTable(self: BaseExportOptions) -> ExportLayerTable

  

   Gets the layer table.

   Returns: The layer table.
  """
  pass
 def GetExportLinetypeTable(self):
  """
  GetExportLinetypeTable(self: BaseExportOptions) -> ExportLinetypeTable

  

   Gets a copy of the line type table.

   Returns: The line type table.
  """
  pass
 def GetExportPatternTable(self):
  """
  GetExportPatternTable(self: BaseExportOptions) -> ExportPatternTable

  

   Gets a copy of the pattern table.

   Returns: The pattern table.
  """
  pass
 @staticmethod
 def GetPredefinedSetupNames(document):
  """
  GetPredefinedSetupNames(document: Document) -> IList[str]

  

   Returns a list of names of predefined setups of export options.

  

   document: A Revit document to retrieve names from.

   Returns: An array of strings representing names of predefined setups.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BaseExportOptions,disposing: bool) """
  pass
 def SetExportFontTable(self,fontTable):
  """
  SetExportFontTable(self: BaseExportOptions,fontTable: ExportFontTable)

   Sets font table to option.

  

   fontTable: The font table to be set.
  """
  pass
 def SetExportLayerTable(self,layerTable):
  """
  SetExportLayerTable(self: BaseExportOptions,layerTable: ExportLayerTable)

   Sets layer table back to option

  

   layerTable: The layer table to be set
  """
  pass
 def SetExportLinetypeTable(self,linetypeTable):
  """
  SetExportLinetypeTable(self: BaseExportOptions,linetypeTable: ExportLinetypeTable)

   Sets the line type table to use during export.

  

   linetypeTable: The line type table to be set.
  """
  pass
 def SetExportPatternTable(self,patternTable):
  """
  SetExportPatternTable(self: BaseExportOptions,patternTable: ExportPatternTable)

   Sets the pattern table to use during export.

  

   patternTable: The pattern table to be set.
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
 Colors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Export color mode.

   Default value is ExportColorMode.IndexColors.



Get: Colors(self: BaseExportOptions) -> ExportColorMode



Set: Colors(self: BaseExportOptions)=value

"""

 HatchPatternsFileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Custom hatch patterns (pat) file name.



Get: HatchPatternsFileName(self: BaseExportOptions) -> str



Set: HatchPatternsFileName(self: BaseExportOptions)=value

"""

 HideReferencePlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to hide reference planes.

   Default value is false.



Get: HideReferencePlane(self: BaseExportOptions) -> bool



Set: HideReferencePlane(self: BaseExportOptions)=value

"""

 HideScopeBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to hide the scope box.

   Default value is false.



Get: HideScopeBox(self: BaseExportOptions) -> bool



Set: HideScopeBox(self: BaseExportOptions)=value

"""

 HideUnreferenceViewTags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to hide unreference view tags.

   Default value is false.



Get: HideUnreferenceViewTags(self: BaseExportOptions) -> bool



Set: HideUnreferenceViewTags(self: BaseExportOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: BaseExportOptions) -> bool



"""

 LayerMapping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of a layer settings standard or filename (with custom layer settings).

   Valid standards are: DGNV7 (only for DGN),AIA,CP83,BS1192,and ISO13567.

   default value is "" (empty) which means if no value is set,

   if no value is set,Revit will use a default value according to the localization.



Get: LayerMapping(self: BaseExportOptions) -> str



Set: LayerMapping(self: BaseExportOptions)=value

"""

 PreserveCoincidentLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to preserve coincident lines.

   Default value is false.



Get: PreserveCoincidentLines(self: BaseExportOptions) -> bool



Set: PreserveCoincidentLines(self: BaseExportOptions)=value

"""

 PropOverrides=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How to export overridden object styles.

   Default value is PropOverrideMode.ByEntity.



Get: PropOverrides(self: BaseExportOptions) -> PropOverrideMode



Set: PropOverrides(self: BaseExportOptions)=value

"""



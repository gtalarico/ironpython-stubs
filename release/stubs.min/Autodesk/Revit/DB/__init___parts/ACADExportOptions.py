class ACADExportOptions(BaseExportOptions,IDisposable):
 """ The base class for options used to export DWG and DXF format files. """
 def Dispose(self):
  """ Dispose(self: BaseExportOptions,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BaseExportOptions,disposing: bool) """
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
 ACAPreference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The preferred way to generate geometry of ACA objects.

   Default value is ACAObjectPreference.Object.



Get: ACAPreference(self: ACADExportOptions) -> ACAObjectPreference



Set: ACAPreference(self: ACADExportOptions)=value

"""

 ExportingAreas=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export area and room geometry,false otherwise.

   Default value is false.



Get: ExportingAreas(self: ACADExportOptions) -> bool



Set: ExportingAreas(self: ACADExportOptions)=value

"""

 ExportOfSolids=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The mode used to export solids in 3D views.

   Default value is SolidGeometry.Polymesh.



Get: ExportOfSolids(self: ACADExportOptions) -> SolidGeometry



Set: ExportOfSolids(self: ACADExportOptions)=value

"""

 FileVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ACADVersion::Default

   Default value is ACADVersion.Default.



Get: FileVersion(self: ACADExportOptions) -> ACADVersion



Set: FileVersion(self: ACADExportOptions)=value

"""

 LineScaling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The scaling mode for the line type.

   Default value is LineScaling.ViewScale.



Get: LineScaling(self: ACADExportOptions) -> LineScaling



Set: LineScaling(self: ACADExportOptions)=value

"""

 LinetypesFileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The custom linetype file name (*.lin).

   Default value is empty.



Get: LinetypesFileName(self: ACADExportOptions) -> str



Set: LinetypesFileName(self: ACADExportOptions)=value

"""

 MarkNonplotLayers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true and the nonplot layer suffix is not empty,all layers whose names contain that suffix will be marked as non-plot.



Get: MarkNonplotLayers(self: ACADExportOptions) -> bool



Set: MarkNonplotLayers(self: ACADExportOptions)=value

"""

 NonplotSuffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If the MarkNonplotLayers attribute is set to true,all layers with names containing this suffix will be marked as non-plot.

   No action will be performed if the suffix is empty.



Get: NonplotSuffix(self: ACADExportOptions) -> str



Set: NonplotSuffix(self: ACADExportOptions)=value

"""

 SharedCoords=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to use the shared coordinate system's origin,false to use the project origin.

   Default value is false.



Get: SharedCoords(self: ACADExportOptions) -> bool



Set: SharedCoords(self: ACADExportOptions)=value

"""

 TargetUnit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The target unit type.

   Default value is ExportUnit.Default.



Get: TargetUnit(self: ACADExportOptions) -> ExportUnit



Set: TargetUnit(self: ACADExportOptions)=value

"""

 TextTreatment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text treatment.

   Deault value is TextTreatment.Exact.



Get: TextTreatment(self: ACADExportOptions) -> TextTreatment



Set: TextTreatment(self: ACADExportOptions)=value

"""



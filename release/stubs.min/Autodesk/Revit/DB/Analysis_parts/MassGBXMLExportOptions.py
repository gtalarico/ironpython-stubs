class MassGBXMLExportOptions(object,IDisposable):
 """
 Options used when exporting a gbXML file from a mass model document.

 

 MassGBXMLExportOptions(massZoneIds: IList[ElementId])

 MassGBXMLExportOptions(massZoneIds: IList[ElementId],massIds: IList[ElementId])
 """
 def Dispose(self):
  """ Dispose(self: MassGBXMLExportOptions) """
  pass
 def GetMassIds(self):
  """
  GetMassIds(self: MassGBXMLExportOptions) -> IList[ElementId]

  

   Gets a list of masses to use as shading surfaces in the exported gbXML--these 

    masses must not have mass floors or mass zones so as not to end up with 

    duplicate surface information in the gbXML output.

  

   Returns: The ids of the masses.
  """
  pass
 def GetMassZoneIds(self):
  """
  GetMassZoneIds(self: MassGBXMLExportOptions) -> IList[ElementId]

  

   Gets a list of mass zones to analyze in the exported gbXML.

   Returns: The ids of the mass zone.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MassGBXMLExportOptions,disposing: bool) """
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
 def __new__(self,massZoneIds,massIds=None):
  """
  __new__(cls: type,massZoneIds: IList[ElementId])

  __new__(cls: type,massZoneIds: IList[ElementId],massIds: IList[ElementId])
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: MassGBXMLExportOptions) -> bool



"""



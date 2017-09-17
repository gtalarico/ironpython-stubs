class ExportUtils(object):
 """ This class provides utilities related to document export. """
 @staticmethod
 def GetExportId(document,elementId):
  """
  GetExportId(document: Document,elementId: ElementId) -> Guid
  
   Retrieves the GUID representing this element in DWF and IFC export.
  
   document: The document.
   elementId: The id of the element.
   Returns: The value of the GUID representing the element in the export context.
  """
  pass
 @staticmethod
 def GetGBXMLDocumentId(document):
  """
  GetGBXMLDocumentId(document: Document) -> Guid
  
   Retrieves the GUID representing this document in exported gbXML files.
  
   document: The document.
   Returns: The value of the GUID representing this document in gbXML export.
  """
  pass
 @staticmethod
 def GetNurbsSurfaceDataForFace(face):
  """
  GetNurbsSurfaceDataForFace(face: Face) -> NurbsSurfaceData
  
   Returns the necessary information to define a NURBS surface for a given Revit 
    HermiteFace or RuledFace.
  
  
   face: The HermiteFace or RuledFace to be converted.
   Returns: A class containing the necessary data to define a NURBS surface.
  """
  pass
 __all__=[
  'GetExportId',
  'GetGBXMLDocumentId',
  'GetNurbsSurfaceDataForFace',
 ]


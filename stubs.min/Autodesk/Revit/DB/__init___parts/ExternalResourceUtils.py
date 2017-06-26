class ExternalResourceUtils(object):
 """ A utility class containing functions related to external resource references. """
 @staticmethod
 def GetAllExternalResourceReferences(document,resourceType=None):
  """
  GetAllExternalResourceReferences(document: Document) -> ISet[ElementId]
  
   Gets the ids of all elements which refer to external resources.
  
   document: The Revit Document containing the external resource references.
   Returns: The ids of all elements which refer to external resources.
  GetAllExternalResourceReferences(document: Document,resourceType: ExternalResourceType) -> ISet[ElementId]
  
   Gets the ids of all elements which refer to a specific type of external 
    resource.
  
  
   document: The Revit Document containing the external resource references.
   resourceType: The type of external resource.
   Returns: The ids of all elements which refer to external resources of the specified type.
  """
  pass
 __all__=[
  'GetAllExternalResourceReferences',
 ]


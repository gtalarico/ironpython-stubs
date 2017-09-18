class ExternalFileUtils(object):
 """ A utility class containing functions related to external file references. """
 @staticmethod
 def GetAllExternalFileReferences(aDoc):
  """
  GetAllExternalFileReferences(aDoc: Document) -> ICollection[ElementId]

  

   Gets the ids of all elements which are external file references.

  

   aDoc: A Revit Document.

   Returns: The ids of all elements which are external file references.
  """
  pass
 @staticmethod
 def GetExternalFileReference(aDoc,elemId):
  """
  GetExternalFileReference(aDoc: Document,elemId: ElementId) -> ExternalFileReference

  

   Gets the external file referencing data for the given element.

  

   aDoc: A Revit Document.

   elemId: The element whose external file reference we want.

   Returns: An object containing path and type information for the given element's external 

    file.
  """
  pass
 @staticmethod
 def IsExternalFileReference(aDoc,elemId):
  """
  IsExternalFileReference(aDoc: Document,elemId: ElementId) -> bool

  

   Determines whether the given element represents an external file.

  

   aDoc: A Revit Document.

   elemId: The element to be checked for an external file reference.

   Returns: True if the given element represents an external file; false otherwise.
  """
  pass
 __all__=[
  'GetAllExternalFileReferences',
  'GetExternalFileReference',
  'IsExternalFileReference',
 ]


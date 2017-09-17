class PropertySetLibrary(Element,IDisposable):
 """ A named collection of property sets. """
 def AddPropertySet(self,propertySetId):
  """
  AddPropertySet(self: PropertySetLibrary,propertySetId: ElementId)
   Adds a property set from the document to this library.
  
   propertySetId: Identifier of the property set to add.
  """
  pass
 def AddPropertySetWithName(self,propertySetId,name):
  """
  AddPropertySetWithName(self: PropertySetLibrary,propertySetId: ElementId,name: str)
   Adds a property set from the document to this library using an alternate name.
  
   propertySetId: Identifier of the property set to add.
   name: The alternate name to use for the property set in the library.
  """
  pass
 def AddToDocument(self,name,document,overwrite):
  """
  AddToDocument(self: PropertySetLibrary,name: str,document: Document,overwrite: bool) -> PropertySetElement
  
   Adds a property set from a library to the document.  The property set
     will 
    be available for use even if the library is unloaded.
  
  
   name: The name of the property set in the library to add to the document.
     Will 
    also become the name of the property set element created in the document.
  
   document: The document to which the property set will be added.
   overwrite: If true,any existing property set with the given name will be overwritten.
   Returns: The new PropertySetElement.
  """
  pass
 def AddToDocumentWithName(self,name,document,overwrite,addAsName):
  """
  AddToDocumentWithName(self: PropertySetLibrary,name: str,document: Document,overwrite: bool,addAsName: str) -> PropertySetElement
  
   Adds a property set from a library to the document.  The property set
     will 
    be available for use even if the library is unloaded.
  
  
   name: The name of the property set in the library to add to the document.
   document: The document to which the property set will be added.
   overwrite: If true,any existing property set with the given name will be overwritten.
   addAsName: The name to use for the new property set element in the document.
   Returns: The new PropertySetElement.
  """
  pass
 @staticmethod
 def Create(document):
  """
  Create(document: Document) -> PropertySetLibrary
  
   Creates a new property set library in the given document.
  
   document: The document in which to create the new property set library.
   Returns: The new PropertySetLibrary.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def ExportXml(self,fileName):
  """
  ExportXml(self: PropertySetLibrary,fileName: str) -> bool
  
   Export this property set library to an external,XML-based file.
  
   fileName: Name of the file to write.
   Returns: True if the export succeeded,otherwise false.
  """
  pass
 @staticmethod
 def Find(doc,name):
  """
  Find(doc: Document,name: str) -> ElementId
  
   Finds an existing PropertySetLibrary with a given name.
  
   doc: The document in which to look for PropertySetLibrary elements with the given 
    name.
  
   name: The name to search for.
   Returns: Identifier of the PropertySetLibrary with the given name,or
     
    invalidElementId if no library with that name exists.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetName(self):
  """
  GetName(self: PropertySetLibrary) -> str
  
   Gets the name of the property set library.
  """
  pass
 def HasPropertySet(self,name):
  """
  HasPropertySet(self: PropertySetLibrary,name: str) -> bool
  
   Determines whether the library has a property set with a given name.
  
   name: The property set name to look for.
   Returns: True if the library contains a property set with the given name,otherwise 
    false.
  """
  pass
 @staticmethod
 def ImportXml(document,fileName,overwriteExisting):
  """
  ImportXml(document: Document,fileName: str,overwriteExisting: bool) -> PropertySetLibrary
  
   Import an external property set library into a Revit document.
  
   document: The document.
   fileName: Full path to a file containing a property set library definition.
   overwriteExisting: If true,any name conflicts will be resolved by overwriting existing
     
    libraries in the document with those being imported.
  
   Returns: The new PropertySetLibrary.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemovePropertySet(self,name):
  """
  RemovePropertySet(self: PropertySetLibrary,name: str) -> bool
  
   Removes a property set with a given name from the library.
  
   name: The name of the property set name to remove.
   Returns: True if a property set with the given name was found and removed,otherwise 
    false.
  """
  pass
 def RenamePropertySet(self,name,newName):
  """
  RenamePropertySet(self: PropertySetLibrary,name: str,newName: str) -> bool
  
   Renames a property set in the library.
  
   name: The name of the existing property set name to rename.
   newName: The new name for the property set.
   Returns: True if the property set was found and renamed,otherwise false.
  """
  pass
 def RenameSubclass(self,oldSubclass,newSubclass):
  """
  RenameSubclass(self: PropertySetLibrary,oldSubclass: str,newSubclass: str) -> int
  
   Changes the subclass field of all property sets in this library from one value 
    to another.
  
  
   oldSubclass: The existing subclass to rename.
   newSubclass: The new subclass applied to all property sets matching the given oldSubclass.
   Returns: The number of property sets whose subclass was changed.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetName(self,name):
  """
  SetName(self: PropertySetLibrary,name: str)
   Sets the name of the property set library.
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
 Locked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether a property set library is locked into a document or not.
   Locked libraries are read-only and cannot be removed.

Get: Locked(self: PropertySetLibrary) -> bool

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether a property set library is read-only or not.
   Read-only libraries cannot be renamed,or added to.

Get: ReadOnly(self: PropertySetLibrary) -> bool

Set: ReadOnly(self: PropertySetLibrary)=value
"""



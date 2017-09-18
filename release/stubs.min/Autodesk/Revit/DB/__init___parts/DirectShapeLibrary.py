class DirectShapeLibrary(object,IDisposable):
 """
 DirectShapeLibrary is used to store pre-created geometry for further referencing via the definition/instance mechanism.

    It is not persistent: the scope of a library object is usually a single data creation session.

    DirectShape::createGeometryInstance and DirectShape::CreateElementInstance will use the current DirectShapeLibrary to

    look up the definitions.

    store a collection of GNodes as definition

    end class DirectShapeDefinition
 """
 def AddDefinition(self,id,*__args):
  """
  AddDefinition(self: DirectShapeLibrary,id: str,GNode: GeometryObject)

   Add a definition to be reused by instances. A definition is a single geometry 

    object.

  

  

   id: ID of the definition to be added. Must be unique.

   GNode: Definition as a single Geometry object

  AddDefinition(self: DirectShapeLibrary,id: str,GNodes: IList[GeometryObject])
  """
  pass
 def AddDefinitionType(self,id,typeId):
  """
  AddDefinitionType(self: DirectShapeLibrary,id: str,typeId: ElementId)

   Add a definition to be reused by instances. Adding a definition type will 

    change how the instances are created.

     When asked to create a definition,

    the library object will look for a corresponding type object.

     If one is 

    found,it will create an instance of geometry stored in the type object. If it 

    is not found,

     the library will look for a list of geometry objects stored 

    as definition,and will copy and transform these

     to create an instance.

  

  

   id: ID of the definition to be added. Must be unique.

   typeId: Element id of the DirectShapeType element that will be used as a definition.
  """
  pass
 def Contains(self,id):
  """
  Contains(self: DirectShapeLibrary,id: str) -> bool

  

   A quick check whether a definition already exists in the library. Checks for 

    stored geometry objects only.

  

  

   id: Definition id

   Returns: True if a geometry definition exists,false otherwise.
  """
  pass
 def ContainsType(self,name):
  """
  ContainsType(self: DirectShapeLibrary,name: str) -> bool

  

   A quick check whether a definition type already exists in the library. Checks 

    for type objects only.

  

  

   name: Definition id

   Returns: True if a geometry definition exists,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: DirectShapeLibrary) """
  pass
 def FindDefinition(self,id):
  """
  FindDefinition(self: DirectShapeLibrary,id: str) -> IList[GeometryObject]

  

   Find a definition by id

  

   id: Definition id. Expecected to be unique

   Returns: List of geometry objects that together define a shape
  """
  pass
 def FindDefinitionType(self,id):
  """
  FindDefinitionType(self: DirectShapeLibrary,id: str) -> ElementId

  

   Find a DirectShapeType element by definition id. The element will be used for 

    creating instances of that definition.

  

  

   id: Definition id. Expected to be unique.

   Returns: Element id of a DirectShapeTypeElement
  """
  pass
 @staticmethod
 def GetDirectShapeLibrary(ADoc):
  """
  GetDirectShapeLibrary(ADoc: Document) -> DirectShapeLibrary

  

   Get the currently active Library object
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DirectShapeLibrary,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: DirectShapeLibrary)

   Removes all definitions from library. This is useful when importing several 

    self-contained data sets within one session.

     Once a data set is imported,

    keeping the definitions specific to that data set will slow down the searches.
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



Get: IsValidObject(self: DirectShapeLibrary) -> bool



"""



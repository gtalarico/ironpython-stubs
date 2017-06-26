class DirectShapeType(ElementType,IDisposable):
 """ The type element associated with a DirectShape element. This element includes data reused by DirectShape elements of the same type. """
 def AppendShape(self,*__args):
  """
  AppendShape(self: DirectShapeType,pGeomArr: IList[GeometryObject])AppendShape(self: DirectShapeType,pGeomArr: IList[GeometryObject],viewType: DirectShapeTargetViewType)AppendShape(self: DirectShapeType,ShapeBuilder: ShapeBuilder)
   Append shape built by the supplied ShapeBuilderObject to shape representation 
    stored in this DirectShapeType.
     The data stored in the supplied 
    ShapeBuilder object will be cleared.
  
  
   ShapeBuilder: The ShapeBuilder object that was used to build the shape to be appended.
  """
  pass
 @staticmethod
 def Create(document,name,categoryId):
  """
  Create(document: Document,name: str,categoryId: ElementId) -> DirectShapeType
  
   Creates a DirectShapeType element.
  
   document: The document that will contain the new element.
   name: Name of the DirectShapeType.
   categoryId: Id of the category assigned to this DirectShapeType. Must be a valid category 
    id.
  
   Returns: The new DirectShapeType.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsValidShape(self,shape,viewType=None):
  """
  IsValidShape(self: DirectShapeType,shape: IList[GeometryObject]) -> bool
  IsValidShape(self: DirectShapeType,shape: IList[GeometryObject],viewType: DirectShapeTargetViewType) -> bool
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetShape(self,*__args):
  """
  SetShape(self: DirectShapeType,pGeomArr: IList[GeometryObject])SetShape(self: DirectShapeType,pBuilder: ShapeBuilder)
   Sets the shape of this object to the one accumulated in the supplied Builder 
    object.
     If the new shape is identical to the old one,the old shape will be 
    kept.
  
  
   pBuilder: A ShapeBuilder object that was used to successfully build geometry to store in 
    this DirectShapeType. The built shape will be
     transferred to the 
    DirectShapeType,and the ShapeBuilder object will be reset.
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

class AssemblyInstance(Element,IDisposable):
 """ Combines multiple elements for tagging,filtering,scheduling and creating isolated assembly views. """
 def AddMemberIds(self,memberIds):
  """ AddMemberIds(self: AssemblyInstance,memberIds: ICollection[ElementId]) """
  pass
 def AllowsAssemblyViewCreation(self):
  """
  AllowsAssemblyViewCreation(self: AssemblyInstance) -> bool
  
   Returns true if assembly views can be created for this Assembly Instance.
  """
  pass
 @staticmethod
 def AreElementsValidForAssembly(document,assemblyMemberIds,assemblyId):
  """ AreElementsValidForAssembly(document: Document,assemblyMemberIds: ICollection[ElementId],assemblyId: ElementId) -> bool """
  pass
 @staticmethod
 def CanRemoveElementsFromAssembly(assemblyInstance,memberIds):
  """ CanRemoveElementsFromAssembly(assemblyInstance: AssemblyInstance,memberIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def CompareAssemblyInstances(instance1,instance2):
  """
  CompareAssemblyInstances(instance1: AssemblyInstance,instance2: AssemblyInstance) -> AssemblyDifference
  
   Compares two assembly instances and returns a result with details about the 
    differences
  
  
   instance1: The first assembly instance to compare
   instance2: the second assembly instance to compare
   Returns: An object describing the difference between the two instances
  """
  pass
 @staticmethod
 def Create(document,assemblyMemberIds,namingCategoryId):
  """ Create(document: Document,assemblyMemberIds: ICollection[ElementId],namingCategoryId: ElementId) -> AssemblyInstance """
  pass
 def Disassemble(self):
  """
  Disassemble(self: AssemblyInstance) -> ICollection[ElementId]
  
   Removes the assembly instance and releases the member elements.
   Returns: ids of elements previously under the assembly instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCenter(self):
  """
  GetCenter(self: AssemblyInstance) -> XYZ
  
   Returns the center of the bounding box for the assembly instance.
     This is 
    the default position for placed assembly instances.
  
   Returns: The position for the center of the assembly instance.
  """
  pass
 def GetMemberIds(self):
  """
  GetMemberIds(self: AssemblyInstance) -> ICollection[ElementId]
  
   Gets member element ids for the assembly instance.
   Returns: Element ids for the members of the assembly instance.
  """
  pass
 def GetTransform(self):
  """
  GetTransform(self: AssemblyInstance) -> Transform
  
   Gets the origin of the assembly instance.
   Returns: The origin of the assembly instance.
  """
  pass
 @staticmethod
 def IsValidNamingCategory(document,namingCategoryId,assemblyMemberIds):
  """ IsValidNamingCategory(document: Document,namingCategoryId: ElementId,assemblyMemberIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def PlaceInstance(document,assemblyTypeId,location):
  """
  PlaceInstance(document: Document,assemblyTypeId: ElementId,location: XYZ) -> AssemblyInstance
  
   Places an assembly instance of a given assembly type at the specified location.
  
   document: The document for the new assembly instance.
   assemblyTypeId: The id of the assembly type to be used for the instance.
   location: The placement location for the instance in project coordinates.
   Returns: The newly created assembly instance.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveMemberIds(self,memberIds):
  """ RemoveMemberIds(self: AssemblyInstance,memberIds: ICollection[ElementId]) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetMemberIds(self,memberIds):
  """ SetMemberIds(self: AssemblyInstance,memberIds: ICollection[ElementId]) """
  pass
 def SetTransform(self,trf):
  """
  SetTransform(self: AssemblyInstance,trf: Transform)
   Sets the origin of the assembly instance.
  
   trf: Transform to be set.
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
 AssemblyTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name for the assembly type.
   All matching assembly instances share this name.
   Unique assembly instances are named automatically based on their naming category.

Get: AssemblyTypeName(self: AssemblyInstance) -> str

Set: AssemblyTypeName(self: AssemblyInstance)=value
"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to find the physical location of the assembly instance within project.

Get: Location(self: AssemblyInstance) -> Location

"""

 NamingCategoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the category that drives the default naming scheme for the assembly instance.

Get: NamingCategoryId(self: AssemblyInstance) -> ElementId

Set: NamingCategoryId(self: AssemblyInstance)=value
"""



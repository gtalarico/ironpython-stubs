class MeshFromGeometryOperationResult(object,IDisposable):
 """
 Describes what TessellatedShapeBuilder has

    built.
 """
 def Dispose(self):
  """ Dispose(self: MeshFromGeometryOperationResult) """
  pass
 def GetIssues(self):
  """
  GetIssues(self: MeshFromGeometryOperationResult) -> IList[MeshFromGeometryOperationIssue]

  

   Returns the array of issues encountered while building a mesh.

   Returns: Array of issues encountered while building a mesh.
  """
  pass
 def GetMesh(self):
  """
  GetMesh(self: MeshFromGeometryOperationResult) -> Mesh

  

   This returns a valid mesh only for the first call. Later calls

     will throw 

    an exception as the mesh is no longer valid in this object.

  

   Returns: Mesh which built.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MeshFromGeometryOperationResult,disposing: bool) """
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
 HasInvalidData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the provided data for which this result was

   obtained were internally inconsistent and could not be

   used in its entirety. For example,for extrusion

   operation,profile loops were degenerate

   or improperly oriented with respect to the extrsuion

   direction.



Get: HasInvalidData(self: MeshFromGeometryOperationResult) -> bool



"""

 IsMeshAvailable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Shows whether the result still contains the mesh

   which was constructed,if any,or whether it has been

   relinquished by 'getMesh'.

   The former is true,the later is false.



Get: IsMeshAvailable(self: MeshFromGeometryOperationResult) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: MeshFromGeometryOperationResult) -> bool



"""

 Tessellated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether while constructing a mesh,it was necessary

   to extrude polylines instead of non-linear curves

   from the profile loops.



Get: Tessellated(self: MeshFromGeometryOperationResult) -> bool



"""



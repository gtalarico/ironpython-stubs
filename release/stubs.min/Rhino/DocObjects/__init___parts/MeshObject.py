class MeshObject(RhinoObject):
 # no doc
 def DuplicateMeshGeometry(self):
  """ DuplicateMeshGeometry(self: MeshObject) -> Mesh """
  pass
 def SetMesh(self,*args):
  """
  SetMesh(self: MeshObject,mesh: Mesh) -> Mesh

  

   Only for developers who are defining custom subclasses of MeshObject.

     Directly sets 

    the internal mesh geometry for this object.  Note that

     this function does not work 

    with Rhino's "undo".

  

   Returns: The old mesh geometry that was set for this object
  """
  pass
 MeshGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MeshGeometry(self: MeshObject) -> Mesh



"""



class MeshFace(object):
 """
 Represents the values of the four indices of a mesh face quad.

    If the third and fourth values are the same,this face represents a

    triangle.

 

 MeshFace(a: int,b: int,c: int)

 MeshFace(a: int,b: int,c: int,d: int)
 """
 def Flip(self):
  """
  Flip(self: MeshFace) -> MeshFace

  

   Reverses the orientation of the face by swapping corners. 

     The first corner is 

    always maintained.
  """
  pass
 def IsValid(self,vertexCount=None):
  """
  IsValid(self: MeshFace,vertexCount: int) -> bool

  

   Gets a value indicating whether or not this mesh face 

     is considered to be valid. 

    Unlike the simple IsValid function,

     this function takes upper bound indices into 

    account.

  

  

   vertexCount: Number of vertices in the mesh that this face is a part of.

   Returns: true if the face is considered valid,false if not.

  IsValid(self: MeshFace) -> bool

  

   Gets a value indicating whether or not this mesh face 

     is considered to be valid. 

    Note that even valid mesh faces 

     could potentially be invalid in the context of a 

    specific Mesh,

     if one or more of the corner indices exceeds the number of 

      

      vertices on the mesh. If you want to perform a complete 

     validity check,use 

    IsValid(int) instead.
  """
  pass
 def Set(self,a,b,c,d=None):
  """
  Set(self: MeshFace,a: int,b: int,c: int,d: int)

   Sets all the corners for this face as a quad.

  

   a: Index of first corner.

   b: Index of second corner.

   c: Index of third corner.

   d: Index of fourth corner.

  Set(self: MeshFace,a: int,b: int,c: int)

   Sets all the corners for this face as a triangle.

  

   a: Index of first corner.

   b: Index of second corner.

   c: Index of third corner.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,a,b,c,d=None):
  """
  __new__[MeshFace]() -> MeshFace

  

  __new__(cls: type,a: int,b: int,c: int)

  __new__(cls: type,a: int,b: int,c: int,d: int)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 A=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first corner index of the mesh face.



Get: A(self: MeshFace) -> int



Set: A(self: MeshFace)=value

"""

 B=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the second corner index of the mesh face.



Get: B(self: MeshFace) -> int



Set: B(self: MeshFace)=value

"""

 C=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the third corner index of the mesh face.



Get: C(self: MeshFace) -> int



Set: C(self: MeshFace)=value

"""

 D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the fourth corner index of the mesh face. 

   If D equals C,the mesh face is considered to be a triangle 

   rather than a quad.



Get: D(self: MeshFace) -> int



Set: D(self: MeshFace)=value

"""

 IsQuad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this mesh face is a quad. 

   A mesh face is considered to be a triangle when C does not equal D,

   thus it is possible for an Invalid mesh face to also be a quad.



Get: IsQuad(self: MeshFace) -> bool



"""

 IsTriangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this mesh face is a triangle. 

   A mesh face is considered to be a triangle when C equals D,thus it is 

   possible for an Invalid mesh face to also be a triangle.



Get: IsTriangle(self: MeshFace) -> bool



"""


 Unset=None


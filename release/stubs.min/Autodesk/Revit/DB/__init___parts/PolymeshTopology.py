class PolymeshTopology(object,IDisposable):
 """ A class representing topology of a polymesh. """
 def Dispose(self):
  """ Dispose(self: PolymeshTopology) """
  pass
 def GetFacet(self,idx):
  """
  GetFacet(self: PolymeshTopology,idx: int) -> PolymeshFacet

  

   Returns a definition of one facet

  

   idx: A zero-based index of the facet

   Returns: An instance of PolymeshFacet that represents

     one facet defined by 3 

    vertices of the polymesh.
  """
  pass
 def GetFacets(self):
  """
  GetFacets(self: PolymeshTopology) -> IList[PolymeshFacet]

  

   Returns a definitions of all facets of the polymesh

   Returns: An array of PolymeshFacet instances,each of which represents

     one facet 

    defined by 3 vertices of the polymesh.
  """
  pass
 def GetNormal(self,idx):
  """
  GetNormal(self: PolymeshTopology,idx: int) -> XYZ

  

   Returns a normal vector at the given index

  

   idx: A zero-based index

   Returns: XYZ value representing a normal vector
  """
  pass
 def GetNormals(self):
  """
  GetNormals(self: PolymeshTopology) -> IList[XYZ]

  

   Returns all normals assigned to the polymesh

   Returns: An array of XYZ values,each representing a normal vector
  """
  pass
 def GetPoint(self,idx):
  """
  GetPoint(self: PolymeshTopology,idx: int) -> XYZ

  

   Returns one point at the given index.

  

   idx: A zero-based index of a polymesh point

   Returns: XYZ coordinates of the point
  """
  pass
 def GetPoints(self):
  """
  GetPoints(self: PolymeshTopology) -> IList[XYZ]

  

   Returns all points of the polymesh.

   Returns: An array of XYZ coordinates
  """
  pass
 def GetUV(self,idx):
  """
  GetUV(self: PolymeshTopology,idx: int) -> UV

  

   Returns one UV coordinate at the given index.

  

   idx: A zero-based index of a UV coordinate

   Returns: UV coordinates at the given index
  """
  pass
 def GetUVs(self):
  """
  GetUVs(self: PolymeshTopology) -> IList[UV]

  

   Returns all UV coordinates assigned to the polymesh

   Returns: An array of UV coordinates
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PolymeshTopology,disposing: bool) """
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
 DistributionOfNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the distribution of normal vectors along the tessellated polymesh surface.



Get: DistributionOfNormals(self: PolymeshTopology) -> DistributionOfNormals



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: PolymeshTopology) -> bool



"""

 NumberOfFacets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of facet in the polymesh.



Get: NumberOfFacets(self: PolymeshTopology) -> int



"""

 NumberOfNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of normals associated with the polymesh



Get: NumberOfNormals(self: PolymeshTopology) -> int



"""

 NumberOfPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of points in the polymesh



Get: NumberOfPoints(self: PolymeshTopology) -> int



"""

 NumberOfUVs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of UV coordinates available for the polymesh.



Get: NumberOfUVs(self: PolymeshTopology) -> int



"""



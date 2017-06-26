class FacetingUtils(object):
 """
 This class is used to convertTrianglesToQuads a triangulated structure into a structure in which some of the triangles
    have been consolidated into quadrilaterals.
 """
 @staticmethod
 def ConvertTrianglesToQuads(triangulation):
  """
  ConvertTrianglesToQuads(triangulation: TriangulationInterface) -> IList[TriOrQuadFacet]
  
   Replaces pairs of adjacent,coplanar triangles by quadrilaterals.
  
   triangulation: A triangulated face,shell,or solid.
   Returns: A collection of triangles and quadrilaterals representing the original 
    triangulated object.
  """
  pass
 __all__=[
  'ConvertTrianglesToQuads',
 ]


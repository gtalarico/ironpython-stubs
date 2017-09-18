class SpaceMorph(object):
 """ Represents a spacial,Euclidean morph. """
 @staticmethod
 def IsMorphable(geometry):
  """
  IsMorphable(geometry: GeometryBase) -> bool

  

   true if the geometry can be morphed by calling SpaceMorph.Morph(geometry)
  """
  pass
 def Morph(self,geometry):
  """
  Morph(self: SpaceMorph,geometry: GeometryBase) -> bool

  

   Apply the space morph to geometry.

  

   geometry: Geometry to morph.

   Returns: true on success,false on failure.
  """
  pass
 def MorphPoint(self,point):
  """
  MorphPoint(self: SpaceMorph,point: Point3d) -> Point3d

  

   Morphs an Euclidean point. This method is abstract.

  

   point: A point that will be morphed by this function.

   Returns: Resulting morphed point.
  """
  pass
 PreserveStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the morph should be done in a way that preserves the structure of the geometry.

   In particular,for NURBS objects,true means that only the control points are moved.

   The PreserveStructure value does not affect the way meshes and points are morphed.

   The default is false.



Get: PreserveStructure(self: SpaceMorph) -> bool



Set: PreserveStructure(self: SpaceMorph)=value

"""

 QuickPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the morph should be done as quickly as possible because the result

   is being used for some type of dynamic preview. If QuickPreview is true,

   the tolerance may be ignored.

   The QuickPreview value does not affect the way meshes and points are morphed.

   The default is false.



Get: QuickPreview(self: SpaceMorph) -> bool



Set: QuickPreview(self: SpaceMorph)=value

"""

 Tolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The desired accuracy of the morph. This value is primarily used for deforming

   surfaces and breps. The default is 0.0 and any value <= 0.0 is ignored by

   morphing functions. The Tolerance value does not affect the way meshes and points

   are morphed.



Get: Tolerance(self: SpaceMorph) -> float



Set: Tolerance(self: SpaceMorph)=value

"""



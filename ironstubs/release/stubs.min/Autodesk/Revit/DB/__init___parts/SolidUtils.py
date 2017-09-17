class SolidUtils(object):
 """ Contains utility functions for solid operations. """
 @staticmethod
 def Clone(solid):
  """
  Clone(solid: Solid) -> Solid
  
   Creates a new Solid which is a copy of the input Solid.
  
   solid: The input solid to be copied.
   Returns: The newly created Solid.
  """
  pass
 @staticmethod
 def CreateTransformed(solid,transform):
  """
  CreateTransformed(solid: Solid,transform: Transform) -> Solid
  
   Creates a new Solid which is the transformation of the input Solid.
  
   solid: The input solid to be transformed.
   transform: The transform (which must be conformal).
   Returns: The newly created Solid.
  """
  pass
 @staticmethod
 def IsValidForTessellation(solidOrShell):
  """
  IsValidForTessellation(solidOrShell: Solid) -> bool
  
   Tests if the input solid or shell is valid for tessellation.
  
   solidOrShell: The solid or shell.
   Returns: True if the solid or shell is valid for tessellation,false otherwise.
  """
  pass
 @staticmethod
 def SplitVolumes(solid):
  """
  SplitVolumes(solid: Solid) -> IList[Solid]
  
   Splits a solid geometry into several separate solids.
  
   solid: The solid.
   Returns: The split solid geometries.
  """
  pass
 @staticmethod
 def TessellateSolidOrShell(solidOrShell,tessellationControls):
  """
  TessellateSolidOrShell(solidOrShell: Solid,tessellationControls: SolidOrShellTessellationControls) -> TriangulatedSolidOrShell
  
   This function facets (i.e.,triangulates) a solid or an open shell. Each 
    boundary
     component of the solid or shell is represented by a single 
    triangulated structure.
  
  
   solidOrShell: The solid or shell to be faceted.
   tessellationControls: This input controls various aspects of the triangulation.
   Returns: The triangulated structures corresponding to the boundary components of the
     
    input solid or the components of the input shell.
  """
  pass
 __all__=[
  'Clone',
  'CreateTransformed',
  'IsValidForTessellation',
  'SplitVolumes',
  'TessellateSolidOrShell',
 ]


class GripObject(RhinoObject):
 # no doc
 def Move(self,*__args):
  """
  Move(self: GripObject,newLocation: Point3d)

   Moves the grip to a new location.

  

   newLocation: New location for grip.

  Move(self: GripObject,delta: Vector3d)

   Moves the grip to a new location.

  

   delta: Translation applied to the OriginalLocation point.

  Move(self: GripObject,xform: Transform)

   Moves the grip to a new location.

  

   xform: Transformation appliead to the OriginalLocation point.
  """
  pass
 def NeighborGrip(self,directionR,directionS,directionT,wrap):
  """
  NeighborGrip(self: GripObject,directionR: int,directionS: int,directionT: int,wrap: bool) -> GripObject

  

   Used to get a grip's logical neighbors,like NURBS curve,suface,

     and cage control 

    point grips.

  

  

   directionR: -1 to go back one grip,+1 to move forward one grip.  For curves,surfaces

     and 

    cages,this is the first parameter direction.

  

   directionS: -1 to go back one grip,+1 to move forward one grip.  For surfaces and

     cages this 

    is the second parameter direction.

  

   directionT: For cages this is the third parameter direction

   Returns: logical neighbor or null if the is no logical neighbor
  """
  pass
 def UndoMove(self):
  """
  UndoMove(self: GripObject)

   Undoes any grip moves made by calling Move.
  """
  pass
 CurrentLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentLocation(self: GripObject) -> Point3d



Set: CurrentLocation(self: GripObject)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Index(self: GripObject) -> int



"""

 Moved=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the grip has moved from OriginalLocation.



Get: Moved(self: GripObject) -> bool



"""

 OriginalLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OriginalLocation(self: GripObject) -> Point3d



"""

 OwnerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OwnerId(self: GripObject) -> Guid



"""

 Weight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The weight of a NURBS control point grip or RhinoMath.UnsetValue

   if the grip is not a NURBS control point grip.



Get: Weight(self: GripObject) -> float



Set: Weight(self: GripObject)=value

"""



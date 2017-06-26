class WallUtils(object):
 """ General Wall utility methods """
 @staticmethod
 def AllowWallJoinAtEnd(wall,end):
  """
  AllowWallJoinAtEnd(wall: Wall,end: int)
   Allows the wall's end to join to other walls. If that end is near other walls 
    it will become joined as a result.
  
  
   wall: The wall in question
   end: 0 or 1 for the beginning or end of the wall's curve
  """
  pass
 @staticmethod
 def DisallowWallJoinAtEnd(wall,end):
  """
  DisallowWallJoinAtEnd(wall: Wall,end: int)
   Sets the wall's end not to join to other walls.
  
   wall: The wall in question
   end: 0 or 1 for the beginning or end of the wall's curve
  """
  pass
 @staticmethod
 def IsWallJoinAllowedAtEnd(wall,end):
  """
  IsWallJoinAllowedAtEnd(wall: Wall,end: int) -> bool
  
   Identifies if the indicated end of the wall allows joins or not.
  
   wall: The wall in question
   end: 0 or 1 for the beginning or end of the wall's curve
   Returns: true if it is allowed to join. false if it is disallowed.
  """
  pass
 __all__=[
  'AllowWallJoinAtEnd',
  'DisallowWallJoinAtEnd',
  'IsWallJoinAllowedAtEnd',
 ]


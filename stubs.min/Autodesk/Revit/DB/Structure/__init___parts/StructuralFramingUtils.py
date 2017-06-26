class StructuralFramingUtils(object):
 """ A collection of Structural Framing Utilities. """
 @staticmethod
 def AllowJoinAtEnd(familyInstance,end):
  """
  AllowJoinAtEnd(familyInstance: FamilyInstance,end: int)
   Sets the indicated end of the framing element to be allowed to join to others.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category.
   end: The index of the end (0 for the start,1 for the end).
  """
  pass
 @staticmethod
 def CanFlipEnds(familyInstance):
  """
  CanFlipEnds(familyInstance: FamilyInstance) -> bool
  
   Determines if the ends of the given framing element can be flipped.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete.
  
   Returns: True for non-concrete line,arc or ellipse framing element,false otherwise.
  """
  pass
 @staticmethod
 def CanSetEndReference(familyInstance,end):
  """
  CanSetEndReference(familyInstance: FamilyInstance,end: int) -> bool
  
   Determines if a reference can be set for the given end of the framing element.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete and joined at the given end.
  
   end: The index of the end (0 for the start,1 for the end).
   Returns: True if reference can be set for the given end of the framing element.
  """
  pass
 @staticmethod
 def DisallowJoinAtEnd(familyInstance,end):
  """
  DisallowJoinAtEnd(familyInstance: FamilyInstance,end: int)
   Sets the indicated end of the framing element to not be allowed to join to 
    others.
  
  
   familyInstance: The FamilyInstance,which must be of a structural framing category.
   end: The index of the end (0 for the start,1 for the end).
  """
  pass
 @staticmethod
 def FlipEnds(familyInstance):
  """
  FlipEnds(familyInstance: FamilyInstance)
   Flips the ends of the structural framing element.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete.
  """
  pass
 @staticmethod
 def GetEndReference(familyInstance,end):
  """
  GetEndReference(familyInstance: FamilyInstance,end: int) -> Reference
  
   Returns a reference to the end of a framing element according to the setback 
    settings.
  
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete and joined.
  
   end: The index of the end (0 for the start,1 for the end).
   Returns: The end reference.
  """
  pass
 @staticmethod
 def IsEndReferenceValid(familyInstance,end,pick):
  """
  IsEndReferenceValid(familyInstance: FamilyInstance,end: int,pick: Reference) -> bool
  
   Determines if the given reference can be set for the given end of the framing 
    element.
  
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete and joined at the given end.
  
   end: The index of the end (0 for the start,1 for the end).
   pick: The reference to be checked against the given end of the framing element.
   Returns: True if the given reference can be set for the given end of the framing element.
  """
  pass
 @staticmethod
 def IsJoinAllowedAtEnd(familyInstance,end):
  """
  IsJoinAllowedAtEnd(familyInstance: FamilyInstance,end: int) -> bool
  
   Identifies if the indicated end of the framing element is allowed to join to 
    others.
  
  
   familyInstance: The FamilyInstance,which must be of a structural framing category.
   end: The index of the end (0 for the start,1 for the end).
   Returns: True if it is allowed to join. False if it is disallowed.
  """
  pass
 @staticmethod
 def RemoveEndReference(familyInstance,end):
  """
  RemoveEndReference(familyInstance: FamilyInstance,end: int)
   Resets the end reference of the structural framing element.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete and joined.
  
   end: The index of the end (0 for the start,1 for the end).
  """
  pass
 @staticmethod
 def SetEndReference(familyInstance,end,pick):
  """
  SetEndReference(familyInstance: FamilyInstance,end: int,pick: Reference)
   Sets the end reference of a framing element.
  
   familyInstance: The FamilyInstance,which must be of a structural framing category,
    non-concrete and joined.
  
   end: The index of the end (0 for the start,1 for the end).
   pick: The reference to set to the given end.
  """
  pass
 __all__=[
  'AllowJoinAtEnd',
  'CanFlipEnds',
  'CanSetEndReference',
  'DisallowJoinAtEnd',
  'FlipEnds',
  'GetEndReference',
  'IsEndReferenceValid',
  'IsJoinAllowedAtEnd',
  'RemoveEndReference',
  'SetEndReference',
 ]


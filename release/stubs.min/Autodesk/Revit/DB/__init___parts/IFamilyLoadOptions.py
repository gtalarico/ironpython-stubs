class IFamilyLoadOptions:
 """ An interface class which provide the callback for family load options. """
 def OnFamilyFound(self,familyInUse,overwriteParameterValues):
  """
  OnFamilyFound(self: IFamilyLoadOptions,familyInUse: bool) -> (bool,bool)

  

   A method called when the family was found in the target document.

  

   familyInUse: Indicates if one or more instances of the family is placed in the project.

   Returns: Return true to continue loading the family,false to cancel.
  """
  pass
 def OnSharedFamilyFound(self,sharedFamily,familyInUse,source,overwriteParameterValues):
  """
  OnSharedFamilyFound(self: IFamilyLoadOptions,sharedFamily: Family,familyInUse: bool) -> (bool,FamilySource,bool)

  

   A method called when the shared family was found in the target document.

  

   sharedFamily: The shared family in the current family document.

   familyInUse: Indicates if one or more instances of the family is placed in the project.

   Returns: Return true to continue loading the family,false to cancel.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

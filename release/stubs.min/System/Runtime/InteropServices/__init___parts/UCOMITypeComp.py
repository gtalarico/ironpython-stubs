class UCOMITypeComp:
 """ Use System.Runtime.InteropServices.ComTypes.ITypeComp instead. """
 def Bind(self,szName,lHashVal,wFlags,ppTInfo,pDescKind,pBindPtr):
  """
  Bind(self: UCOMITypeComp,szName: str,lHashVal: int,wFlags: Int16) -> (UCOMITypeInfo,DESCKIND,BINDPTR)

  

   Maps a name to a member of a type,or binds global variables and functions contained in a type 

    library.

  

  

   szName: The name to bind.

   lHashVal: A hash value for szName computed by LHashValOfNameSys.

   wFlags: A flags word containing one or more of the invoke flags defined in the INVOKEKIND enumeration.
  """
  pass
 def BindType(self,szName,lHashVal,ppTInfo,ppTComp):
  """
  BindType(self: UCOMITypeComp,szName: str,lHashVal: int) -> (UCOMITypeInfo,UCOMITypeComp)

  

   Binds to the type descriptions contained within a type library.

  

   szName: The name to bind.

   lHashVal: A hash value for szName determined by LHashValOfNameSys.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

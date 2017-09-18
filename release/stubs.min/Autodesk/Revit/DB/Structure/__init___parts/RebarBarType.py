class RebarBarType(ElementType,IDisposable):
 """ A Rebar type object that is used in the generation of Rebar """
 @staticmethod
 def Create(ADoc):
  """
  Create(ADoc: Document) -> RebarBarType

  

   Creates a new RebarBarType object
  """
  pass
 @staticmethod
 def CreateDefaultRebarBarType(ADoc):
  """
  CreateDefaultRebarBarType(ADoc: Document) -> ElementId

  

   Creates a new RebarBarType object with a default name.

  

   ADoc: The document.

   Returns: The newly created type id.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAutoCalcHookLengths(self,hookId):
  """
  GetAutoCalcHookLengths(self: RebarBarType,hookId: ElementId) -> bool

  

   Identifies if the hook lengths of a hook type are automatically calculated for 

    this bar type

  

  

   hookId: id of the hook type

   Returns: True if the hook lengths are automatically calculated,otherwise false
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetHookLength(self,hookId):
  """
  GetHookLength(self: RebarBarType,hookId: ElementId) -> float

  

   Identifies the hook length for a hook type

  

   hookId: id of the hook type

   Returns: The hook length for a hook type
  """
  pass
 def GetHookOffsetLength(self,hookId):
  """
  GetHookOffsetLength(self: RebarBarType,hookId: ElementId) -> float

  

   Identifies the hook offset length for a hook type

  

   hookId: id of the hook type

   Returns: The hook offset length for a hook type
  """
  pass
 def GetHookPermission(self,hookId):
  """
  GetHookPermission(self: RebarBarType,hookId: ElementId) -> bool

  

   Identifies if a hook type is permitted for this bar type

  

   hookId: id of the hook type

   Returns: True if the hook type is permitted for this bar type,otherwise false
  """
  pass
 def GetHookTangentLength(self,hookId):
  """
  GetHookTangentLength(self: RebarBarType,hookId: ElementId) -> float

  

   Identifies the hook tangent length for a hook type

  

   hookId: id of the hook type

   Returns: The hook tangent length for a hook type
  """
  pass
 def GetReinforcementRoundingManager(self):
  """
  GetReinforcementRoundingManager(self: RebarBarType) -> RebarRoundingManager

  

   Returns an object for managing reinforcement rounding override settings.

   Returns: The rounding manager.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetAutoCalcHookLengths(self,hookId,autoCalculated):
  """
  SetAutoCalcHookLengths(self: RebarBarType,hookId: ElementId,autoCalculated: bool)

   Identifies if the hook lengths of a hook type are automatically calculated for 

    this bar type

  

  

   hookId: id of the hook type

   autoCalculated: True if the hook lengths should be automatically calculated,otherwise false

    

     When it is false,default hook length and default hook offset length will be 

    reported
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetHookLength(self,hookId,hookLength):
  """
  SetHookLength(self: RebarBarType,hookId: ElementId,hookLength: float)

   Identifies the hook length for a hook type

  

   hookId: id of the hook type

   hookLength: The hook length for a hook type
  """
  pass
 def SetHookOffsetLength(self,hookId,newLength):
  """
  SetHookOffsetLength(self: RebarBarType,hookId: ElementId,newLength: float)

   Identifies the hook offset length for a hook type

  

   hookId: id of the hook type

   newLength: The hook offset length for a hook type
  """
  pass
 def SetHookPermission(self,hookId,permission):
  """
  SetHookPermission(self: RebarBarType,hookId: ElementId,permission: bool)

   Identifies if a hook type is permitted for this bar type

  

   hookId: id of the hook type

   permission: True if the hook type should be permitted for this bar type,otherwise false
  """
  pass
 def SetHookTangentLength(self,hookId,newLength):
  """
  SetHookTangentLength(self: RebarBarType,hookId: ElementId,newLength: float)

   Identifies the hook tangent length for a hook type

  

   hookId: id of the hook type

   newLength: The hook tangent length for a hook type
  """
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
 BarDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines bar diameter of rebar



Get: BarDiameter(self: RebarBarType) -> float



Set: BarDiameter(self: RebarBarType)=value

"""

 DeformationType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines bar deformation type.



Get: DeformationType(self: RebarBarType) -> RebarDeformationType



Set: DeformationType(self: RebarBarType)=value

"""

 MaximumBendRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines maximum bend radius of rebar



Get: MaximumBendRadius(self: RebarBarType) -> float



Set: MaximumBendRadius(self: RebarBarType)=value

"""

 StandardBendDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines bar bend diameter for rebar whose style is standard



Get: StandardBendDiameter(self: RebarBarType) -> float



Set: StandardBendDiameter(self: RebarBarType)=value

"""

 StandardHookBendDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines hook bend diameter for rebar whose style is standard



Get: StandardHookBendDiameter(self: RebarBarType) -> float



Set: StandardHookBendDiameter(self: RebarBarType)=value

"""

 StirrupTieBendDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines bar and hook bend diameter for rebar whose style is stirrup/tie



Get: StirrupTieBendDiameter(self: RebarBarType) -> float



Set: StirrupTieBendDiameter(self: RebarBarType)=value

"""



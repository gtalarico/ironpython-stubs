class RebarConstraint(object,IDisposable):
 """ A class representing a constraint on a handle of a rebar element. """
 def Dispose(self):
  """ Dispose(self: RebarConstraint) """
  pass
 def GetConstraintType(self):
  """
  GetConstraintType(self: RebarConstraint) -> RebarConstraintType
  
   Returns the RebarConstraintType of a RebarConstraint.
   Returns: The RebarConstraintType of the specified RebarConstraint.
  """
  pass
 def GetDistanceToTargetCover(self):
  """
  GetDistanceToTargetCover(self: RebarConstraint) -> float
  
   Returns the distance from the RebarConstrainedHandle to the target Host Cover 
    Element surface.
     The RebarConstraintType of the RebarConstraint must be 
    'ToCover.'
  """
  pass
 def GetDistanceToTargetHostFace(self):
  """
  GetDistanceToTargetHostFace(self: RebarConstraint) -> float
  
   Returns the distance from the RebarConstrainedHandle to the target Host Element 
    surface.
     The RebarConstraintType of the RebarConstraint must be 
    'FixedDistanceToHostFace.'
  """
  pass
 def GetRebarConstraintTargetHostFaceType(self):
  """
  GetRebarConstraintTargetHostFaceType(self: RebarConstraint) -> RebarConstraintTargetHostFaceType
  
   Returns the RebarConstraintTargetHostFaceType of the host Element face to which
    
     the RebarConstraint is attached.  The RebarConstraintType of the 
    RebarConstraint
     must be 'FixedDistanceToHostFace' or 'ToCover.'
  """
  pass
 def GetTargetElement(self):
  """
  GetTargetElement(self: RebarConstraint) -> Element
  
   Returns the Element object (either Host or Rebar) which provides the constraint.
  """
  pass
 def GetTargetHostFaceReference(self):
  """
  GetTargetHostFaceReference(self: RebarConstraint) -> Reference
  
   Returns a reference to the host Element face to which the RebarConstraint is 
    attached.
     The RebarConstraintType of the RebarConstraint must be 
    'FixedDistanceToHostFace' or 'ToCover.'
  
   Returns: Requested reference.
  """
  pass
 def GetTargetRebarAngleOnBarOrHookBend(self):
  """
  GetTargetRebarAngleOnBarOrHookBend(self: RebarConstraint) -> int
  
   Returns the angular increment along a bar or hook bend to which the 
    RebarConstraint is attached.
  
   Returns: The angular increment relative to the reference bar edge.
  """
  pass
 def GetTargetRebarBendNumber(self):
  """
  GetTargetRebarBendNumber(self: RebarConstraint) -> int
  
   Returns the number of the bend on the other Rebar Element to which this 
    RebarConstraint is attached.
     The RebarConstraint must be of 
    RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
     must 
    be 'BarBend.'
  """
  pass
 def GetTargetRebarConstraintType(self):
  """
  GetTargetRebarConstraintType(self: RebarConstraint) -> TargetRebarConstraintType
  
   Returns the TargetRebarConstraintType of the handle on the other Rebar Element
  
    to which this RebarConstraint is attached. The RebarConstraintType of the
    
     RebarConstraint must be 'ToOtherRebar.'
  """
  pass
 def GetTargetRebarEdgeNumber(self):
  """
  GetTargetRebarEdgeNumber(self: RebarConstraint) -> int
  
   Returns the number of the edge on the other Rebar Element to which this 
    RebarConstraint is attached.
     The RebarConstraint must be of 
    RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
     must 
    be 'Edge.'
  """
  pass
 def GetTargetRebarHookBarEnd(self):
  """
  GetTargetRebarHookBarEnd(self: RebarConstraint) -> int
  
   Returns 0 or 1 to indicate which end hook on the other Rebar Element to which 
    this RebarConstraint is attached.
     The RebarConstraint must be of 
    RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
     must 
    be 'HookBend.'
  """
  pass
 def HasAnEdgeNumber(self):
  """
  HasAnEdgeNumber(self: RebarConstraint) -> bool
  
   Checks if the getTargetRebarEdgeNumber method can be called for the 
    RebarConstraint.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: RebarConstraint,other: RebarConstraint) -> bool
  
   Returns true if the specified RebarConstraint is the same as 'this.'  The 
    method
     can be used to determine which of the RebarConstraint candidates 
    offered by the
     RebarConstraintsManager is currently active.
  """
  pass
 def IsFixedDistanceToHostFace(self):
  """
  IsFixedDistanceToHostFace(self: RebarConstraint) -> bool
  
   Returns true if the RebarConstraintType of the RebarConstraint is 
    'FixedDistanceToHostFace.'
  """
  pass
 def IsToCover(self):
  """
  IsToCover(self: RebarConstraint) -> bool
  
   Returns true if the RebarConstraintType of the RebarConstraint is 'ToCover.'
  """
  pass
 def IsToHostFaceOrCover(self):
  """
  IsToHostFaceOrCover(self: RebarConstraint) -> bool
  
   Returns true if the RebarConstraintType of the RebarConstraint is either 
    'FixedDistanceToHostFace' or 'ToCover.'
  """
  pass
 def IsToOtherRebar(self):
  """
  IsToOtherRebar(self: RebarConstraint) -> bool
  
   Returns true if the RebarConstraintType of the RebarConstraint is 
    'ToOtherRebar.'
  """
  pass
 def IsValid(self):
  """
  IsValid(self: RebarConstraint) -> bool
  
   Checks that the RebarConstraint still has access to valid Rebar constraint data
    
     and that its RebarConstraintsManager is still valid.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarConstraint,disposing: bool) """
  pass
 def SetDistanceToTargetCover(self,distanceToTargetCover):
  """
  SetDistanceToTargetCover(self: RebarConstraint,distanceToTargetCover: float)
   Sets the distance from the RebarConstrainedHandle to the target Host Cover 
    Element surface.
     The RebarConstraintType of the RebarConstraint must be 
    'ToCover.'
  
  
   distanceToTargetCover: The distance is given as an offset value,the sign of which depends on Host 
    Cover direction.
  """
  pass
 def SetDistanceToTargetHostFace(self,offset):
  """
  SetDistanceToTargetHostFace(self: RebarConstraint,offset: float)
   Sets the distance from the RebarConstrainedHandle to the target Host Element 
    surface.
     The RebarConstraintType of the RebarConstraint must be 
    'FixedDistanceToHostFace.'
  
  
   offset: The distance is given as an offset value,the sign of which depends on Host 
    Face direction.
  """
  pass
 def TargetIsBarBend(self):
  """
  TargetIsBarBend(self: RebarConstraint) -> bool
  
   Returns true if the RebarTargetConstraintType of the RebarConstraint is 
    'BarBend'
  """
  pass
 def TargetIsHookBend(self):
  """
  TargetIsHookBend(self: RebarConstraint) -> bool
  
   Returns true if the RebarTargetConstraintType of the RebarConstraint is 
    'HookBend'
  """
  pass
 def TargetRebarConstraintTypeIsEdge(self):
  """
  TargetRebarConstraintTypeIsEdge(self: RebarConstraint) -> bool
  
   Returns true if the RebarConstraintType of the RebarConstraint is 
    'ToOtherRebar,'
     and the RebarConstraint is attached to an edge of the other 
    Rebar Element.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarConstraint) -> bool

"""



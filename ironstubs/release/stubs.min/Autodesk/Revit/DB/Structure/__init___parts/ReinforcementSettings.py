class ReinforcementSettings(Element,IDisposable):
 """ Provides access to project-wide reinforcement settings. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFabricRoundingManager(self):
  """
  GetFabricRoundingManager(self: ReinforcementSettings) -> FabricRoundingManager
  
   Returns an object for managing reinforcement rounding override settings used by 
    FabricSheetType and FabricSheet elements.
  
   Returns: The rounding manager.
  """
  pass
 def GetRebarRoundingManager(self):
  """
  GetRebarRoundingManager(self: ReinforcementSettings) -> RebarRoundingManager
  
   Returns an object for managing reinforcement rounding override settings used by 
    RebarBarTypes,Rebar and RebarInSystem elements.
  
   Returns: The rounding manager.
  """
  pass
 def GetReinforcementAbbreviationTag(self,tagType):
  """
  GetReinforcementAbbreviationTag(self: ReinforcementSettings,tagType: ReinforcementAbbreviationTagType) -> str
  
   Gets one abbreviation tag for desired ReinforcementAbbreviationTagType.
  
   tagType: Defines the type of abbreviation tag.
   Returns: Abbreviation tag value
  """
  pass
 def GetReinforcementAbbreviationTags(self,objectType):
  """
  GetReinforcementAbbreviationTags(self: ReinforcementSettings,objectType: ReinforcementAbbreviationObjectType) -> IList[ReinforcementAbbreviationTag]
  
   Gets a list of abbreviation tags for desired reinforcement object type.
  
   objectType: Defines the type of desired reinforcement object for abbreviation tags.
   Returns: An array of ReinforcementAbbreviationTag that will define all abbreviations for 
    given reinforcement object.
  """
  pass
 @staticmethod
 def GetReinforcementSettings(cda):
  """
  GetReinforcementSettings(cda: Document) -> ReinforcementSettings
  
   Obtains the ReinforcementSettings object for the specified project document.
  
   cda: A project document.
   Returns: The ReinforcementSettings object.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: ReinforcementSettings,other: ReinforcementSettings) -> bool
  
   Checks if Reinforcement Settings is equal to other
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetReinforcementAbbreviationTag(self,tagType,abbreviationTag):
  """
  SetReinforcementAbbreviationTag(self: ReinforcementSettings,tagType: ReinforcementAbbreviationTagType,abbreviationTag: str)
   Sets one abbreviation tag for desired ReinforcementAbbreviationTagType.
  
   tagType: Defines the type of abbreviation tag.
   abbreviationTag: Abbreviation tag value to set.
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
 HostStructuralRebar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Host Structural Rebar within Area and Path Reinforcement with touching AtomHostStructuralRebar.

Get: HostStructuralRebar(self: ReinforcementSettings) -> bool

Set: HostStructuralRebar(self: ReinforcementSettings)=value
"""

 NumberVaryingLengthRebarsIndividually=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Use this option to modify the way varying length bars are numbered (individually or as a whole).

Get: NumberVaryingLengthRebarsIndividually(self: ReinforcementSettings) -> bool

Set: NumberVaryingLengthRebarsIndividually(self: ReinforcementSettings)=value
"""

 RebarPresentationInSection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default presentation mode for rebar sets,when:
   The view direction is perpendicular to the rebar normal and the rebar set is cut.The view direction is not perpendicular to the rebar normal and the view direction is not parallel to the rebar normal.

Get: RebarPresentationInSection(self: ReinforcementSettings) -> RebarPresentationMode

Set: RebarPresentationInSection(self: ReinforcementSettings)=value
"""

 RebarPresentationInView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default presentation mode for rebar sets,when the view direction is perpendicular to the rebar normal and the rebar set is not cut.

Get: RebarPresentationInView(self: ReinforcementSettings) -> RebarPresentationMode

Set: RebarPresentationInView(self: ReinforcementSettings)=value
"""

 RebarShapeDefinesEndTreatments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End Treatments are defined by Rebar Shape of Rebar element. Can be changed if document contains no rebars,area reinforcements and path reinforcements.

Get: RebarShapeDefinesEndTreatments(self: ReinforcementSettings) -> bool

Set: RebarShapeDefinesEndTreatments(self: ReinforcementSettings)=value
"""

 RebarShapeDefinesHooks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hooks are defined by Rebar Shape of Rebar element. Can be changed if document contains no rebars,area reinforcements and path reinforcements.

Get: RebarShapeDefinesHooks(self: ReinforcementSettings) -> bool

Set: RebarShapeDefinesHooks(self: ReinforcementSettings)=value
"""

 RebarVaryingLengthNumberSuffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A unique identifier used for a bar within a variable length rebar set.

Get: RebarVaryingLengthNumberSuffix(self: ReinforcementSettings) -> str

Set: RebarVaryingLengthNumberSuffix(self: ReinforcementSettings)=value
"""



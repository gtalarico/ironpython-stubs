class AdaptiveComponentInstanceUtils(object):
 """ An interface for Adaptive Component Instances. """
 @staticmethod
 def CreateAdaptiveComponentInstance(doc,famSymb):
  """
  CreateAdaptiveComponentInstance(doc: Document,famSymb: FamilySymbol) -> FamilyInstance
  
   Creates a FamilyInstance of Adaptive Component Family.
  
   doc: The Document
   famSymb: The FamilySymbol
   Returns: The Family Instance
  """
  pass
 @staticmethod
 def GetInstancePlacementPointElementRefIds(famInst):
  """
  GetInstancePlacementPointElementRefIds(famInst: FamilyInstance) -> IList[ElementId]
  
   Gets Placement Adaptive Point Element Ref ids to which the instance geometry 
    adapts.
  
  
   famInst: The FamilyInstance.
   Returns: The Placement Adaptive Point Element Ref ids to which the instance geometry 
    adapts.
  """
  pass
 @staticmethod
 def GetInstancePointElementRefIds(famInst):
  """
  GetInstancePointElementRefIds(famInst: FamilyInstance) -> IList[ElementId]
  
   Gets Adaptive Point Element Ref ids to which the instance geometry adapts.
  
   famInst: The FamilyInstance.
   Returns: The Adaptive Point Element Ref ids to which the instance geometry adapts.
  """
  pass
 @staticmethod
 def GetInstanceShapeHandlePointElementRefIds(famInst):
  """
  GetInstanceShapeHandlePointElementRefIds(famInst: FamilyInstance) -> IList[ElementId]
  
   Gets Shape Handle Adaptive Point Element Ref ids to which the instance geometry 
    adapts.
  
  
   famInst: The FamilyInstance
   Returns: The Shape Handle Adaptive Point Element Ref ids to which the instance geometry 
    adapts.
  """
  pass
 @staticmethod
 def HasAdaptiveFamilySymbol(famInst):
  """
  HasAdaptiveFamilySymbol(famInst: FamilyInstance) -> bool
  
   Verifies if a FamilyInstance has an Adaptive Family Symbol.
  
   famInst: The FamilyInstance
   Returns: True if the FamilyInstance has an Adaptive Family Symbol.
  """
  pass
 @staticmethod
 def IsAdaptiveComponentInstance(famInst):
  """
  IsAdaptiveComponentInstance(famInst: FamilyInstance) -> bool
  
   Verifies if a FamilyInstance is an Adaptive Component Instance.
  
   famInst: The FamilyInstance
   Returns: True if the FamilyInstance has an Adaptive Component Instances.
  """
  pass
 @staticmethod
 def IsAdaptiveFamilySymbol(famSymb):
  """
  IsAdaptiveFamilySymbol(famSymb: FamilySymbol) -> bool
  
   Verifies if a FamilySymbol is a valid Adaptive Family Symbol.
  
   famSymb: The FamilySymbol
   Returns: True if the FamilySymbol is a valid Adaptive Family Symbol.
  """
  pass
 @staticmethod
 def IsInstanceFlipped(famInst):
  """
  IsInstanceFlipped(famInst: FamilyInstance) -> bool
  
   Gets the value of the flip parameter on the adaptive instance.
  
   famInst: The FamilyInstance
   Returns: True if the instance is flipped.
  """
  pass
 @staticmethod
 def MoveAdaptiveComponentInstance(famInst,trf,unHost):
  """
  MoveAdaptiveComponentInstance(famInst: FamilyInstance,trf: Transform,unHost: bool)
   Moves Adaptive Component Instance by the specified transformation.
  
   famInst: The FamilyInstance
   trf: The Transformation
   unHost: True if the move should disassociate the Point Element Refs from their hosts.
   
      False if the Point Element Refs remain hosted.
  """
  pass
 @staticmethod
 def SetInstanceFlipped(famInst,flip):
  """
  SetInstanceFlipped(famInst: FamilyInstance,flip: bool)
   Sets the value of the flip parameter on the adaptive instance.
  
   famInst: The FamilyInstance
   flip: The flip flag
  """
  pass
 __all__=[
  'CreateAdaptiveComponentInstance',
  'GetInstancePlacementPointElementRefIds',
  'GetInstancePointElementRefIds',
  'GetInstanceShapeHandlePointElementRefIds',
  'HasAdaptiveFamilySymbol',
  'IsAdaptiveComponentInstance',
  'IsAdaptiveFamilySymbol',
  'IsInstanceFlipped',
  'MoveAdaptiveComponentInstance',
  'SetInstanceFlipped',
 ]


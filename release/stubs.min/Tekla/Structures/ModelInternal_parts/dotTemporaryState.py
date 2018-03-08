class dotTemporaryState(object):
 # no doc
 @staticmethod
 def ClearAllStates():
  """ ClearAllStates() -> bool """
  pass
 @staticmethod
 def ClearState(MO):
  """ ClearState(MO: ModelObject) -> bool """
  pass
 @staticmethod
 def SetColor(*__args):
  """
  SetColor(ModelObjects: ArrayList,Color: Color) -> bool
  SetColor(MO: ModelObject,Color: Color) -> bool
  """
  pass
 @staticmethod
 def SetColor_FAST(ModelObjects,Color):
  """ SetColor_FAST(ModelObjects: ArrayList,Color: Color) -> bool """
  pass
 @staticmethod
 def SetState(*__args):
  """
  SetState(ModelObjects: ArrayList,State: dotTemporaryStatesEnum,Transparency: dotTemporaryTransparenciesEnum) -> bool
  SetState(ModelObjects: ArrayList,State: dotTemporaryStatesEnum) -> bool
  SetState(Color: Color) -> bool
  SetState(State: dotTemporaryStatesEnum,Transparency: dotTemporaryTransparenciesEnum) -> bool
  SetState(State: dotTemporaryStatesEnum) -> bool
  SetState(MO: ModelObject,State: dotTemporaryStatesEnum) -> bool
  """
  pass
 @staticmethod
 def SetState_FAST(ModelObjects,State,Transparency=None):
  """
  SetState_FAST(ModelObjects: ArrayList,State: dotTemporaryStatesEnum) -> bool
  SetState_FAST(ModelObjects: ArrayList,State: dotTemporaryStatesEnum,Transparency: dotTemporaryTransparenciesEnum) -> bool
  """
  pass
 OBJECT_MAX_SIZE=5000
 __all__=[
  '__reduce_ex__',
  'ClearAllStates',
  'ClearState',
  'OBJECT_MAX_SIZE',
  'SetColor',
  'SetColor_FAST',
  'SetState',
  'SetState_FAST',
 ]


class StringNormalizationExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StringNormalizationExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def IsNormalized(value,normalizationForm=None):
  """
  IsNormalized(value: str) -> bool
  IsNormalized(value: str,normalizationForm: NormalizationForm) -> bool
  """
  pass
 @staticmethod
 def Normalize(value,normalizationForm=None):
  """
  Normalize(value: str) -> str
  Normalize(value: str,normalizationForm: NormalizationForm) -> str
  """
  pass
 __all__=[
  'IsNormalized',
  'Normalize',
 ]


class ValueType(object):
 """ Provides the base class for value types. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ValueType()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass

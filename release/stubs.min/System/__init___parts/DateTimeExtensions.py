class DateTimeExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DateTimeExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def AddWorkday(date):
  """ AddWorkday(date: DateTime) -> DateTime """
  pass
 @staticmethod
 def IsSameDay(dtSelf,dtOther):
  """ IsSameDay(dtSelf: DateTime,dtOther: DateTime) -> bool """
  pass
 @staticmethod
 def IsWorkday(date):
  """ IsWorkday(date: DateTime) -> bool """
  pass
 __all__=[
  'AddWorkday',
  'IsSameDay',
  'IsWorkday',
 ]


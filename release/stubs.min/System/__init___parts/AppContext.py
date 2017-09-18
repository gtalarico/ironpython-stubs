class AppContext(object):
 # no doc
 @staticmethod
 def GetData(name):
  """ GetData(name: str) -> object """
  pass
 @staticmethod
 def SetSwitch(switchName,isEnabled):
  """ SetSwitch(switchName: str,isEnabled: bool) """
  pass
 @staticmethod
 def TryGetSwitch(switchName,isEnabled):
  """ TryGetSwitch(switchName: str) -> (bool,bool) """
  pass
 BaseDirectory='C:\\Program Files (x86)\\IronPython-2.7.7\\'
 TargetFrameworkName='.NETFramework,Version=v4.0'
 __all__=[
  'GetData',
  'SetSwitch',
  'TryGetSwitch',
 ]


class SyntaxCheck(object):
 """ Provides methods to verify the machine name and path conform to a specific syntax. This class cannot be inherited. """
 @staticmethod
 def CheckMachineName(value):
  """
  CheckMachineName(value: str) -> bool

  

   Checks the syntax of the machine name to confirm that it does not contain "\".

  

   value: A string containing the machine name to check.

   Returns: true if value matches the proper machine name format; otherwise,false.
  """
  pass
 @staticmethod
 def CheckPath(value):
  """
  CheckPath(value: str) -> bool

  

   Checks the syntax of the path to see whether it starts with "\\".

  

   value: A string containing the path to check.

   Returns: true if value matches the proper path format; otherwise,false.
  """
  pass
 @staticmethod
 def CheckRootedPath(value):
  """
  CheckRootedPath(value: str) -> bool

  

   Checks the syntax of the path to see if it starts with "\" or drive letter "C:".

  

   value: A string containing the path to check.

   Returns: true if value matches the proper path format; otherwise,false.
  """
  pass
 __all__=[
  'CheckMachineName',
  'CheckPath',
  'CheckRootedPath',
 ]


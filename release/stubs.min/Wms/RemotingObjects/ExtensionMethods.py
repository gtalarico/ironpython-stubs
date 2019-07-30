# encoding: utf-8
# module Wms.RemotingObjects.ExtensionMethods calls itself ExtensionMethods
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ExtensionMethods(object):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExtensionMethods()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetMd5HashString(input):
  """ GetMd5HashString(input: MemoryStream) -> str """
  pass
 @staticmethod
 def IsInteger(input):
  """
  IsInteger(input: str) -> bool
  
   Checks if string is an integer,only contains numeric characters.
     This also works for very,very big intergers.
  
   input: string to check if its an integer
   Returns: Wether string contains only an integer,fails when decimals are used.
  """
  pass
 @staticmethod
 def IsNullOrEmpty(source):
  """
  IsNullOrEmpty[T](source: IEnumerable[T]) -> bool
  IsNullOrEmpty(source: str) -> bool
  """
  pass
 @staticmethod
 def ToHexString(input):
  """ ToHexString(input: str) -> str """
  pass
 __all__=[
  'GetMd5HashString',
  'IsInteger',
  'IsNullOrEmpty',
  'ToHexString',
 ]



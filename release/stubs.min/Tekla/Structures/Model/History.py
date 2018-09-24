# encoding: utf-8
# module Tekla.Structures.Model.History calls itself History
# from Tekla.Structures.Model,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ModelHistory(object):
 # no doc
 @staticmethod
 def GetCurrentModificationStamp():
  """ GetCurrentModificationStamp() -> ModificationStamp """
  pass
 @staticmethod
 def GetDeletedObjects(ModStamp):
  """ GetDeletedObjects(ModStamp: ModificationStamp) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def GetDeletedObjectsWithType(ModStamp,Enum):
  """ GetDeletedObjectsWithType(ModStamp: ModificationStamp,Enum: ModelObjectEnum) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def GetLocalChanges():
  """ GetLocalChanges() -> ModificationInfo """
  pass
 @staticmethod
 def GetModifications(Name,*__args):
  """
  GetModifications(Name: str,ObjectTypes: IEnumerable[ModelObjectEnum],PrevStamp: ModificationStamp) -> ModificationInfo
  GetModifications(Name: str,PrevStamp: ModificationStamp) -> ModificationInfo
  """
  pass
 @staticmethod
 def GetModifiedObjects(ModStamp):
  """ GetModifiedObjects(ModStamp: ModificationStamp) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def GetModifiedObjectsWithType(ModStamp,Enum):
  """ GetModifiedObjectsWithType(ModStamp: ModificationStamp,Enum: ModelObjectEnum) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def GetNotSharedObjects():
  """ GetNotSharedObjects() -> ModelObjectEnumerator """
  pass
 @staticmethod
 def TakeModifications(Name,*__args):
  """
  TakeModifications(Name: str,ObjectTypes: IEnumerable[ModelObjectEnum],PrevStamp: ModificationStamp) -> ModificationInfo
  TakeModifications(Name: str,PrevStamp: ModificationStamp) -> ModificationInfo
  """
  pass
 @staticmethod
 def UpdateModificationStampToLatest(modificationStampKey):
  """ UpdateModificationStampToLatest(modificationStampKey: str) """
  pass
 __all__=[
  '__reduce_ex__',
  'GetCurrentModificationStamp',
  'GetDeletedObjects',
  'GetDeletedObjectsWithType',
  'GetLocalChanges',
  'GetModifications',
  'GetModifiedObjects',
  'GetModifiedObjectsWithType',
  'GetNotSharedObjects',
  'TakeModifications',
  'UpdateModificationStampToLatest',
 ]


class ModificationInfo(object):
 # no doc
 Deleted=None
 Modified=None
 ModifiedWithInfo=None


class ModificationStamp(object):
 """
 ModificationStamp()
 ModificationStamp(LocalStamp: int,ServerStamp: int)
 """
 @staticmethod
 def __new__(self,LocalStamp=None,ServerStamp=None):
  """
  __new__(cls: type)
  __new__(cls: type,LocalStamp: int,ServerStamp: int)
  """
  pass
 Guid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Guid(self: ModificationStamp) -> str

"""

 LocalStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocalStamp(self: ModificationStamp) -> int

Set: LocalStamp(self: ModificationStamp)=value
"""

 ServerStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ServerStamp(self: ModificationStamp) -> int

Set: ServerStamp(self: ModificationStamp)=value
"""



class ModifiedObjectInfo(object):
 # no doc
 IsAttributeChanged=None
 IsCreated=None
 IsModified=None
 IsNumberingChanged=None
 ModelObject=None



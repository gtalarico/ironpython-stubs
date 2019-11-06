# encoding: utf-8
# module Wms.RemotingObjects.StorageClassification calls itself StorageClassification
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class LocationClassification(DbObject):
 """ LocationClassification() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LocationClassification()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 AisleFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AisleFrom(self: LocationClassification) -> str

Set: AisleFrom(self: LocationClassification)=value
"""

 AisleTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AisleTo(self: LocationClassification) -> str

Set: AisleTo(self: LocationClassification)=value
"""

 BlockFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BlockFrom(self: LocationClassification) -> str

Set: BlockFrom(self: LocationClassification)=value
"""

 BlockTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BlockTo(self: LocationClassification) -> str

Set: BlockTo(self: LocationClassification)=value
"""

 ColumnFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ColumnFrom(self: LocationClassification) -> str

Set: ColumnFrom(self: LocationClassification)=value
"""

 ColumnTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ColumnTo(self: LocationClassification) -> str

Set: ColumnTo(self: LocationClassification)=value
"""

 HasScript=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HasScript(self: LocationClassification) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: LocationClassification) -> int

Set: Id(self: LocationClassification)=value
"""

 Script=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Script(self: LocationClassification) -> str

Set: Script(self: LocationClassification)=value
"""

 ShelveFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShelveFrom(self: LocationClassification) -> str

Set: ShelveFrom(self: LocationClassification)=value
"""

 ShelveTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShelveTo(self: LocationClassification) -> str

Set: ShelveTo(self: LocationClassification)=value
"""

 StorageAssignmentClassificationId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StorageAssignmentClassificationId(self: LocationClassification) -> int

Set: StorageAssignmentClassificationId(self: LocationClassification)=value
"""

 UseScript=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UseScript(self: LocationClassification) -> bool

Set: UseScript(self: LocationClassification)=value
"""

 WarehouseLayoutSettingsId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseLayoutSettingsId(self: LocationClassification) -> int

Set: WarehouseLayoutSettingsId(self: LocationClassification)=value
"""



class LocationClassifications(FindableList):
 """ LocationClassifications() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LocationClassifications()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember=None
 ValueMember=None


class LocationClassificationsFilter(object):
 """
 LocationClassificationsFilter()
 LocationClassificationsFilter(storageAssignmentClassificationId: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LocationClassificationsFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,storageAssignmentClassificationId=None):
  """
  __new__(cls: type)
  __new__(cls: type,storageAssignmentClassificationId: int)
  """
  pass
 StorageAssignmentClassificationId=None


class StorageAssignmentClassification(DbObject):
 """ StorageAssignmentClassification() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StorageAssignmentClassification()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Code=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Code(self: StorageAssignmentClassification) -> str

Set: Code(self: StorageAssignmentClassification)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: StorageAssignmentClassification) -> int

Set: Id(self: StorageAssignmentClassification)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: StorageAssignmentClassification) -> str

Set: Name(self: StorageAssignmentClassification)=value
"""

 SortOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SortOrder(self: StorageAssignmentClassification) -> int

Set: SortOrder(self: StorageAssignmentClassification)=value
"""



class StorageAssignmentClassifications(FindableList):
 """ StorageAssignmentClassifications() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StorageAssignmentClassifications()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember=None
 ValueMember=None


class StorageAssignmentClassificationsFilter(object):
 """
 StorageAssignmentClassificationsFilter()
 StorageAssignmentClassificationsFilter(id: int)
 StorageAssignmentClassificationsFilter(id: int,searchText: str)
 StorageAssignmentClassificationsFilter(searchText: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StorageAssignmentClassificationsFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,id: int)
  __new__(cls: type,id: int,searchText: str)
  __new__(cls: type,searchText: str)
  """
  pass
 Id=None
 SearchText=None



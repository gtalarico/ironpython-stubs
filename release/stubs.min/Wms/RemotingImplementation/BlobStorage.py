# encoding: utf-8
# module Wms.RemotingImplementation.BlobStorage calls itself BlobStorage
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class BlobExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BlobExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetOriginalFilename(properties):
  """
  GetOriginalFilename(properties: BlobProperties) -> str
  GetOriginalFilename(properties: BlobDescriptor) -> str
  """
  pass
 @staticmethod
 def SetOriginalFilename(properties,originalFilename):
  """
  SetOriginalFilename(properties: BlobProperties,originalFilename: str) -> BlobProperties
  SetOriginalFilename(properties: BlobDescriptor,originalFilename: str) -> BlobDescriptor
  """
  pass
 __all__=[
  'GetOriginalFilename',
  'SetOriginalFilename',
 ]


class StorageProvider(object):
 """ StorageProvider(innerProvider: IStorageProvider) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StorageProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def DeleteBlobAsync(self,blobId):
  """ DeleteBlobAsync(self: StorageProvider,blobId: int) -> Task """
  pass
 def GetBlobDbInformation(self,blobId):
  """ GetBlobDbInformation(self: StorageProvider,blobId: int) -> Blobs """
  pass
 def GetBlobDescriptorAsync(self,blobId):
  """ GetBlobDescriptorAsync(self: StorageProvider,blobId: int) -> Task[BlobDescriptor] """
  pass
 def GetBlobStreamAsync(self,blobId):
  """ GetBlobStreamAsync(self: StorageProvider,blobId: int) -> Task[Stream] """
  pass
 def SaveBlobStreamAsync(self,containerName,blobName,source,properties,closeStream):
  """ SaveBlobStreamAsync(self: StorageProvider,containerName: str,blobName: str,source: Stream,properties: BlobProperties,closeStream: bool) -> Task[int] """
  pass
 @staticmethod
 def __new__(self,innerProvider):
  """ __new__(cls: type,innerProvider: IStorageProvider) """
  pass


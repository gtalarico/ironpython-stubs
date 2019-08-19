# encoding: utf-8
# module Wms.RemotingImplementation.BlobStorage calls itself BlobStorage
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BlobExtensions():
    # no doc
    @staticmethod
    def GetOriginalFilename(properties):
        """
        GetOriginalFilename(properties: BlobProperties) -> str
        GetOriginalFilename(properties: BlobDescriptor) -> str
        """
        pass

    @staticmethod
    def SetOriginalFilename(properties, originalFilename):
        """
        SetOriginalFilename(properties: BlobProperties, originalFilename: str) -> BlobProperties
        SetOriginalFilename(properties: BlobDescriptor, originalFilename: str) -> BlobDescriptor
        """
        pass

    __all__ = [
        'GetOriginalFilename',
        'SetOriginalFilename',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return BlobExtensions()

class StorageProvider():
    """ StorageProvider(innerProvider: IStorageProvider) """
    def DeleteBlobAsync(self, blobId):
        """ DeleteBlobAsync(self: StorageProvider, blobId: int) -> Task """
        pass

    def GetBlobDbInformation(self, blobId):
        """ GetBlobDbInformation(self: StorageProvider, blobId: int) -> Blobs """
        pass

    def GetBlobDescriptorAsync(self, blobId):
        """ GetBlobDescriptorAsync(self: StorageProvider, blobId: int) -> Task[BlobDescriptor] """
        pass

    def GetBlobStreamAsync(self, blobId):
        """ GetBlobStreamAsync(self: StorageProvider, blobId: int) -> Task[Stream] """
        pass

    def SaveBlobStreamAsync(self, containerName, blobName, source, properties, closeStream):
        """ SaveBlobStreamAsync(self: StorageProvider, containerName: str, blobName: str, source: Stream, properties: BlobProperties, closeStream: bool) -> Task[int] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, innerProvider):
        """ __new__(cls: type, innerProvider: IStorageProvider) """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return StorageProvider()


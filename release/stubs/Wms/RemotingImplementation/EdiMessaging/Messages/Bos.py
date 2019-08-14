from Wms.EdiMessaging import *
# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging.Messages.Bos calls itself Bos
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BosFile():
    """ BosFile() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosFile()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def Create(name, fileStream):
        """ Create(name: str, fileStream: Stream) -> BosFile """
        pass

    Base64Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base64Content(self: BosFile) -> str

Set: Base64Content(self: BosFile) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BosFile) -> str

Set: Name(self: BosFile) = value
"""



class BosFileExtensions():
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosFileExtensions()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def AddFile(files, name, *__args):
        """
        AddFile(files: List[BosFile], name: str, pathToFile: str) -> List[BosFile]
        AddFile(files: List[BosFile], name: str, fileStream: Stream) -> List[BosFile]
        """
        pass

    __all__ = [
        'AddFile',
    ]


class BosInboundFile(BosFile):
    """ BosInboundFile() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFile()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    ScannerSerialNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScannerSerialNo(self: BosInboundFile) -> str

Set: ScannerSerialNo(self: BosInboundFile) = value
"""



class BosInboundFileExtensions():
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileExtensions()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def SetFile(file, name, serialno, fileStream):
        """ SetFile(file: BosInboundFile, name: str, serialno: str, fileStream: Stream) -> BosInboundFile """
        pass

    @staticmethod
    def ToBase64String(fileStream):
        """ ToBase64String(fileStream: Stream) -> str """
        pass

    __all__ = [
        'SetFile',
        'ToBase64String',
    ]


class BosInboundFileMessage(MessageBase):
    """
    BosInboundFileMessage()
    BosInboundFileMessage(message: IMessage)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileMessage()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: BosInboundFileMessage) -> BosInboundFileMessageData

Set: Data(self: BosInboundFileMessage) = value
"""


    TypeName = 'BOS Inbound File: {0}'


class BosInboundFileMessageData():
    """ BosInboundFileMessageData() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileMessageData()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    File = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: File(self: BosInboundFileMessageData) -> BosInboundFile

Set: File(self: BosInboundFileMessageData) = value
"""



class BosOutboundFilesMessage(MessageBase):
    """
    BosOutboundFilesMessage()
    BosOutboundFilesMessage(message: IMessage)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosOutboundFilesMessage()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: BosOutboundFilesMessage) -> BosOutboundFilesMessageData

Set: Data(self: BosOutboundFilesMessage) = value
"""


    TypeName = 'BOS Outbound File'


class BosOutboundFilesMessageData():
    """ BosOutboundFilesMessageData() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosOutboundFilesMessageData()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    Files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Files(self: BosOutboundFilesMessageData) -> List[BosFile]

Set: Files(self: BosOutboundFilesMessageData) = value
"""




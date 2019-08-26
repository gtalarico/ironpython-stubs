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


    Instance = BosFile()
    """hardcoded/returns an instance of the class"""

class BosFileExtensions():
    # no doc
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

    Instance = BosFileExtensions()
    """hardcoded/returns an instance of the class"""

class BosInboundFile(BosFile):
    """ BosInboundFile() """
    ScannerSerialNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScannerSerialNo(self: BosInboundFile) -> str

Set: ScannerSerialNo(self: BosInboundFile) = value
"""


    Instance = BosInboundFile()
    """hardcoded/returns an instance of the class"""

class BosInboundFileExtensions():
    # no doc
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

    Instance = BosInboundFileExtensions()
    """hardcoded/returns an instance of the class"""

class BosInboundFileMessage(MessageBase):
    """
    BosInboundFileMessage()
    BosInboundFileMessage(message: IMessage)
    """
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

    Instance = BosInboundFileMessage()
    """hardcoded/returns an instance of the class"""

class BosInboundFileMessageData():
    """ BosInboundFileMessageData() """
    File = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: File(self: BosInboundFileMessageData) -> BosInboundFile

Set: File(self: BosInboundFileMessageData) = value
"""


    Instance = BosInboundFileMessageData()
    """hardcoded/returns an instance of the class"""

class BosOutboundFilesMessage(MessageBase):
    """
    BosOutboundFilesMessage()
    BosOutboundFilesMessage(message: IMessage)
    """
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

    Instance = BosOutboundFilesMessage()
    """hardcoded/returns an instance of the class"""

class BosOutboundFilesMessageData():
    """ BosOutboundFilesMessageData() """
    Files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Files(self: BosOutboundFilesMessageData) -> List[BosFile]

Set: Files(self: BosOutboundFilesMessageData) = value
"""


    Instance = BosOutboundFilesMessageData()
    """hardcoded/returns an instance of the class"""


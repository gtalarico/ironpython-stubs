# encoding: utf-8
# module Wms.RemotingImplementation.Extensions calls itself Extensions
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataFlowExtensions():
    # no doc
    @staticmethod
    def CopyResultFrom(this, from_):
        """ CopyResultFrom[(T1, T2)](this: DataFlowObject[T1], from: DataFlowObject[T2]) -> DataFlowObject[T1] """
        pass

    __all__ = [
        'CopyResultFrom',
    ]

    Instance = DataFlowExtensions()
    """hardcoded/returns an instance of the class"""

class GeneralExtensionMethods():
    # no doc
    @staticmethod
    def GetCultureForUser(general, userid):
        """ GetCultureForUser(general: General, userid: int) -> CultureInfo """
        pass

    __all__ = [
        'GetCultureForUser',
    ]

    Instance = GeneralExtensionMethods()
    """hardcoded/returns an instance of the class"""

class HttpClientExtensions():
    # no doc
    @staticmethod
    def DownloadFileAsync(client, url, filepath, cancellationToken, fileMode):
        """ DownloadFileAsync(client: HttpClient, url: str, filepath: str, cancellationToken: CancellationToken, fileMode: FileMode) -> Task """
        pass

    __all__ = [
        'DownloadFileAsync',
    ]

    Instance = HttpClientExtensions()
    """hardcoded/returns an instance of the class"""


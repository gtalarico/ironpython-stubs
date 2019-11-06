# encoding: utf-8
# module Wms.RemotingObjects.ExtensionMethods calls itself ExtensionMethods
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExtensionMethods():
    """  """
    @staticmethod
    def GetMd5HashString(input):
        """ GetMd5HashString(input: MemoryStream) -> str """
        pass

    @staticmethod
    def IsInteger(input):
        """
        IsInteger(input: str) -> bool
        
            Checks if string is an integer, only contains numeric characters.
                    This also works for very, very big intergers.
        
            input: string to check if its an integer
            Returns: Wether string contains only an integer, fails when decimals are used.
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

    __all__ = [
        'GetMd5HashString',
        'IsInteger',
        'IsNullOrEmpty',
        'ToHexString',
    ]

    Instance = ExtensionMethods()
    """hardcoded/returns an instance of the class"""


# encoding: utf-8
# module Wms.SharedInfra.Cryptography.PasswordHashing calls itself PasswordHashing
# from Wms.SharedInfra, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HashBytes():
    """ HashBytes() """
    Instance = HashBytes
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def CreateFromString(key, salt):
        """ CreateFromString(key: str, salt: str) -> HashBytes """
        pass

    Key = None
    Salt = None


class HashBytesExtensions():
    # no doc
    Instance = HashBytesExtensions
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromString(hashBytes, key, salt):
        """ FromString(hashBytes: HashBytes, key: str, salt: str) -> HashBytes """
        pass

    @staticmethod
    def KeyAsString(hashBytes):
        """ KeyAsString(hashBytes: HashBytes) -> str """
        pass

    @staticmethod
    def SaltAsString(hashBytes):
        """ SaltAsString(hashBytes: HashBytes) -> str """
        pass

    __all__ = [
        'FromString',
        'KeyAsString',
        'SaltAsString',
    ]


class IPasswordHasher:
    # no doc
    Instance = IPasswordHasher
    """hardcoded/returns an instance of the class"""
    def Hash(self, password, saltLength=None, keyLength=None, iterations=None):
        """
        Hash(self: IPasswordHasher, password: str, saltLength: int, keyLength: int, iterations: int) -> HashBytes
        Hash(self: IPasswordHasher, password: str) -> HashBytes
        """
        pass

    def Verify(self, password, salt, key, iterations=None):
        """
        Verify(self: IPasswordHasher, password: str, salt: Array[Byte], key: Array[Byte], iterations: int) -> bool
        Verify(self: IPasswordHasher, password: str, salt: Array[Byte], key: Array[Byte]) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PBKDF2PasswordHasher:
    """ PBKDF2PasswordHasher() """
    Instance = PBKDF2PasswordHasher
    """hardcoded/returns an instance of the class"""
    def Hash(self, password, saltLength=None, keyLength=None, iterations=None):
        """
        Hash(self: PBKDF2PasswordHasher, password: str, saltLength: int, keyLength: int, iterations: int) -> HashBytes
        Hash(self: PBKDF2PasswordHasher, password: str) -> HashBytes
        """
        pass

    def Verify(self, password, salt, key, iterations=None):
        """
        Verify(self: PBKDF2PasswordHasher, password: str, salt: Array[Byte], key: Array[Byte], iterations: int) -> bool
        Verify(self: PBKDF2PasswordHasher, password: str, salt: Array[Byte], key: Array[Byte]) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass



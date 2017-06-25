# encoding: utf-8
# module Rhino.DocObjects.Custom calls itself Custom
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class UserData(object):
    # no doc
    @staticmethod
    def Copy(source, destination):
        """ Copy(source: CommonObject, destination: CommonObject) """
        pass

    def Dispose(self):
        """ Dispose(self: UserData) """
        pass

    @staticmethod
    def MoveUserDataFrom(objectWithUserData):
        """ MoveUserDataFrom(objectWithUserData: CommonObject) -> Guid """
        pass

    @staticmethod
    def MoveUserDataTo(objectToGetUserData, id, append):
        """ MoveUserDataTo(objectToGetUserData: CommonObject, id: Guid, append: bool) """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """ OnDuplicate(self: UserData, source: UserData) """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """ OnTransform(self: UserData, transform: Transform) """
        pass

    def Read(self, *args): #cannot find CLR method
        """ Read(self: UserData, archive: BinaryArchiveReader) -> bool """
        pass

    def Write(self, *args): #cannot find CLR method
        """ Write(self: UserData, archive: BinaryArchiveWriter) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: UserData) -> str

"""

    ShouldWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShouldWrite(self: UserData) -> bool

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: UserData) -> Transform

"""



class UnknownUserData(UserData):
    """ UnknownUserData(pointerNativeUserData: IntPtr) """
    def Dispose(self):
        """ Dispose(self: UserData, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pointerNativeUserData):
        """ __new__(cls: type, pointerNativeUserData: IntPtr) """
        pass


class UserDataList(object):
    # no doc
    def Add(self, userdata):
        """ Add(self: UserDataList, userdata: UserData) -> bool """
        pass

    def Find(self, userdataType):
        """ Find(self: UserDataList, userdataType: Type) -> UserData """
        pass

    def Remove(self, userdata):
        """ Remove(self: UserDataList, userdata: UserData) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: UserDataList) -> int

"""



class UserDictionary(UserData):
    """ UserDictionary() """
    def Dispose(self):
        """ Dispose(self: UserData, disposing: bool) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: UserDictionary) -> str

"""

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dictionary(self: UserDictionary) -> ArchivableDictionary

"""

    ShouldWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShouldWrite(self: UserDictionary) -> bool

"""




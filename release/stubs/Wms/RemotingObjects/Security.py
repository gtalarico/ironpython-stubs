# encoding: utf-8
# module Wms.RemotingObjects.Security calls itself Security
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AuthenticationArgs():
    """
    Contains all required fields for login
    
    AuthenticationArgs()
    """
    ClientName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ClientName(self: AuthenticationArgs) -> str

Set: ClientName(self: AuthenticationArgs) = value
"""

    ClientTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ClientTime(self: AuthenticationArgs) -> DateTime

Set: ClientTime(self: AuthenticationArgs) = value
"""

    ClientVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ClientVersion(self: AuthenticationArgs) -> Version

Set: ClientVersion(self: AuthenticationArgs) = value
"""

    DeviceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeviceType(self: AuthenticationArgs) -> DeviceTypesEnum

Set: DeviceType(self: AuthenticationArgs) = value
"""

    MacAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MacAddress(self: AuthenticationArgs) -> str

Set: MacAddress(self: AuthenticationArgs) = value
"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Password(self: AuthenticationArgs) -> str

Set: Password(self: AuthenticationArgs) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UserName(self: AuthenticationArgs) -> str

Set: UserName(self: AuthenticationArgs) = value
"""


    Instance = AuthenticationArgs()
    """hardcoded/returns an instance of the class"""

class RemotingIdentity():
    """ RemotingIdentity(accessId: str, clientName: str, userName: str) """
    def Equals(self, *__args):
        """
        Equals(self: RemotingIdentity, obj: object) -> bool
        Equals(self: RemotingIdentity, other: RemotingIdentity) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RemotingIdentity) -> int """
        pass

    def ToSession(self):
        """
        ToSession(self: RemotingIdentity) -> Session
        
            Converts a RemotingIdentity object to a smaller, leaner Session object for storage.
        """
        pass

    def ToString(self):
        """ ToString(self: RemotingIdentity) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accessId, clientName, userName):
        """ __new__(cls: type, accessId: str, clientName: str, userName: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AccessId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AccessId(self: RemotingIdentity) -> str

"""

    ClientName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ClientName(self: RemotingIdentity) -> str

"""

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Device(self: RemotingIdentity) -> Device

Set: Device(self: RemotingIdentity) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EndPoint(self: RemotingIdentity) -> str

Set: EndPoint(self: RemotingIdentity) = value
"""

    IsAnonymous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsAnonymous(self: RemotingIdentity) -> bool

"""

    PreferredLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreferredLanguage(self: RemotingIdentity) -> str

Set: PreferredLanguage(self: RemotingIdentity) = value
"""

    UserDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UserDisplayName(self: RemotingIdentity) -> str

Set: UserDisplayName(self: RemotingIdentity) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UserId(self: RemotingIdentity) -> int

Set: UserId(self: RemotingIdentity) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UserName(self: RemotingIdentity) -> str

"""

    Zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Zone(self: RemotingIdentity) -> Zone

Set: Zone(self: RemotingIdentity) = value
"""


    Anonymous = None

    Instance = RemotingIdentity()
    """hardcoded/returns an instance of the class"""


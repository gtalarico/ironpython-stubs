# encoding: utf-8
# module System.Security.Claims calls itself Claims
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Claim(object):
    """
    Claim(reader: BinaryReader)
    Claim(reader: BinaryReader, subject: ClaimsIdentity)
    Claim(type: str, value: str)
    Claim(type: str, value: str, valueType: str)
    Claim(type: str, value: str, valueType: str, issuer: str)
    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str)
    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity)
    """
    def Clone(self, identity=None):
        """
        Clone(self: Claim, identity: ClaimsIdentity) -> Claim
        Clone(self: Claim) -> Claim
        """
        pass

    def ToString(self):
        """ ToString(self: Claim) -> str """
        pass

    def WriteTo(self, writer):
        """ WriteTo(self: Claim, writer: BinaryWriter) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, reader: BinaryReader)
        __new__(cls: type, reader: BinaryReader, subject: ClaimsIdentity)
        __new__(cls: type, type: str, value: str)
        __new__(cls: type, type: str, value: str, valueType: str)
        __new__(cls: type, type: str, value: str, valueType: str, issuer: str)
        __new__(cls: type, type: str, value: str, valueType: str, issuer: str, originalIssuer: str)
        __new__(cls: type, type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity)
        __new__(cls: type, other: Claim)
        __new__(cls: type, other: Claim, subject: ClaimsIdentity)
        """
        pass

    CustomSerializationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Issuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Issuer(self: Claim) -> str

"""

    OriginalIssuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalIssuer(self: Claim) -> str

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: Claim) -> IDictionary[str, str]

"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subject(self: Claim) -> ClaimsIdentity

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Claim) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Claim) -> str

"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: Claim) -> str

"""



class ClaimsIdentity(object, IIdentity):
    """
    ClaimsIdentity()
    ClaimsIdentity(identity: IIdentity)
    ClaimsIdentity(claims: IEnumerable[Claim])
    ClaimsIdentity(authenticationType: str)
    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str)
    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim])
    ClaimsIdentity(authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(reader: BinaryReader)
    """
    def AddClaim(self, claim):
        """ AddClaim(self: ClaimsIdentity, claim: Claim) """
        pass

    def AddClaims(self, claims):
        """ AddClaims(self: ClaimsIdentity, claims: IEnumerable[Claim]) """
        pass

    def Clone(self):
        """ Clone(self: ClaimsIdentity) -> ClaimsIdentity """
        pass

    def CreateClaim(self, *args): #cannot find CLR method
        """ CreateClaim(self: ClaimsIdentity, reader: BinaryReader) -> Claim """
        pass

    def FindAll(self, *__args):
        """
        FindAll(self: ClaimsIdentity, type: str) -> IEnumerable[Claim]
        FindAll(self: ClaimsIdentity, match: Predicate[Claim]) -> IEnumerable[Claim]
        """
        pass

    def FindFirst(self, *__args):
        """
        FindFirst(self: ClaimsIdentity, type: str) -> Claim
        FindFirst(self: ClaimsIdentity, match: Predicate[Claim]) -> Claim
        """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: ClaimsIdentity, info: SerializationInfo, context: StreamingContext) """
        pass

    def HasClaim(self, *__args):
        """
        HasClaim(self: ClaimsIdentity, type: str, value: str) -> bool
        HasClaim(self: ClaimsIdentity, match: Predicate[Claim]) -> bool
        """
        pass

    def RemoveClaim(self, claim):
        """ RemoveClaim(self: ClaimsIdentity, claim: Claim) """
        pass

    def TryRemoveClaim(self, claim):
        """ TryRemoveClaim(self: ClaimsIdentity, claim: Claim) -> bool """
        pass

    def WriteTo(self, writer):
        """ WriteTo(self: ClaimsIdentity, writer: BinaryWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, identity: IIdentity)
        __new__(cls: type, claims: IEnumerable[Claim])
        __new__(cls: type, authenticationType: str)
        __new__(cls: type, claims: IEnumerable[Claim], authenticationType: str)
        __new__(cls: type, identity: IIdentity, claims: IEnumerable[Claim])
        __new__(cls: type, authenticationType: str, nameType: str, roleType: str)
        __new__(cls: type, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
        __new__(cls: type, identity: IIdentity, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
        __new__(cls: type, reader: BinaryReader)
        __new__(cls: type, other: ClaimsIdentity)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, info: SerializationInfo)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Actor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Actor(self: ClaimsIdentity) -> ClaimsIdentity

Set: Actor(self: ClaimsIdentity) = value
"""

    AuthenticationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AuthenticationType(self: ClaimsIdentity) -> str

"""

    BootstrapContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BootstrapContext(self: ClaimsIdentity) -> object

Set: BootstrapContext(self: ClaimsIdentity) = value
"""

    Claims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Claims(self: ClaimsIdentity) -> IEnumerable[Claim]

"""

    CustomSerializationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAuthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthenticated(self: ClaimsIdentity) -> bool

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: ClaimsIdentity) -> str

Set: Label(self: ClaimsIdentity) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClaimsIdentity) -> str

"""

    NameClaimType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameClaimType(self: ClaimsIdentity) -> str

"""

    RoleClaimType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoleClaimType(self: ClaimsIdentity) -> str

"""


    DefaultIssuer = 'LOCAL AUTHORITY'
    DefaultNameClaimType = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'
    DefaultRoleClaimType = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/role'


class ClaimsPrincipal(object, IPrincipal):
    """
    ClaimsPrincipal()
    ClaimsPrincipal(identity: IIdentity)
    ClaimsPrincipal(identities: IEnumerable[ClaimsIdentity])
    ClaimsPrincipal(principal: IPrincipal)
    ClaimsPrincipal(reader: BinaryReader)
    """
    def AddIdentities(self, identities):
        """ AddIdentities(self: ClaimsPrincipal, identities: IEnumerable[ClaimsIdentity]) """
        pass

    def AddIdentity(self, identity):
        """ AddIdentity(self: ClaimsPrincipal, identity: ClaimsIdentity) """
        pass

    def Clone(self):
        """ Clone(self: ClaimsPrincipal) -> ClaimsPrincipal """
        pass

    def CreateClaimsIdentity(self, *args): #cannot find CLR method
        """ CreateClaimsIdentity(self: ClaimsPrincipal, reader: BinaryReader) -> ClaimsIdentity """
        pass

    def FindAll(self, *__args):
        """
        FindAll(self: ClaimsPrincipal, type: str) -> IEnumerable[Claim]
        FindAll(self: ClaimsPrincipal, match: Predicate[Claim]) -> IEnumerable[Claim]
        """
        pass

    def FindFirst(self, *__args):
        """
        FindFirst(self: ClaimsPrincipal, type: str) -> Claim
        FindFirst(self: ClaimsPrincipal, match: Predicate[Claim]) -> Claim
        """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: ClaimsPrincipal, info: SerializationInfo, context: StreamingContext) """
        pass

    def HasClaim(self, *__args):
        """
        HasClaim(self: ClaimsPrincipal, type: str, value: str) -> bool
        HasClaim(self: ClaimsPrincipal, match: Predicate[Claim]) -> bool
        """
        pass

    def IsInRole(self, role):
        """ IsInRole(self: ClaimsPrincipal, role: str) -> bool """
        pass

    def PrimaryIdentitySelector(self, *args): #cannot find CLR method
        """ Func[IEnumerable[ClaimsIdentity], ClaimsIdentity](object: object, method: IntPtr) """
        pass

    def WriteTo(self, writer):
        """ WriteTo(self: ClaimsPrincipal, writer: BinaryWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, identities: IEnumerable[ClaimsIdentity])
        __new__(cls: type, identity: IIdentity)
        __new__(cls: type, principal: IPrincipal)
        __new__(cls: type, reader: BinaryReader)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Claims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Claims(self: ClaimsPrincipal) -> IEnumerable[Claim]

"""

    CustomSerializationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Identities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identities(self: ClaimsPrincipal) -> IEnumerable[ClaimsIdentity]

"""

    Identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identity(self: ClaimsPrincipal) -> IIdentity

"""


    ClaimsPrincipalSelector = None
    Current = None


class ClaimTypes(object):
    # no doc
    Actor = 'http://schemas.xmlsoap.org/ws/2009/09/identity/claims/actor'
    Anonymous = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/anonymous'
    Authentication = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/authentication'
    AuthenticationInstant = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationinstant'
    AuthenticationMethod = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod'
    AuthorizationDecision = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/authorizationdecision'
    CookiePath = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/cookiepath'
    Country = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/country'
    DateOfBirth = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/dateofbirth'
    DenyOnlyPrimaryGroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlyprimarygroupsid'
    DenyOnlyPrimarySid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlyprimarysid'
    DenyOnlySid = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/denyonlysid'
    DenyOnlyWindowsDeviceGroup = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlywindowsdevicegroup'
    Dns = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/dns'
    Dsa = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/dsa'
    Email = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress'
    Expiration = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/expiration'
    Expired = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/expired'
    Gender = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/gender'
    GivenName = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname'
    GroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid'
    Hash = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/hash'
    HomePhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/homephone'
    IsPersistent = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/ispersistent'
    Locality = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/locality'
    MobilePhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/mobilephone'
    Name = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'
    NameIdentifier = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier'
    OtherPhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/otherphone'
    PostalCode = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/postalcode'
    PrimaryGroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/primarygroupsid'
    PrimarySid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid'
    Role = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/role'
    Rsa = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/rsa'
    SerialNumber = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/serialnumber'
    Sid = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid'
    Spn = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/spn'
    StateOrProvince = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/stateorprovince'
    StreetAddress = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/streetaddress'
    Surname = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname'
    System = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/system'
    Thumbprint = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/thumbprint'
    Upn = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn'
    Uri = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/uri'
    UserData = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/userdata'
    Version = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/version'
    Webpage = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/webpage'
    WindowsAccountName = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname'
    WindowsDeviceClaim = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsdeviceclaim'
    WindowsDeviceGroup = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsdevicegroup'
    WindowsFqbnVersion = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsfqbnversion'
    WindowsSubAuthority = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowssubauthority'
    WindowsUserClaim = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsuserclaim'
    X500DistinguishedName = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/x500distinguishedname'
    __all__ = [
        'Actor',
        'Anonymous',
        'Authentication',
        'AuthenticationInstant',
        'AuthenticationMethod',
        'AuthorizationDecision',
        'CookiePath',
        'Country',
        'DateOfBirth',
        'DenyOnlyPrimaryGroupSid',
        'DenyOnlyPrimarySid',
        'DenyOnlySid',
        'DenyOnlyWindowsDeviceGroup',
        'Dns',
        'Dsa',
        'Email',
        'Expiration',
        'Expired',
        'Gender',
        'GivenName',
        'GroupSid',
        'Hash',
        'HomePhone',
        'IsPersistent',
        'Locality',
        'MobilePhone',
        'Name',
        'NameIdentifier',
        'OtherPhone',
        'PostalCode',
        'PrimaryGroupSid',
        'PrimarySid',
        'Role',
        'Rsa',
        'SerialNumber',
        'Sid',
        'Spn',
        'StateOrProvince',
        'StreetAddress',
        'Surname',
        'System',
        'Thumbprint',
        'Upn',
        'Uri',
        'UserData',
        'Version',
        'Webpage',
        'WindowsAccountName',
        'WindowsDeviceClaim',
        'WindowsDeviceGroup',
        'WindowsFqbnVersion',
        'WindowsSubAuthority',
        'WindowsUserClaim',
        'X500DistinguishedName',
    ]


class ClaimValueTypes(object):
    # no doc
    Base64Binary = 'http://www.w3.org/2001/XMLSchema#base64Binary'
    Base64Octet = 'http://www.w3.org/2001/XMLSchema#base64Octet'
    Boolean = 'http://www.w3.org/2001/XMLSchema#boolean'
    Date = 'http://www.w3.org/2001/XMLSchema#date'
    DateTime = 'http://www.w3.org/2001/XMLSchema#dateTime'
    DaytimeDuration = 'http://www.w3.org/TR/2002/WD-xquery-operators-20020816#dayTimeDuration'
    DnsName = 'http://schemas.xmlsoap.org/claims/dns'
    Double = 'http://www.w3.org/2001/XMLSchema#double'
    DsaKeyValue = 'http://www.w3.org/2000/09/xmldsig#DSAKeyValue'
    Email = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress'
    Fqbn = 'http://www.w3.org/2001/XMLSchema#fqbn'
    HexBinary = 'http://www.w3.org/2001/XMLSchema#hexBinary'
    Integer = 'http://www.w3.org/2001/XMLSchema#integer'
    Integer32 = 'http://www.w3.org/2001/XMLSchema#integer32'
    Integer64 = 'http://www.w3.org/2001/XMLSchema#integer64'
    KeyInfo = 'http://www.w3.org/2000/09/xmldsig#KeyInfo'
    Rfc822Name = 'urn:oasis:names:tc:xacml:1.0:data-type:rfc822Name'
    Rsa = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/rsa'
    RsaKeyValue = 'http://www.w3.org/2000/09/xmldsig#RSAKeyValue'
    Sid = 'http://www.w3.org/2001/XMLSchema#sid'
    String = 'http://www.w3.org/2001/XMLSchema#string'
    Time = 'http://www.w3.org/2001/XMLSchema#time'
    UInteger32 = 'http://www.w3.org/2001/XMLSchema#uinteger32'
    UInteger64 = 'http://www.w3.org/2001/XMLSchema#uinteger64'
    UpnName = 'http://schemas.xmlsoap.org/claims/UPN'
    X500Name = 'urn:oasis:names:tc:xacml:1.0:data-type:x500Name'
    YearMonthDuration = 'http://www.w3.org/TR/2002/WD-xquery-operators-20020816#yearMonthDuration'
    __all__ = [
        'Base64Binary',
        'Base64Octet',
        'Boolean',
        'Date',
        'DateTime',
        'DaytimeDuration',
        'DnsName',
        'Double',
        'DsaKeyValue',
        'Email',
        'Fqbn',
        'HexBinary',
        'Integer',
        'Integer32',
        'Integer64',
        'KeyInfo',
        'Rfc822Name',
        'Rsa',
        'RsaKeyValue',
        'Sid',
        'String',
        'Time',
        'UInteger32',
        'UInteger64',
        'UpnName',
        'X500Name',
        'YearMonthDuration',
    ]


class DynamicRoleClaimProvider(object):
    # no doc
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity, claims):
        """ AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]) """
        pass

    __all__ = [
        'AddDynamicRoleClaims',
    ]



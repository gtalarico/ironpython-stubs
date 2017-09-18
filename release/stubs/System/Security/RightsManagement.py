# encoding: utf-8
# module System.Security.RightsManagement calls itself RightsManagement
# from WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AuthenticationType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the method of rights management authentication.
    
    enum AuthenticationType, values: Internal (3), Passport (1), Windows (0), WindowsPassport (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Internal = None
    Passport = None
    value__ = None
    Windows = None
    WindowsPassport = None


class ContentGrant(object):
    """
    Represents a right granted to a user to access information in a rights managed document.
    
    ContentGrant(user: ContentUser, right: ContentRight)
    ContentGrant(user: ContentUser, right: ContentRight, validFrom: DateTime, validUntil: DateTime)
    """
    @staticmethod # known case of __new__
    def __new__(self, user, right, validFrom=None, validUntil=None):
        """
        __new__(cls: type, user: ContentUser, right: ContentRight)
        __new__(cls: type, user: ContentUser, right: ContentRight, validFrom: DateTime, validUntil: DateTime)
        """
        pass

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.RightsManagement.ContentRight that is granted.

Get: Right(self: ContentGrant) -> ContentRight

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user who is granted the access System.Security.RightsManagement.ContentGrant.Right.

Get: User(self: ContentGrant) -> ContentUser

"""

    ValidFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the starting date and time that the granted System.Security.RightsManagement.ContentGrant.Right begins.

Get: ValidFrom(self: ContentGrant) -> DateTime

"""

    ValidUntil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ending date and time that the granted System.Security.RightsManagement.ContentGrant.Right expires.

Get: ValidUntil(self: ContentGrant) -> DateTime

"""



class ContentRight(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies rights that can be granted to users for accessing content in a rights managed document.
    
    enum ContentRight, values: DocumentEdit (11), Edit (1), Export (12), Extract (3), Forward (7), ObjectModel (4), Owner (5), Print (2), Reply (8), ReplyAll (9), Sign (10), View (0), ViewRightsData (6)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DocumentEdit = None
    Edit = None
    Export = None
    Extract = None
    Forward = None
    ObjectModel = None
    Owner = None
    Print = None
    Reply = None
    ReplyAll = None
    Sign = None
    value__ = None
    View = None
    ViewRightsData = None


class ContentUser(object):
    """
    Represents a user or user-group for granting access to rights managed content.
    
    ContentUser(name: str, authenticationType: AuthenticationType)
    """
    def Equals(self, obj):
        """
        Equals(self: ContentUser, obj: object) -> bool
        
            Returns a value that indicates whether this System.Security.RightsManagement.ContentUser is 
             equivalent to another given instance.
        
        
            obj: The user instance to compare for equality.
            Returns: true if System.Security.RightsManagement.ContentUser.Name and 
             System.Security.RightsManagement.ContentUser.AuthenticationType are the same for both this user 
             and the given user; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ContentUser) -> int
        
            Returns a computed hash code based on the user System.Security.RightsManagement.ContentUser.Name 
             and System.Security.RightsManagement.ContentUser.AuthenticationType.
        
            Returns: A hash code computed from the user System.Security.RightsManagement.ContentUser.Name and 
             System.Security.RightsManagement.ContentUser.AuthenticationType.
        """
        pass

    def IsAuthenticated(self):
        """
        IsAuthenticated(self: ContentUser) -> bool
        
            Returns a value that indicates whether the user is currently authenticated.
            Returns: true if the user is currently authenticated; otherwise, false.  The default is false until 
             authenticated.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, authenticationType):
        """ __new__(cls: type, name: str, authenticationType: AuthenticationType) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AuthenticationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.RightsManagement.AuthenticationType specified to the System.Security.RightsManagement.ContentUser.#ctor(System.String,System.Security.RightsManagement.AuthenticationType) constructor.

Get: AuthenticationType(self: ContentUser) -> AuthenticationType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user or group name specified to the System.Security.RightsManagement.ContentUser.#ctor(System.String,System.Security.RightsManagement.AuthenticationType) constructor.

Get: Name(self: ContentUser) -> str

"""


    AnyoneUser = None
    OwnerUser = None


class CryptoProvider(object, IDisposable):
    """ Provides digital rights management services for encrypting and decrypting protected content. """
    def Decrypt(self, cryptoText):
        """
        Decrypt(self: CryptoProvider, cryptoText: Array[Byte]) -> Array[Byte]
        
            Decrypts cipher text to clear text.
        
            cryptoText: The cipher text to decrypt.
            Returns: The decrypted clear text of cryptoText.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CryptoProvider)
            Releases all resources used by the System.Security.RightsManagement.CryptoProvider.
        """
        pass

    def Encrypt(self, clearText):
        """
        Encrypt(self: CryptoProvider, clearText: Array[Byte]) -> Array[Byte]
        
            Encrypts clear text to cipher text.
        
            clearText: The clear text content to encrypt.
            Returns: Encrypted cipher text of the given clearText.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BlockSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cipher block size, in bytes.

Get: BlockSize(self: CryptoProvider) -> int

"""

    BoundGrants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection listing the rights that passed verification and that are granted to the user.

Get: BoundGrants(self: CryptoProvider) -> ReadOnlyCollection[ContentGrant]

"""

    CanDecrypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the user has rights to decrypt.

Get: CanDecrypt(self: CryptoProvider) -> bool

"""

    CanEncrypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the user has rights to encrypt.

Get: CanEncrypt(self: CryptoProvider) -> bool

"""

    CanMergeBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether System.Security.RightsManagement.CryptoProvider.Encrypt(System.Byte[]) and System.Security.RightsManagement.CryptoProvider.Decrypt(System.Byte[]) can accept buffers that are different block sizes in length.

Get: CanMergeBlocks(self: CryptoProvider) -> bool

"""



class LocalizedNameDescriptionPair(object):
    """
    Represents an immutable (read-only) pair of "Name" and "Description" strings.
    
    LocalizedNameDescriptionPair(name: str, description: str)
    """
    def Equals(self, obj):
        """
        Equals(self: LocalizedNameDescriptionPair, obj: object) -> bool
        
            Indicates whether the System.Security.RightsManagement.LocalizedNameDescriptionPair.Name and 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Description properties of a given 
             object match those of this System.Security.RightsManagement.LocalizedNameDescriptionPair.
        
        
            obj: The object to compare the System.Security.RightsManagement.LocalizedNameDescriptionPair.Name and 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Description properties of.
        
            Returns: true if the System.Security.RightsManagement.LocalizedNameDescriptionPair.Name and 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Description properties of the 
             given object match those of this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LocalizedNameDescriptionPair) -> int
        
            Gets a computed hash code based on the 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Name and 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Description properties.
        
            Returns: A computed hash code based on the 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Name and 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.Description properties of this 
             System.Security.RightsManagement.LocalizedNameDescriptionPair.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, description):
        """ __new__(cls: type, name: str, description: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the locale description.

Get: Description(self: LocalizedNameDescriptionPair) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the locale name.

Get: Name(self: LocalizedNameDescriptionPair) -> str

"""



class PublishLicense(object):
    """
    Represents a signed rights managed publish license.
    
    PublishLicense(signedPublishLicense: str)
    """
    def AcquireUseLicense(self, secureEnvironment):
        """
        AcquireUseLicense(self: PublishLicense, secureEnvironment: SecureEnvironment) -> UseLicense
        
            Attempts to acquire a System.Security.RightsManagement.UseLicense for a user or user group in a 
             specified System.Security.RightsManagement.SecureEnvironment.
        
        
            secureEnvironment: The secure environment for license activation and binding.
            Returns: The System.Security.RightsManagement.UseLicense for a user or user group in the specified 
             secureEnvironment.
        """
        pass

    def AcquireUseLicenseNoUI(self, secureEnvironment):
        """
        AcquireUseLicenseNoUI(self: PublishLicense, secureEnvironment: SecureEnvironment) -> UseLicense
        
            Attempts to acquire a System.Security.RightsManagement.UseLicense for a user or user group in a 
             specified System.Security.RightsManagement.SecureEnvironment.
        
        
            secureEnvironment: The secure environment for license activation and binding.
            Returns: The System.Security.RightsManagement.UseLicense for a user or user group in the specified 
             secureEnvironment.
        """
        pass

    def DecryptUnsignedPublishLicense(self, cryptoProvider):
        """
        DecryptUnsignedPublishLicense(self: PublishLicense, cryptoProvider: CryptoProvider) -> UnsignedPublishLicense
        
            Returns a decrypted System.Security.RightsManagement.UnsignedPublishLicense version of this 
             signed System.Security.RightsManagement.PublishLicense.
        
        
            cryptoProvider: The rights management service to use for decrypting the license.
            Returns: A decrypted, unsigned version of this license.
        """
        pass

    def ToString(self):
        """
        ToString(self: PublishLicense) -> str
        
            Returns the serialized XrML�string that was�used to create this license.
            Returns: The serialized�Extensible Rights Markup Language (XrML) string that was�used to create this 
             license.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, signedPublishLicense):
        """ __new__(cls: type, signedPublishLicense: str) """
        pass

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the publisher-created content identifier.

Get: ContentId(self: PublishLicense) -> Guid

"""

    ReferralInfoName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the contact name for the author or publisher of the content.

Get: ReferralInfoName(self: PublishLicense) -> str

"""

    ReferralInfoUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the contact URI for the author or publisher of the content.

Get: ReferralInfoUri(self: PublishLicense) -> Uri

"""

    UseLicenseAcquisitionUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URI to use for acquiring a System.Security.RightsManagement.UseLicense.

Get: UseLicenseAcquisitionUrl(self: PublishLicense) -> Uri

"""



class RightsManagementException(Exception, ISerializable, _Exception):
    """
    Represents an error condition when a rights management operation cannot complete successfully.
    
    RightsManagementException()
    RightsManagementException(message: str)
    RightsManagementException(message: str, innerException: Exception)
    RightsManagementException(failureCode: RightsManagementFailureCode)
    RightsManagementException(failureCode: RightsManagementFailureCode, message: str)
    RightsManagementException(failureCode: RightsManagementFailureCode, innerException: Exception)
    RightsManagementException(failureCode: RightsManagementFailureCode, message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RightsManagementException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo store with the parameter name and 
             information about the exception.
        
        
            info: The object that holds the serialized data.
            context: The contextual information about the source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, failureCode: RightsManagementFailureCode)
        __new__(cls: type, failureCode: RightsManagementFailureCode, message: str)
        __new__(cls: type, failureCode: RightsManagementFailureCode, innerException: Exception)
        __new__(cls: type, failureCode: RightsManagementFailureCode, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FailureCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.RightsManagement.RightsManagementFailureCode for the error.

Get: FailureCode(self: RightsManagementException) -> RightsManagementFailureCode

"""



class RightsManagementFailureCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies error conditions that can occur when performing a rights management operation.
    
    enum RightsManagementFailureCode, values: Aborted (-2147168447), ActivationFailed (-2147168448), AdEntryNotFound (-2147168419), AlreadyInProgress (-2147168456), AuthenticationFailed (-2147168445), BadGetInfoQuery (-2147168494), BindAccessPrincipalNotEnabling (-2147168478), BindAccessUnsatisfied (-2147168477), BindContentNotInEndUseLicense (-2147168479), BindIndicatedPrincipalMissing (-2147168476), BindIntervalTimeViolated (-2147168465), BindMachineNotFoundInGroupIdentity (-2147168475), BindNoApplicableRevocationList (-2147168472), BindNoSatisfiedRightsGroup (-2147168464), BindPolicyViolation (-2147168485), BindRevocationListStale (-2147168473), BindRevokedIssuer (-2147168483), BindRevokedLicense (-2147168484), BindRevokedModule (-2147168480), BindRevokedPrincipal (-2147168482), BindRevokedResource (-2147168481), BindSpecifiedWorkMissing (-2147168463), BindValidityTimeViolated (-2147168488), BrokenCertChain (-2147168487), ClockRollbackDetected (-2147168491), CryptoOperationUnsupported (-2147168492), DebuggerDetected (-2147168416), EmailNotVerified (-2147168422), EnablingPrincipalFailure (-2147168496), EncryptionNotPermitted (-2147168508), EnvironmentCannotLoad (-2147168501), EnvironmentNotLoaded (-2147168502), ExpiredOfficialIssuanceLicenseTemplate (-2147168425), GlobalOptionAlreadySet (-2147168396), GroupIdentityNotSet (-2147168455), HidCorrupted (-2147168442), HidInvalid (-2147168423), IdMismatch (-2147168459), IncompatibleObjects (-2147168498), InfoNotInLicense (-2147168511), InfoNotPresent (-2147168495), InstallationFailed (-2147168443), InvalidAlgorithmType (-2147168503), InvalidClientLicensorCertificate (-2147168424), InvalidEmail (-2147168437), InvalidEncodingType (-2147168505), InvalidHandle (-2147168468), InvalidIssuanceLicenseTemplate (-2147168428), InvalidKeyLength (-2147168427), InvalidLicense (-2147168512), InvalidLicenseSignature (-2147168510), InvalidLockboxPath (-2147168399), InvalidLockboxType (-2147168400), InvalidNumericalValue (-2147168504), InvalidRegistryPath (-2147168398), InvalidServerResponse (-2147168441), InvalidTimeInfo (-2147168431), InvalidVersion (-2147168506), KeyTypeUnsupported (-2147168493), LibraryFail (-2147168497), LibraryUnsupportedPlugIn (-2147168474), LicenseAcquisitionFailed (-2147168460), LicenseBindingToWindowsIdentityFailed (-2147168429), ManifestPolicyViolation (-2147183860), MetadataNotSet (-2147168433), NeedsGroupIdentityActivation (-2147168450), NeedsMachineActivation (-2147168451), NoAesCryptoProvider (-2147168397), NoConnect (-2147168453), NoDistributionPointUrlFound (-2147168457), NoLicense (-2147168452), NoMoreData (-2147168461), NotAChain (-2147168418), NotSet (-2147168434), OutdatedModule (-2147168435), OutOfQuota (-2147168446), OwnerLicenseNotFound (-2147168395), QueryReportsNoResults (-2147168490), RecordNotFound (-2147168454), RequestDenied (-2147168417), RevocationInfoNotSet (-2147168432), RightNotGranted (-2147168507), RightNotSet (-2147168430), ServerError (-2147168444), ServerNotFound (-2147168438), ServiceGone (-2147168420), ServiceMoved (-2147168421), ServiceNotFound (-2147168440), Success (0), TooManyCertificates (-2147168458), TooManyLoadedEnvironments (-2147168500), UnexpectedException (-2147168489), UseDefault (-2147168439), ValidityTimeViolation (-2147168436)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Aborted = None
    ActivationFailed = None
    AdEntryNotFound = None
    AlreadyInProgress = None
    AuthenticationFailed = None
    BadGetInfoQuery = None
    BindAccessPrincipalNotEnabling = None
    BindAccessUnsatisfied = None
    BindContentNotInEndUseLicense = None
    BindIndicatedPrincipalMissing = None
    BindIntervalTimeViolated = None
    BindMachineNotFoundInGroupIdentity = None
    BindNoApplicableRevocationList = None
    BindNoSatisfiedRightsGroup = None
    BindPolicyViolation = None
    BindRevocationListStale = None
    BindRevokedIssuer = None
    BindRevokedLicense = None
    BindRevokedModule = None
    BindRevokedPrincipal = None
    BindRevokedResource = None
    BindSpecifiedWorkMissing = None
    BindValidityTimeViolated = None
    BrokenCertChain = None
    ClockRollbackDetected = None
    CryptoOperationUnsupported = None
    DebuggerDetected = None
    EmailNotVerified = None
    EnablingPrincipalFailure = None
    EncryptionNotPermitted = None
    EnvironmentCannotLoad = None
    EnvironmentNotLoaded = None
    ExpiredOfficialIssuanceLicenseTemplate = None
    GlobalOptionAlreadySet = None
    GroupIdentityNotSet = None
    HidCorrupted = None
    HidInvalid = None
    IdMismatch = None
    IncompatibleObjects = None
    InfoNotInLicense = None
    InfoNotPresent = None
    InstallationFailed = None
    InvalidAlgorithmType = None
    InvalidClientLicensorCertificate = None
    InvalidEmail = None
    InvalidEncodingType = None
    InvalidHandle = None
    InvalidIssuanceLicenseTemplate = None
    InvalidKeyLength = None
    InvalidLicense = None
    InvalidLicenseSignature = None
    InvalidLockboxPath = None
    InvalidLockboxType = None
    InvalidNumericalValue = None
    InvalidRegistryPath = None
    InvalidServerResponse = None
    InvalidTimeInfo = None
    InvalidVersion = None
    KeyTypeUnsupported = None
    LibraryFail = None
    LibraryUnsupportedPlugIn = None
    LicenseAcquisitionFailed = None
    LicenseBindingToWindowsIdentityFailed = None
    ManifestPolicyViolation = None
    MetadataNotSet = None
    NeedsGroupIdentityActivation = None
    NeedsMachineActivation = None
    NoAesCryptoProvider = None
    NoConnect = None
    NoDistributionPointUrlFound = None
    NoLicense = None
    NoMoreData = None
    NotAChain = None
    NotSet = None
    OutdatedModule = None
    OutOfQuota = None
    OwnerLicenseNotFound = None
    QueryReportsNoResults = None
    RecordNotFound = None
    RequestDenied = None
    RevocationInfoNotSet = None
    RightNotGranted = None
    RightNotSet = None
    ServerError = None
    ServerNotFound = None
    ServiceGone = None
    ServiceMoved = None
    ServiceNotFound = None
    Success = None
    TooManyCertificates = None
    TooManyLoadedEnvironments = None
    UnexpectedException = None
    UseDefault = None
    ValidityTimeViolation = None
    value__ = None


class SecureEnvironment(object, IDisposable):
    """ Represents a secure client session for user activation, license binding, and other rights management operations. """
    @staticmethod
    def Create(applicationManifest, *__args):
        """
        Create(applicationManifest: str, authentication: AuthenticationType, userActivationMode: UserActivationMode) -> SecureEnvironment
        
            Creates a secure client session given an application rights manifest, 
             System.Security.RightsManagement.AuthenticationType, and 
             System.Security.RightsManagement.UserActivationMode.
        
        
            applicationManifest: The application rights manifest.
            authentication: The method of authentication.
            userActivationMode: The type of the user rights account certificate.
            Returns: A secure client session for activation, license binding, and other rights management operations.
        Create(applicationManifest: str, user: ContentUser) -> SecureEnvironment
        
            Creates a secure client session for a specified user with a given rights manifest.
        
            applicationManifest: The application rights manifest.
            user: The user or user-group for granting access to rights managed content.
            Returns: A secure client session for activation, license binding, and other rights management operations.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SecureEnvironment)
            Releases all resources used by the System.Security.RightsManagement.SecureEnvironment.
        """
        pass

    @staticmethod
    def GetActivatedUsers():
        """
        GetActivatedUsers() -> ReadOnlyCollection[ContentUser]
        
            Returns a list of the activated users.
            Returns: A list of the currently activated users.
        """
        pass

    @staticmethod
    def IsUserActivated(user):
        """
        IsUserActivated(user: ContentUser) -> bool
        
            Indicates whether a given user has been activated for accessing rights managed content.
        
            user: The user or user-group for granting access to rights managed content.
            Returns: true if the given user has been activated for accessing rights managed content; otherwise, false.
        """
        pass

    @staticmethod
    def RemoveActivatedUser(user):
        """
        RemoveActivatedUser(user: ContentUser)
            Removes the license activation for a specified user.
        
            user: The user to remove the license activation for.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ApplicationManifest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.RightsManagement.SecureEnvironment.ApplicationManifest specified when the System.Security.RightsManagement.SecureEnvironment was created.

Get: ApplicationManifest(self: SecureEnvironment) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user or user-group specified when the System.Security.RightsManagement.SecureEnvironment was created.

Get: User(self: SecureEnvironment) -> ContentUser

"""



class UnsignedPublishLicense(object):
    """
    Represents an unsigned rights managed�System.Security.RightsManagement.PublishLicense or an unsigned System.Security.RightsManagement.PublishLicense template.
    
    UnsignedPublishLicense()
    UnsignedPublishLicense(publishLicenseTemplate: str)
    """
    def Sign(self, secureEnvironment, authorUseLicense):
        """
        Sign(self: UnsignedPublishLicense, secureEnvironment: SecureEnvironment) -> (PublishLicense, UseLicense)
        
            Creates a signed System.Security.RightsManagement.PublishLicense and returns a 
             System.Security.RightsManagement.UseLicense for the document author.
        
        
            secureEnvironment: The secure environment for license activation and binding.
            Returns: The signed System.Security.RightsManagement.PublishLicense that is created by signing this 
             System.Security.RightsManagement.UnsignedPublishLicense.
        """
        pass

    def ToString(self):
        """
        ToString(self: UnsignedPublishLicense) -> str
        
            Returns a serialized template created from the XrML of the 
             System.Security.RightsManagement.UnsignedPublishLicense.
        
            Returns: A serialized template created from the XrML of the 
             System.Security.RightsManagement.UnsignedPublishLicense.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, publishLicenseTemplate=None):
        """
        __new__(cls: type)
        __new__(cls: type, publishLicenseTemplate: str)
        """
        pass

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the publisher-created content identifier.

Get: ContentId(self: UnsignedPublishLicense) -> Guid

Set: ContentId(self: UnsignedPublishLicense) = value
"""

    Grants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of assigned user rights.

Get: Grants(self: UnsignedPublishLicense) -> ICollection[ContentGrant]

"""

    LocalizedNameDescriptionDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of name and description pairs.

Get: LocalizedNameDescriptionDictionary(self: UnsignedPublishLicense) -> IDictionary[int, LocalizedNameDescriptionPair]

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the content owner.

Get: Owner(self: UnsignedPublishLicense) -> ContentUser

Set: Owner(self: UnsignedPublishLicense) = value
"""

    ReferralInfoName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the contact name for the author or publisher of the content.

Get: ReferralInfoName(self: UnsignedPublishLicense) -> str

Set: ReferralInfoName(self: UnsignedPublishLicense) = value
"""

    ReferralInfoUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the contact URI for the author or publisher of the content.

Get: ReferralInfoUri(self: UnsignedPublishLicense) -> Uri

Set: ReferralInfoUri(self: UnsignedPublishLicense) = value
"""



class UseLicense(object):
    """
    Represents a license that enables access to protected rights managed content.
    
    UseLicense(useLicense: str)
    """
    def Bind(self, secureEnvironment):
        """
        Bind(self: UseLicense, secureEnvironment: SecureEnvironment) -> CryptoProvider
        
            Binds the license to a given System.Security.RightsManagement.SecureEnvironment.
        
            secureEnvironment: The environment to bind the license to.
            Returns: A System.Security.RightsManagement.CryptoProvider instance if the license binding succeeded; 
             otherwise, null.
        """
        pass

    def Equals(self, x):
        """
        Equals(self: UseLicense, x: object) -> bool
        
            Indicates if this license is equivalent to another given license.
        
            x: The license to compare.
            Returns: true if both licenses are the equivalent; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UseLicense) -> int
        
            Returns the hash code associated with this license.
            Returns: A hash code for this license.
        """
        pass

    def ToString(self):
        """
        ToString(self: UseLicense) -> str
        
            Returns the serialized XrML string used to create this license.
            Returns: The serialized Extensible Rights Markup Language (XrML) string originally passed to the 
             System.Security.RightsManagement.UseLicense.#ctor(System.String) constructor.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, useLicense):
        """ __new__(cls: type, useLicense: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ApplicationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application data dictionary that contains key/value pairs passed from the publishing application to the consuming application.

Get: ApplicationData(self: UseLicense) -> IDictionary[str, str]

"""

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content identifier created by the publisher.

Get: ContentId(self: UseLicense) -> Guid

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the owner of the license.

Get: Owner(self: UseLicense) -> ContentUser

"""



class UserActivationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of user Rights Account Certificate to request for rights management activation.
    
    enum UserActivationMode, values: Permanent (0), Temporary (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Permanent = None
    Temporary = None
    value__ = None



# encoding: utf-8
# module System.Security.Cryptography.X509Certificates calls itself X509Certificates
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class OpenFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the way to open the X.509 certificate store.
    
    enum (flags) OpenFlags, values: IncludeArchived (8), MaxAllowed (2), OpenExistingOnly (4), ReadOnly (0), ReadWrite (1)
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

    IncludeArchived = None
    MaxAllowed = None
    OpenExistingOnly = None
    ReadOnly = None
    ReadWrite = None
    value__ = None


class PublicKey(object):
    """
    Represents a certificate's public key information. This class cannot be inherited.
    
    PublicKey(oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData)
    """
    @staticmethod # known case of __new__
    def __new__(self, oid, parameters, keyValue):
        """ __new__(cls: type, oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData) """
        pass

    EncodedKeyValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ASN.1-encoded representation of the public key value.

Get: EncodedKeyValue(self: PublicKey) -> AsnEncodedData

"""

    EncodedParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ASN.1-encoded representation of the public key parameters.

Get: EncodedParameters(self: PublicKey) -> AsnEncodedData

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Security.Cryptography.RSACryptoServiceProvider or System.Security.Cryptography.DSACryptoServiceProvider object representing the public key.

Get: Key(self: PublicKey) -> AsymmetricAlgorithm

"""

    Oid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object identifier (OID) object of the public key.

Get: Oid(self: PublicKey) -> Oid

"""



class StoreLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the location of the X.509 certificate store.
    
    enum StoreLocation, values: CurrentUser (1), LocalMachine (2)
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

    CurrentUser = None
    LocalMachine = None
    value__ = None


class StoreName(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the name of the X.509 certificate store to open.
    
    enum StoreName, values: AddressBook (1), AuthRoot (2), CertificateAuthority (3), Disallowed (4), My (5), Root (6), TrustedPeople (7), TrustedPublisher (8)
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

    AddressBook = None
    AuthRoot = None
    CertificateAuthority = None
    Disallowed = None
    My = None
    Root = None
    TrustedPeople = None
    TrustedPublisher = None
    value__ = None


class X500DistinguishedName(AsnEncodedData):
    """
    Represents the distinguished name of an X509 certificate. This class cannot be inherited.
    
    X500DistinguishedName(encodedDistinguishedName: Array[Byte])
    X500DistinguishedName(encodedDistinguishedName: AsnEncodedData)
    X500DistinguishedName(distinguishedName: X500DistinguishedName)
    X500DistinguishedName(distinguishedName: str)
    X500DistinguishedName(distinguishedName: str, flag: X500DistinguishedNameFlags)
    """
    def Decode(self, flag):
        """
        Decode(self: X500DistinguishedName, flag: X500DistinguishedNameFlags) -> str
        
            Decodes a distinguished name using the characteristics specified by the flag parameter.
        
            flag: A flag that specifies the characteristics of the 
             System.Security.Cryptography.X509Certificates.X500DistinguishedName object.
        
            Returns: The decoded distinguished name.
        """
        pass

    def Format(self, multiLine):
        """
        Format(self: X500DistinguishedName, multiLine: bool) -> str
        
            Returns a formatted version of an X500 distinguished name for printing or for output to a text 
             window or to a console.
        
        
            multiLine: true if the return string should contain carriage returns; otherwise, false.
            Returns: A formatted string that represents the X500 distinguished name.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, encodedDistinguishedName: Array[Byte])
        __new__(cls: type, encodedDistinguishedName: AsnEncodedData)
        __new__(cls: type, distinguishedName: X500DistinguishedName)
        __new__(cls: type, distinguishedName: str)
        __new__(cls: type, distinguishedName: str, flag: X500DistinguishedNameFlags)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the comma-delimited distinguished name from an X500 certificate.

Get: Name(self: X500DistinguishedName) -> str

"""



class X500DistinguishedNameFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies characteristics of the X.500 distinguished name.
    
    enum (flags) X500DistinguishedNameFlags, values: DoNotUsePlusSign (32), DoNotUseQuotes (64), ForceUTF8Encoding (16384), None (0), Reversed (1), UseCommas (128), UseNewLines (256), UseSemicolons (16), UseT61Encoding (8192), UseUTF8Encoding (4096)
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

    DoNotUsePlusSign = None
    DoNotUseQuotes = None
    ForceUTF8Encoding = None
    None = None
    Reversed = None
    UseCommas = None
    UseNewLines = None
    UseSemicolons = None
    UseT61Encoding = None
    UseUTF8Encoding = None
    value__ = None


class X509Extension(AsnEncodedData):
    """
    Represents an X509 extension.
    
    X509Extension(oid: str, rawData: Array[Byte], critical: bool)
    X509Extension(encodedExtension: AsnEncodedData, critical: bool)
    X509Extension(oid: Oid, rawData: Array[Byte], critical: bool)
    """
    def CopyFrom(self, asnEncodedData):
        """
        CopyFrom(self: X509Extension, asnEncodedData: AsnEncodedData)
            Copies the extension properties of the specified System.Security.Cryptography.AsnEncodedData 
             object.
        
        
            asnEncodedData: The System.Security.Cryptography.AsnEncodedData to be copied.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, oid: str, rawData: Array[Byte], critical: bool)
        __new__(cls: type, encodedExtension: AsnEncodedData, critical: bool)
        __new__(cls: type, oid: Oid, rawData: Array[Byte], critical: bool)
        """
        pass

    Critical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value indicating whether the extension is critical.

Get: Critical(self: X509Extension) -> bool

Set: Critical(self: X509Extension) = value
"""



class X509BasicConstraintsExtension(X509Extension):
    """
    Defines the constraints set on a certificate. This class cannot be inherited.
    
    X509BasicConstraintsExtension()
    X509BasicConstraintsExtension(certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool)
    X509BasicConstraintsExtension(encodedBasicConstraints: AsnEncodedData, critical: bool)
    """
    def CopyFrom(self, asnEncodedData):
        """
        CopyFrom(self: X509BasicConstraintsExtension, asnEncodedData: AsnEncodedData)
            Initializes a new instance of the 
             System.Security.Cryptography.X509Certificates.X509BasicConstraintsExtension class using an 
             System.Security.Cryptography.AsnEncodedData object.
        
        
            asnEncodedData: The encoded data to use to create the extension.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool)
        __new__(cls: type, encodedBasicConstraints: AsnEncodedData, critical: bool)
        """
        pass

    CertificateAuthority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a certificate is a certificate authority (CA) certificate.

Get: CertificateAuthority(self: X509BasicConstraintsExtension) -> bool

"""

    HasPathLengthConstraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a certificate has a restriction on the number of path levels it allows.

Get: HasPathLengthConstraint(self: X509BasicConstraintsExtension) -> bool

"""

    PathLengthConstraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of levels allowed in a certificate's path.

Get: PathLengthConstraint(self: X509BasicConstraintsExtension) -> int

"""



class X509Certificate(object, IDisposable, IDeserializationCallback, ISerializable):
    """
    Provides methods that help you use X.509 v.3 certificates.
    
    X509Certificate()
    X509Certificate(data: Array[Byte])
    X509Certificate(rawData: Array[Byte], password: str)
    X509Certificate(rawData: Array[Byte], password: SecureString)
    X509Certificate(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(fileName: str)
    X509Certificate(fileName: str, password: str)
    X509Certificate(fileName: str, password: SecureString)
    X509Certificate(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(handle: IntPtr)
    X509Certificate(cert: X509Certificate)
    X509Certificate(info: SerializationInfo, context: StreamingContext)
    """
    @staticmethod
    def CreateFromCertFile(filename):
        """
        CreateFromCertFile(filename: str) -> X509Certificate
        
            Creates an X.509v3 certificate from the specified PKCS7 signed file.
        
            filename: The path of the PKCS7 signed file from which to create the X.509 certificate.
            Returns: The newly created X.509 certificate.
        """
        pass

    @staticmethod
    def CreateFromSignedFile(filename):
        """
        CreateFromSignedFile(filename: str) -> X509Certificate
        
            Creates an X.509v3 certificate from the specified signed file.
        
            filename: The path of the signed file from which to create the X.509 certificate.
            Returns: The newly created X.509 certificate.
        """
        pass

    def Dispose(self):
        """ Dispose(self: X509Certificate) """
        pass

    def Equals(self, *__args):
        """
        Equals(self: X509Certificate, other: X509Certificate) -> bool
        
            Compares two System.Security.Cryptography.X509Certificates.X509Certificate objects for equality.
        
            other: An System.Security.Cryptography.X509Certificates.X509Certificate object to compare to the 
             current object.
        
            Returns: true if the current System.Security.Cryptography.X509Certificates.X509Certificate object is 
             equal to the object specified by the other parameter; otherwise, false.
        
        Equals(self: X509Certificate, obj: object) -> bool
        
            Compares two System.Security.Cryptography.X509Certificates.X509Certificate objects for equality.
        
            obj: An System.Security.Cryptography.X509Certificates.X509Certificate object to compare to the 
             current object.
        
            Returns: true if the current System.Security.Cryptography.X509Certificates.X509Certificate object is 
             equal to the object specified by the other parameter; otherwise, false.
        """
        pass

    def Export(self, contentType, password=None):
        """
        Export(self: X509Certificate, contentType: X509ContentType, password: SecureString) -> Array[Byte]
        
            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a 
             byte array using the specified format and a password.
        
        
            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes 
             how to format the output data.
        
            password: The password required to access the X.509 certificate data.
            Returns: A byte array that represents the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        
        Export(self: X509Certificate, contentType: X509ContentType, password: str) -> Array[Byte]
        
            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a 
             byte array in a format described by one of the 
             System.Security.Cryptography.X509Certificates.X509ContentType values, and using the specified 
             password.
        
        
            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes 
             how to format the output data.
        
            password: The password required to access the X.509 certificate data.
            Returns: An array of bytes that represents the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        
        Export(self: X509Certificate, contentType: X509ContentType) -> Array[Byte]
        
            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a 
             byte array in a format described by one of the 
             System.Security.Cryptography.X509Certificates.X509ContentType values.
        
        
            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes 
             how to format the output data.
        
            Returns: An array of bytes that represents the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        """
        pass

    def FormatDate(self, *args): #cannot find CLR method
        """
        FormatDate(date: DateTime) -> str
        
            Converts the specified date and time to a string.
        
            date: The date and time to convert.
            Returns: A string representation of the value of the System.DateTime object.
        """
        pass

    def GetCertHash(self):
        """
        GetCertHash(self: X509Certificate) -> Array[Byte]
        
            Returns the hash value for the X.509v3 certificate as an array of bytes.
            Returns: The hash value for the X.509 certificate.
        """
        pass

    def GetCertHashString(self):
        """
        GetCertHashString(self: X509Certificate) -> str
        
            Returns the SHA1 hash value for the X.509v3 certificate as a hexadecimal string.
            Returns: The hexadecimal string representation of the X.509 certificate hash value.
        """
        pass

    def GetEffectiveDateString(self):
        """
        GetEffectiveDateString(self: X509Certificate) -> str
        
            Returns the effective date of this X.509v3 certificate.
            Returns: The effective date for this X.509 certificate.
        """
        pass

    def GetExpirationDateString(self):
        """
        GetExpirationDateString(self: X509Certificate) -> str
        
            Returns the expiration date of this X.509v3 certificate.
            Returns: The expiration date for this X.509 certificate.
        """
        pass

    def GetFormat(self):
        """
        GetFormat(self: X509Certificate) -> str
        
            Returns the name of the format of this X.509v3 certificate.
            Returns: The format of this X.509 certificate.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: X509Certificate) -> int
        
            Returns the hash code for the X.509v3 certificate as an integer.
            Returns: The hash code for the X.509 certificate as an integer.
        """
        pass

    def GetIssuerName(self):
        """
        GetIssuerName(self: X509Certificate) -> str
        
            Returns the name of the certification authority that issued the X.509v3 certificate.
            Returns: The name of the certification authority that issued the X.509 certificate.
        """
        pass

    def GetKeyAlgorithm(self):
        """
        GetKeyAlgorithm(self: X509Certificate) -> str
        
            Returns the key algorithm information for this X.509v3 certificate.
            Returns: The key algorithm information for this X.509 certificate as a string.
        """
        pass

    def GetKeyAlgorithmParameters(self):
        """
        GetKeyAlgorithmParameters(self: X509Certificate) -> Array[Byte]
        
            Returns the key algorithm parameters for the X.509v3 certificate.
            Returns: The key algorithm parameters for the X.509 certificate as an array of bytes.
        """
        pass

    def GetKeyAlgorithmParametersString(self):
        """
        GetKeyAlgorithmParametersString(self: X509Certificate) -> str
        
            Returns the key algorithm parameters for the X.509v3 certificate.
            Returns: The key algorithm parameters for the X.509 certificate as a hexadecimal string.
        """
        pass

    def GetName(self):
        """
        GetName(self: X509Certificate) -> str
        
            Returns the name of the principal to which the certificate was issued.
            Returns: The name of the principal to which the certificate was issued.
        """
        pass

    def GetPublicKey(self):
        """
        GetPublicKey(self: X509Certificate) -> Array[Byte]
        
            Returns the public key for the X.509v3 certificate.
            Returns: The public key for the X.509 certificate as an array of bytes.
        """
        pass

    def GetPublicKeyString(self):
        """
        GetPublicKeyString(self: X509Certificate) -> str
        
            Returns the public key for the X.509v3 certificate.
            Returns: The public key for the X.509 certificate as a hexadecimal string.
        """
        pass

    def GetRawCertData(self):
        """
        GetRawCertData(self: X509Certificate) -> Array[Byte]
        
            Returns the raw data for the entire X.509v3 certificate.
            Returns: A byte array containing the X.509 certificate data.
        """
        pass

    def GetRawCertDataString(self):
        """
        GetRawCertDataString(self: X509Certificate) -> str
        
            Returns the raw data for the entire X.509v3 certificate.
            Returns: The X.509 certificate data as a hexadecimal string.
        """
        pass

    def GetSerialNumber(self):
        """
        GetSerialNumber(self: X509Certificate) -> Array[Byte]
        
            Returns the serial number of the X.509v3 certificate.
            Returns: The serial number of the X.509 certificate as an array of bytes.
        """
        pass

    def GetSerialNumberString(self):
        """
        GetSerialNumberString(self: X509Certificate) -> str
        
            Returns the serial number of the X.509v3 certificate.
            Returns: The serial number of the X.509 certificate as a hexadecimal string.
        """
        pass

    def Import(self, *__args):
        """
        Import(self: X509Certificate, fileName: str)
            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with 
             information from a certificate file.
        
        
            fileName: The name of a certificate file represented as a string.
        Import(self: X509Certificate, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with 
             information from a certificate file, a password, and a 
             System.Security.Cryptography.X509Certificates.X509KeyStorageFlags value.
        
        
            fileName: The name of a certificate file represented as a string.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the 
             certificate.
        
        Import(self: X509Certificate, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate object with 
             information from a certificate file, a password, and a key storage flag.
        
        
            fileName: The name of a certificate file.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the 
             certificate.
        
        Import(self: X509Certificate, rawData: Array[Byte])
            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with data 
             from a byte array.
        
        
            rawData: A byte array containing data from an X.509 certificate.
        Import(self: X509Certificate, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object using data 
             from a byte array, a password, and flags for determining how the private key is imported.
        
        
            rawData: A byte array containing data from an X.509 certificate.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the 
             certificate.
        
        Import(self: X509Certificate, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate object using data 
             from a byte array, a password, and a key storage flag.
        
        
            rawData: A byte array that contains data from an X.509 certificate.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the 
             certificate.
        """
        pass

    def Reset(self):
        """
        Reset(self: X509Certificate)
            Resets the state of the System.Security.Cryptography.X509Certificates.X509Certificate2 object.
        """
        pass

    def ToString(self, fVerbose=None):
        """
        ToString(self: X509Certificate, fVerbose: bool) -> str
        
            Returns a string representation of the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object, with extra information, if 
             specified.
        
        
            fVerbose: true to produce the verbose form of the string representation; otherwise, false.
            Returns: A string representation of the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        
        ToString(self: X509Certificate) -> str
        
            Returns a string representation of the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        
            Returns: A string representation of the current 
             System.Security.Cryptography.X509Certificates.X509Certificate object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, data: Array[Byte])
        __new__(cls: type, rawData: Array[Byte], password: str)
        __new__(cls: type, rawData: Array[Byte], password: SecureString)
        __new__(cls: type, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, password: str)
        __new__(cls: type, fileName: str, password: SecureString)
        __new__(cls: type, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, handle: IntPtr)
        __new__(cls: type, cert: X509Certificate)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to a Microsoft Cryptographic API certificate context described by an unmanaged PCCERT_CONTEXT structure.

Get: Handle(self: X509Certificate) -> IntPtr

"""

    Issuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the certificate authority that issued the X.509v3 certificate.

Get: Issuer(self: X509Certificate) -> str

"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the subject distinguished name from the certificate.

Get: Subject(self: X509Certificate) -> str

"""



class X509Certificate2(X509Certificate, IDisposable, IDeserializationCallback, ISerializable):
    """
    Represents an X.509 certificate.
    
    X509Certificate2()
    X509Certificate2(rawData: Array[Byte])
    X509Certificate2(rawData: Array[Byte], password: str)
    X509Certificate2(rawData: Array[Byte], password: SecureString)
    X509Certificate2(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(fileName: str)
    X509Certificate2(fileName: str, password: str)
    X509Certificate2(fileName: str, password: SecureString)
    X509Certificate2(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(handle: IntPtr)
    X509Certificate2(certificate: X509Certificate)
    """
    def Dispose(self):
        """ Dispose(self: X509Certificate, disposing: bool) """
        pass

    @staticmethod
    def GetCertContentType(*__args):
        """
        GetCertContentType(fileName: str) -> X509ContentType
        
            Indicates the type of certificate contained in a file.
        
            fileName: The name of a certificate file.
            Returns: An System.Security.Cryptography.X509Certificates.X509ContentType object.
        GetCertContentType(rawData: Array[Byte]) -> X509ContentType
        
            Indicates the type of certificate contained in a byte array.
        
            rawData: A byte array containing data from an X.509 certificate.
            Returns: An System.Security.Cryptography.X509Certificates.X509ContentType object.
        """
        pass

    def GetNameInfo(self, nameType, forIssuer):
        """
        GetNameInfo(self: X509Certificate2, nameType: X509NameType, forIssuer: bool) -> str
        
            Gets the subject and issuer names from a certificate.
        
            nameType: The System.Security.Cryptography.X509Certificates.X509NameType value for the subject.
            forIssuer: true to include the issuer name; otherwise, false.
            Returns: The name of the certificate.
        """
        pass

    def Import(self, *__args):
        """
        Import(self: X509Certificate2, fileName: str)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object with 
             information from a certificate file.
        
        
            fileName: The name of a certificate.
        Import(self: X509Certificate2, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object with 
             information from a certificate file, a password, and a 
             System.Security.Cryptography.X509Certificates.X509KeyStorageFlags value.
        
        
            fileName: The name of a certificate file.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the private 
             key of the certificate.
        
        Import(self: X509Certificate2, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object with 
             information from a certificate file, a password, and a key storage flag.
        
        
            fileName: The name of a certificate file.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the private 
             key of the certificate.
        
        Import(self: X509Certificate2, rawData: Array[Byte])
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object with data 
             from a byte array.
        
        
            rawData: A byte array containing data from an X.509 certificate.
        Import(self: X509Certificate2, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object using data 
             from a byte array, a password, and flags for determining how to import the private key.
        
        
            rawData: A byte array containing data from an X.509 certificate.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the private 
             key of the certificate.
        
        Import(self: X509Certificate2, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
            Populates an System.Security.Cryptography.X509Certificates.X509Certificate2 object using data 
             from a byte array, a password, and a key storage flag.
        
        
            rawData: A byte array that contains data from an X.509 certificate.
            password: The password required to access the X.509 certificate data.
            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the private 
             key of the certificate.
        """
        pass

    def Reset(self):
        """
        Reset(self: X509Certificate2)
            Resets the state of an System.Security.Cryptography.X509Certificates.X509Certificate2 object.
        """
        pass

    def ToString(self, verbose=None):
        """
        ToString(self: X509Certificate2, verbose: bool) -> str
        
            Displays an X.509 certificate in text format.
        
            verbose: true to display the public key, private key, extensions, and so forth; false to display 
             information that is similar to the 
             System.Security.Cryptography.X509Certificates.X509Certificate2 class, including thumbprint, 
             serial number, subject and issuer names, and so on.
        
            Returns: The certificate information.
        ToString(self: X509Certificate2) -> str
        
            Displays an X.509 certificate in text format.
            Returns: The certificate information.
        """
        pass

    def Verify(self):
        """
        Verify(self: X509Certificate2) -> bool
        
            Performs a X.509 chain validation using basic validation policy.
            Returns: true if the validation succeeds; false if the validation fails.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, rawData: Array[Byte])
        __new__(cls: type, rawData: Array[Byte], password: str)
        __new__(cls: type, rawData: Array[Byte], password: SecureString)
        __new__(cls: type, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, password: str)
        __new__(cls: type, fileName: str, password: SecureString)
        __new__(cls: type, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
        __new__(cls: type, handle: IntPtr)
        __new__(cls: type, certificate: X509Certificate)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Archived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating that an X.509 certificate is archived.

Get: Archived(self: X509Certificate2) -> bool

Set: Archived(self: X509Certificate2) = value
"""

    Extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Security.Cryptography.X509Certificates.X509Extension objects.

Get: Extensions(self: X509Certificate2) -> X509ExtensionCollection

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the associated alias for a certificate.

Get: FriendlyName(self: X509Certificate2) -> str

Set: FriendlyName(self: X509Certificate2) = value
"""

    HasPrivateKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an System.Security.Cryptography.X509Certificates.X509Certificate2 object contains a private key.

Get: HasPrivateKey(self: X509Certificate2) -> bool

"""

    IssuerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distinguished name of the certificate issuer.

Get: IssuerName(self: X509Certificate2) -> X500DistinguishedName

"""

    NotAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date in local time after which a certificate is no longer valid.

Get: NotAfter(self: X509Certificate2) -> DateTime

"""

    NotBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date in local time on which a certificate becomes valid.

Get: NotBefore(self: X509Certificate2) -> DateTime

"""

    PrivateKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.Cryptography.AsymmetricAlgorithm object that represents the private key associated with a certificate.

Get: PrivateKey(self: X509Certificate2) -> AsymmetricAlgorithm

Set: PrivateKey(self: X509Certificate2) = value
"""

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Security.Cryptography.X509Certificates.X509Certificate2.PublicKey object associated with a certificate.

Get: PublicKey(self: X509Certificate2) -> PublicKey

"""

    RawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw data of a certificate.

Get: RawData(self: X509Certificate2) -> Array[Byte]

"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the serial number of a certificate.

Get: SerialNumber(self: X509Certificate2) -> str

"""

    SignatureAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm used to create the signature of a certificate.

Get: SignatureAlgorithm(self: X509Certificate2) -> Oid

"""

    SubjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the subject distinguished name from a certificate.

Get: SubjectName(self: X509Certificate2) -> X500DistinguishedName

"""

    Thumbprint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the thumbprint of a certificate.

Get: Thumbprint(self: X509Certificate2) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the X.509 format version of a certificate.

Get: Version(self: X509Certificate2) -> int

"""



class X509CertificateCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Defines a collection that stores System.Security.Cryptography.X509Certificates.X509Certificate objects.
    
    X509CertificateCollection()
    X509CertificateCollection(value: X509CertificateCollection)
    X509CertificateCollection(value: Array[X509Certificate])
    """
    def Add(self, value):
        """
        Add(self: X509CertificateCollection, value: X509Certificate) -> int
        
            Adds an System.Security.Cryptography.X509Certificates.X509Certificate with the specified value 
             to the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
        
            value: The System.Security.Cryptography.X509Certificates.X509Certificate to add to the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
            Returns: The index into the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection at which the new 
             System.Security.Cryptography.X509Certificates.X509Certificate was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: X509CertificateCollection, value: X509CertificateCollection)
            Copies the elements of the specified 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection to the end of the 
             current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
        
            value: The System.Security.Cryptography.X509Certificates.X509CertificateCollection containing the 
             objects to add to the collection.
        
        AddRange(self: X509CertificateCollection, value: Array[X509Certificate])
            Copies the elements of an array of type 
             System.Security.Cryptography.X509Certificates.X509Certificate to the end of the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
        
            value: The array of type System.Security.Cryptography.X509Certificates.X509Certificate containing the 
             objects to add to the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: X509CertificateCollection, value: X509Certificate) -> bool
        
            Gets a value indicating whether the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection contains the specified 
             System.Security.Cryptography.X509Certificates.X509Certificate.
        
        
            value: The System.Security.Cryptography.X509Certificates.X509Certificate to locate.
            Returns: true if the System.Security.Cryptography.X509Certificates.X509Certificate is contained in this 
             collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: X509CertificateCollection, array: Array[X509Certificate], index: int)
            Copies the System.Security.Cryptography.X509Certificates.X509Certificate values in the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection to a one-dimensional 
             System.Array instance at the specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
            index: The index into array to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: X509CertificateCollection) -> X509CertificateEnumerator
        
            Returns an enumerator that can iterate through the 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
            Returns: An enumerator of the subelements of 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection you can use to iterate 
             through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: X509CertificateCollection) -> int
        
            Builds a hash value based on all values contained in the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
            Returns: A hash value based on all values contained in the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: X509CertificateCollection, value: X509Certificate) -> int
        
            Returns the index of the specified System.Security.Cryptography.X509Certificates.X509Certificate 
             in the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
        
            value: The System.Security.Cryptography.X509Certificates.X509Certificate to locate.
            Returns: The index of the System.Security.Cryptography.X509Certificates.X509Certificate specified by the 
             value parameter in the System.Security.Cryptography.X509Certificates.X509CertificateCollection, 
             if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: X509CertificateCollection, index: int, value: X509Certificate)
            Inserts a System.Security.Cryptography.X509Certificates.X509Certificate into the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection at the specified index.
        
        
            index: The zero-based index where value should be inserted.
            value: The System.Security.Cryptography.X509Certificates.X509Certificate to insert.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: X509CertificateCollection, value: X509Certificate)
            Removes a specific System.Security.Cryptography.X509Certificates.X509Certificate from the 
             current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        
        
            value: The System.Security.Cryptography.X509Certificates.X509Certificate to remove from the current 
             System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: X509CertificateCollection)
        __new__(cls: type, value: Array[X509Certificate])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


    X509CertificateEnumerator = None


class X509Certificate2Collection(X509CertificateCollection, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.Security.Cryptography.X509Certificates.X509Certificate2 objects. This class cannot be inherited.
    
    X509Certificate2Collection()
    X509Certificate2Collection(certificate: X509Certificate2)
    X509Certificate2Collection(certificates: X509Certificate2Collection)
    X509Certificate2Collection(certificates: Array[X509Certificate2])
    """
    def Add(self, *__args):
        """
        Add(self: X509Certificate2Collection, certificate: X509Certificate2) -> int
        
            Adds an object to the end of the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection.
        
        
            certificate: An X.509 certificate represented as an 
             System.Security.Cryptography.X509Certificates.X509Certificate2 object.
        
            Returns: The System.Security.Cryptography.X509Certificates.X509Certificate2Collection index at which the 
             certificate has been added.
        """
        pass

    def AddRange(self, *__args):
        """
        AddRange(self: X509Certificate2Collection, certificates: X509Certificate2Collection)
            Adds multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object to another 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            certificates: An System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        AddRange(self: X509Certificate2Collection, certificates: Array[X509Certificate2])
            Adds multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an array 
             to the System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            certificates: An array of System.Security.Cryptography.X509Certificates.X509Certificate2 objects.
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: X509Certificate2Collection, certificate: X509Certificate2) -> bool
        
            Determines whether the System.Security.Cryptography.X509Certificates.X509Certificate2Collection 
             object contains a specific certificate.
        
        
            certificate: The System.Security.Cryptography.X509Certificates.X509Certificate2 object to locate in the 
             collection.
        
            Returns: true if the System.Security.Cryptography.X509Certificates.X509Certificate2Collection contains 
             the specified certificate; otherwise, false.
        """
        pass

    def Export(self, contentType, password=None):
        """
        Export(self: X509Certificate2Collection, contentType: X509ContentType, password: str) -> Array[Byte]
        
            Exports X.509 certificate information into a byte array using a password.
        
            contentType: A supported System.Security.Cryptography.X509Certificates.X509ContentType object.
            password: A string used to protect the byte array.
            Returns: X.509 certificate information in a byte array.
        Export(self: X509Certificate2Collection, contentType: X509ContentType) -> Array[Byte]
        
            Exports X.509 certificate information into a byte array.
        
            contentType: A supported System.Security.Cryptography.X509Certificates.X509ContentType object.
            Returns: X.509 certificate information in a byte array.
        """
        pass

    def Find(self, findType, findValue, validOnly):
        """
        Find(self: X509Certificate2Collection, findType: X509FindType, findValue: object, validOnly: bool) -> X509Certificate2Collection
        
            Searches an System.Security.Cryptography.X509Certificates.X509Certificate2Collection object 
             using the search criteria specified by the 
             System.Security.Cryptography.X509Certificates.X509FindType enumeration and the findValue object.
        
        
            findType: One of the System.Security.Cryptography.X509Certificates.X509FindType  values.
            findValue: The search criteria as an object.
            validOnly: true to allow only valid certificates to be returned from the search; otherwise, false.
            Returns: An System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: X509Certificate2Collection) -> X509Certificate2Enumerator
        
            Returns an enumerator that can iterate through a 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
            Returns: An System.Security.Cryptography.X509Certificates.X509Certificate2Enumerator object that can 
             iterate through the System.Security.Cryptography.X509Certificates.X509Certificate2Collection 
             object.
        """
        pass

    def Import(self, *__args):
        """
        Import(self: X509Certificate2Collection, fileName: str)
            Imports a certificate file into a 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            fileName: The name of the file containing the certificate information.
        Import(self: X509Certificate2Collection, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
            Imports a certificate file that requires a password into a 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            fileName: The name of the file containing the certificate information.
            password: The password required to access the certificate information.
            keyStorageFlags: A bitwise combination of the enumeration values that control how and where the private key is 
             imported.
        
        Import(self: X509Certificate2Collection, rawData: Array[Byte])
            Imports a certificate in the form of a byte array into a 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            rawData: A byte array containing data from an X.509 certificate.
        Import(self: X509Certificate2Collection, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
            Imports a certificate, in the form of a byte array that requires a password to access the 
             certificate, into a System.Security.Cryptography.X509Certificates.X509Certificate2Collection 
             object.
        
        
            rawData: A byte array containing data from an 
             System.Security.Cryptography.X509Certificates.X509Certificate2 object.
        
            password: The password required to access the certificate information.
            keyStorageFlags: A bitwise combination of the enumeration values that control how and where the private key is 
             imported.
        """
        pass

    def Insert(self, index, *__args):
        """
        Insert(self: X509Certificate2Collection, index: int, certificate: X509Certificate2)
            Inserts an object into the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object at the specified 
             index.
        
        
            index: The zero-based index at which to insert certificate.
            certificate: The System.Security.Cryptography.X509Certificates.X509Certificate2 object to insert.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: X509Certificate2Collection, certificate: X509Certificate2)
            Removes the first occurrence of a certificate from the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            certificate: The System.Security.Cryptography.X509Certificates.X509Certificate2 object to be removed from the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        """
        pass

    def RemoveRange(self, certificates):
        """
        RemoveRange(self: X509Certificate2Collection, certificates: X509Certificate2Collection)
            Removes multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object from another 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            certificates: An System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        RemoveRange(self: X509Certificate2Collection, certificates: Array[X509Certificate2])
            Removes multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an 
             array from an System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
        
            certificates: An array of System.Security.Cryptography.X509Certificates.X509Certificate2 objects.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, certificate: X509Certificate2)
        __new__(cls: type, certificates: X509Certificate2Collection)
        __new__(cls: type, certificates: Array[X509Certificate2])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class X509Certificate2Enumerator(object, IEnumerator):
    """ Supports a simple iteration over a System.Security.Cryptography.X509Certificates.X509Certificate2Collection object. This class cannot be inherited. """
    def MoveNext(self):
        """
        MoveNext(self: X509Certificate2Enumerator) -> bool
        
            Advances the enumerator to the next element in the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: X509Certificate2Enumerator)
            Sets the enumerator to its initial position, which is before the first element in the 
             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

Get: Current(self: X509Certificate2Enumerator) -> X509Certificate2

"""



class X509Chain(object, IDisposable):
    """
    Represents a chain-building engine for System.Security.Cryptography.X509Certificates.X509Certificate2 certificates.
    
    X509Chain(useMachineContext: bool)
    X509Chain()
    X509Chain(chainContext: IntPtr)
    """
    def Build(self, certificate):
        """
        Build(self: X509Chain, certificate: X509Certificate2) -> bool
        
            Builds an X.509 chain using the policy specified in 
             System.Security.Cryptography.X509Certificates.X509ChainPolicy.
        
        
            certificate: An System.Security.Cryptography.X509Certificates.X509Certificate2 object.
            Returns: true if the X.509 certificate is valid; otherwise, false.
        """
        pass

    @staticmethod
    def Create():
        """
        Create() -> X509Chain
        
            Creates an System.Security.Cryptography.X509Certificates.X509Chain object after querying for the 
             mapping defined in the CryptoConfig file, and maps the chain to that mapping.
        
            Returns: An System.Security.Cryptography.X509Certificates.X509Chain object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: X509Chain) """
        pass

    def Reset(self):
        """
        Reset(self: X509Chain)
            Clears the current System.Security.Cryptography.X509Certificates.X509Chain object.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, useMachineContext: bool)
        __new__(cls: type, chainContext: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ChainContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to an X.509 chain.

Get: ChainContext(self: X509Chain) -> IntPtr

"""

    ChainElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Security.Cryptography.X509Certificates.X509ChainElement objects.

Get: ChainElements(self: X509Chain) -> X509ChainElementCollection

"""

    ChainPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.Cryptography.X509Certificates.X509ChainPolicy to use when building an X.509 certificate chain.

Get: ChainPolicy(self: X509Chain) -> X509ChainPolicy

Set: ChainPolicy(self: X509Chain) = value
"""

    ChainStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the status of each element in an System.Security.Cryptography.X509Certificates.X509Chain object.

Get: ChainStatus(self: X509Chain) -> Array[X509ChainStatus]

"""

    SafeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SafeHandle(self: X509Chain) -> SafeX509ChainHandle

"""



class X509ChainElement(object):
    """ Represents an element of an X.509 chain. """
    Certificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the X.509 certificate at a particular chain element.

Get: Certificate(self: X509ChainElement) -> X509Certificate2

"""

    ChainElementStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error status of the current X.509 certificate in a chain.

Get: ChainElementStatus(self: X509ChainElement) -> Array[X509ChainStatus]

"""

    Information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets additional error information from an unmanaged certificate chain structure.

Get: Information(self: X509ChainElement) -> str

"""



class X509ChainElementCollection(object, ICollection, IEnumerable):
    """ Represents a collection of System.Security.Cryptography.X509Certificates.X509ChainElement objects. This class cannot be inherited. """
    def CopyTo(self, array, index):
        """
        CopyTo(self: X509ChainElementCollection, array: Array[X509ChainElement], index: int)
            Copies an System.Security.Cryptography.X509Certificates.X509ChainElementCollection object into 
             an array, starting at the specified index.
        
        
            array: An array of System.Security.Cryptography.X509Certificates.X509ChainElement objects.
            index: An integer representing the index value.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: X509ChainElementCollection) -> X509ChainElementEnumerator
        
            Gets an System.Security.Cryptography.X509Certificates.X509ChainElementEnumerator object that can 
             be used to navigate through a collection of chain elements.
        
            Returns: An System.Security.Cryptography.X509Certificates.X509ChainElementEnumerator object.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: X509ChainElementCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection of chain elements is synchronized.

Get: IsSynchronized(self: X509ChainElementCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to an System.Security.Cryptography.X509Certificates.X509ChainElementCollection object.

Get: SyncRoot(self: X509ChainElementCollection) -> object

"""



class X509ChainElementEnumerator(object, IEnumerator):
    """ Supports a simple iteration over an System.Security.Cryptography.X509Certificates.X509ChainElementCollection. This class cannot be inherited. """
    def MoveNext(self):
        """
        MoveNext(self: X509ChainElementEnumerator) -> bool
        
            Advances the enumerator to the next element in the 
             System.Security.Cryptography.X509Certificates.X509ChainElementCollection.
        
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: X509ChainElementEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the 
             System.Security.Cryptography.X509Certificates.X509ChainElementCollection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the System.Security.Cryptography.X509Certificates.X509ChainElementCollection.

Get: Current(self: X509ChainElementEnumerator) -> X509ChainElement

"""



class X509ChainPolicy(object):
    """
    Represents the chain policy to be applied when building an X509 certificate chain. This class cannot be inherited.
    
    X509ChainPolicy()
    """
    def Reset(self):
        """
        Reset(self: X509ChainPolicy)
            Resets the System.Security.Cryptography.X509Certificates.X509ChainPolicy members to their 
             default values.
        """
        pass

    ApplicationPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of object identifiers (OIDs) specifying which application policies or enhanced key usages (EKUs) the certificate supports.

Get: ApplicationPolicy(self: X509ChainPolicy) -> OidCollection

"""

    CertificatePolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of object identifiers (OIDs) specifying which certificate policies the certificate supports.

Get: CertificatePolicy(self: X509ChainPolicy) -> OidCollection

"""

    ExtraStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents an additional collection of certificates that can be searched by the chaining engine when validating a certificate chain.

Get: ExtraStore(self: X509ChainPolicy) -> X509Certificate2Collection

"""

    RevocationFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets values for X509 revocation flags.

Get: RevocationFlag(self: X509ChainPolicy) -> X509RevocationFlag

Set: RevocationFlag(self: X509ChainPolicy) = value
"""

    RevocationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets values for X509 certificate revocation mode.

Get: RevocationMode(self: X509ChainPolicy) -> X509RevocationMode

Set: RevocationMode(self: X509ChainPolicy) = value
"""

    UrlRetrievalTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time span that elapsed during online revocation verification or downloading the certificate revocation list (CRL).

Get: UrlRetrievalTimeout(self: X509ChainPolicy) -> TimeSpan

Set: UrlRetrievalTimeout(self: X509ChainPolicy) = value
"""

    VerificationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets verification flags for the certificate.

Get: VerificationFlags(self: X509ChainPolicy) -> X509VerificationFlags

Set: VerificationFlags(self: X509ChainPolicy) = value
"""

    VerificationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time that the certificate was verified expressed in local time.

Get: VerificationTime(self: X509ChainPolicy) -> DateTime

Set: VerificationTime(self: X509ChainPolicy) = value
"""



class X509ChainStatus(object):
    """ Provides a simple structure for storing X509 chain status and error information. """
    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the status of the X509 chain.

Get: Status(self: X509ChainStatus) -> X509ChainStatusFlags

Set: Status(self: X509ChainStatus) = value
"""

    StatusInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies a description of the System.Security.Cryptography.X509Certificates.X509Chain.ChainStatus value.

Get: StatusInformation(self: X509ChainStatus) -> str

Set: StatusInformation(self: X509ChainStatus) = value
"""



class X509ChainStatusFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the status of an X509 chain.
    
    enum (flags) X509ChainStatusFlags, values: CtlNotSignatureValid (262144), CtlNotTimeValid (131072), CtlNotValidForUsage (524288), Cyclic (128), ExplicitDistrust (67108864), HasExcludedNameConstraint (32768), HasNotDefinedNameConstraint (8192), HasNotPermittedNameConstraint (16384), HasNotSupportedCriticalExtension (134217728), HasNotSupportedNameConstraint (4096), HasWeakSignature (1048576), InvalidBasicConstraints (1024), InvalidExtension (256), InvalidNameConstraints (2048), InvalidPolicyConstraints (512), NoError (0), NoIssuanceChainPolicy (33554432), NotSignatureValid (8), NotTimeNested (2), NotTimeValid (1), NotValidForUsage (16), OfflineRevocation (16777216), PartialChain (65536), RevocationStatusUnknown (64), Revoked (4), UntrustedRoot (32)
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

    CtlNotSignatureValid = None
    CtlNotTimeValid = None
    CtlNotValidForUsage = None
    Cyclic = None
    ExplicitDistrust = None
    HasExcludedNameConstraint = None
    HasNotDefinedNameConstraint = None
    HasNotPermittedNameConstraint = None
    HasNotSupportedCriticalExtension = None
    HasNotSupportedNameConstraint = None
    HasWeakSignature = None
    InvalidBasicConstraints = None
    InvalidExtension = None
    InvalidNameConstraints = None
    InvalidPolicyConstraints = None
    NoError = None
    NoIssuanceChainPolicy = None
    NotSignatureValid = None
    NotTimeNested = None
    NotTimeValid = None
    NotValidForUsage = None
    OfflineRevocation = None
    PartialChain = None
    RevocationStatusUnknown = None
    Revoked = None
    UntrustedRoot = None
    value__ = None


class X509ContentType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the format of an X.509 certificate.
    
    enum X509ContentType, values: Authenticode (6), Cert (1), Pfx (3), Pkcs12 (3), Pkcs7 (5), SerializedCert (2), SerializedStore (4), Unknown (0)
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

    Authenticode = None
    Cert = None
    Pfx = None
    Pkcs12 = None
    Pkcs7 = None
    SerializedCert = None
    SerializedStore = None
    Unknown = None
    value__ = None


class X509EnhancedKeyUsageExtension(X509Extension):
    """
    Defines the collection of object identifiers (OIDs) that indicates the applications that use the key. This class cannot be inherited.
    
    X509EnhancedKeyUsageExtension()
    X509EnhancedKeyUsageExtension(enhancedKeyUsages: OidCollection, critical: bool)
    X509EnhancedKeyUsageExtension(encodedEnhancedKeyUsages: AsnEncodedData, critical: bool)
    """
    def CopyFrom(self, asnEncodedData):
        """
        CopyFrom(self: X509EnhancedKeyUsageExtension, asnEncodedData: AsnEncodedData)
            Initializes a new instance of the 
             System.Security.Cryptography.X509Certificates.X509EnhancedKeyUsageExtension class using an 
             System.Security.Cryptography.AsnEncodedData object.
        
        
            asnEncodedData: The encoded data to use to create the extension.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, enhancedKeyUsages: OidCollection, critical: bool)
        __new__(cls: type, encodedEnhancedKeyUsages: AsnEncodedData, critical: bool)
        """
        pass

    EnhancedKeyUsages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of object identifiers (OIDs) that indicate the applications that use the key.

Get: EnhancedKeyUsages(self: X509EnhancedKeyUsageExtension) -> OidCollection

"""



class X509ExtensionCollection(object, ICollection, IEnumerable):
    """
    Represents a collection of System.Security.Cryptography.X509Certificates.X509Extension objects. This class cannot be inherited.
    
    X509ExtensionCollection()
    """
    def Add(self, extension):
        """
        Add(self: X509ExtensionCollection, extension: X509Extension) -> int
        
            Adds an System.Security.Cryptography.X509Certificates.X509Extension object to an 
             System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.
        
        
            extension: An System.Security.Cryptography.X509Certificates.X509Extension  object to add to the 
             System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.
        
            Returns: The index at which the extension parameter was added.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: X509ExtensionCollection, array: Array[X509Extension], index: int)
            Copies a collection into an array starting at the specified index.
        
            array: An array of System.Security.Cryptography.X509Certificates.X509Extension objects.
            index: The location in the array at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: X509ExtensionCollection) -> X509ExtensionEnumerator
        
            Returns an enumerator that can iterate through an 
             System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.
        
            Returns: An System.Security.Cryptography.X509Certificates.X509ExtensionEnumerator object to use to 
             iterate through the System.Security.Cryptography.X509Certificates.X509ExtensionCollection 
             object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Security.Cryptography.X509Certificates.X509Extension objects in a System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

Get: Count(self: X509ExtensionCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is guaranteed to be thread safe.

Get: IsSynchronized(self: X509ExtensionCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that you can use to synchronize access to the System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

Get: SyncRoot(self: X509ExtensionCollection) -> object

"""



class X509ExtensionEnumerator(object, IEnumerator):
    """ Supports a simple iteration over a System.Security.Cryptography.X509Certificates.X509ExtensionCollection. This class cannot be inherited. """
    def MoveNext(self):
        """
        MoveNext(self: X509ExtensionEnumerator) -> bool
        
            Advances the enumerator to the next element in the 
             System.Security.Cryptography.X509Certificates.X509ExtensionCollection.
        
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: X509ExtensionEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the 
             System.Security.Cryptography.X509Certificates.X509ExtensionCollection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the System.Security.Cryptography.X509Certificates.X509ExtensionCollection.

Get: Current(self: X509ExtensionEnumerator) -> X509Extension

"""



class X509FindType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of value the System.Security.Cryptography.X509Certificates.X509Certificate2Collection.Find(System.Security.Cryptography.X509Certificates.X509FindType,System.Object,System.Boolean) method searches for.
    
    enum X509FindType, values: FindByApplicationPolicy (10), FindByCertificatePolicy (11), FindByExtension (12), FindByIssuerDistinguishedName (4), FindByIssuerName (3), FindByKeyUsage (13), FindBySerialNumber (5), FindBySubjectDistinguishedName (2), FindBySubjectKeyIdentifier (14), FindBySubjectName (1), FindByTemplateName (9), FindByThumbprint (0), FindByTimeExpired (8), FindByTimeNotYetValid (7), FindByTimeValid (6)
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

    FindByApplicationPolicy = None
    FindByCertificatePolicy = None
    FindByExtension = None
    FindByIssuerDistinguishedName = None
    FindByIssuerName = None
    FindByKeyUsage = None
    FindBySerialNumber = None
    FindBySubjectDistinguishedName = None
    FindBySubjectKeyIdentifier = None
    FindBySubjectName = None
    FindByTemplateName = None
    FindByThumbprint = None
    FindByTimeExpired = None
    FindByTimeNotYetValid = None
    FindByTimeValid = None
    value__ = None


class X509IncludeOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how much of the X.509 certificate chain should be included in the X.509 data.
    
    enum X509IncludeOption, values: EndCertOnly (2), ExcludeRoot (1), None (0), WholeChain (3)
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

    EndCertOnly = None
    ExcludeRoot = None
    None = None
    value__ = None
    WholeChain = None


class X509KeyStorageFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines where and how to export the private key of an X.509 certificate.
    
    enum (flags) X509KeyStorageFlags, values: DefaultKeySet (0), Exportable (4), MachineKeySet (2), PersistKeySet (16), UserKeySet (1), UserProtected (8)
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

    DefaultKeySet = None
    Exportable = None
    MachineKeySet = None
    PersistKeySet = None
    UserKeySet = None
    UserProtected = None
    value__ = None


class X509KeyUsageExtension(X509Extension):
    """
    Defines the usage of a key contained within an X.509 certificate.  This class cannot be inherited.
    
    X509KeyUsageExtension()
    X509KeyUsageExtension(keyUsages: X509KeyUsageFlags, critical: bool)
    X509KeyUsageExtension(encodedKeyUsage: AsnEncodedData, critical: bool)
    """
    def CopyFrom(self, asnEncodedData):
        """
        CopyFrom(self: X509KeyUsageExtension, asnEncodedData: AsnEncodedData)
            Initializes a new instance of the 
             System.Security.Cryptography.X509Certificates.X509KeyUsageExtension class using an 
             System.Security.Cryptography.AsnEncodedData object.
        
        
            asnEncodedData: The encoded data to use to create the extension.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, keyUsages: X509KeyUsageFlags, critical: bool)
        __new__(cls: type, encodedKeyUsage: AsnEncodedData, critical: bool)
        """
        pass

    KeyUsages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key usage flag associated with the certificate.

Get: KeyUsages(self: X509KeyUsageExtension) -> X509KeyUsageFlags

"""



class X509KeyUsageFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines how the certificate key can be used. If this value is not defined, the key can be used for any purpose.
    
    enum (flags) X509KeyUsageFlags, values: CrlSign (2), DataEncipherment (16), DecipherOnly (32768), DigitalSignature (128), EncipherOnly (1), KeyAgreement (8), KeyCertSign (4), KeyEncipherment (32), None (0), NonRepudiation (64)
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

    CrlSign = None
    DataEncipherment = None
    DecipherOnly = None
    DigitalSignature = None
    EncipherOnly = None
    KeyAgreement = None
    KeyCertSign = None
    KeyEncipherment = None
    None = None
    NonRepudiation = None
    value__ = None


class X509NameType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of name the X509 certificate contains.
    
    enum X509NameType, values: DnsFromAlternativeName (4), DnsName (3), EmailName (1), SimpleName (0), UpnName (2), UrlName (5)
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

    DnsFromAlternativeName = None
    DnsName = None
    EmailName = None
    SimpleName = None
    UpnName = None
    UrlName = None
    value__ = None


class X509RevocationFlag(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies which X509 certificates in the chain should be checked for revocation.
    
    enum X509RevocationFlag, values: EndCertificateOnly (0), EntireChain (1), ExcludeRoot (2)
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

    EndCertificateOnly = None
    EntireChain = None
    ExcludeRoot = None
    value__ = None


class X509RevocationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the mode used to check for X509 certificate revocation.
    
    enum X509RevocationMode, values: NoCheck (0), Offline (2), Online (1)
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

    NoCheck = None
    Offline = None
    Online = None
    value__ = None


class X509Store(object, IDisposable):
    """
    Represents an X.509 store, which is a physical store where certificates are persisted and managed. This class cannot be inherited.
    
    X509Store()
    X509Store(storeName: str)
    X509Store(storeName: StoreName)
    X509Store(storeLocation: StoreLocation)
    X509Store(storeName: StoreName, storeLocation: StoreLocation)
    X509Store(storeName: str, storeLocation: StoreLocation)
    X509Store(storeHandle: IntPtr)
    """
    def Add(self, certificate):
        """
        Add(self: X509Store, certificate: X509Certificate2)
            Adds a certificate to an X.509 certificate store.
        
            certificate: The certificate to add.
        """
        pass

    def AddRange(self, certificates):
        """
        AddRange(self: X509Store, certificates: X509Certificate2Collection)
            Adds a collection of certificates to an X.509 certificate store.
        
            certificates: The collection of certificates to add.
        """
        pass

    def Close(self):
        """
        Close(self: X509Store)
            Closes an X.509 certificate store.
        """
        pass

    def Dispose(self):
        """ Dispose(self: X509Store) """
        pass

    def Open(self, flags):
        """
        Open(self: X509Store, flags: OpenFlags)
            Opens an X.509 certificate store or creates a new store, depending on 
             System.Security.Cryptography.X509Certificates.OpenFlags flag settings.
        
        
            flags: A bitwise combination of enumeration values that specifies the way to open the X.509 certificate 
             store.
        """
        pass

    def Remove(self, certificate):
        """
        Remove(self: X509Store, certificate: X509Certificate2)
            Removes a certificate from an X.509 certificate store.
        
            certificate: The certificate to remove.
        """
        pass

    def RemoveRange(self, certificates):
        """
        RemoveRange(self: X509Store, certificates: X509Certificate2Collection)
            Removes a range of certificates from an X.509 certificate store.
        
            certificates: A range of certificates to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, storeName: str)
        __new__(cls: type, storeName: StoreName)
        __new__(cls: type, storeLocation: StoreLocation)
        __new__(cls: type, storeName: StoreName, storeLocation: StoreLocation)
        __new__(cls: type, storeName: str, storeLocation: StoreLocation)
        __new__(cls: type, storeHandle: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Certificates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a collection of certificates located in an X.509 certificate store.

Get: Certificates(self: X509Store) -> X509Certificate2Collection

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location of the X.509 certificate store.

Get: Location(self: X509Store) -> StoreLocation

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the X.509 certificate store.

Get: Name(self: X509Store) -> str

"""

    StoreHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.IntPtr handle to an HCERTSTORE store.

Get: StoreHandle(self: X509Store) -> IntPtr

"""



class X509SubjectKeyIdentifierExtension(X509Extension):
    """
    Defines a string that identifies a certificate's subject key identifier (SKI). This class cannot be inherited.
    
    X509SubjectKeyIdentifierExtension()
    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: str, critical: bool)
    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: Array[Byte], critical: bool)
    X509SubjectKeyIdentifierExtension(encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool)
    X509SubjectKeyIdentifierExtension(key: PublicKey, critical: bool)
    X509SubjectKeyIdentifierExtension(key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool)
    """
    def CopyFrom(self, asnEncodedData):
        """
        CopyFrom(self: X509SubjectKeyIdentifierExtension, asnEncodedData: AsnEncodedData)
            Creates a new instance of the 
             System.Security.Cryptography.X509Certificates.X509SubjectKeyIdentifierExtension class by copying 
             information from encoded data.
        
        
            asnEncodedData: The System.Security.Cryptography.AsnEncodedData object to use to create the extension.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, subjectKeyIdentifier: str, critical: bool)
        __new__(cls: type, subjectKeyIdentifier: Array[Byte], critical: bool)
        __new__(cls: type, encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool)
        __new__(cls: type, key: PublicKey, critical: bool)
        __new__(cls: type, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool)
        """
        pass

    SubjectKeyIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string that represents the subject key identifier (SKI) for a certificate.

Get: SubjectKeyIdentifier(self: X509SubjectKeyIdentifierExtension) -> str

"""



class X509SubjectKeyIdentifierHashAlgorithm(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the type of hash algorithm to use with the System.Security.Cryptography.X509Certificates.X509SubjectKeyIdentifierExtension class.
    
    enum X509SubjectKeyIdentifierHashAlgorithm, values: CapiSha1 (2), Sha1 (0), ShortSha1 (1)
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

    CapiSha1 = None
    Sha1 = None
    ShortSha1 = None
    value__ = None


class X509VerificationFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies conditions under which verification of certificates in the X509 chain should be conducted.
    
    enum (flags) X509VerificationFlags, values: AllFlags (4095), AllowUnknownCertificateAuthority (16), IgnoreCertificateAuthorityRevocationUnknown (1024), IgnoreCtlNotTimeValid (2), IgnoreCtlSignerRevocationUnknown (512), IgnoreEndRevocationUnknown (256), IgnoreInvalidBasicConstraints (8), IgnoreInvalidName (64), IgnoreInvalidPolicy (128), IgnoreNotTimeNested (4), IgnoreNotTimeValid (1), IgnoreRootRevocationUnknown (2048), IgnoreWrongUsage (32), NoFlag (0)
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

    AllFlags = None
    AllowUnknownCertificateAuthority = None
    IgnoreCertificateAuthorityRevocationUnknown = None
    IgnoreCtlNotTimeValid = None
    IgnoreCtlSignerRevocationUnknown = None
    IgnoreEndRevocationUnknown = None
    IgnoreInvalidBasicConstraints = None
    IgnoreInvalidName = None
    IgnoreInvalidPolicy = None
    IgnoreNotTimeNested = None
    IgnoreNotTimeValid = None
    IgnoreRootRevocationUnknown = None
    IgnoreWrongUsage = None
    NoFlag = None
    value__ = None



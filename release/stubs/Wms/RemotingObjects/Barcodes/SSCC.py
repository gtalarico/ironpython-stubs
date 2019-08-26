# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.SSCC calls itself SSCC
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GS1Prefixes():
    # no doc
    Prefixes = None
    __all__ = []

    Instance = GS1Prefixes()
    """hardcoded/returns an instance of the class"""

class SSCC:
    """
    SSCC(barcode: str)
    SSCC(extensionDigit: int, companyPrefix: str, serial: int)
    """
    def Equals(self, *__args):
        """
        Equals(self: SSCC, other: SSCC) -> bool
        
            Compares the given Wms.RemotingObjects.Barcodes.SSCC.SSCC to this instance
        Equals(self: SSCC, obj: object) -> bool
        """
        pass

    @staticmethod
    def Get(barcode):
        """
        Get(barcode: str) -> IGeneratedBarcode
        
            Static function to create a Wms.RemotingObjects.Barcodes.SSCC.SSCC instance of the given System.String
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SSCC) -> int """
        pass

    def HasValidCompanyPrefix(self):
        """
        HasValidCompanyPrefix(self: SSCC) -> bool
        
            Checks if the company prefix is a valid GS1 company prefix
        """
        pass

    @staticmethod
    def IsValid(barcode):
        """
        IsValid(barcode: str) -> bool
        
            Checks if input is valid SSCC code.
                    Strips expected cosmetic characters.
                    Deprecated use 
             Wms.RemotingObjects.Barcodes.SSCC.SSCC.TryParse(System.String,Wms.RemotingObjects.Barcodes.SSCC.SSCC@) instead.
        
        
            barcode: uncleaned barcode
        """
        pass

    def ToBarcode(self, includeApplicationIdentifier=None):
        """
        ToBarcode(self: SSCC) -> str
        
            Returns this instance as a barcode
        ToBarcode(self: SSCC, includeApplicationIdentifier: bool) -> str
        
            Returns this instance as a barcode
        
            includeApplicationIdentifier: True to include the Application Identifier in 
                    the result System.String, otherwise false
        """
        pass

    def ToReadableCode(self, includeApplicationIdentifier=None):
        """
        ToReadableCode(self: SSCC) -> str
        
            Creates a readable System.String of the barcode
            Returns: System.String with the readable barcode
        ToReadableCode(self: SSCC, includeApplicationIdentifier: bool) -> str
        
            Creates a readable System.String of the barcode
        
            includeApplicationIdentifier: True to include the Application Identifier in 
                    the result System.String, otherwise false
            Returns: System.String with the readable barcode
        """
        pass

    def ToString(self, format=None, provider=None):
        """
        ToString(self: SSCC) -> str
        
            Formats to machine readable string.
        ToString(self: SSCC, format: str) -> str
        ToString(self: SSCC, format: str, provider: IFormatProvider) -> str
        
            Formats to a string. (Capital letter does left pad, lower case just takes number).
                    Aa - Aplicaiton identifier,
                    Ee - Extension digit,
                
                 Cc - Company prefix,
                    Ss - Serial reference,
                    Ii - integrity check digit,
                    Zz - Complete sscc code machine readable,
                  
               Hh - human readable complete code.
        
        
            format: Format to string to. following characters get replaced:
                    Aa - Aplicaiton identifier,
                    Ee - Extension digit,
                    Cc - Company prefix,
         
                        Ss - Serial reference,
                    Ii - integrity check digit,
                    Zz - Complete sscc code machine readable,
                    Hh - human readable 
             complete code.
        
            Returns: string in the format provided.
        """
        pass

    @staticmethod
    def TryParse(input, sscc):
        """
        TryParse(input: str) -> (bool, SSCC)
        
            Tries to parse SSCC string to struct.
                    Can only parse 18 or 20 digit strings.
        
            input: un cleaned barcode/sscc string to parse
            Returns: Wether or not parsing succeeded
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, barcode: str)
        __new__(cls: type, extensionDigit: int, companyPrefix: str, serial: int)
        __new__[SSCC]() -> SSCC
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

    CheckDigit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated check digit of a SSCC barcode

Get: CheckDigit(self: SSCC) -> int

"""

    CompanyNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompanyNumber(self: SSCC) -> Int64

"""

    CompanyPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 company prefix of a SSCC barcode

Get: CompanyPrefix(self: SSCC) -> str

"""

    ExtensionDigit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension digit of a SSCC barcode

Get: ExtensionDigit(self: SSCC) -> int

"""

    Serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The serial reference of a SSCC barcode

Get: Serial(self: SSCC) -> int

"""

    SerialFromBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The serial reference of a SSCC barcode, including the leading zero's

Get: SerialFromBarcode(self: SSCC) -> str

"""


    Instance = SSCC()
    """hardcoded/returns an instance of the class"""


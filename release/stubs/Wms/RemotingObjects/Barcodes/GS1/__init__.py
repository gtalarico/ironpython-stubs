# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.GS1 calls itself GS1
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationIdentifiers():
    """ ApplicationIdentifiers() """
    AdditionalProductIdentification = '240'
    AmountDue_DefinedValutaBand = '390n'
    AmountDue_WithISOValutaCode = '391n'
    AmountInParts_Quantity_Each = '30'
    BasisCountryOfTheWares_ISO3166Format = '422'
    Batch_Number = '10'
    BePayingAmount_DefinedValutaBand = '392n'
    BePayingAmount_WithISOValutaCode = '393n'
    CompanySpecificInternal_1 = '91'
    CompanySpecificInternal_2 = '92'
    CompanySpecificInternal_3 = '93'
    CompanySpecificInternal_4 = '94'
    CompanySpecificInternal_5 = '95'
    CompanySpecificInternal_6 = '96'
    CompanySpecificInternal_7 = '97'
    CompanySpecificInternal_8 = '98'
    CompanySpecificInternal_9 = '99'
    ContainerGrossVolume_CubicFeet = '368n'
    ContainerGrossVolume_CubicInches = '367n'
    ContainerGrossVolume_CubicMeters = '336n'
    ContainerGrossVolume_CubicYards = '369n'
    ContainerGrossVolume_Gallonen = '363n'
    ContainerGrossVolume_Liters = '335n'
    ContainerGrossVolume_Quarts = '362n'
    ContainerGrossWeight_Kilogram = '330n'
    ContainerGrossWeight_Pounds = '340n'
    ContainerHeigth_Feed = '348n'
    ContainerHeigth_Inches = '347n'
    ContainerHeigth_Meter = '333n'
    ContainerHeigth_Yards = '349n'
    ContainerKilogramPerSquareMeter = '337n'
    ContainerLength_Feet = '342n'
    ContainerLength_Inches = '341n'
    ContainerLength_Meter = '331n'
    ContainerLength_Yards = '343n'
    ContainerSurface_SquareFeed = '354n'
    ContainerSurface_SquareInches = '353n'
    ContainerSurface_SquareMeter = '334n'
    ContainerSurface_SquareYards = '355n'
    ContainerWidth_Feed = '345n'
    ContainerWidth_Inches = '344n'
    ContainerWidth_Meter = '332n'
    ContainerWidth_Yards = '346n'
    CouponExtendedCode_NSC = '8102'
    CouponExtendedCode_NSC_offerCcode = '8100'
    CouponExtendedCode_NSC_offerCcode_EndOfOfferCode = '8101'
    CustomerPartsNumber = '241'
    DataAndTimeOfManufacturing = '8008'
    DeliveryNumber = '402'
    DueDate_JJMMDD = '12'
    EAN_NumberOfTheWaresInTheShippingUnit = '02'
    EAN_NumberOfTradingUnit = '01'
    EAN_UCC_GlobalLocationNumber_Distributor = '412'
    EAN_UCC_GlobalLocationNumber_FinalRecipient = '413'
    EAN_UCC_GlobalLocationNumber_GoodsRecipient = '410'
    EAN_UCC_GlobalLocationNumber_InvoiceRecipient = '411'
    EAN_UCC_GlobalLocationNumber_PhysicalLocation = '414'
    EAN_UCC_GlobalLocationNumber_ToBilligParticipant = '415'
    ExpiryDate_JJMMDD = '17'
    GLN_extension_component = '254'
    GlobalIdentifierSerialisedForTrade = '252'
    GlobalIndividualAssetIdentifier = '8004'
    GlobalReturnableAssetIdentifier = '8003'
    GlobalServiceRelationNumber = '8018'
    Global_Coupon_Number = '255'
    Global_Document_Type_Identifier = '253'
    HIBCCNumber = '22'
    IBAN = '8007'
    IdentifikationOfAProductComponent = '8006'
    JobNumberOfGoodsRecipient = '400'
    Lot_Number = '23n'
    Made_to_Order_variation_no = '242'
    Mutually_Agreed_Between_Trading_Partners = '90'
    Nato_Stock_Number = '7001'
    NetVolume_Ounces = '357n'
    NetWeight_Kilogram = '310n'
    NetWeight_TroyOunces = '356n'
    NumberBillCoverNumber = '8020'
    Packaging_Component_Number = '243'
    PackingDate_JJMMDD = '13'
    ProductHeigth_Feed = '328n'
    ProductHeigth_Inches = '327n'
    ProductHeigth_Meter = '313n'
    ProductHeigth_Yards = '329n'
    Production_Date_JJMMDD = '11'
    ProductLength_Feet = '322n'
    ProductLength_Inches = '321n'
    ProductLength_Meter = '311n'
    ProductLength_Yards = '323n'
    ProductModel = '20'
    ProductNetVolume_CubicFeet = '365n'
    ProductNetVolume_CubicInches = '364n'
    ProductNetVolume_CubicMeters = '316n'
    ProductNetVolume_CubicYards = '366n'
    ProductNetVolume_Gallonen = '361n'
    ProductNetVolume_Liters = '315n'
    ProductNetVolume_Quarts = '360n'
    ProductNetWeight_Pounds = '320n'
    ProductSurface_SquareFeet = '351n'
    ProductSurface_SquareInches = '350n'
    ProductSurface_SquareMeter = '314n'
    ProductSurface_SquareYards = '352n'
    ProductWidth_Feed = '325n'
    ProductWidth_Inches = '324n'
    ProductWidth_Meter = '312n'
    ProductWidth_Yards = '326n'
    QuantityInParts = '37'
    ReferenceToTheBasisUnit = '251'
    RolesProducts = '8001'
    RoutingCode = '403'
    SalesPricePerUnit = '8005'
    Sell_by_Date__JJMMDD = '15'
    SerialNumber = '21'
    SerialNumberForMobilePhones = '8002'
    SerialNumberOfAIntegratedModule = '250'
    SerialShippingContainerCode = '00'
    ShippingNumber = '401'
    ZipCodeOfRecipient_withCountryCode = '421'
    ZipCodeOfRecipient_withoutCountryCode = '420'

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ApplicationIdentifiers()

class GS1Barcode:
    """
    GS1Barcode()
    GS1Barcode(applicationIdentifier: str, value: str)
    """
    def ToBarcode(self, includeApplicationIdentifier=None):
        """
        ToBarcode(self: GS1Barcode) -> str
        
            Converts this Wms.RemotingObjects.Barcodes.GS1.GS1Barcode to a System.String, usable for barcodes (HRI)
        ToBarcode(self: GS1Barcode, includeApplicationIdentifier: bool) -> str
        """
        pass

    def ToReadableCode(self, includeApplicationIdentifier=None):
        """
        ToReadableCode(self: GS1Barcode) -> str
        
            Converts this Wms.RemotingObjects.Barcodes.GS1.GS1Barcode to a System.String, readable for humans (Non-HRI)
        ToReadableCode(self: GS1Barcode, includeApplicationIdentifier: bool) -> str
        
            Creates a readable System.String of the barcode
        
            includeApplicationIdentifier: True to include the Application Identifier in 
                    the result System.String, otherwise false
            Returns: System.String with the readable barcode
        """
        pass

    def ToString(self):
        """ ToString(self: GS1Barcode) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, applicationIdentifier=None, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, applicationIdentifier: str, value: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GS1Barcode()

class ItemNumberHelper():
    """ A class to validate GS1 article numbers """
    @staticmethod
    def GetItemNumberType(articleNumber):
        """
        GetItemNumberType(articleNumber: str) -> ItemNumberType
        
            Get ItemNumberType
        
            articleNumber: ASIN, EAN8, EAN13, GTIN, ISBN10, ISBN13, UPC
        """
        pass

    @staticmethod
    def IsValidAsin(asin):
        """
        IsValidAsin(asin: str) -> bool
        
            Validate ASIN
        """
        pass

    @staticmethod
    def IsValidEan(code):
        """
        IsValidEan(code: str) -> bool
        
            Validate European Article Number
        """
        pass

    @staticmethod
    def IsValidGtin(code):
        """
        IsValidGtin(code: str) -> bool
        
            Validate Global Trade Item Number
        """
        pass

    @staticmethod
    def IsValidIsbn10(isbn10):
        """
        IsValidIsbn10(isbn10: str) -> bool
        
            Validate ISBN10
        """
        pass

    @staticmethod
    def IsValidIsbn13(isbn13):
        """
        IsValidIsbn13(isbn13: str) -> bool
        
            Validate ISBN13
        """
        pass

    @staticmethod
    def IsValidIssn(code):
        """
        IsValidIssn(code: str) -> bool
        
            Validate ISSN
        """
        pass

    @staticmethod
    def IsValidUpc(code):
        """
        IsValidUpc(code: str) -> bool
        
            Validate a UPC
            Returns: Whether or not the code is a valid UPC.
        """
        pass

    @staticmethod
    def TryConvertToGtin(code, gtin):
        """
        TryConvertToGtin(code: str) -> (bool, str)
        
            Attempts to convert a UPC or EAN13 to a GTIN.
        
            code: Code to convert
            Returns: True on success, false on failure
        """
        pass

    __all__ = [
        '__reduce_ex__',
        'GetItemNumberType',
        'IsValidAsin',
        'IsValidEan',
        'IsValidGtin',
        'IsValidIsbn10',
        'IsValidIsbn13',
        'IsValidIssn',
        'IsValidUpc',
        'TryConvertToGtin',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ItemNumberHelper()

class ItemNumberType:
    """ enum ItemNumberType, values: ASIN (1), EAN13 (3), EAN8 (2), GTIN (4), ISBN10 (5), ISBN13 (6), ISSN (9), SKU (7), Unknown (0), UPC (8) """
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

    ASIN = None
    EAN13 = None
    EAN8 = None
    GTIN = None
    ISBN10 = None
    ISBN13 = None
    ISSN = None
    SKU = None
    Unknown = None
    UPC = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ItemNumberType()

# variables with complex values


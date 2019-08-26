# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.ColliReferences calls itself ColliReferences
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ColliBarcodeResult():
    """ ColliBarcodeResult() """
    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ColliBarcodeResult) -> str

Set: Barcode(self: ColliBarcodeResult) = value
"""

    FaultMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaultMessage(self: ColliBarcodeResult) -> str

Set: FaultMessage(self: ColliBarcodeResult) = value
"""

    IsOwnCompanySSCC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the barcode is a SSCC barcode of this company

Get: IsOwnCompanySSCC(self: ColliBarcodeResult) -> bool

Set: IsOwnCompanySSCC(self: ColliBarcodeResult) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ColliBarcodeResult) -> ReferenceType

Set: Type(self: ColliBarcodeResult) = value
"""


    Instance = ColliBarcodeResult()
    """hardcoded/returns an instance of the class"""

class ValidateColliReferencesArgs():
    """
    ValidateColliReferencesArgs()
    ValidateColliReferencesArgs(innerReference: str, outerReference: str, *exclusion: Array[object])
    """
    @staticmethod # known case of __new__
    def __new__(self, innerReference=None, outerReference=None, exclusion=None):
        """
        __new__(cls: type)
        __new__(cls: type, innerReference: str, outerReference: str, *exclusion: Array[object])
        """
        pass

    ExclusionList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExclusionList(self: ValidateColliReferencesArgs) -> List[object]

Set: ExclusionList(self: ValidateColliReferencesArgs) = value
"""

    InnerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerReference(self: ValidateColliReferencesArgs) -> str

Set: InnerReference(self: ValidateColliReferencesArgs) = value
"""

    OuterReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterReference(self: ValidateColliReferencesArgs) -> str

Set: OuterReference(self: ValidateColliReferencesArgs) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: ValidateColliReferencesArgs) -> ValidateColliReferencesResult

Set: Result(self: ValidateColliReferencesArgs) = value
"""


    Instance = ValidateColliReferencesArgs()
    """hardcoded/returns an instance of the class"""

class ValidateColliReferencesResult():
    """
    ValidateColliReferencesResult()
    ValidateColliReferencesResult(isInnerReferenceValid: bool, isOuterReferenceValid: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, isInnerReferenceValid=None, isOuterReferenceValid=None):
        """
        __new__(cls: type)
        __new__(cls: type, isInnerReferenceValid: bool, isOuterReferenceValid: bool)
        """
        pass

    IsInnerReferenceValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInnerReferenceValid(self: ValidateColliReferencesResult) -> Nullable[bool]

Set: IsInnerReferenceValid(self: ValidateColliReferencesResult) = value
"""

    IsOuterReferenceValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOuterReferenceValid(self: ValidateColliReferencesResult) -> Nullable[bool]

Set: IsOuterReferenceValid(self: ValidateColliReferencesResult) = value
"""


    Instance = ValidateColliReferencesResult()
    """hardcoded/returns an instance of the class"""


from Wms.RemotingObjects import DbObject
from System import Object
# encoding: utf-8
# module Wms.RemotingObjects.NumberRanges calls itself NumberRanges
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GenerateArgs():
    """
    GenerateArgs()
    GenerateArgs(numberRange: NumberRange)
    """
    @staticmethod # known case of __new__
    def __new__(self, numberRange=None):
        """
        __new__(cls: type)
        __new__(cls: type, numberRange: NumberRange)
        """
        pass

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arguments(self: GenerateArgs) -> Array[object]

Set: Arguments(self: GenerateArgs) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GenerateArgs) -> int

Set: Length(self: GenerateArgs) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: GenerateArgs) -> str

Set: Prefix(self: GenerateArgs) = value
"""

    StartingNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartingNumber(self: GenerateArgs) -> int

Set: StartingNumber(self: GenerateArgs) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: GenerateArgs) -> str

Set: Suffix(self: GenerateArgs) = value
"""


    Instance = GenerateArgs()
    """hardcoded/returns an instance of the class"""

class GenerateNumbersBaseArgs():
    """
    GenerateNumbersBaseArgs()
    GenerateNumbersBaseArgs(id: int, type: NumberRangeType)
    GenerateNumbersBaseArgs(id: int, type: NumberRangeType, numbersToGenerate: int)
    """
    def AddGenerationArgs(self, args, numbersToGenerate):
        """ AddGenerationArgs(self: GenerateNumbersBaseArgs, args: GenerateArgs, numbersToGenerate: int) """
        pass

    def AddGenerator(self, generator, args, numbersToGenerate):
        """ AddGenerator(self: GenerateNumbersBaseArgs, generator: IGenerator, args: GenerateArgs, numbersToGenerate: int) """
        pass

    def Generate(self):
        """
        Generate(self: GenerateNumbersBaseArgs) -> IEnumerable[IGeneratedBarcode]
        
            Generates a range of numbers
        """
        pass

    def GenerateOne(self):
        """
        GenerateOne(self: GenerateNumbersBaseArgs) -> IGeneratedBarcode
        
            Generates a single number
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id=None, type=None, numbersToGenerate=None):
        """
        __new__(cls: type)
        __new__(cls: type, id: int, type: NumberRangeType)
        __new__(cls: type, id: int, type: NumberRangeType, numbersToGenerate: int)
        """
        pass

    AdditionalArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AdditionalArguments(self: GenerateNumbersBaseArgs) -> SerializableDictionary[str, object]

"""

    Ascending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Ascending(self: GenerateNumbersBaseArgs) -> bool

Set: Ascending(self: GenerateNumbersBaseArgs) = value
"""

    HasGenerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasGenerator(self: GenerateNumbersBaseArgs) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the number range

Get: Id(self: GenerateNumbersBaseArgs) -> int

Set: Id(self: GenerateNumbersBaseArgs) = value
"""

    NumbersToGenerate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Amount of numbers to generate (default = 1)

Get: NumbersToGenerate(self: GenerateNumbersBaseArgs) -> int

Set: NumbersToGenerate(self: GenerateNumbersBaseArgs) = value
"""

    RegisterNumbersAsUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to True to register the numbers as used within BOXwise so they cannot be reused.

Get: RegisterNumbersAsUsed(self: GenerateNumbersBaseArgs) -> bool

Set: RegisterNumbersAsUsed(self: GenerateNumbersBaseArgs) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of numbers to generate

Get: Type(self: GenerateNumbersBaseArgs) -> NumberRangeType

Set: Type(self: GenerateNumbersBaseArgs) = value
"""


    Instance = GenerateNumbersBaseArgs()
    """hardcoded/returns an instance of the class"""

class GenerateBarcodeLabelArgs(GenerateNumbersBaseArgs):
    """
    GenerateBarcodeLabelArgs()
    GenerateBarcodeLabelArgs(id: int, type: NumberRangeType)
    GenerateBarcodeLabelArgs(id: int, type: NumberRangeType, numbersToGenerate: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, id=None, type=None, numbersToGenerate=None):
        """
        __new__(cls: type)
        __new__(cls: type, id: int, type: NumberRangeType)
        __new__(cls: type, id: int, type: NumberRangeType, numbersToGenerate: int)
        """
        pass

    LabelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LabelName(self: GenerateBarcodeLabelArgs) -> str

Set: LabelName(self: GenerateBarcodeLabelArgs) = value
"""

    Printer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Override printer, otherwise printer is chosen through printer rules.

Get: Printer(self: GenerateBarcodeLabelArgs) -> str

Set: Printer(self: GenerateBarcodeLabelArgs) = value
"""

    PrintingOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Override printing options, otherwise options is chosen through printer rules.

Get: PrintingOptions(self: GenerateBarcodeLabelArgs) -> PrintingOptions

Set: PrintingOptions(self: GenerateBarcodeLabelArgs) = value
"""


    Instance = GenerateBarcodeLabelArgs()
    """hardcoded/returns an instance of the class"""

class GetNumberRangeArgs():
    """ GetNumberRangeArgs() """
    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetNumberRangeArgs) -> str

Set: Filter(self: GetNumberRangeArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: GetNumberRangeArgs) -> int

Set: Id(self: GetNumberRangeArgs) = value
"""

    IsTypeSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTypeSet(self: GetNumberRangeArgs) -> bool

Set: IsTypeSet(self: GetNumberRangeArgs) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GetNumberRangeArgs) -> NumberRangeType

Set: Type(self: GetNumberRangeArgs) = value
"""


    Default = None

    Instance = GetNumberRangeArgs()
    """hardcoded/returns an instance of the class"""

class NumberRange(DbObject):
    """ NumberRange() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current number

Get: Current(self: NumberRange) -> int

Set: Current(self: NumberRange) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description

Get: Description(self: NumberRange) -> str

Set: Description(self: NumberRange) = value
"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The starting number

Get: From(self: NumberRange) -> int

Set: From(self: NumberRange) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the range

Get: Id(self: NumberRange) -> int

Set: Id(self: NumberRange) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Eventually fixed length of the generated number (Left padded with 0)

Get: Length(self: NumberRange) -> int

Set: Length(self: NumberRange) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional. The prefix for the generated numbers

Get: Prefix(self: NumberRange) -> str

Set: Prefix(self: NumberRange) = value
"""

    RangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: RangeType(self: NumberRange) -> NumberRangeType

Set: RangeType(self: NumberRange) = value
"""

    ResetBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user who performed the reset

Get: ResetBy(self: NumberRange) -> str

Set: ResetBy(self: NumberRange) = value
"""

    ResetOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date on which this range was reset

Get: ResetOn(self: NumberRange) -> DateTime

Set: ResetOn(self: NumberRange) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional. The suffix for the generated numbers

Get: Suffix(self: NumberRange) -> str

Set: Suffix(self: NumberRange) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end number

Get: To(self: NumberRange) -> int

Set: To(self: NumberRange) = value
"""


    Instance = NumberRange()
    """hardcoded/returns an instance of the class"""

class NumberRangeType(Object):
    """ enum NumberRangeType, values: PickBatch (2), Regular (0), SSCC (1) """
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

    PickBatch = None
    Regular = None
    SSCC = None
    value__ = None

    Instance = NumberRangeType()
    """hardcoded/returns an instance of the class"""


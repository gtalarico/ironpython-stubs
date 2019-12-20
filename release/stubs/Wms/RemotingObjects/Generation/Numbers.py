from System import Object
# encoding: utf-8
# module Wms.RemotingObjects.Generation.Numbers calls itself Numbers
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GeneratorBase(Object):
    """ GeneratorBase() """
    def Generate(self, startingNumber, numbersToGenerate, ascending, prefix, suffix, length, arguments):
        """
        Generate(self: GeneratorBase, startingNumber: int, numbersToGenerate: int, ascending: bool, prefix: str, suffix: str, length: int, *arguments: Array[object]) -> IEnumerable[IGeneratedBarcode]
        
            prefix: Optional
            suffix: Optional
            length: Optional
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    RangeLocker = None

    Instance = GeneratorBase()
    """hardcoded/returns an instance of the class"""

class IGenerator(Object):
    # no doc
    def Generate(self, startingNumber, numbersToGenerate, ascending, prefix, suffix, length, arguments):
        """ Generate(self: IGenerator, startingNumber: int, numbersToGenerate: int, ascending: bool, prefix: str, suffix: str, length: int, *arguments: Array[object]) -> IEnumerable[IGeneratedBarcode] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IGenerator()
    """hardcoded/returns an instance of the class"""

class SSCCGenerator(GeneratorBase):
    """ SSCCGenerator() """
    def Generate(self, startingNumber, numbersToGenerate, ascending, prefix, suffix, length, arguments):
        """
        Generate(self: SSCCGenerator, startingNumber: int, numbersToGenerate: int, ascending: bool, prefix: str, suffix: str, length: int, *arguments: Array[object]) -> IEnumerable[IGeneratedBarcode]
        
            prefix: ignored
            suffix: ignored
            length: ignored
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Instance = SSCCGenerator()
    """hardcoded/returns an instance of the class"""

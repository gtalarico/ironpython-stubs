# encoding: utf-8
# module Wms.RemotingImplementation.Generation.Labels calls itself Labels
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class LabelGeneratorBase():
    """ LabelGeneratorBase() """
    Instance = LabelGeneratorBase
    """hardcoded/returns an instance of the class"""
    def ConvertBarcodeToPrintLine(self, *args): #cannot find CLR method
        """ ConvertBarcodeToPrintLine(self: LabelGeneratorBase, barcode: IGeneratedBarcode) -> PrintLineBase """
        pass

    def GenerateAndPrintLabels(self, dfObject):
        """ GenerateAndPrintLabels(self: LabelGeneratorBase, dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> DataFlowObject[GenerateBarcodeLabelArgs] """
        pass

    def GetPrintJobLabel(self, *args): #cannot find CLR method
        """ GetPrintJobLabel(self: LabelGeneratorBase) -> str """
        pass

    def GetPrintLabel(self, *args): #cannot find CLR method
        """ GetPrintLabel(self: LabelGeneratorBase, dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> (bool, PrintLabel) """
        pass

    DfObject = None
    PrintLines = None
    Range = None


class SSCCLabelGenerator(LabelGeneratorBase):
    """ SSCCLabelGenerator() """
    Instance = SSCCLabelGenerator
    """hardcoded/returns an instance of the class"""
    DfObject = None
    PrintLines = None
    Range = None



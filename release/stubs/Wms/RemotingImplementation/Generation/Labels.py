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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return LabelGeneratorBase()

class SSCCLabelGenerator(LabelGeneratorBase):
    """ SSCCLabelGenerator() """
    DfObject = None
    PrintLines = None
    Range = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return SSCCLabelGenerator()


# encoding: utf-8
# module Wms.RemotingImplementation.Generation.Labels calls itself Labels
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class LabelGeneratorBase:
 """ LabelGeneratorBase() """
 def ConvertBarcodeToPrintLine(self,*args):
  """ ConvertBarcodeToPrintLine(self: LabelGeneratorBase,barcode: IGeneratedBarcode) -> PrintLineBase """
  pass
 def GenerateAndPrintLabels(self,dfObject):
  """ GenerateAndPrintLabels(self: LabelGeneratorBase,dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> DataFlowObject[GenerateBarcodeLabelArgs] """
  pass
 def GetPrintJobLabel(self,*args):
  """ GetPrintJobLabel(self: LabelGeneratorBase) -> str """
  pass
 def GetPrintLabel(self,*args):
  """ GetPrintLabel(self: LabelGeneratorBase,dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> (bool,PrintLabel) """
  pass
 DfObject=None
 PrintLines=None
 Range=None


class SSCCLabelGenerator:
 """ SSCCLabelGenerator() """
 DfObject=None
 PrintLines=None
 Range=None



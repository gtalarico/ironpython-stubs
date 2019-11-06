# encoding: utf-8
# module Wms.RemotingImplementation.Reports calls itself Reports
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class IReportDataArgsProvider:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IReportDataArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: IReportDataArgsProvider) -> ReportDataArgs

"""



class IReportExportArgsProvider:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IReportExportArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ExportArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExportArgs(self: IReportExportArgsProvider) -> ReportExportArgs

"""



class IReportPrintArgsProvider:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IReportPrintArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: IReportPrintArgsProvider) -> ReportPrintArgs

"""



class IReportRenderer:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IReportRenderer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Export(self,*__args):
  """
  Export[T](self: IReportRenderer,provider: T) -> ReportExport
  Export(self: IReportRenderer,args: ReportExportArgs,dataArgs: ReportDataArgs) -> ReportExport
  """
  pass
 def Print(self,*__args):
  """ Print[T](self: IReportRenderer,provider: T)Print(self: IReportRenderer,args: ReportPrintArgs,dataArgs: ReportDataArgs) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class ReportArgs(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ReportFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReportFile(self: ReportArgs) -> str

Set: ReportFile(self: ReportArgs)=value
"""

 ReportParameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReportParameters(self: ReportArgs) -> Dictionary[str,object]

Set: ReportParameters(self: ReportArgs)=value
"""



class ReportDataArgs(object):
 """ ReportDataArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportDataArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 DataSources=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataSources(self: ReportDataArgs) -> Dictionary[str,object]

Set: DataSources(self: ReportDataArgs)=value
"""

 MetaData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MetaData(self: ReportDataArgs) -> SerializableDictionary[str,str]

Set: MetaData(self: ReportDataArgs)=value
"""



class ReportExport(object):
 """ ReportExport() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportExport()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Buffer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Buffer(self: ReportExport) -> Array[Byte]

Set: Buffer(self: ReportExport)=value
"""

 Encoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Encoding(self: ReportExport) -> str

Set: Encoding(self: ReportExport)=value
"""

 FileExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FileExtension(self: ReportExport) -> str

Set: FileExtension(self: ReportExport)=value
"""

 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Format(self: ReportExport) -> ReportExportFormat

Set: Format(self: ReportExport)=value
"""

 MimeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MimeType(self: ReportExport) -> str

Set: MimeType(self: ReportExport)=value
"""

 NumberOfPages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumberOfPages(self: ReportExport) -> int

Set: NumberOfPages(self: ReportExport)=value
"""



class ReportExportArgs(ReportArgs):
 """ ReportExportArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportExportArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Format(self: ReportExportArgs) -> ReportExportFormat

Set: Format(self: ReportExportArgs)=value
"""



class ReportExportFormat:
 """ enum ReportExportFormat,values: Excel (1),Image (3),PDF (0),Word (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportExportFormat()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Excel=None
 Image=None
 PDF=None
 value__=None
 Word=None


class ReportPrintArgs(ReportArgs):
 """ ReportPrintArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportPrintArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 DocumentName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DocumentName(self: ReportPrintArgs) -> str

Set: DocumentName(self: ReportPrintArgs)=value
"""

 NoOfCopies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NoOfCopies(self: ReportPrintArgs) -> int

Set: NoOfCopies(self: ReportPrintArgs)=value
"""

 PrinterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrinterName(self: ReportPrintArgs) -> str

Set: PrinterName(self: ReportPrintArgs)=value
"""



# variables with complex values


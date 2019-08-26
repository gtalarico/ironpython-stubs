# encoding: utf-8
# module Wms.RemotingImplementation.Reports.RDL calls itself RDL
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RDLIsolatedReportRendererExecutor():
    """ RDLIsolatedReportRendererExecutor(lifetime: TimeSpan) """
    def Export(self, args, dataArgs):
        """ Export(self: RDLIsolatedReportRendererExecutor, args: ReportExportArgs, dataArgs: ReportDataArgs) -> ReportExport """
        pass

    def Print(self, args, dataArgs):
        """ Print(self: RDLIsolatedReportRendererExecutor, args: ReportPrintArgs, dataArgs: ReportDataArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lifetime):
        """ __new__(cls: type, lifetime: TimeSpan) """
        pass

    StateServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateServer(self: RDLIsolatedReportRendererExecutor) -> MarshalledLogger

"""

    StateServerChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Instance = RDLIsolatedReportRendererExecutor()
    """hardcoded/returns an instance of the class"""

class RDLReportRenderer:
    """ RDLReportRenderer() """
    def Export(self, *__args):
        """
        Export[T](self: RDLReportRenderer, provider: T) -> ReportExport
        Export(self: RDLReportRenderer, args: ReportExportArgs, dataArgs: ReportDataArgs) -> ReportExport
        """
        pass

    def Print(self, *__args):
        """ Print[T](self: RDLReportRenderer, provider: T)Print(self: RDLReportRenderer, args: ReportPrintArgs, dataArgs: ReportDataArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = RDLReportRenderer()
    """hardcoded/returns an instance of the class"""

class Utilities():
    """ Utilities() """
    @staticmethod
    def LoadNativeAssemblies(rootApplicationPath):
        """ LoadNativeAssemblies(rootApplicationPath: str) """
        pass

    Instance = Utilities()
    """hardcoded/returns an instance of the class"""


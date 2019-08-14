# encoding: utf-8
# module Wms.RemotingImplementation.InboundProcessing calls itself InboundProcessing
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ProcessInboundOrderHelper():
    """ ProcessInboundOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessInboundOrderHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Execute(self):
        """ Execute(self: ProcessInboundOrderHelper) -> Tuple[ProcessInboundReceiveLinesResult, DataFlowObject[ProcessInboundReceiveLinesArgs]] """
        pass

    def SaveErpResults(self, *args): #cannot find CLR method
        """ SaveErpResults(self: ProcessInboundOrderHelper) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessAdhocPurchaseOrderHelper(ProcessInboundOrderHelper):
    """ ProcessAdhocPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessAdhocPurchaseOrderHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessAdhocRmaOrderHelper(ProcessInboundOrderHelper):
    """ ProcessAdhocRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessAdhocRmaOrderHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessInboundReceiveLinesFactory():
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessInboundReceiveLinesFactory()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def CreateHelper(dfObject, stockManager, general):
        """ CreateHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager, general: IGeneral) -> ProcessInboundOrderHelper """
        pass

    __all__ = [
        'CreateHelper',
    ]


class ProcessPreReceiptHelper(ProcessInboundOrderHelper):
    """ ProcessPreReceiptHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessPreReceiptHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessPurchaseOrderHelper(ProcessInboundOrderHelper):
    """ ProcessPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessPurchaseOrderHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessRmaOrderHelper(ProcessInboundOrderHelper):
    """ ProcessRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ProcessRmaOrderHelper()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None



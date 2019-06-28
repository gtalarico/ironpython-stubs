# encoding: utf-8
# module Wms.RemotingImplementation.InboundProcessing calls itself InboundProcessing
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ProcessInboundOrderHelper:
    """ ProcessInboundOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
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


class ProcessAdhocPurchaseOrderHelper:
    """ ProcessAdhocPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessAdhocRmaOrderHelper:
    """ ProcessAdhocRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessInboundReceiveLinesFactory:
    # no doc
    @staticmethod
    def CreateHelper(dfObject, stockManager, general):
        """ CreateHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager, general: IGeneral) -> ProcessInboundOrderHelper """
        pass

    __all__ = [
        'CreateHelper',
    ]


class ProcessPreReceiptHelper:
    """ ProcessPreReceiptHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessPurchaseOrderHelper:
    """ ProcessPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None


class ProcessRmaOrderHelper:
    """ ProcessRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None



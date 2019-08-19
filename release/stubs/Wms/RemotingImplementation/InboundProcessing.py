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

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessInboundOrderHelper()

class ProcessAdhocPurchaseOrderHelper(ProcessInboundOrderHelper):
    """ ProcessAdhocPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessAdhocPurchaseOrderHelper()

class ProcessAdhocRmaOrderHelper(ProcessInboundOrderHelper):
    """ ProcessAdhocRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessAdhocRmaOrderHelper()

class ProcessInboundReceiveLinesFactory():
    # no doc
    @staticmethod
    def CreateHelper(dfObject, stockManager, general):
        """ CreateHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager, general: IGeneral) -> ProcessInboundOrderHelper """
        pass

    __all__ = [
        'CreateHelper',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessInboundReceiveLinesFactory()

class ProcessPreReceiptHelper(ProcessInboundOrderHelper):
    """ ProcessPreReceiptHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessPreReceiptHelper()

class ProcessPurchaseOrderHelper(ProcessInboundOrderHelper):
    """ ProcessPurchaseOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessPurchaseOrderHelper()

class ProcessRmaOrderHelper(ProcessInboundOrderHelper):
    """ ProcessRmaOrderHelper(dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
    @staticmethod # known case of __new__
    def __new__(self, dfObject, stockManager):
        """ __new__(cls: type, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs], stockManager: IStockManager) """
        pass

    _erpResults = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ProcessRmaOrderHelper()


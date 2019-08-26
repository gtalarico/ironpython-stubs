from Wms.RemotingImplementation.TaskScheduler import *
from Wms.EdiMessaging.Processor import *
# encoding: utf-8
# module Wms.RemotingImplementation.PrintJobs calls itself PrintJobs
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BwServerPrintJobMessageProcessor(MessageProcessor):
    """ BwServerPrintJobMessageProcessor(queueProvider: IQueueProvider) """
    @staticmethod # known case of __new__
    def __new__(self, queueProvider):
        """ __new__(cls: type, queueProvider: IQueueProvider) """
        pass

    _queueProvider = None

    Instance = BwServerPrintJobMessageProcessor()
    """hardcoded/returns an instance of the class"""

class CleanupDocumentQueueTask(TaskBase):
    """ CleanupDocumentQueueTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: CleanupDocumentQueueTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: CleanupDocumentQueueTask) -> TimeSpan

"""


    Instance = CleanupDocumentQueueTask()
    """hardcoded/returns an instance of the class"""

class DocumentQueueExtensionMethods():
    # no doc
    @staticmethod
    def AddPrintJobSync(queue, job):
        """ AddPrintJobSync(queue: IAddPrintJob, job: AddPrintJob) -> Guid """
        pass

    @staticmethod
    def AddReport(docQueue, report, jobType, attributes, printerId, printingOptions):
        """ AddReport[T](docQueue: IAddPrintJob, report: T, jobType: str, attributes: SerializableDictionary[str, str], printerId: str, printingOptions: PrintingOptions) -> Task[Guid] """
        pass

    @staticmethod
    def AddReportSync(docQueue, report, jobType, attributes, printerId, printingOptions):
        """ AddReportSync[T](docQueue: IAddPrintJob, report: T, jobType: str, attributes: SerializableDictionary[str, str], printerId: str, printingOptions: PrintingOptions) -> Guid """
        pass

    @staticmethod
    def ParseDocumentTypeString(documentType):
        """ ParseDocumentTypeString(documentType: str) -> DocumentTypeEnum """
        pass

    __all__ = [
        'AddPrintJobSync',
        'AddReport',
        'AddReportSync',
        'ParseDocumentTypeString',
    ]

    Instance = DocumentQueueExtensionMethods()
    """hardcoded/returns an instance of the class"""

class JsonMessageDispatcher():
    """ JsonMessageDispatcher(queueProvider: IQueueProvider) """
    def PublishMessage(self, message):
        """ PublishMessage(self: JsonMessageDispatcher, message: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, queueProvider):
        """ __new__(cls: type, queueProvider: IQueueProvider) """
        pass

    Instance = JsonMessageDispatcher()
    """hardcoded/returns an instance of the class"""

class PrintJobExtensions():
    # no doc
    @staticmethod
    def RegisterMsQueue(container, resolverName, host, queueName):
        """ RegisterMsQueue(container: IUnityContainer, resolverName: str, host: str, queueName: str) """
        pass

    __all__ = [
        'RegisterMsQueue',
    ]

    Instance = PrintJobExtensions()
    """hardcoded/returns an instance of the class"""

class PrintJobQueueDispatcher(JsonMessageDispatcher):
    """ PrintJobQueueDispatcher(queueProvider: IQueueProvider) """
    @staticmethod # known case of __new__
    def __new__(self, queueProvider):
        """ __new__(cls: type, queueProvider: IQueueProvider) """
        pass

    Instance = PrintJobQueueDispatcher()
    """hardcoded/returns an instance of the class"""

class PrintJobsOnStartupValidator():
    """ PrintJobsOnStartupValidator(messageDispatcher: PrintJobQueueDispatcher) """
    def Start(self, cancellationToken):
        """ Start(self: PrintJobsOnStartupValidator, cancellationToken: CancellationToken) -> Task """
        pass

    @staticmethod # known case of __new__
    def __new__(self, messageDispatcher):
        """ __new__(cls: type, messageDispatcher: PrintJobQueueDispatcher) """
        pass

    Instance = PrintJobsOnStartupValidator()
    """hardcoded/returns an instance of the class"""

class PrintJobsQueuer():
    """ PrintJobsQueuer(messageDispatcher: PrintJobQueueDispatcher, storageProvider: StorageProvider) """
    def QueueNextPrintJob(self, *args): #cannot find CLR method
        """ QueueNextPrintJob(self: PrintJobsQueuer) -> int """
        pass

    def TryQueueOpenPrintJobs(self):
        """ TryQueueOpenPrintJobs(self: PrintJobsQueuer) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, messageDispatcher, storageProvider):
        """ __new__(cls: type, messageDispatcher: PrintJobQueueDispatcher, storageProvider: StorageProvider) """
        pass

    Instance = PrintJobsQueuer()
    """hardcoded/returns an instance of the class"""

# variables with complex values


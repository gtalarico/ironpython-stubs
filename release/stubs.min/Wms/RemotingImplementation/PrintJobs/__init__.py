# encoding: utf-8
# module Wms.RemotingImplementation.PrintJobs calls itself PrintJobs
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BwServerPrintJobMessageProcessor:
 """ BwServerPrintJobMessageProcessor(queueProvider: IQueueProvider) """
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass
 _queueProvider=None


class CleanupDocumentQueueTask:
 """ CleanupDocumentQueueTask(settings: SystemSettings) """
 def Run(self):
  """ Run(self: CleanupDocumentQueueTask) """
  pass
 @staticmethod
 def __new__(self,settings):
  """ __new__(cls: type,settings: SystemSettings) """
  pass
 Interval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Interval(self: CleanupDocumentQueueTask) -> TimeSpan

"""



class DocumentQueueExtensionMethods:
 # no doc
 @staticmethod
 def AddPrintJobSync(queue,job):
  """ AddPrintJobSync(queue: IAddPrintJob,job: AddPrintJob) -> Guid """
  pass
 @staticmethod
 def AddReport(docQueue,report,jobType,attributes,printerId,printingOptions):
  """ AddReport[T](docQueue: IAddPrintJob,report: T,jobType: str,attributes: SerializableDictionary[str,str],printerId: str,printingOptions: PrintingOptions) -> Task[Guid] """
  pass
 @staticmethod
 def AddReportSync(docQueue,report,jobType,attributes,printerId,printingOptions):
  """ AddReportSync[T](docQueue: IAddPrintJob,report: T,jobType: str,attributes: SerializableDictionary[str,str],printerId: str,printingOptions: PrintingOptions) -> Guid """
  pass
 @staticmethod
 def ParseDocumentTypeString(documentType):
  """ ParseDocumentTypeString(documentType: str) -> DocumentTypeEnum """
  pass
 __all__=[
  'AddPrintJobSync',
  'AddReport',
  'AddReportSync',
  'ParseDocumentTypeString',
 ]


class JsonMessageDispatcher:
 """ JsonMessageDispatcher(queueProvider: IQueueProvider) """
 def PublishMessage(self,message):
  """ PublishMessage(self: JsonMessageDispatcher,message: object) """
  pass
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass

class PrintJobExtensions:
 # no doc
 @staticmethod
 def RegisterMsQueue(container,resolverName,host,queueName):
  """ RegisterMsQueue(container: IUnityContainer,resolverName: str,host: str,queueName: str) """
  pass
 __all__=[
  'RegisterMsQueue',
 ]


class PrintJobQueueDispatcher:
 """ PrintJobQueueDispatcher(queueProvider: IQueueProvider) """
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass

class PrintJobsOnStartupValidator:
 """ PrintJobsOnStartupValidator(messageDispatcher: PrintJobQueueDispatcher) """
 def Start(self,cancellationToken):
  """ Start(self: PrintJobsOnStartupValidator,cancellationToken: CancellationToken) -> Task """
  pass
 @staticmethod
 def __new__(self,messageDispatcher):
  """ __new__(cls: type,messageDispatcher: PrintJobQueueDispatcher) """
  pass

class PrintJobsQueuer:
 """ PrintJobsQueuer(messageDispatcher: PrintJobQueueDispatcher,storageProvider: StorageProvider) """
 def QueueNextPrintJob(self,*args):
  """ QueueNextPrintJob(self: PrintJobsQueuer) -> int """
  pass
 def TryQueueOpenPrintJobs(self):
  """ TryQueueOpenPrintJobs(self: PrintJobsQueuer) -> bool """
  pass
 @staticmethod
 def __new__(self,messageDispatcher,storageProvider):
  """ __new__(cls: type,messageDispatcher: PrintJobQueueDispatcher,storageProvider: StorageProvider) """
  pass

# variables with complex values


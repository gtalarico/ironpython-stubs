# encoding: utf-8
# module Wms.RemotingImplementation.PrintJobs calls itself PrintJobs
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class BwServerPrintJobMessageProcessor(MessageProcessor):
 """ BwServerPrintJobMessageProcessor(queueProvider: IQueueProvider) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BwServerPrintJobMessageProcessor()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass
 _queueProvider=None


class CleanupDocumentQueueTask(TaskBase):
 """ CleanupDocumentQueueTask(settings: SystemSettings) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CleanupDocumentQueueTask()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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



class DocumentQueueExtensionMethods(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DocumentQueueExtensionMethods()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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


class JsonMessageDispatcher(object):
 """ JsonMessageDispatcher(queueProvider: IQueueProvider) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return JsonMessageDispatcher()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def PublishMessage(self,message):
  """ PublishMessage(self: JsonMessageDispatcher,message: object) """
  pass
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass

class PrintJobExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintJobExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def RegisterMsQueue(container,resolverName,host,queueName):
  """ RegisterMsQueue(container: IUnityContainer,resolverName: str,host: str,queueName: str) """
  pass
 __all__=[
  'RegisterMsQueue',
 ]


class PrintJobQueueDispatcher(JsonMessageDispatcher):
 """ PrintJobQueueDispatcher(queueProvider: IQueueProvider) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintJobQueueDispatcher()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,queueProvider):
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass

class PrintJobsOnStartupValidator(object):
 """ PrintJobsOnStartupValidator(messageDispatcher: PrintJobQueueDispatcher) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintJobsOnStartupValidator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Start(self,cancellationToken):
  """ Start(self: PrintJobsOnStartupValidator,cancellationToken: CancellationToken) -> Task """
  pass
 @staticmethod
 def __new__(self,messageDispatcher):
  """ __new__(cls: type,messageDispatcher: PrintJobQueueDispatcher) """
  pass

class PrintJobsQueuer(object):
 """ PrintJobsQueuer(messageDispatcher: PrintJobQueueDispatcher,storageProvider: StorageProvider) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintJobsQueuer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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


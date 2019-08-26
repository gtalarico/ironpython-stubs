# encoding: utf-8
# module Wms.RemotingObjects.DocumentQueue.Messages calls itself Messages
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ChangePrintJobStatusMessage():
    """ ChangePrintJobStatusMessage() """
    ExternalJobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Job id giving by External service.

Get: ExternalJobId(self: ChangePrintJobStatusMessage) -> str

Set: ExternalJobId(self: ChangePrintJobStatusMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Job id giving by BOXwise server.

Get: JobId(self: ChangePrintJobStatusMessage) -> str

Set: JobId(self: ChangePrintJobStatusMessage) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Informational message about the new status.

Get: Message(self: ChangePrintJobStatusMessage) -> str

Set: Message(self: ChangePrintJobStatusMessage) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """New status the job got on this change.

Get: NewStatus(self: ChangePrintJobStatusMessage) -> PrintJobStatusEnum

Set: NewStatus(self: ChangePrintJobStatusMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A timestamp in UTC when this message was created

Get: TimeStamp(self: ChangePrintJobStatusMessage) -> DateTime

Set: TimeStamp(self: ChangePrintJobStatusMessage) = value
"""


    Instance = ChangePrintJobStatusMessage()
    """hardcoded/returns an instance of the class"""

class GetStatusOfJobsMessage():
    """
    request a status update of multiple jobs.
    
    GetStatusOfJobsMessage()
    """
    Jobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Jobs we want a report of, if possible.

Get: Jobs(self: GetStatusOfJobsMessage) -> List[Item]

Set: Jobs(self: GetStatusOfJobsMessage) = value
"""


    Item = None

    Instance = GetStatusOfJobsMessage()
    """hardcoded/returns an instance of the class"""

class PrintJobDispatchedMessage():
    """
    Message to let boxwise know printerjob has been dispatched to printer(service).
    
    PrintJobDispatchedMessage()
    """
    ExternalJobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Job id the job got by the external platform when dispatching job.

Get: ExternalJobId(self: PrintJobDispatchedMessage) -> str

Set: ExternalJobId(self: PrintJobDispatchedMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Job id giving by BOXwise server.

Get: JobId(self: PrintJobDispatchedMessage) -> str

Set: JobId(self: PrintJobDispatchedMessage) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Informational message.

Get: Message(self: PrintJobDispatchedMessage) -> str

Set: Message(self: PrintJobDispatchedMessage) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current status of the job, expect to be: dispatched

Get: NewStatus(self: PrintJobDispatchedMessage) -> PrintJobStatusEnum

Set: NewStatus(self: PrintJobDispatchedMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A timestamp in UTC when this message was created

Get: TimeStamp(self: PrintJobDispatchedMessage) -> DateTime

Set: TimeStamp(self: PrintJobDispatchedMessage) = value
"""


    Instance = PrintJobDispatchedMessage()
    """hardcoded/returns an instance of the class"""

class StartPrintJobMessage():
    """
    Message to request a print of a document.
    
    StartPrintJobMessage()
    """
    BlobContainerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Blob container name where the document contents are stored under.

Get: BlobContainerName(self: StartPrintJobMessage) -> str

Set: BlobContainerName(self: StartPrintJobMessage) = value
"""

    BlobName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Blob name where the document contents are stored under.

Get: BlobName(self: StartPrintJobMessage) -> str

Set: BlobName(self: StartPrintJobMessage) = value
"""

    DocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name that will be usd for the print job (seen in the print job queue).

Get: DocumentName(self: StartPrintJobMessage) -> str

Set: DocumentName(self: StartPrintJobMessage) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of document to print (pdf/raw etc)

Get: DocumentType(self: StartPrintJobMessage) -> DocumentTypeEnum

Set: DocumentType(self: StartPrintJobMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Job id giving by BOXwise server.

Get: JobId(self: StartPrintJobMessage) -> str

Set: JobId(self: StartPrintJobMessage) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the printer in the external service.

Get: PrinterId(self: StartPrintJobMessage) -> str

Set: PrinterId(self: StartPrintJobMessage) = value
"""

    PrinterOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Printer options to use for doing this printjob.

Get: PrinterOptions(self: StartPrintJobMessage) -> PrintingOptions

Set: PrinterOptions(self: StartPrintJobMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A timestamp in UTC when this message was created

Get: TimeStamp(self: StartPrintJobMessage) -> DateTime

Set: TimeStamp(self: StartPrintJobMessage) = value
"""


    Instance = StartPrintJobMessage()
    """hardcoded/returns an instance of the class"""


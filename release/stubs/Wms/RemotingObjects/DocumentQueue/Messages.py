# encoding: utf-8
# module Wms.RemotingObjects.DocumentQueue.Messages calls itself Messages
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ChangePrintJobStatusMessage:
    """ ChangePrintJobStatusMessage() """
    ExternalJobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalJobId(self: ChangePrintJobStatusMessage) -> str

Set: ExternalJobId(self: ChangePrintJobStatusMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobId(self: ChangePrintJobStatusMessage) -> str

Set: JobId(self: ChangePrintJobStatusMessage) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ChangePrintJobStatusMessage) -> str

Set: Message(self: ChangePrintJobStatusMessage) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: ChangePrintJobStatusMessage) -> PrintJobStatusEnum

Set: NewStatus(self: ChangePrintJobStatusMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: ChangePrintJobStatusMessage) -> DateTime

Set: TimeStamp(self: ChangePrintJobStatusMessage) = value
"""



class GetStatusOfJobsMessage:
    """ GetStatusOfJobsMessage() """
    Jobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Jobs(self: GetStatusOfJobsMessage) -> List[Item]

Set: Jobs(self: GetStatusOfJobsMessage) = value
"""


    Item = None


class PrintJobDispatchedMessage:
    """ PrintJobDispatchedMessage() """
    ExternalJobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalJobId(self: PrintJobDispatchedMessage) -> str

Set: ExternalJobId(self: PrintJobDispatchedMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobId(self: PrintJobDispatchedMessage) -> str

Set: JobId(self: PrintJobDispatchedMessage) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: PrintJobDispatchedMessage) -> str

Set: Message(self: PrintJobDispatchedMessage) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: PrintJobDispatchedMessage) -> PrintJobStatusEnum

Set: NewStatus(self: PrintJobDispatchedMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: PrintJobDispatchedMessage) -> DateTime

Set: TimeStamp(self: PrintJobDispatchedMessage) = value
"""



class StartPrintJobMessage:
    """ StartPrintJobMessage() """
    BlobContainerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlobContainerName(self: StartPrintJobMessage) -> str

Set: BlobContainerName(self: StartPrintJobMessage) = value
"""

    BlobName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlobName(self: StartPrintJobMessage) -> str

Set: BlobName(self: StartPrintJobMessage) = value
"""

    DocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentName(self: StartPrintJobMessage) -> str

Set: DocumentName(self: StartPrintJobMessage) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentType(self: StartPrintJobMessage) -> DocumentTypeEnum

Set: DocumentType(self: StartPrintJobMessage) = value
"""

    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobId(self: StartPrintJobMessage) -> str

Set: JobId(self: StartPrintJobMessage) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterId(self: StartPrintJobMessage) -> str

Set: PrinterId(self: StartPrintJobMessage) = value
"""

    PrinterOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterOptions(self: StartPrintJobMessage) -> PrintingOptions

Set: PrinterOptions(self: StartPrintJobMessage) = value
"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: StartPrintJobMessage) -> DateTime

Set: TimeStamp(self: StartPrintJobMessage) = value
"""




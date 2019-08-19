from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.DocumentQueue calls itself DocumentQueue
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddPrintJob():
    """ AddPrintJob() """
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extra attributes to store on the print message,
            this is not mandatory here since direct print job doesn't pass the print rules but instead uses printerId that is provided.

Get: Attributes(self: AddPrintJob) -> SerializableDictionary[str, str]

Set: Attributes(self: AddPrintJob) = value
"""

    DocumentSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Source to get the document from to store it in blob storage.

Get: DocumentSource(self: AddPrintJob) -> IDocumentSource

Set: DocumentSource(self: AddPrintJob) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(file) type of the document you are printing.

Get: DocumentType(self: AddPrintJob) -> DocumentTypeEnum

Set: DocumentType(self: AddPrintJob) = value
"""

    JobType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A name for the type/category of document to print
            Eg: Picklist, ERP packageslip, SendLabel, etc.

Get: JobType(self: AddPrintJob) -> str

Set: JobType(self: AddPrintJob) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name for the print job.

Get: Label(self: AddPrintJob) -> str

Set: Label(self: AddPrintJob) = value
"""

    NumberOfPages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPages(self: AddPrintJob) -> int

Set: NumberOfPages(self: AddPrintJob) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the printer that you want to use.
            If not provided a printer will be chosen through the rule engine

Get: PrinterId(self: AddPrintJob) -> str

Set: PrinterId(self: AddPrintJob) = value
"""

    PrintingOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extra (override) print options for this specific print job.

Get: PrintingOptions(self: AddPrintJob) -> PrintingOptions

Set: PrintingOptions(self: AddPrintJob) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AddPrintJob()

class Attachment():
    """
    A is a printable document.
    
    Attachment()
    """
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Raw bytes to be printed.

Get: Document(self: Attachment) -> Array[Byte]

Set: Document(self: Attachment) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of document, eg:
            PDF - pdf file (printed using external tool (printpdf.bat)).
            ZPL - Zebra label (printed by label printer).
            Rest is printed as raw bytes document.

Get: DocumentType(self: Attachment) -> DocumentTypeEnum

Set: DocumentType(self: Attachment) = value
"""

    JobType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A key to identify the type of this attachment

Get: JobType(self: Attachment) -> str

Set: JobType(self: Attachment) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this document

Get: Label(self: Attachment) -> str

Set: Label(self: Attachment) = value
"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The meta data of this attachment

Get: Metadata(self: Attachment) -> SerializableDictionary[str, str]

Set: Metadata(self: Attachment) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return Attachment()

class AttributeValue():
    """ AttributeValue() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: AttributeValue) -> str

Set: Code(self: AttributeValue) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: AttributeValue) -> str

Set: Description(self: AttributeValue) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AttributeValue()

class DocumentDescriptor():
    """
    DocumentDescriptor()
    DocumentDescriptor(code: str, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, code=None, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, code: str, description: str)
        """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unique code to identify the type of document

Get: Code(self: DocumentDescriptor) -> str

Set: Code(self: DocumentDescriptor) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A readable description of the document

Get: Description(self: DocumentDescriptor) -> str

Set: Description(self: DocumentDescriptor) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return DocumentDescriptor()

class GetPrinterRulesArgs():
    """ GetPrinterRulesArgs() """
    FileTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileTypes(self: GetPrinterRulesArgs) -> Array[str]

Set: FileTypes(self: GetPrinterRulesArgs) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetPrinterRulesArgs) -> str

Set: Filter(self: GetPrinterRulesArgs) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: GetPrinterRulesArgs) -> Nullable[bool]

Set: IsActive(self: GetPrinterRulesArgs) = value
"""

    JobTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobTypes(self: GetPrinterRulesArgs) -> Array[str]

Set: JobTypes(self: GetPrinterRulesArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetPrinterRulesArgs()

class GetPrintJobAttributesArgs():
    """ GetPrintJobAttributesArgs() """
    DefaultAttributesOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if only the default set of attributes should be retrieved

Get: DefaultAttributesOnly(self: GetPrintJobAttributesArgs) -> bool

Set: DefaultAttributesOnly(self: GetPrintJobAttributesArgs) = value
"""

    JobType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobType(self: GetPrintJobAttributesArgs) -> str

Set: JobType(self: GetPrintJobAttributesArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetPrintJobAttributesArgs()

class GetPrintJobAuditLogArgs():
    """ GetPrintJobAuditLogArgs() """
    JobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobId(self: GetPrintJobAuditLogArgs) -> int

Set: JobId(self: GetPrintJobAuditLogArgs) = value
"""

    PagingParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PagingParams(self: GetPrintJobAuditLogArgs) -> PagingParams

Set: PagingParams(self: GetPrintJobAuditLogArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetPrintJobAuditLogArgs()

class GetPrintJobsArgs():
    """ GetPrintJobsArgs() """
    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetPrintJobsArgs) -> str

Set: Filter(self: GetPrintJobsArgs) = value
"""

    JobTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobTypes(self: GetPrintJobsArgs) -> Array[str]

Set: JobTypes(self: GetPrintJobsArgs) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: GetPrintJobsArgs) -> Array[int]

Set: Status(self: GetPrintJobsArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetPrintJobsArgs()

class IAddPrintJob:
    """
    Interface abstraction for adding print jobs.
                Needed for projects who can't directly use RemotingImplementation
    """
    def AddPrintJob(self, printjob):
        """
        AddPrintJob(self: IAddPrintJob, printjob: AddPrintJob) -> Task[Guid]
        
            Add print job.
                    Returns guid id of job when job has been queued.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IAddPrintJob()

class Operator():
    """
    Operator()
    Operator(code: str, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, code=None, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, code: str, description: str)
        """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Operator) -> str

Set: Code(self: Operator) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Operator) -> str

Set: Description(self: Operator) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return Operator()

class PrintJobAttribute():
    """
    PrintJobAttribute()
    PrintJobAttribute(code: str)
    PrintJobAttribute(code: str, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, code=None, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, code: str)
        __new__(cls: type, code: str, description: str)
        """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: PrintJobAttribute) -> str

Set: Code(self: PrintJobAttribute) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PrintJobAttribute) -> str

Set: Description(self: PrintJobAttribute) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintJobAttribute()

class PrintJobAuditLogEntry(DbObject):
    """ PrintJobAuditLogEntry() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PrintJobAuditLogEntry) -> str

Set: Description(self: PrintJobAuditLogEntry) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PrintJobAuditLogEntry) -> int

Set: Id(self: PrintJobAuditLogEntry) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: PrintJobAuditLogEntry) -> MessageStatus

Set: NewStatus(self: PrintJobAuditLogEntry) = value
"""

    OldStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldStatus(self: PrintJobAuditLogEntry) -> MessageStatus

Set: OldStatus(self: PrintJobAuditLogEntry) = value
"""

    StatusChangedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusChangedOn(self: PrintJobAuditLogEntry) -> DateTime

Set: StatusChangedOn(self: PrintJobAuditLogEntry) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintJobAuditLogEntry()

class PrintJobConstants():
    # no doc
    QueueFromAgentResolverKey = 'BwPrintJobsReturn'
    QueueToAgentResolverKey = 'BwPrintJobs'
    __all__ = [
        'QueueFromAgentResolverKey',
        'QueueToAgentResolverKey',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintJobConstants()

class PrintJobStatus:
    """ enum PrintJobStatus, values: Dispatched (18), Enqueued (10), Handled (20), HandledWithErrors (30), Handling (15), New (0), ReSubmitted (40), Unknown (50) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Dispatched = None
    Enqueued = None
    Handled = None
    HandledWithErrors = None
    Handling = None
    New = None
    ReSubmitted = None
    Unknown = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintJobStatus()

class PrintJobType():
    """
    PrintJobType()
    PrintJobType(id: str, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, id=None, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, id: str, description: str)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PrintJobType) -> str

Set: Description(self: PrintJobType) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PrintJobType) -> str

Set: Id(self: PrintJobType) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintJobType()

class PrintRule(DbObject):
    """ PrintRule() """
    def Equals(self, *__args):
        """
        Equals(self: PrintRule, obj: object) -> bool
        Equals(self: PrintRule, other: PrintRule) -> bool
        """
        pass

    def ToString(self):
        """ ToString(self: PrintRule) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Conditions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Conditions(self: PrintRule) -> List[PrintRuleLine]

Set: Conditions(self: PrintRule) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PrintRule) -> str

Set: Description(self: PrintRule) = value
"""

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Device(self: PrintRule) -> str

Set: Device(self: PrintRule) = value
"""

    DeviceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceType(self: PrintRule) -> str

Set: DeviceType(self: PrintRule) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentType(self: PrintRule) -> DocumentTypeEnum

Set: DocumentType(self: PrintRule) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PrintRule) -> int

Set: Id(self: PrintRule) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: PrintRule) -> bool

Set: IsActive(self: PrintRule) = value
"""

    IsSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSystem(self: PrintRule) -> bool

Set: IsSystem(self: PrintRule) = value
"""

    JobType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobType(self: PrintRule) -> str

Set: JobType(self: PrintRule) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: PrintRule) -> str

Set: Label(self: PrintRule) = value
"""

    LabelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelId(self: PrintRule) -> str

Set: LabelId(self: PrintRule) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterId(self: PrintRule) -> str

Set: PrinterId(self: PrintRule) = value
"""

    PrintingOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintingOptions(self: PrintRule) -> PrintingOptions

Set: PrintingOptions(self: PrintRule) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: PrintRule) -> int

Set: Priority(self: PrintRule) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserId(self: PrintRule) -> str

Set: UserId(self: PrintRule) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: PrintRule) -> str

Set: ZoneId(self: PrintRule) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintRule()

class PrintRuleLine(DbObject):
    """
    PrintRuleLine()
    PrintRuleLine(field: str, operator: str, value: str)
    PrintRuleLine(field: str, operator: str, values: IEnumerable[str])
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, field=None, operator=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, field: str, operator: str, value: str)
        __new__(cls: type, field: str, operator: str, values: IEnumerable[str])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Field(self: PrintRuleLine) -> str

Set: Field(self: PrintRuleLine) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PrintRuleLine) -> int

Set: Id(self: PrintRuleLine) = value
"""

    Operator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operator(self: PrintRuleLine) -> str

Set: Operator(self: PrintRuleLine) = value
"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: PrintRuleLine) -> IEnumerable[str]

Set: Values(self: PrintRuleLine) = value
"""

    ValuesAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValuesAsString(self: PrintRuleLine) -> str

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PrintRuleLine()

class QueuedPrintJob(DbObject):
    """ QueuedPrintJob() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BlobId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the blob content

Get: BlobId(self: QueuedPrintJob) -> int

Set: BlobId(self: QueuedPrintJob) = value
"""

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of copies

Get: Copies(self: QueuedPrintJob) -> int

Set: Copies(self: QueuedPrintJob) = value
"""

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the computer/client that created this print job.

Get: Device(self: QueuedPrintJob) -> str

Set: Device(self: QueuedPrintJob) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of file to print

Get: DocumentType(self: QueuedPrintJob) -> DocumentTypeEnum

Set: DocumentType(self: QueuedPrintJob) = value
"""

    FileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the file to print in bytes.

Get: FileSize(self: QueuedPrintJob) -> int

Set: FileSize(self: QueuedPrintJob) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifying Id of the print job

Get: Id(self: QueuedPrintJob) -> Guid

Set: Id(self: QueuedPrintJob) = value
"""

    JobType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A key to defince the type of this job (ie a PrintJobTypeItemLabel or PrintJobTypePickingList).
            This key can be used to translate it to a readable description to display.

Get: JobType(self: QueuedPrintJob) -> str

Set: JobType(self: QueuedPrintJob) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Informative name of the print job

Get: Label(self: QueuedPrintJob) -> str

Set: Label(self: QueuedPrintJob) = value
"""

    PageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of pages

Get: PageSize(self: QueuedPrintJob) -> str

Set: PageSize(self: QueuedPrintJob) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the printer, where the job will be printed on.

Get: PrinterId(self: QueuedPrintJob) -> str

Set: PrinterId(self: QueuedPrintJob) = value
"""

    PrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterName(self: QueuedPrintJob) -> str

Set: PrinterName(self: QueuedPrintJob) = value
"""

    PrintRuleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the printrule that was used to decide the printer to print from.

Get: PrintRuleId(self: QueuedPrintJob) -> Nullable[int]

Set: PrintRuleId(self: QueuedPrintJob) = value
"""

    Resubmitted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this print job was resubmitted

Get: Resubmitted(self: QueuedPrintJob) -> bool

Set: Resubmitted(self: QueuedPrintJob) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current state of the print job.

Get: Status(self: QueuedPrintJob) -> PrintJobStatus

Set: Status(self: QueuedPrintJob) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the user that created this print job.

Get: UserName(self: QueuedPrintJob) -> str

Set: UserName(self: QueuedPrintJob) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the zone of which the print job was created

Get: ZoneId(self: QueuedPrintJob) -> int

Set: ZoneId(self: QueuedPrintJob) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return QueuedPrintJob()

class RedispatchPrintJobArgs():
    """ RedispatchPrintJobArgs() """
    JobIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobIds(self: RedispatchPrintJobArgs) -> Array[Guid]

Set: JobIds(self: RedispatchPrintJobArgs) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterId(self: RedispatchPrintJobArgs) -> str

Set: PrinterId(self: RedispatchPrintJobArgs) = value
"""

    PrintingOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintingOptions(self: RedispatchPrintJobArgs) -> PrintingOptions

Set: PrintingOptions(self: RedispatchPrintJobArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return RedispatchPrintJobArgs()

# variables with complex values


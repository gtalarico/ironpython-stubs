# encoding: utf-8
# module Wms.RemotingObjects.Notifications calls itself Notifications
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddNotificationGroupArgs:
    """ AddNotificationGroupArgs() """
    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GotoLink(self: AddNotificationGroupArgs) -> str

Set: GotoLink(self: AddNotificationGroupArgs) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: AddNotificationGroupArgs) -> str

Set: Key(self: AddNotificationGroupArgs) = value
"""



class DeleteNotificationByReferenceArgs:
    """ DeleteNotificationByReferenceArgs() """
    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: DeleteNotificationByReferenceArgs) -> str

Set: GroupKey(self: DeleteNotificationByReferenceArgs) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: DeleteNotificationByReferenceArgs) -> str

Set: Reference(self: DeleteNotificationByReferenceArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: DeleteNotificationByReferenceArgs) -> Nullable[int]

Set: ZoneId(self: DeleteNotificationByReferenceArgs) = value
"""



class DeleteNotificationGroupArgs:
    """ DeleteNotificationGroupArgs() """
    ForceDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceDelete(self: DeleteNotificationGroupArgs) -> bool

Set: ForceDelete(self: DeleteNotificationGroupArgs) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: DeleteNotificationGroupArgs) -> str

Set: Key(self: DeleteNotificationGroupArgs) = value
"""



class ExecuteNotificationSummaryArgs:
    """ ExecuteNotificationSummaryArgs() """
    def TryGetConfiguration(self, key):
        """
        TryGetConfiguration[T](self: ExecuteNotificationSummaryArgs, key: str) -> T
        TryGetConfiguration(self: ExecuteNotificationSummaryArgs, key: str) -> object
        """
        pass

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: ExecuteNotificationSummaryArgs) -> Dictionary[str, object]

Set: Configuration(self: ExecuteNotificationSummaryArgs) = value
"""

    GivenName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GivenName(self: ExecuteNotificationSummaryArgs) -> str

Set: GivenName(self: ExecuteNotificationSummaryArgs) = value
"""

    LastTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastTime(self: ExecuteNotificationSummaryArgs) -> DateTime

Set: LastTime(self: ExecuteNotificationSummaryArgs) = value
"""

    ThisTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThisTime(self: ExecuteNotificationSummaryArgs) -> DateTime

Set: ThisTime(self: ExecuteNotificationSummaryArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserId(self: ExecuteNotificationSummaryArgs) -> int

Set: UserId(self: ExecuteNotificationSummaryArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: ExecuteNotificationSummaryArgs) -> int

Set: ZoneId(self: ExecuteNotificationSummaryArgs) = value
"""



class GetNotificationsArgs:
    """ GetNotificationsArgs() """
    LimitPerGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitPerGroup(self: GetNotificationsArgs) -> Nullable[int]

Set: LimitPerGroup(self: GetNotificationsArgs) = value
"""

    NewerThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewerThan(self: GetNotificationsArgs) -> Nullable[DateTime]

Set: NewerThan(self: GetNotificationsArgs) = value
"""

    NotificationGroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NotificationGroupKey(self: GetNotificationsArgs) -> str

Set: NotificationGroupKey(self: GetNotificationsArgs) = value
"""

    OlderThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OlderThan(self: GetNotificationsArgs) -> Nullable[DateTime]

Set: OlderThan(self: GetNotificationsArgs) = value
"""

    SeverityAtLeast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeverityAtLeast(self: GetNotificationsArgs) -> NotificationSeverity

Set: SeverityAtLeast(self: GetNotificationsArgs) = value
"""

    SortAsc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortAsc(self: GetNotificationsArgs) -> bool

Set: SortAsc(self: GetNotificationsArgs) = value
"""

    SortColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortColumn(self: GetNotificationsArgs) -> GetNotificationsSortOrder

Set: SortColumn(self: GetNotificationsArgs) = value
"""

    StartPerGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPerGroup(self: GetNotificationsArgs) -> Nullable[int]

Set: StartPerGroup(self: GetNotificationsArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserId(self: GetNotificationsArgs) -> Nullable[int]

Set: UserId(self: GetNotificationsArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: GetNotificationsArgs) -> int

Set: ZoneId(self: GetNotificationsArgs) = value
"""



class GetNotificationsSortOrder:
    """ enum GetNotificationsSortOrder, values: Default (0), Importance (1) """
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

    Default = None
    Importance = None
    value__ = None


class HasNotificationsArgs:
    """ HasNotificationsArgs() """
    NewerThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewerThan(self: HasNotificationsArgs) -> Nullable[DateTime]

Set: NewerThan(self: HasNotificationsArgs) = value
"""

    OlderThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OlderThan(self: HasNotificationsArgs) -> Nullable[DateTime]

Set: OlderThan(self: HasNotificationsArgs) = value
"""

    SeverityAtLeast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeverityAtLeast(self: HasNotificationsArgs) -> NotificationSeverity

Set: SeverityAtLeast(self: HasNotificationsArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserId(self: HasNotificationsArgs) -> Nullable[int]

Set: UserId(self: HasNotificationsArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: HasNotificationsArgs) -> int

Set: ZoneId(self: HasNotificationsArgs) = value
"""



class InsertNotificationArgs:
    """ InsertNotificationArgs() """
    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GotoLink(self: InsertNotificationArgs) -> str

Set: GotoLink(self: InsertNotificationArgs) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: InsertNotificationArgs) -> str

Set: GroupKey(self: InsertNotificationArgs) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: InsertNotificationArgs) -> str

Set: Reference(self: InsertNotificationArgs) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Severity(self: InsertNotificationArgs) -> NotificationSeverity

Set: Severity(self: InsertNotificationArgs) = value
"""

    TranslationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslationData(self: InsertNotificationArgs) -> str

Set: TranslationData(self: InsertNotificationArgs) = value
"""

    TranslationKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslationKey(self: InsertNotificationArgs) -> str

Set: TranslationKey(self: InsertNotificationArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: InsertNotificationArgs) -> Nullable[int]

Set: ZoneId(self: InsertNotificationArgs) = value
"""



class Notification:
    """ Notification() """
    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: Notification) -> DateTime

Set: CreatedOn(self: Notification) = value
"""

    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GotoLink(self: Notification) -> str

Set: GotoLink(self: Notification) = value
"""

    GroupGotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupGotoLink(self: Notification) -> str

Set: GroupGotoLink(self: Notification) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: Notification) -> str

Set: GroupKey(self: Notification) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Notification) -> int

Set: Id(self: Notification) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: Notification) -> str

Set: Reference(self: Notification) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Severity(self: Notification) -> NotificationSeverity

Set: Severity(self: Notification) = value
"""

    TotalInGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalInGroup(self: Notification) -> int

Set: TotalInGroup(self: Notification) = value
"""

    TranslationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslationData(self: Notification) -> str

Set: TranslationData(self: Notification) = value
"""

    TranslationKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslationKey(self: Notification) -> str

Set: TranslationKey(self: Notification) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: Notification) -> int

Set: ZoneId(self: Notification) = value
"""



class NotificationGroup:
    """ NotificationGroup() """
    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GotoLink(self: NotificationGroup) -> str

Set: GotoLink(self: NotificationGroup) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: NotificationGroup) -> str

Set: Key(self: NotificationGroup) = value
"""



class NotificationSeverity:
    """ enum NotificationSeverity, values: Critical (10), Informational (0), Warning (5) """
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

    Critical = None
    Informational = None
    value__ = None
    Warning = None


class NotificationSummaryConfiguration:
    """ NotificationSummaryConfiguration() """
    ExecutionConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecutionConfig(self: NotificationSummaryConfiguration) -> Dictionary[str, object]

Set: ExecutionConfig(self: NotificationSummaryConfiguration) = value
"""

    ExecutionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecutionType(self: NotificationSummaryConfiguration) -> str

Set: ExecutionType(self: NotificationSummaryConfiguration) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NotificationSummaryConfiguration) -> int

Set: Id(self: NotificationSummaryConfiguration) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: NotificationSummaryConfiguration) -> bool

Set: IsActive(self: NotificationSummaryConfiguration) = value
"""

    LastTimeExecuted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastTimeExecuted(self: NotificationSummaryConfiguration) -> DateTime

Set: LastTimeExecuted(self: NotificationSummaryConfiguration) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NotificationSummaryConfiguration) -> str

Set: Name(self: NotificationSummaryConfiguration) = value
"""

    NextTimeToExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextTimeToExecute(self: NotificationSummaryConfiguration) -> DateTime

Set: NextTimeToExecute(self: NotificationSummaryConfiguration) = value
"""

    ScheduleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScheduleType(self: NotificationSummaryConfiguration) -> str

Set: ScheduleType(self: NotificationSummaryConfiguration) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserId(self: NotificationSummaryConfiguration) -> int

Set: UserId(self: NotificationSummaryConfiguration) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZoneId(self: NotificationSummaryConfiguration) -> int

Set: ZoneId(self: NotificationSummaryConfiguration) = value
"""




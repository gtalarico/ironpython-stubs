# encoding: utf-8
# module Wms.RemotingObjects.Notifications calls itself Notifications
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddNotificationGroupArgs():
    """
    Model to add a notification group.
    
    AddNotificationGroupArgs()
    """
    Instance = AddNotificationGroupArgs
    """hardcoded/returns an instance of the class"""
    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """optional goto link, user can click on to see origin of notifications from this group

Get: GotoLink(self: AddNotificationGroupArgs) -> str

Set: GotoLink(self: AddNotificationGroupArgs) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Group key under which notifications can be grouped. Linked to Wms.RemotingObjects.Notifications.Notification.GroupKey.

Get: Key(self: AddNotificationGroupArgs) -> str

Set: Key(self: AddNotificationGroupArgs) = value
"""



class DeleteNotificationByReferenceArgs():
    """
    Message to delete notification by Wms.RemotingObjects.Notifications.Notification.Reference.
                The notification creator can define a Wms.RemotingObjects.Notifications.Notification.Reference by which this notification can be deleted.
    
    DeleteNotificationByReferenceArgs()
    """
    Instance = DeleteNotificationByReferenceArgs
    """hardcoded/returns an instance of the class"""
    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """optional filter, will only delete notifications in this group.

Get: GroupKey(self: DeleteNotificationByReferenceArgs) -> str

Set: GroupKey(self: DeleteNotificationByReferenceArgs) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Mandatory reference of the notification(s)

Get: Reference(self: DeleteNotificationByReferenceArgs) -> str

Set: Reference(self: DeleteNotificationByReferenceArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """optional filter, will only delete notifications with this zone.

Get: ZoneId(self: DeleteNotificationByReferenceArgs) -> Nullable[int]

Set: ZoneId(self: DeleteNotificationByReferenceArgs) = value
"""



class DeleteNotificationGroupArgs():
    """
    Model to delete a notification group
    
    DeleteNotificationGroupArgs()
    """
    Instance = DeleteNotificationGroupArgs
    """hardcoded/returns an instance of the class"""
    ForceDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forces delete even when notifications still exist under group.

Get: ForceDelete(self: DeleteNotificationGroupArgs) -> bool

Set: ForceDelete(self: DeleteNotificationGroupArgs) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Group to delete

Get: Key(self: DeleteNotificationGroupArgs) -> str

Set: Key(self: DeleteNotificationGroupArgs) = value
"""



class ExecuteNotificationSummaryArgs():
    """
    Input model for execution of Summary
    
    ExecuteNotificationSummaryArgs()
    """
    Instance = ExecuteNotificationSummaryArgs
    """hardcoded/returns an instance of the class"""
    def TryGetConfiguration(self, key):
        """
        TryGetConfiguration[T](self: ExecuteNotificationSummaryArgs, key: str) -> T
        TryGetConfiguration(self: ExecuteNotificationSummaryArgs, key: str) -> object
        """
        pass

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration saved on the summary generated from the INotificationSummaryExecution.GetConfigurationForm

Get: Configuration(self: ExecuteNotificationSummaryArgs) -> Dictionary[str, object]

Set: Configuration(self: ExecuteNotificationSummaryArgs) = value
"""

    GivenName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name given by user in portal. 
            Might be usefull later for custom reports.

Get: GivenName(self: ExecuteNotificationSummaryArgs) -> str

Set: GivenName(self: ExecuteNotificationSummaryArgs) = value
"""

    LastTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Last time summary was executed

Get: LastTime(self: ExecuteNotificationSummaryArgs) -> DateTime

Set: LastTime(self: ExecuteNotificationSummaryArgs) = value
"""

    ThisTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The datetime this summary was supposed to execute.
            This should be ~ DateTime.Now, but for data consistency you have this value. It could be execution of summary was delayed.

Get: ThisTime(self: ExecuteNotificationSummaryArgs) -> DateTime

Set: ThisTime(self: ExecuteNotificationSummaryArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User where the summary is registered on.

Get: UserId(self: ExecuteNotificationSummaryArgs) -> int

Set: UserId(self: ExecuteNotificationSummaryArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Zone where summary is registered on.

Get: ZoneId(self: ExecuteNotificationSummaryArgs) -> int

Set: ZoneId(self: ExecuteNotificationSummaryArgs) = value
"""



class GetNotificationsArgs():
    """
    Model for requesting notifications INoticationCenter.GetNotifications
    
    GetNotificationsArgs()
    """
    Instance = GetNotificationsArgs
    """hardcoded/returns an instance of the class"""
    LimitPerGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Paging page size per group, amount of notifications to return.

Get: LimitPerGroup(self: GetNotificationsArgs) -> Nullable[int]

Set: LimitPerGroup(self: GetNotificationsArgs) = value
"""

    NewerThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set, only takes notifications that are newer than this value.

Get: NewerThan(self: GetNotificationsArgs) -> Nullable[DateTime]

Set: NewerThan(self: GetNotificationsArgs) = value
"""

    NotificationGroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optionally filter only on

Get: NotificationGroupKey(self: GetNotificationsArgs) -> str

Set: NotificationGroupKey(self: GetNotificationsArgs) = value
"""

    OlderThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set, only takes notifications that are older than this value.

Get: OlderThan(self: GetNotificationsArgs) -> Nullable[DateTime]

Set: OlderThan(self: GetNotificationsArgs) = value
"""

    SeverityAtLeast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sevirty that is filtered in.

Get: SeverityAtLeast(self: GetNotificationsArgs) -> NotificationSeverity

Set: SeverityAtLeast(self: GetNotificationsArgs) = value
"""

    SortAsc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if you want to sort ascending, otherwise descending.
            (counter intuative but most of the time you want newest first, so descending).

Get: SortAsc(self: GetNotificationsArgs) -> bool

Set: SortAsc(self: GetNotificationsArgs) = value
"""

    SortColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the way you want the data to be sorted.

Get: SortColumn(self: GetNotificationsArgs) -> GetNotificationsSortOrder

Set: SortColumn(self: GetNotificationsArgs) = value
"""

    StartPerGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Paging params per group, amount of notifications to skip before return notifications.

Get: StartPerGroup(self: GetNotificationsArgs) -> Nullable[int]

Set: StartPerGroup(self: GetNotificationsArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set filers away notifications seen by this user

Get: UserId(self: GetNotificationsArgs) -> Nullable[int]

Set: UserId(self: GetNotificationsArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notifications in zone.

Get: ZoneId(self: GetNotificationsArgs) -> int

Set: ZoneId(self: GetNotificationsArgs) = value
"""



class GetNotificationsSortOrder:
    """ enum GetNotificationsSortOrder, values: Default (0), Importance (1) """
    Instance = GetNotificationsSortOrder
    """hardcoded/returns an instance of the class"""
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


class HasNotificationsArgs():
    """ HasNotificationsArgs() """
    Instance = HasNotificationsArgs
    """hardcoded/returns an instance of the class"""
    NewerThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set, only takes notifications that are newer than this value.

Get: NewerThan(self: HasNotificationsArgs) -> Nullable[DateTime]

Set: NewerThan(self: HasNotificationsArgs) = value
"""

    OlderThan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set, only takes notifications that are older than this value.

Get: OlderThan(self: HasNotificationsArgs) -> Nullable[DateTime]

Set: OlderThan(self: HasNotificationsArgs) = value
"""

    SeverityAtLeast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sevirty that is filtered in.

Get: SeverityAtLeast(self: HasNotificationsArgs) -> NotificationSeverity

Set: SeverityAtLeast(self: HasNotificationsArgs) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set filers away notifications seen by this user

Get: UserId(self: HasNotificationsArgs) -> Nullable[int]

Set: UserId(self: HasNotificationsArgs) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notifications in zone.

Get: ZoneId(self: HasNotificationsArgs) -> int

Set: ZoneId(self: HasNotificationsArgs) = value
"""



class InsertNotificationArgs():
    """
    Message to insert Wms.RemotingObjects.Notifications.Notification in the notificatoin center
    
    InsertNotificationArgs()
    """
    Instance = InsertNotificationArgs
    """hardcoded/returns an instance of the class"""
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



class Notification():
    """
    Base model for notifications as external sources see notification.
                
                Internally notification might have more properties.
    
    Notification()
    """
    Instance = Notification
    """hardcoded/returns an instance of the class"""
    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time the issue was created.

Get: CreatedOn(self: Notification) -> DateTime

Set: CreatedOn(self: Notification) = value
"""

    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Link where user can see where the notification originated from.

Get: GotoLink(self: Notification) -> str

Set: GotoLink(self: Notification) = value
"""

    GroupGotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Goto link users can click on on the group.

Get: GroupGotoLink(self: Notification) -> str

Set: GroupGotoLink(self: Notification) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to Notification group

Get: GroupKey(self: Notification) -> str

Set: GroupKey(self: Notification) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Generated Id by notificationcenter (actulaly db) for the notification.

Get: Id(self: Notification) -> int

Set: Id(self: Notification) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference generated by creator of the notification.
            Can be used to later delete the notification by creator.

Get: Reference(self: Notification) -> str

Set: Reference(self: Notification) = value
"""

    Severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of severity of this message.

Get: Severity(self: Notification) -> NotificationSeverity

Set: Severity(self: Notification) = value
"""

    TotalInGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Amount of notifications in group

Get: TotalInGroup(self: Notification) -> int

Set: TotalInGroup(self: Notification) = value
"""

    TranslationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data that is formatted into the message.
            It is used as: string.Format(Translations[TranslationKey], TranslationData);.

Get: TranslationData(self: Notification) -> str

Set: TranslationData(self: Notification) = value
"""

    TranslationKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Key for translation of the message.
            It is used as: string.Format(Translations[TranslationKey], TranslationData);.

Get: TranslationKey(self: Notification) -> str

Set: TranslationKey(self: Notification) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For which zone the notification is for.

Get: ZoneId(self: Notification) -> int

Set: ZoneId(self: Notification) = value
"""



class NotificationGroup():
    """
    Return model for getting notification groups
    
    NotificationGroup()
    """
    Instance = NotificationGroup
    """hardcoded/returns an instance of the class"""
    GotoLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional goto link for notification group

Get: GotoLink(self: NotificationGroup) -> str

Set: GotoLink(self: NotificationGroup) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique key for this notificationGroup

Get: Key(self: NotificationGroup) -> str

Set: Key(self: NotificationGroup) = value
"""



class NotificationSeverity:
    """
    Defines the intensity/importance of the notification.
    
    enum NotificationSeverity, values: Critical (10), Informational (0), Warning (5)
    """
    Instance = NotificationSeverity
    """hardcoded/returns an instance of the class"""
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


class NotificationSummaryConfiguration():
    """
    Notification summary configuration model.
                Its like a planned schedule to execute a INotificationSummaryExecution at the planned  times.
    
    NotificationSummaryConfiguration()
    """
    Instance = NotificationSummaryConfiguration
    """hardcoded/returns an instance of the class"""
    ExecutionConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dynamic (json) dictionary of options used by INotificationSummaryExecution.ExecuteSummary.
            Also see Wms.RemotingObjects.Notifications.ExecuteNotificationSummaryArgs.Configuration.

Get: ExecutionConfig(self: NotificationSummaryConfiguration) -> Dictionary[str, object]

Set: ExecutionConfig(self: NotificationSummaryConfiguration) = value
"""

    ExecutionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Resolver key of the INotificationSummaryExecution.

Get: ExecutionType(self: NotificationSummaryConfiguration) -> str

Set: ExecutionType(self: NotificationSummaryConfiguration) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the configuration.
            
            If id is zero it has not yet been saved in database and will be inserted in database when saved.

Get: Id(self: NotificationSummaryConfiguration) -> int

Set: Id(self: NotificationSummaryConfiguration) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wether or not configuration should be executed.
            If false configuration will not be executed and datetime wont be updated.

Get: IsActive(self: NotificationSummaryConfiguration) -> bool

Set: IsActive(self: NotificationSummaryConfiguration) = value
"""

    LastTimeExecuted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """From where should the first execution take as period.

Get: LastTimeExecuted(self: NotificationSummaryConfiguration) -> DateTime

Set: LastTimeExecuted(self: NotificationSummaryConfiguration) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name given by user for this configuration

Get: Name(self: NotificationSummaryConfiguration) -> str

Set: Name(self: NotificationSummaryConfiguration) = value
"""

    NextTimeToExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """First time schedule should execute.

Get: NextTimeToExecute(self: NotificationSummaryConfiguration) -> DateTime

Set: NextTimeToExecute(self: NotificationSummaryConfiguration) = value
"""

    ScheduleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Resolver key of the INotificationSummarySchedule.

Get: ScheduleType(self: NotificationSummaryConfiguration) -> str

Set: ScheduleType(self: NotificationSummaryConfiguration) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User linked to the NotificationSummary.

Get: UserId(self: NotificationSummaryConfiguration) -> int

Set: UserId(self: NotificationSummaryConfiguration) = value
"""

    ZoneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Zone linked to the NotificationSummary.

Get: ZoneId(self: NotificationSummaryConfiguration) -> int

Set: ZoneId(self: NotificationSummaryConfiguration) = value
"""




class EntryWrittenEventArgs(EventArgs):
    """
    Provides data for the System.Diagnostics.EventLog.EntryWritten event.
    
    EntryWrittenEventArgs()
    EntryWrittenEventArgs(entry: EventLogEntry)
    """
    @staticmethod # known case of __new__
    def __new__(self, entry=None):
        """
        __new__(cls: type)
        __new__(cls: type, entry: EventLogEntry)
        """
        pass

    Entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the event log entry that was written to the log.

Get: Entry(self: EntryWrittenEventArgs) -> EventLogEntry

"""



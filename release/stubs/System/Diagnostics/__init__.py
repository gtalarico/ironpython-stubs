# encoding: utf-8
# module System.Diagnostics calls itself Diagnostics
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Switch(object):
    """ Provides an abstract base class to create new debugging and tracing switches. """
    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: Switch) -> Array[str]
        
            Gets the custom attributes supported by the switch.
            Returns: A string array that contains the names of the custom attributes supported by the switch, or null 
             if there no custom attributes are supported.
        """
        pass

    def OnSwitchSettingChanged(self, *args): #cannot find CLR method
        """
        OnSwitchSettingChanged(self: Switch)
            Invoked when the System.Diagnostics.Switch.SwitchSetting property is changed.
        """
        pass

    def OnValueChanged(self, *args): #cannot find CLR method
        """
        OnValueChanged(self: Switch)
            Invoked when the System.Diagnostics.Switch.Value property is changed.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, defaultSwitchValue: str)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom switch attributes defined in the application configuration file.

Get: Attributes(self: Switch) -> StringDictionary

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a description of the switch.

Get: Description(self: Switch) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name used to identify the switch.

Get: DisplayName(self: Switch) -> str

"""

    SwitchSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current setting for this switch.

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the switch.

"""



class BooleanSwitch(Switch):
    """
    Provides a simple on/off switch that controls debugging and tracing output.
    
    BooleanSwitch(displayName: str, description: str)
    BooleanSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, displayName, description, defaultSwitchValue=None):
        """
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, defaultSwitchValue: str)
        """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the switch is enabled or disabled.

Get: Enabled(self: BooleanSwitch) -> bool

Set: Enabled(self: BooleanSwitch) = value
"""

    SwitchSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current setting for this switch.

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the switch.

"""



class ConditionalAttribute(Attribute, _Attribute):
    """
    Indicates to compilers that a method call or attribute should be ignored unless a specified conditional compilation symbol is defined.
    
    ConditionalAttribute(conditionString: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, conditionString):
        """ __new__(cls: type, conditionString: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ConditionString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the conditional compilation symbol that is associated with the System.Diagnostics.ConditionalAttribute attribute.

Get: ConditionString(self: ConditionalAttribute) -> str

"""



class TraceListener(MarshalByRefObject, IDisposable):
    """ Provides the abstract base class for the listeners who monitor trace and debug output. """
    def Close(self):
        """
        Close(self: TraceListener)
            When overridden in a derived class, closes the output stream so it no longer receives tracing or 
             debugging output.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TraceListener)
            Releases all resources used by the System.Diagnostics.TraceListener.
        """
        pass

    def Fail(self, message, detailMessage=None):
        """
        Fail(self: TraceListener, message: str, detailMessage: str)
            Emits an error message and a detailed error message to the listener you create when you 
             implement the System.Diagnostics.TraceListener class.
        
        
            message: A message to emit.
            detailMessage: A detailed message to emit.
        Fail(self: TraceListener, message: str)
            Emits an error message to the listener you create when you implement the 
             System.Diagnostics.TraceListener class.
        
        
            message: A message to emit.
        """
        pass

    def Flush(self):
        """
        Flush(self: TraceListener)
            When overridden in a derived class, flushes the output buffer.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])
            Writes trace information, an array of data objects and event information to the listener 
             specific output.
        
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            data: An array of objects to emit as data.
        TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)
            Writes trace information, a data object and event information to the listener specific output.
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            data: The trace data to emit.
        """
        pass

    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])
            Writes trace information, a formatted array of objects and event information to the listener 
             specific output.
        
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            format: A format string that contains zero or more format items, which correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)
            Writes trace information, a message, and event information to the listener specific output.
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            message: A message to write.
        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int)
            Writes trace and event information to the listener specific output.
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
        """
        pass

    def TraceTransfer(self, eventCache, source, id, message, relatedActivityId):
        """
        TraceTransfer(self: TraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid)
            Writes trace information, a message, a related activity identity and event information to the 
             listener specific output.
        
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            id: A numeric identifier for the event.
            message: A message to write.
            relatedActivityId: A System.Guid  object identifying a related activity.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: TraceListener, message: str, category: str)
            Writes a category name and a message to the listener you create when you implement the 
             System.Diagnostics.TraceListener class.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        Write(self: TraceListener, o: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the 
             listener you create when you implement the System.Diagnostics.TraceListener class.
        
        
            o: An System.Object whose fully qualified class name you want to write.
            category: A category name used to organize the output.
        Write(self: TraceListener, message: str)
            When overridden in a derived class, writes the specified message to the listener you create in 
             the derived class.
        
        
            message: A message to write.
        Write(self: TraceListener, o: object)
            Writes the value of the object's System.Object.ToString method to the listener you create when 
             you implement the System.Diagnostics.TraceListener class.
        
        
            o: An System.Object whose fully qualified class name you want to write.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: TraceListener, message: str, category: str)
            Writes a category name and a message to the listener you create when you implement the 
             System.Diagnostics.TraceListener class, followed by a line terminator.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        WriteLine(self: TraceListener, o: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the 
             listener you create when you implement the System.Diagnostics.TraceListener class, followed by a 
             line terminator.
        
        
            o: An System.Object whose fully qualified class name you want to write.
            category: A category name used to organize the output.
        WriteLine(self: TraceListener, message: str)
            When overridden in a derived class, writes a message to the listener you create in the derived 
             class, followed by a line terminator.
        
        
            message: A message to write.
        WriteLine(self: TraceListener, o: object)
            Writes the value of the object's System.Object.ToString method to the listener you create when 
             you implement the System.Diagnostics.TraceListener class, followed by a line terminator.
        
        
            o: An System.Object whose fully qualified class name you want to write.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom trace listener attributes defined in the application configuration file.

Get: Attributes(self: TraceListener) -> StringDictionary

"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the trace filter for the trace listener.

Get: Filter(self: TraceListener) -> TraceFilter

Set: Filter(self: TraceListener) = value
"""

    IndentLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the indent level.

Get: IndentLevel(self: TraceListener) -> int

Set: IndentLevel(self: TraceListener) = value
"""

    IndentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of spaces in an indent.

Get: IndentSize(self: TraceListener) -> int

Set: IndentSize(self: TraceListener) = value
"""

    IsThreadSafe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the trace listener is thread safe.

Get: IsThreadSafe(self: TraceListener) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a name for this System.Diagnostics.TraceListener.

Get: Name(self: TraceListener) -> str

Set: Name(self: TraceListener) = value
"""

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""

    TraceOutputOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the trace output options.

Get: TraceOutputOptions(self: TraceListener) -> TraceOptions

Set: TraceOutputOptions(self: TraceListener) = value
"""



class TextWriterTraceListener(TraceListener, IDisposable):
    """
    Directs tracing or debugging output to a System.IO.TextWriter or to a System.IO.Stream, such as System.IO.FileStream.
    
    TextWriterTraceListener()
    TextWriterTraceListener(stream: Stream)
    TextWriterTraceListener(stream: Stream, name: str)
    TextWriterTraceListener(writer: TextWriter)
    TextWriterTraceListener(writer: TextWriter, name: str)
    TextWriterTraceListener(fileName: str)
    TextWriterTraceListener(fileName: str, name: str)
    """
    def Close(self):
        """
        Close(self: TextWriterTraceListener)
            Closes the System.Diagnostics.TextWriterTraceListener.Writer so that it no longer receives 
             tracing or debugging output.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextWriterTraceListener, disposing: bool)
            Disposes this System.Diagnostics.TextWriterTraceListener object.
        
            disposing: true to release managed resources; if false, 
             System.Diagnostics.TextWriterTraceListener.Dispose(System.Boolean) has no effect.
        """
        pass

    def Flush(self):
        """
        Flush(self: TextWriterTraceListener)
            Flushes the output buffer for the System.Diagnostics.TextWriterTraceListener.Writer.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: TextWriterTraceListener, message: str)
            Writes a message to this instance's System.Diagnostics.TextWriterTraceListener.Writer.
        
            message: A message to write.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: TextWriterTraceListener, message: str)
            Writes a message to this instance's System.Diagnostics.TextWriterTraceListener.Writer followed 
             by a line terminator. The default line terminator is a carriage return followed by a line feed 
             (\r\n).
        
        
            message: A message to write.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, name: str)
        __new__(cls: type, writer: TextWriter)
        __new__(cls: type, writer: TextWriter, name: str)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, name: str)
        """
        pass

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""

    Writer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text writer that receives the tracing or debugging output.

Get: Writer(self: TextWriterTraceListener) -> TextWriter

Set: Writer(self: TextWriterTraceListener) = value
"""



class ConsoleTraceListener(TextWriterTraceListener, IDisposable):
    """
    Directs tracing or debugging output to either the standard output or the standard error stream.
    
    ConsoleTraceListener()
    ConsoleTraceListener(useErrorStream: bool)
    """
    def Close(self):
        """
        Close(self: ConsoleTraceListener)
            Closes the output to the stream specified for this trace listener.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextWriterTraceListener, disposing: bool)
            Disposes this System.Diagnostics.TextWriterTraceListener object.
        
            disposing: true to release managed resources; if false, 
             System.Diagnostics.TextWriterTraceListener.Dispose(System.Boolean) has no effect.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, useErrorStream=None):
        """
        __new__(cls: type)
        __new__(cls: type, useErrorStream: bool)
        """
        pass

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""



class CorrelationManager(object):
    """ Correlates traces that are part of a logical transaction. """
    def StartLogicalOperation(self, operationId=None):
        """
        StartLogicalOperation(self: CorrelationManager)
            Starts a logical operation on a thread.
        StartLogicalOperation(self: CorrelationManager, operationId: object)
            Starts a logical operation with the specified identity on a thread.
        
            operationId: An object identifying the operation.
        """
        pass

    def StopLogicalOperation(self):
        """
        StopLogicalOperation(self: CorrelationManager)
            Stops the current logical operation.
        """
        pass

    ActivityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the identity for a global activity.

Get: ActivityId(self: CorrelationManager) -> Guid

Set: ActivityId(self: CorrelationManager) = value
"""

    LogicalOperationStack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical operation stack from the call context.

Get: LogicalOperationStack(self: CorrelationManager) -> Stack

"""



class CounterCreationData(object):
    """
    Defines the counter type, name, and Help string for a custom counter.
    
    CounterCreationData(counterName: str, counterHelp: str, counterType: PerformanceCounterType)
    CounterCreationData()
    """
    @staticmethod # known case of __new__
    def __new__(self, counterName=None, counterHelp=None, counterType=None):
        """
        __new__(cls: type)
        __new__(cls: type, counterName: str, counterHelp: str, counterType: PerformanceCounterType)
        """
        pass

    CounterHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the custom counter's description.

Get: CounterHelp(self: CounterCreationData) -> str

Set: CounterHelp(self: CounterCreationData) = value
"""

    CounterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the custom counter.

Get: CounterName(self: CounterCreationData) -> str

Set: CounterName(self: CounterCreationData) = value
"""

    CounterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the performance counter type of the custom counter.

Get: CounterType(self: CounterCreationData) -> PerformanceCounterType

Set: CounterType(self: CounterCreationData) = value
"""



class CounterCreationDataCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.CounterCreationData objects.
    
    CounterCreationDataCollection()
    CounterCreationDataCollection(value: CounterCreationDataCollection)
    CounterCreationDataCollection(value: Array[CounterCreationData])
    """
    def Add(self, value):
        """
        Add(self: CounterCreationDataCollection, value: CounterCreationData) -> int
        
            Adds an instance of the System.Diagnostics.CounterCreationData class to the collection.
        
            value: A System.Diagnostics.CounterCreationData object to append to the existing collection.
            Returns: The index of the new System.Diagnostics.CounterCreationData object.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CounterCreationDataCollection, value: CounterCreationDataCollection)
            Adds the specified collection of System.Diagnostics.CounterCreationData instances to the 
             collection.
        
        
            value: A collection of System.Diagnostics.CounterCreationData instances to append to the existing 
             collection.
        
        AddRange(self: CounterCreationDataCollection, value: Array[CounterCreationData])
            Adds the specified array of System.Diagnostics.CounterCreationData instances to the collection.
        
            value: An array of System.Diagnostics.CounterCreationData instances to append to the existing 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CounterCreationDataCollection, value: CounterCreationData) -> bool
        
            Determines whether a System.Diagnostics.CounterCreationData instance exists in the collection.
        
            value: The System.Diagnostics.CounterCreationData object to find in the collection.
            Returns: true if the specified System.Diagnostics.CounterCreationData object exists in the collection; 
             otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CounterCreationDataCollection, array: Array[CounterCreationData], index: int)
            Copies the elements of the System.Diagnostics.CounterCreationData to an array, starting at the 
             specified index of the array.
        
        
            array: An array of System.Diagnostics.CounterCreationData instances to add to the collection.
            index: The location at which to add the new instances.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CounterCreationDataCollection, value: CounterCreationData) -> int
        
            Returns the index of a System.Diagnostics.CounterCreationData object in the collection.
        
            value: The System.Diagnostics.CounterCreationData object to locate in the collection.
            Returns: The zero-based index of the specified System.Diagnostics.CounterCreationData, if it is found, in 
             the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CounterCreationDataCollection, index: int, value: CounterCreationData)
            Inserts a System.Diagnostics.CounterCreationData object into the collection, at the specified 
             index.
        
        
            index: The zero-based index of the location at which the System.Diagnostics.CounterCreationData is to 
             be inserted.
        
            value: The System.Diagnostics.CounterCreationData to insert into the collection.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CounterCreationDataCollection, value: object)
            Checks the specified object to determine whether it is a valid 
             System.Diagnostics.CounterCreationData type.
        
        
            value: The object that will be validated.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: CounterCreationDataCollection, value: CounterCreationData)
            Removes a System.Diagnostics.CounterCreationData object from the collection.
        
            value: The System.Diagnostics.CounterCreationData to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: CounterCreationDataCollection)
        __new__(cls: type, value: Array[CounterCreationData])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CounterSample(object):
    """
    Defines a structure that holds the raw data for a performance counter.
    
    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType)
    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType, counterTimeStamp: Int64)
    """
    @staticmethod
    def Calculate(counterSample, nextCounterSample=None):
        """
        Calculate(counterSample: CounterSample, nextCounterSample: CounterSample) -> Single
        
            Calculates the performance data of the counter, using two sample points. This method is 
             generally used for calculated performance counter types, such as averages.
        
        
            counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating 
             performance data.
        
            nextCounterSample: The System.Diagnostics.CounterSample structure to use as an ending point for calculating 
             performance data.
        
            Returns: The calculated performance value.
        Calculate(counterSample: CounterSample) -> Single
        
            Calculates the performance data of the counter, using a single sample point. This method is 
             generally used for uncalculated performance counter types.
        
        
            counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating 
             performance data.
        
            Returns: The calculated performance value.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: CounterSample, sample: CounterSample) -> bool
        
            Indicates whether the specified System.Diagnostics.CounterSample structure is equal to the 
             current System.Diagnostics.CounterSample structure.
        
        
            sample: The System.Diagnostics.CounterSample structure to be compared with this instance.
            Returns: true if sample is equal to the current instance; otherwise, false.
        Equals(self: CounterSample, o: object) -> bool
        
            Indicates whether the specified structure is a System.Diagnostics.CounterSample structure and is 
             identical to the current System.Diagnostics.CounterSample structure.
        
        
            o: The System.Diagnostics.CounterSample structure to be compared with the current structure.
            Returns: true if o is a System.Diagnostics.CounterSample structure and is identical to the current 
             instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CounterSample) -> int
        
            Gets a hash code for the current counter sample.
            Returns: A hash code for the current counter sample.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rawValue, baseValue, counterFrequency, systemFrequency, timeStamp, timeStamp100nSec, counterType, counterTimeStamp=None):
        """
        __new__[CounterSample]() -> CounterSample
        
        __new__(cls: type, rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType)
        __new__(cls: type, rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType, counterTimeStamp: Int64)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BaseValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an optional, base raw value for the counter.

Get: BaseValue(self: CounterSample) -> Int64

"""

    CounterFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw counter frequency.

Get: CounterFrequency(self: CounterSample) -> Int64

"""

    CounterTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the counter's time stamp.

Get: CounterTimeStamp(self: CounterSample) -> Int64

"""

    CounterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the performance counter type.

Get: CounterType(self: CounterSample) -> PerformanceCounterType

"""

    RawValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw value of the counter.

Get: RawValue(self: CounterSample) -> Int64

"""

    SystemFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw system frequency.

Get: SystemFrequency(self: CounterSample) -> Int64

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw time stamp.

Get: TimeStamp(self: CounterSample) -> Int64

"""

    TimeStamp100nSec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw, high-fidelity time stamp.

Get: TimeStamp100nSec(self: CounterSample) -> Int64

"""


    Empty = None


class CounterSampleCalculator(object):
    """ Provides a set of utility functions for interpreting performance counter data. """
    @staticmethod
    def ComputeCounterValue(*__args):
        """
        ComputeCounterValue(oldSample: CounterSample, newSample: CounterSample) -> Single
        
            Computes the calculated value of two raw counter samples.
        
            oldSample: A System.Diagnostics.CounterSample that indicates a previous sample the system has taken.
            newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.
            Returns: A floating-point representation of the performance counter's calculated value.
        ComputeCounterValue(newSample: CounterSample) -> Single
        
            Computes the calculated value of a single raw counter sample.
        
            newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.
            Returns: A floating-point representation of the performance counter's calculated value.
        """
        pass

    __all__ = [
        'ComputeCounterValue',
    ]


class DataReceivedEventArgs(EventArgs):
    """ Provides data for the System.Diagnostics.Process.OutputDataReceived and System.Diagnostics.Process.ErrorDataReceived events. """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line of characters that was written to a redirected System.Diagnostics.Process output stream.

Get: Data(self: DataReceivedEventArgs) -> str

"""



class DataReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Diagnostics.Process.OutputDataReceived event or System.Diagnostics.Process.ErrorDataReceived event of a System.Diagnostics.Process.
    
    DataReceivedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DataReceivedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Debug(object):
    """ Provides a set of methods and properties that help debug your code. This class cannot be inherited. """
    @staticmethod
    def Assert(condition, message=None, *__args):
        """
        Assert(condition: bool, message: str, detailMessage: str)
            Checks for a condition; if the condition is false, outputs two specified messages and displays a 
             message box that shows the call stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the specified messages are not 
             sent and the message box is not displayed.
        
            message: The message to send to the System.Diagnostics.Trace.Listeners collection.
            detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.
        Assert(condition: bool, message: str, detailMessageFormat: str, *args: Array[object])
            Checks for a condition; if the condition is false, outputs two messages (simple and formatted) 
             and displays a message box that shows the call stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the specified messages are not 
             sent and the message box is not displayed.
        
            message: The message to send to the System.Diagnostics.Trace.Listeners collection.
            detailMessageFormat: The composite format string (see Remarks) to send to the System.Diagnostics.Trace.Listeners 
             collection. This message contains text intermixed with zero or more format items, which 
             correspond to objects in the args array.
        
            args: An object array that contains zero or more objects to format.
        Assert(condition: bool)
            Checks for a condition; if the condition is false, displays a message box that shows the call 
             stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, a failure message is not sent 
             and the message box is not displayed.
        
        Assert(condition: bool, message: str)
            Checks for a condition; if the condition is false, outputs a specified message and displays a 
             message box that shows the call stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the specified message is not 
             sent and the message box is not displayed.
        
            message: The message to send to the System.Diagnostics.Trace.Listeners collection.
        """
        pass

    @staticmethod
    def Close():
        """
        Close()
            Flushes the output buffer and then calls the Close method on each of the 
             System.Diagnostics.Debug.Listeners.
        """
        pass

    @staticmethod
    def Fail(message, detailMessage=None):
        """
        Fail(message: str, detailMessage: str)
            Emits an error message and a detailed error message.
        
            message: A message to emit.
            detailMessage: A detailed message to emit.
        Fail(message: str)
            Emits the specified error message.
        
            message: A message to emit.
        """
        pass

    @staticmethod
    def Flush():
        """
        Flush()
            Flushes the output buffer and causes buffered data to write to the 
             System.Diagnostics.Debug.Listeners collection.
        """
        pass

    @staticmethod
    def Indent():
        """
        Indent()
            Increases the current System.Diagnostics.Debug.IndentLevel by one.
        """
        pass

    @staticmethod
    def Print(*__args):
        """
        Print(format: str, *args: Array[object])
            Writes a formatted string followed by a line terminator to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            format: A composite format string (see Remarks) that contains text intermixed with zero or more format 
             items, which correspond to objects in the args array.
        
            args: An object array containing zero or more objects to format.
        Print(message: str)
            Writes a message followed by a line terminator to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            message: The message to write.
        """
        pass

    @staticmethod
    def Unindent():
        """
        Unindent()
            Decreases the current System.Diagnostics.Debug.IndentLevel by one.
        """
        pass

    @staticmethod
    def Write(*__args):
        """
        Write(message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        Write(value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Debug.Listeners collection.
        
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
            category: A category name used to organize the output.
        Write(message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection.
        
            message: A message to write.
        Write(value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
        """
        pass

    @staticmethod
    def WriteIf(condition, *__args):
        """
        WriteIf(condition: bool, message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the category name and message 
             are written to the trace listeners in the collection.
        
            message: A message to write.
            category: A category name used to organize the output.
        WriteIf(condition: bool, value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the category name and value 
             are written to the trace listeners in the collection.
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
            category: A category name used to organize the output.
        WriteIf(condition: bool, message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if 
             a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the message is written to the 
             trace listeners in the collection.
        
            message: A message to write.
        WriteIf(condition: bool, value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the value is written to the 
             trace listeners in the collection.
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
        """
        pass

    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine(value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Debug.Listeners collection.
        
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
            category: A category name used to organize the output.
        WriteLine(format: str, *args: Array[object])
            Writes a formatted message followed by a line terminator to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            format: A composite format string (see Remarks) that contains text intermixed with zero or more format 
             items, which correspond to objects in the args array.
        
            args: An object array containing zero or more objects to format.
        WriteLine(message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        WriteLine(message: str)
            Writes a message followed by a line terminator to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            message: A message to write.
        WriteLine(value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection.
        
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
        """
        pass

    @staticmethod
    def WriteLineIf(condition, *__args):
        """
        WriteLineIf(condition: bool, message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            message: A message to write.
            category: A category name used to organize the output.
        WriteLineIf(condition: bool, value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the category name and value 
             are written to the trace listeners in the collection.
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
            category: A category name used to organize the output.
        WriteLineIf(condition: bool, message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if 
             a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the message is written to the 
             trace listeners in the collection.
        
            message: A message to write.
        WriteLineIf(condition: bool, value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Debug.Listeners collection if a condition is true.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the value is written to the 
             trace listeners in the collection.
        
            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
        """
        pass

    AutoFlush = False
    IndentLevel = 0
    IndentSize = 4
    Listeners = None
    __all__ = [
        'Assert',
        'Close',
        'Fail',
        'Flush',
        'Indent',
        'Print',
        'Unindent',
        'Write',
        'WriteIf',
        'WriteLine',
        'WriteLineIf',
    ]


class DebuggableAttribute(Attribute, _Attribute):
    """
    Modifies code generation for runtime just-in-time (JIT) debugging. This class cannot be inherited.
    
    DebuggableAttribute(isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)
    DebuggableAttribute(modes: DebuggingModes)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)
        __new__(cls: type, modes: DebuggingModes)
        """
        pass

    DebuggingFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the debugging modes for the attribute.

Get: DebuggingFlags(self: DebuggableAttribute) -> DebuggingModes

"""

    IsJITOptimizerDisabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the runtime optimizer is disabled.

Get: IsJITOptimizerDisabled(self: DebuggableAttribute) -> bool

"""

    IsJITTrackingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the runtime will track information during code generation for the debugger.

Get: IsJITTrackingEnabled(self: DebuggableAttribute) -> bool

"""


    DebuggingModes = None


class Debugger(object):
    """
    Enables communication with a debugger. This class cannot be inherited.
    
    Debugger()
    """
    @staticmethod
    def Break():
        """
        Break()
            Signals a breakpoint to an attached debugger.
        """
        pass

    @staticmethod
    def IsLogging():
        """
        IsLogging() -> bool
        
            Checks to see if logging is enabled by an attached debugger.
            Returns: true if a debugger is attached and logging is enabled; otherwise, false. The attached debugger 
             is the registered managed debugger in the DbgManagedDebugger registry key. For more information 
             on this key, see Enabling JIT-Attach Debugging.
        """
        pass

    @staticmethod
    def Launch():
        """
        Launch() -> bool
        
            Launches and attaches a debugger to the process.
            Returns: true if the startup is successful or if the debugger is already attached; otherwise, false.
        """
        pass

    @staticmethod
    def Log(level, category, message):
        """
        Log(level: int, category: str, message: str)
            Posts a message for the attached debugger.
        
            level: A description of the importance of the message.
            category: The category of the message.
            message: The message to show.
        """
        pass

    @staticmethod
    def NotifyOfCrossThreadDependency():
        """
        NotifyOfCrossThreadDependency()
            Notifies a debugger that execution is about to enter a path that involves a cross-thread 
             dependency.
        """
        pass

    DefaultCategory = None
    IsAttached = False


class DebuggerBrowsableAttribute(Attribute, _Attribute):
    """
    Determines if and how a member is displayed in the debugger variable windows. This class cannot be inherited.
    
    DebuggerBrowsableAttribute(state: DebuggerBrowsableState)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state):
        """ __new__(cls: type, state: DebuggerBrowsableState) """
        pass

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display state for the attribute.

Get: State(self: DebuggerBrowsableAttribute) -> DebuggerBrowsableState

"""



class DebuggerBrowsableState(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides display instructions for the debugger.
    
    enum DebuggerBrowsableState, values: Collapsed (2), Never (0), RootHidden (3)
    """
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

    Collapsed = None
    Never = None
    RootHidden = None
    value__ = None


class DebuggerDisplayAttribute(Attribute, _Attribute):
    """
    Determines how a class or field is displayed in the debugger variable windows.
    
    DebuggerDisplayAttribute(value: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name to display in the debugger variable windows.

Get: Name(self: DebuggerDisplayAttribute) -> str

Set: Name(self: DebuggerDisplayAttribute) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the attribute's target.

Get: Target(self: DebuggerDisplayAttribute) -> Type

Set: Target(self: DebuggerDisplayAttribute) = value
"""

    TargetTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type name of the attribute's target.

Get: TargetTypeName(self: DebuggerDisplayAttribute) -> str

Set: TargetTypeName(self: DebuggerDisplayAttribute) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string to display in the type column of the debugger variable windows.

Get: Type(self: DebuggerDisplayAttribute) -> str

Set: Type(self: DebuggerDisplayAttribute) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the string to display in the value column of the debugger variable windows.

Get: Value(self: DebuggerDisplayAttribute) -> str

"""



class DebuggerHiddenAttribute(Attribute, _Attribute):
    """
    Specifies the System.Diagnostics.DebuggerHiddenAttribute. This class cannot be inherited.
    
    DebuggerHiddenAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DebuggerNonUserCodeAttribute(Attribute, _Attribute):
    """
    Identifies a type or member that is not part of the user code for an application.
    
    DebuggerNonUserCodeAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DebuggerStepperBoundaryAttribute(Attribute, _Attribute):
    """
    Indicates the code following the attribute is to be executed in run, not step, mode.
    
    DebuggerStepperBoundaryAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DebuggerStepThroughAttribute(Attribute, _Attribute):
    """
    Instructs the debugger to step through the code instead of stepping into the code. This class cannot be inherited.
    
    DebuggerStepThroughAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DebuggerTypeProxyAttribute(Attribute, _Attribute):
    """
    Specifies the display proxy for a type.
    
    DebuggerTypeProxyAttribute(type: Type)
    DebuggerTypeProxyAttribute(typeName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        pass

    ProxyTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name of the proxy type.

Get: ProxyTypeName(self: DebuggerTypeProxyAttribute) -> str

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target type for the attribute.

Get: Target(self: DebuggerTypeProxyAttribute) -> Type

Set: Target(self: DebuggerTypeProxyAttribute) = value
"""

    TargetTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the target type.

Get: TargetTypeName(self: DebuggerTypeProxyAttribute) -> str

Set: TargetTypeName(self: DebuggerTypeProxyAttribute) = value
"""



class DebuggerVisualizerAttribute(Attribute, _Attribute):
    """
    Specifies that the type has a visualizer. This class cannot be inherited.
    
    DebuggerVisualizerAttribute(visualizerTypeName: str)
    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSourceTypeName: str)
    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSource: Type)
    DebuggerVisualizerAttribute(visualizer: Type)
    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSource: Type)
    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSourceTypeName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, visualizerTypeName: str)
        __new__(cls: type, visualizerTypeName: str, visualizerObjectSourceTypeName: str)
        __new__(cls: type, visualizerTypeName: str, visualizerObjectSource: Type)
        __new__(cls: type, visualizer: Type)
        __new__(cls: type, visualizer: Type, visualizerObjectSource: Type)
        __new__(cls: type, visualizer: Type, visualizerObjectSourceTypeName: str)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the description of the visualizer.

Get: Description(self: DebuggerVisualizerAttribute) -> str

Set: Description(self: DebuggerVisualizerAttribute) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target type when the attribute is applied at the assembly level.

Get: Target(self: DebuggerVisualizerAttribute) -> Type

Set: Target(self: DebuggerVisualizerAttribute) = value
"""

    TargetTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the fully qualified type name when the attribute is applied at the assembly level.

Get: TargetTypeName(self: DebuggerVisualizerAttribute) -> str

Set: TargetTypeName(self: DebuggerVisualizerAttribute) = value
"""

    VisualizerObjectSourceTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualified type name of the visualizer object source.

Get: VisualizerObjectSourceTypeName(self: DebuggerVisualizerAttribute) -> str

"""

    VisualizerTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualified type name of the visualizer.

Get: VisualizerTypeName(self: DebuggerVisualizerAttribute) -> str

"""



class DefaultTraceListener(TraceListener, IDisposable):
    """
    Provides the default output methods and behavior for tracing.
    
    DefaultTraceListener()
    """
    def Dispose(self):
        """
        Dispose(self: TraceListener, disposing: bool)
            Releases the unmanaged resources used by the System.Diagnostics.TraceListener and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Fail(self, message, detailMessage=None):
        """
        Fail(self: DefaultTraceListener, message: str, detailMessage: str)
            Emits or displays detailed messages and a stack trace for an assertion that always fails.
        
            message: The message to emit or display.
            detailMessage: The detailed message to emit or display.
        Fail(self: DefaultTraceListener, message: str)
            Emits or displays a message and a stack trace for an assertion that always fails.
        
            message: The message to emit or display.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: DefaultTraceListener, message: str)
            Writes the output to the OutputDebugString function and to the 
             System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String) method.
        
        
            message: The message to write to OutputDebugString and 
             System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String).
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: DefaultTraceListener, message: str)
            Writes the output to the OutputDebugString function and to the 
             System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String) method, followed by a 
             carriage return and line feed (\r\n).
        
        
            message: The message to write to OutputDebugString and 
             System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String).
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AssertUiEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the application is running in user-interface mode.

Get: AssertUiEnabled(self: DefaultTraceListener) -> bool

Set: AssertUiEnabled(self: DefaultTraceListener) = value
"""

    LogFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of a log file to write trace or debug messages to.

Get: LogFileName(self: DefaultTraceListener) -> str

Set: LogFileName(self: DefaultTraceListener) = value
"""

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""



class DelimitedListTraceListener(TextWriterTraceListener, IDisposable):
    """
    Directs tracing or debugging output to a text writer, such as a stream writer, or to a stream, such as a file stream.
    
    DelimitedListTraceListener(stream: Stream)
    DelimitedListTraceListener(stream: Stream, name: str)
    DelimitedListTraceListener(writer: TextWriter)
    DelimitedListTraceListener(writer: TextWriter, name: str)
    DelimitedListTraceListener(fileName: str)
    DelimitedListTraceListener(fileName: str, name: str)
    """
    def Dispose(self):
        """
        Dispose(self: TextWriterTraceListener, disposing: bool)
            Disposes this System.Diagnostics.TextWriterTraceListener object.
        
            disposing: true to release managed resources; if false, 
             System.Diagnostics.TextWriterTraceListener.Dispose(System.Boolean) has no effect.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: DelimitedListTraceListener) -> Array[str]
        
            Returns the custom configuration file attribute supported by the delimited trace listener.
            Returns: A string array that contains the single value "delimiter".
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])
            Writes trace information, an array of data objects, and event information to the output file or 
             stream.
        
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            data: An array of data objects to write to the output file or stream.
        TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)
            Writes trace information, a data object, and event information to the output file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            data: A data object to write to the output file or stream.
        """
        pass

    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)
            Writes trace information, a message, and event information to the output file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            message: The trace message to write to the output file or stream.
        TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])
            Writes trace information, a formatted array of objects, and event information to the output file 
             or stream.
        
        
            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and 
             stack trace information.
        
            source: A name used to identify the output, typically the name of the application that generated the 
             trace event.
        
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A numeric identifier for the event.
            format: A format string that contains zero or more format items that correspond to objects in the args 
             array.
        
            args: An array containing zero or more objects to format.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, name: str)
        __new__(cls: type, writer: TextWriter)
        __new__(cls: type, writer: TextWriter, name: str)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, name: str)
        """
        pass

    Delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the delimiter for the delimited list.

Get: Delimiter(self: DelimitedListTraceListener) -> str

Set: Delimiter(self: DelimitedListTraceListener) = value
"""

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""



class DiagnosticsConfigurationHandler(object, IConfigurationSectionHandler):
    """
    Handles the diagnostics section of configuration files.
    
    DiagnosticsConfigurationHandler()
    """
    def Create(self, parent, configContext, section):
        """
        Create(self: DiagnosticsConfigurationHandler, parent: object, configContext: object, section: XmlNode) -> object
        
            Parses the configuration settings for the <system.diagnostics> Element section of configuration 
             files.
        
        
            parent: The object inherited from the parent path
            configContext: Reserved. Used in ASP.NET to convey the virtual path of the configuration being evaluated.
            section: The root XML node at the section to handle.
            Returns: A new configuration object, in the form of a System.Collections.Hashtable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


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



class EntryWrittenEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Diagnostics.EventLog.EntryWritten event of an System.Diagnostics.EventLog.
    
    EntryWrittenEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EntryWrittenEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class EventInstance(object):
    """
    Represents language-neutral information for an event log entry.
    
    EventInstance(instanceId: Int64, categoryId: int)
    EventInstance(instanceId: Int64, categoryId: int, entryType: EventLogEntryType)
    """
    @staticmethod # known case of __new__
    def __new__(self, instanceId, categoryId, entryType=None):
        """
        __new__(cls: type, instanceId: Int64, categoryId: int)
        __new__(cls: type, instanceId: Int64, categoryId: int, entryType: EventLogEntryType)
        """
        pass

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the resource identifier that specifies the application-defined category of the event entry.

Get: CategoryId(self: EventInstance) -> int

Set: CategoryId(self: EventInstance) = value
"""

    EntryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event type of the event log entry.

Get: EntryType(self: EventInstance) -> EventLogEntryType

Set: EntryType(self: EventInstance) = value
"""

    InstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the resource identifier that designates the message text of the event entry.

Get: InstanceId(self: EventInstance) -> Int64

Set: InstanceId(self: EventInstance) = value
"""



class EventLog(Component, IComponent, IDisposable, ISupportInitialize):
    """
    Provides interaction with Windows event logs.
    
    EventLog()
    EventLog(logName: str)
    EventLog(logName: str, machineName: str)
    EventLog(logName: str, machineName: str, source: str)
    """
    def BeginInit(self):
        """
        BeginInit(self: EventLog)
            Begins the initialization of an System.Diagnostics.EventLog used on a form or used by another 
             component. The initialization occurs at runtime.
        """
        pass

    def Clear(self):
        """
        Clear(self: EventLog)
            Removes all entries from the event log.
        """
        pass

    def Close(self):
        """
        Close(self: EventLog)
            Closes the event log and releases read and write handles.
        """
        pass

    @staticmethod
    def CreateEventSource(*__args):
        """
        CreateEventSource(sourceData: EventSourceCreationData)
            Establishes a valid event source for writing localized event messages, using the specified 
             configuration properties for the event source and the corresponding event log.
        
        
            sourceData: The configuration properties for the event source and its target event log.
        CreateEventSource(source: str, logName: str, machineName: str)
            Establishes the specified source name as a valid event source for writing entries to a log on 
             the specified computer. This method can also be used to create a new custom log on the specified 
             computer.
        
        
            source: The source by which the application is registered on the specified computer.
            logName: The name of the log the source's entries are written to. Possible values include Application, 
             System, or a custom event log. If you do not specify a value, logName defaults to Application.
        
            machineName: The name of the computer to register this event source with, or "." for the local computer.
        CreateEventSource(source: str, logName: str)
            Establishes the specified source name as a valid event source for writing entries to a log on 
             the local computer. This method can also create a new custom log on the local computer.
        
        
            source: The source name by which the application is registered on the local computer.
            logName: The name of the log the source's entries are written to. Possible values include Application, 
             System, or a custom event log.
        """
        pass

    @staticmethod
    def Delete(logName, machineName=None):
        """
        Delete(logName: str, machineName: str)
            Removes an event log from the specified computer.
        
            logName: The name of the log to delete. Possible values include: Application, Security, System, and any 
             custom event logs on the specified computer.
        
            machineName: The name of the computer to delete the log from, or "." for the local computer.
        Delete(logName: str)
            Removes an event log from the local computer.
        
            logName: The name of the log to delete. Possible values include: Application, Security, System, and any 
             custom event logs on the computer.
        """
        pass

    @staticmethod
    def DeleteEventSource(source, machineName=None):
        """
        DeleteEventSource(source: str, machineName: str)
            Removes the application's event source registration from the specified computer.
        
            source: The name by which the application is registered in the event log system.
            machineName: The name of the computer to remove the registration from, or "." for the local computer.
        DeleteEventSource(source: str)
            Removes the event source registration from the event log of the local computer.
        
            source: The name by which the application is registered in the event log system.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: EventLog, disposing: bool)
            Releases the unmanaged resources used by the System.Diagnostics.EventLog, and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndInit(self):
        """
        EndInit(self: EventLog)
            Ends the initialization of an System.Diagnostics.EventLog used on a form or by another 
             component. The initialization occurs at runtime.
        """
        pass

    @staticmethod
    def Exists(logName, machineName=None):
        """
        Exists(logName: str, machineName: str) -> bool
        
            Determines whether the log exists on the specified computer.
        
            logName: The log for which to search. Possible values include: Application, Security, System, other 
             application-specific logs (such as those associated with Active Directory), or any custom log on 
             the computer.
        
            machineName: The name of the computer on which to search for the log, or "." for the local computer.
            Returns: true if the log exists on the specified computer; otherwise, false.
        Exists(logName: str) -> bool
        
            Determines whether the log exists on the local computer.
        
            logName: The name of the log to search for. Possible values include: Application, Security, System, other 
             application-specific logs (such as those associated with Active Directory), or any custom log on 
             the computer.
        
            Returns: true if the log exists on the local computer; otherwise, false.
        """
        pass

    @staticmethod
    def GetEventLogs(machineName=None):
        """
        GetEventLogs(machineName: str) -> Array[EventLog]
        
            Searches for all event logs on the given computer and creates an array of 
             System.Diagnostics.EventLog objects that contain the list.
        
        
            machineName: The computer on which to search for event logs.
            Returns: An array of type System.Diagnostics.EventLog that represents the logs on the given computer.
        GetEventLogs() -> Array[EventLog]
        
            Searches for all event logs on the local computer and creates an array of 
             System.Diagnostics.EventLog objects that contain the list.
        
            Returns: An array of type System.Diagnostics.EventLog that represents the logs on the local computer.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    @staticmethod
    def LogNameFromSourceName(source, machineName):
        """
        LogNameFromSourceName(source: str, machineName: str) -> str
        
            Gets the name of the log to which the specified source is registered.
        
            source: The name of the event source.
            machineName: The name of the computer on which to look, or "." for the local computer.
            Returns: The name of the log associated with the specified source in the registry.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ModifyOverflowPolicy(self, action, retentionDays):
        """
        ModifyOverflowPolicy(self: EventLog, action: OverflowAction, retentionDays: int)
            Changes the configured behavior for writing new entries when the event log reaches its maximum 
             file size.
        
        
            action: The overflow behavior for writing new entries to the event log.
            retentionDays: The minimum number of days each event log entry is retained. This parameter is used only if 
             action is set to System.Diagnostics.OverflowAction.OverwriteOlder.
        """
        pass

    def RegisterDisplayName(self, resourceFile, resourceId):
        """
        RegisterDisplayName(self: EventLog, resourceFile: str, resourceId: Int64)
            Specifies the localized name of the event log, which is displayed in the server Event Viewer.
        
            resourceFile: The fully specified path to a localized resource file.
            resourceId: The resource identifier that indexes a localized string within the resource file.
        """
        pass

    @staticmethod
    def SourceExists(source, machineName=None):
        """
        SourceExists(source: str, machineName: str) -> bool
        
            Determines whether an event source is registered on a specified computer.
        
            source: The name of the event source.
            machineName: The name the computer on which to look, or "." for the local computer.
            Returns: true if the event source is registered on the given computer; otherwise, false.
        SourceExists(source: str) -> bool
        
            Determines whether an event source is registered on the local computer.
        
            source: The name of the event source.
            Returns: true if the event source is registered on the local computer; otherwise, false.
        """
        pass

    def WriteEntry(self, *__args):
        """
        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16)
            Writes an entry with the given message text, application-defined event identifier, and 
             application-defined category to the event log.
        
        
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
            category: The application-specific subcategory associated with the message.
        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int)
            Writes an entry with the given message text and application-defined event identifier to the 
             event log, using the specified registered event source.
        
        
            source: The source by which the application is registered on the specified computer.
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16)
            Writes an entry with the given message text, application-defined event identifier, and 
             application-defined category to the event log, using the specified registered event source. The 
             category can be used by the Event Viewer to filter events in the log.
        
        
            source: The source by which the application is registered on the specified computer.
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
            category: The application-specific subcategory associated with the message.
        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte])
            Writes an entry with the given message text, application-defined event identifier, and 
             application-defined category to the event log, and appends binary data to the message.
        
        
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
            category: The application-specific subcategory associated with the message.
            rawData: An array of bytes that holds the binary data associated with the entry.
        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte])
            Writes an entry with the given message text, application-defined event identifier, and 
             application-defined category to the event log (using the specified registered event source) and 
             appends binary data to the message.
        
        
            source: The source by which the application is registered on the specified computer.
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
            category: The application-specific subcategory associated with the message.
            rawData: An array of bytes that holds the binary data associated with the entry.
        WriteEntry(source: str, message: str)
            Writes an information type entry with the given message text to the event log, using the 
             specified registered event source.
        
        
            source: The source by which the application is registered on the specified computer.
            message: The string to write to the event log.
        WriteEntry(self: EventLog, message: str)
            Writes an information type entry, with the given message text, to the event log.
        
            message: The string to write to the event log.
        WriteEntry(self: EventLog, message: str, type: EventLogEntryType)
            Writes an error, warning, information, success audit, or failure audit entry with the given 
             message text to the event log.
        
        
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int)
            Writes an entry with the given message text and application-defined event identifier to the 
             event log.
        
        
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
            eventID: The application-specific identifier for the event.
        WriteEntry(source: str, message: str, type: EventLogEntryType)
            Writes an error, warning, information, success audit, or failure audit entry with the given 
             message text to the event log, using the specified registered event source.
        
        
            source: The source by which the application is registered on the specified computer.
            message: The string to write to the event log.
            type: One of the System.Diagnostics.EventLogEntryType values.
        """
        pass

    def WriteEvent(self, *__args):
        """
        WriteEvent(source: str, instance: EventInstance, *values: Array[object])
            Writes an event log entry with the given event data and message replacement strings, using the 
             specified registered event source.
        
        
            source: The name of the event source registered for the application on the specified computer.
            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.
            values: An array of strings to merge into the message text of the event log entry.
        WriteEvent(source: str, instance: EventInstance, data: Array[Byte], *values: Array[object])
            Writes an event log entry with the given event data, message replacement strings, and associated 
             binary data, and using the specified registered event source.
        
        
            source: The name of the event source registered for the application on the specified computer.
            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.
            data: An array of bytes that holds the binary data associated with the entry.
            values: An array of strings to merge into the message text of the event log entry.
        WriteEvent(self: EventLog, instance: EventInstance, *values: Array[object])
            Writes a localized entry to the event log.
        
            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.
            values: An array of strings to merge into the message text of the event log entry.
        WriteEvent(self: EventLog, instance: EventInstance, data: Array[Byte], *values: Array[object])
            Writes an event log entry with the given event data, message replacement strings, and associated 
             binary data.
        
        
            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.
            data: An array of bytes that holds the binary data associated with the entry.
            values: An array of strings to merge into the message text of the event log entry.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logName=None, machineName=None, source=None):
        """
        __new__(cls: type)
        __new__(cls: type, logName: str)
        __new__(cls: type, logName: str, machineName: str)
        __new__(cls: type, logName: str, machineName: str, source: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    EnableRaisingEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Diagnostics.EventLog receives System.Diagnostics.EventLog.EntryWritten event notifications.

Get: EnableRaisingEvents(self: EventLog) -> bool

Set: EnableRaisingEvents(self: EventLog) = value
"""

    Entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the contents of the event log.

Get: Entries(self: EventLog) -> EventLogEntryCollection

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the log to read from or write to.

Get: Log(self: EventLog) -> str

Set: Log(self: EventLog) = value
"""

    LogDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the event log's friendly name.

Get: LogDisplayName(self: EventLog) -> str

"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the computer on which to read or write events.

Get: MachineName(self: EventLog) -> str

Set: MachineName(self: EventLog) = value
"""

    MaximumKilobytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum event log size in kilobytes.

Get: MaximumKilobytes(self: EventLog) -> Int64

Set: MaximumKilobytes(self: EventLog) = value
"""

    MinimumRetentionDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of days to retain entries in the event log.

Get: MinimumRetentionDays(self: EventLog) -> int

"""

    OverflowAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configured behavior for storing new entries when the event log reaches its maximum log file size.

Get: OverflowAction(self: EventLog) -> OverflowAction

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the source name to register and use when writing to the event log.

Get: Source(self: EventLog) -> str

Set: Source(self: EventLog) = value
"""

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object used to marshal the event handler calls issued as a result of an System.Diagnostics.EventLog entry written event.

Get: SynchronizingObject(self: EventLog) -> ISynchronizeInvoke

Set: SynchronizingObject(self: EventLog) = value
"""


    EntryWritten = None


class EventLogEntry(Component, IComponent, IDisposable, ISerializable):
    """ Encapsulates a single record in the event log. This class cannot be inherited. """
    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: EventLogEntry, otherEntry: EventLogEntry) -> bool
        
            Performs a comparison between two event log entries.
        
            otherEntry: The System.Diagnostics.EventLogEntry to compare.
            Returns: true if the System.Diagnostics.EventLogEntry objects are identical; otherwise, false.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text associated with the System.Diagnostics.EventLogEntry.CategoryNumber property for this entry.

Get: Category(self: EventLogEntry) -> str

"""

    CategoryNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category number of the event log entry.

Get: CategoryNumber(self: EventLogEntry) -> Int16

"""

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the binary data associated with the entry.

Get: Data(self: EventLogEntry) -> Array[Byte]

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    EntryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the event type of this entry.

Get: EntryType(self: EventLogEntry) -> EventLogEntryType

"""

    EventID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application-specific event identifier for the current event entry.

Get: EventID(self: EventLogEntry) -> int

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this entry in the event log.

Get: Index(self: EventLogEntry) -> int

"""

    InstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resource identifier that designates the message text of the event entry.

Get: InstanceId(self: EventLogEntry) -> Int64

"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the computer on which this entry was generated.

Get: MachineName(self: EventLogEntry) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the localized message associated with this event entry.

Get: Message(self: EventLogEntry) -> str

"""

    ReplacementStrings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the replacement strings associated with the event log entry.

Get: ReplacementStrings(self: EventLogEntry) -> Array[str]

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the application that generated this event.

Get: Source(self: EventLogEntry) -> str

"""

    TimeGenerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the local time at which this event was generated.

Get: TimeGenerated(self: EventLogEntry) -> DateTime

"""

    TimeWritten = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the local time at which this event was written to the log.

Get: TimeWritten(self: EventLogEntry) -> DateTime

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the user who is responsible for this event.

Get: UserName(self: EventLogEntry) -> str

"""



class EventLogEntryCollection(object, ICollection, IEnumerable):
    """ Defines size and enumerators for a collection of System.Diagnostics.EventLogEntry instances. """
    def CopyTo(self, entries, index):
        """
        CopyTo(self: EventLogEntryCollection, entries: Array[EventLogEntry], index: int)
            Copies the elements of the System.Diagnostics.EventLogEntryCollection to an array of 
             System.Diagnostics.EventLogEntry instances, starting at a particular array index.
        
        
            entries: The one-dimensional array of System.Diagnostics.EventLogEntry instances that is the destination 
             of the elements copied from the collection. The array must have zero-based indexing.
        
            index: The zero-based index in the array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: EventLogEntryCollection) -> IEnumerator
        
            Supports a simple iteration over the System.Diagnostics.EventLogEntryCollection object.
            Returns: An object that can be used to iterate over the collection.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of entries in the event log (that is, the number of elements in the System.Diagnostics.EventLogEntry collection).

Get: Count(self: EventLogEntryCollection) -> int

"""



class EventLogEntryType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the event type of an event log entry.
    
    enum EventLogEntryType, values: Error (1), FailureAudit (16), Information (4), SuccessAudit (8), Warning (2)
    """
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

    Error = None
    FailureAudit = None
    Information = None
    SuccessAudit = None
    value__ = None
    Warning = None


class EventLogPermission(ResourcePermissionBase, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls code access permissions for event logging.
    
    EventLogPermission()
    EventLogPermission(state: PermissionState)
    EventLogPermission(permissionAccess: EventLogPermissionAccess, machineName: str)
    EventLogPermission(permissionAccessEntries: Array[EventLogPermissionEntry])
    """
    def AddPermissionAccess(self, *args): #cannot find CLR method
        """
        AddPermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Adds a permission entry to the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to add.
        """
        pass

    def Clear(self, *args): #cannot find CLR method
        """
        Clear(self: ResourcePermissionBase)
            Clears the permission of the added permission entries.
        """
        pass

    def GetPermissionEntries(self, *args): #cannot find CLR method
        """
        GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry]
        
            Returns an array of the System.Security.Permissions.ResourcePermissionBaseEntry objects added to 
             this permission.
        
            Returns: An array of System.Security.Permissions.ResourcePermissionBaseEntry objects that were added to 
             this permission.
        """
        pass

    def RemovePermissionAccess(self, *args): #cannot find CLR method
        """
        RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Removes a permission entry from the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, permissionAccess: EventLogPermissionAccess, machineName: str)
        __new__(cls: type, permissionAccessEntries: Array[EventLogPermissionEntry])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PermissionAccessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an enumeration value that describes the types of access that you are giving the resource.

"""

    PermissionEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of permission entries for this permissions request.

Get: PermissionEntries(self: EventLogPermission) -> EventLogPermissionEntryCollection

"""

    TagNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of strings that identify the resource you are protecting.

"""



class EventLogPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines access levels used by System.Diagnostics.EventLog permission classes.
    
    enum (flags) EventLogPermissionAccess, values: Administer (48), Audit (10), Browse (2), Instrument (6), None (0), Write (16)
    """
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

    Administer = None
    Audit = None
    Browse = None
    Instrument = None
    None = None
    value__ = None
    Write = None


class EventLogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows declaritive permission checks for event logging.
    
    EventLogPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: EventLogPermissionAttribute) -> IPermission
        
            Creates the permission based on the System.Diagnostics.EventLogPermissionAttribute.MachineName 
             property and the requested access levels that are set through the 
             System.Diagnostics.EventLogPermissionAttribute.PermissionAccess property on the attribute.
        
            Returns: An System.Security.IPermission that represents the created permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action):
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the computer on which events might be read.

Get: MachineName(self: EventLogPermissionAttribute) -> str

Set: MachineName(self: EventLogPermissionAttribute) = value
"""

    PermissionAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the access levels used in the permissions request.

Get: PermissionAccess(self: EventLogPermissionAttribute) -> EventLogPermissionAccess

Set: PermissionAccess(self: EventLogPermissionAttribute) = value
"""



class EventLogPermissionEntry(object):
    """
    Defines the smallest unit of a code access security permission that is set for an System.Diagnostics.EventLog.
    
    EventLogPermissionEntry(permissionAccess: EventLogPermissionAccess, machineName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, permissionAccess, machineName):
        """ __new__(cls: type, permissionAccess: EventLogPermissionAccess, machineName: str) """
        pass

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the computer on which to read or write events.

Get: MachineName(self: EventLogPermissionEntry) -> str

"""

    PermissionAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the permission access levels used in the permissions request.

Get: PermissionAccess(self: EventLogPermissionEntry) -> EventLogPermissionAccess

"""



class EventLogPermissionEntryCollection(CollectionBase, IList, ICollection, IEnumerable):
    """ Contains a strongly typed collection of System.Diagnostics.EventLogPermissionEntry objects. """
    def Add(self, value):
        """
        Add(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int
        
            Adds a specified System.Diagnostics.EventLogPermissionEntry to this collection.
        
            value: The System.Diagnostics.EventLogPermissionEntry to add.
            Returns: The zero-based index of the added System.Diagnostics.EventLogPermissionEntry.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntryCollection)
            Appends a set of specified permission entries to this collection.
        
            value: A System.Diagnostics.EventLogPermissionEntryCollection that contains the permission entries to 
             add.
        
        AddRange(self: EventLogPermissionEntryCollection, value: Array[EventLogPermissionEntry])
            Appends a set of specified permission entries to this collection.
        
            value: An array of type System.Diagnostics.EventLogPermissionEntry objects that contains the permission 
             entries to add.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> bool
        
            Determines whether this collection contains a specified 
             System.Diagnostics.EventLogPermissionEntry.
        
        
            value: The System.Diagnostics.EventLogPermissionEntry to find.
            Returns: true if the specified System.Diagnostics.EventLogPermissionEntry belongs to this collection; 
             otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: EventLogPermissionEntryCollection, array: Array[EventLogPermissionEntry], index: int)
            Copies the permission entries from this collection to an array, starting at a particular index 
             of the array.
        
        
            array: An array of type System.Diagnostics.EventLogPermissionEntry that receives this collection's 
             permission entries.
        
            index: The zero-based index at which to begin copying the permission entries.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int
        
            Determines the index of a specified permission entry in this collection.
        
            value: The permission entry to search for.
            Returns: The zero-based index of the specified permission entry, or -1 if the permission entry was not 
             found in the collection.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: EventLogPermissionEntryCollection, index: int, value: EventLogPermissionEntry)
            Inserts a permission entry into this collection at a specified index.
        
            index: The zero-based index of the collection at which to insert the permission entry.
            value: The permission entry to insert into this collection.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: EventLogPermissionEntryCollection)
            Performs additional custom processes after clearing the contents of the collection.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: EventLogPermissionEntryCollection, index: int, value: object)
            Performs additional custom processes before a new permission entry is inserted into the 
             collection.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the permission entry at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: EventLogPermissionEntryCollection, index: int, value: object)
            Performs additional custom processes when removing a new permission entry from the collection.
        
            index: The zero-based index at which value can be found.
            value: The permission entry to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: EventLogPermissionEntryCollection, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the collection.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the permission entry at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry)
            Removes a specified permission entry from this collection.
        
            value: The permission entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class EventLogTraceListener(TraceListener, IDisposable):
    """
    Provides a simple listener that directs tracing or debugging output to an System.Diagnostics.EventLog.
    
    EventLogTraceListener()
    EventLogTraceListener(eventLog: EventLog)
    EventLogTraceListener(source: str)
    """
    def Close(self):
        """
        Close(self: EventLogTraceListener)
            Closes the event log so that it no longer receives tracing or debugging output.
        """
        pass

    def Dispose(self):
        """ Dispose(self: EventLogTraceListener, disposing: bool) """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def TraceData(self, eventCache, source, severity, id, data):
        """
        TraceData(self: EventLogTraceListener, eventCache: TraceEventCache, source: str, severity: TraceEventType, id: int, *data: Array[object])
            Writes trace information, an array of data objects, and event information to the event log.
        
            eventCache: An object that contains the current process ID, thread ID, and stack trace information.
            source: A name used to identify the output; typically the name of the application that generated the 
             trace event.
        
            severity: One of the enumeration values that specifies the type of event that has caused the trace.
            id: A numeric identifier for the event. The combination of source and id uniquely identifies an 
             event.
        
            data: An array of data objects.
        TraceData(self: EventLogTraceListener, eventCache: TraceEventCache, source: str, severity: TraceEventType, id: int, data: object)
            Writes trace information, a data object, and event information to the event log.
        
            eventCache: An object that contains the current process ID, thread ID, and stack trace information.
            source: A name used to identify the output; typically the name of the application that generated the 
             trace event.
        
            severity: One of the enumeration values that specifies the type of event that has caused the trace.
            id: A numeric identifier for the event. The combination of source and id uniquely identifies an 
             event.
        
            data: A data object to write to the output file or stream.
        """
        pass

    def TraceEvent(self, eventCache, source, *__args):
        """
        TraceEvent(self: EventLogTraceListener, eventCache: TraceEventCache, source: str, severity: TraceEventType, id: int, message: str)
            Writes trace information, a message, and event information to the event log.
        
            eventCache: An object that contains the current process ID, thread ID, and stack trace information.
            source: A name used to identify the output; typically the name of the application that generated the 
             trace event.
        
            severity: One of the enumeration values that specifies the type of event that has caused the trace.
            id: A numeric identifier for the event. The combination of source and id uniquely identifies an 
             event.
        
            message: The trace message.
        TraceEvent(self: EventLogTraceListener, eventCache: TraceEventCache, source: str, severity: TraceEventType, id: int, format: str, *args: Array[object])
            Writes trace information, a formatted array of objects, and event information to the event log.
        
            eventCache: An object that contains the current process ID, thread ID, and stack trace information.
            source: A name used to identify the output; typically the name of the application that generated the 
             trace event.
        
            severity: One of the enumeration values that specifies the type of event that has caused the trace.
            id: A numeric identifier for the event. The combination of source and id uniquely identifies an 
             event.
        
            format: A format string that contains zero or more format items that correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: EventLogTraceListener, message: str)
            Writes a message to the event log for this instance.
        
            message: The message to write.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: EventLogTraceListener, message: str)
            Writes a message to the event log for this instance.
        
            message: The message to write.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, eventLog: EventLog)
        __new__(cls: type, source: str)
        """
        pass

    EventLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event log to write to.

Get: EventLog(self: EventLogTraceListener) -> EventLog

Set: EventLog(self: EventLogTraceListener) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of this System.Diagnostics.EventLogTraceListener.

Get: Name(self: EventLogTraceListener) -> str

Set: Name(self: EventLogTraceListener) = value
"""

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""



class EventSourceCreationData(object):
    """
    Represents the configuration settings used to create an event log source on the local computer or a remote computer.
    
    EventSourceCreationData(source: str, logName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, source, logName):
        """ __new__(cls: type, source: str, logName: str) """
        pass

    CategoryCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of categories in the category resource file.

Get: CategoryCount(self: EventSourceCreationData) -> int

Set: CategoryCount(self: EventSourceCreationData) = value
"""

    CategoryResourceFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path of the resource file that contains category strings for the source.

Get: CategoryResourceFile(self: EventSourceCreationData) -> str

Set: CategoryResourceFile(self: EventSourceCreationData) = value
"""

    LogName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the event log to which the source writes entries.

Get: LogName(self: EventSourceCreationData) -> str

Set: LogName(self: EventSourceCreationData) = value
"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the computer on which to register the event source.

Get: MachineName(self: EventSourceCreationData) -> str

Set: MachineName(self: EventSourceCreationData) = value
"""

    MessageResourceFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path of the message resource file that contains message formatting strings for the source.

Get: MessageResourceFile(self: EventSourceCreationData) -> str

Set: MessageResourceFile(self: EventSourceCreationData) = value
"""

    ParameterResourceFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path of the resource file that contains message parameter strings for the source.

Get: ParameterResourceFile(self: EventSourceCreationData) -> str

Set: ParameterResourceFile(self: EventSourceCreationData) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name to register with the event log as an event source.

Get: Source(self: EventSourceCreationData) -> str

Set: Source(self: EventSourceCreationData) = value
"""



class TraceFilter(object):
    """ Provides the base class for trace filter implementations. """
    def ShouldTrace(self, cache, source, eventType, id, formatOrMessage, args, data1, data):
        """
        ShouldTrace(self: TraceFilter, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: Array[object], data1: object, data: Array[object]) -> bool
        
            When overridden in a derived class, determines whether the trace listener should trace the event.
        
            cache: The System.Diagnostics.TraceEventCache that contains information for the trace event.
            source: The name of the source.
            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 
             the trace.
        
            id: A trace identifier number.
            formatOrMessage: Either the format to use for writing an array of arguments specified by the args parameter, or a 
             message to write.
        
            args: An array of argument objects.
            data1: A trace data object.
            data: An array of trace data objects.
            Returns: true to trace the specified event; otherwise, false.
        """
        pass


class EventTypeFilter(TraceFilter):
    """
    Indicates whether a listener should trace based on the event type.
    
    EventTypeFilter(level: SourceLevels)
    """
    def ShouldTrace(self, cache, source, eventType, id, formatOrMessage, args, data1, data):
        """
        ShouldTrace(self: EventTypeFilter, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: Array[object], data1: object, data: Array[object]) -> bool
        
            Determines whether the trace listener should trace the event.
        
            cache: A System.Diagnostics.TraceEventCache that represents the information cache for the trace event.
            source: The name of the source.
            eventType: One of the System.Diagnostics.TraceEventType values.
            id: A trace identifier number.
            formatOrMessage: The format to use for writing an array of arguments, or a message to write.
            args: An array of argument objects.
            data1: A trace data object.
            data: An array of trace data objects.
            Returns: trueif the trace should be produced; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, level):
        """ __new__(cls: type, level: SourceLevels) """
        pass

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event type of the messages to trace.

Get: EventType(self: EventTypeFilter) -> SourceLevels

Set: EventType(self: EventTypeFilter) = value
"""



class FileVersionInfo(object):
    """ Provides version information for a physical file on disk. """
    @staticmethod
    def GetVersionInfo(fileName):
        """
        GetVersionInfo(fileName: str) -> FileVersionInfo
        
            Returns a System.Diagnostics.FileVersionInfo representing the version information associated 
             with the specified file.
        
        
            fileName: The fully qualified path and name of the file to retrieve the version information for.
            Returns: A System.Diagnostics.FileVersionInfo containing information about the file. If the file did not 
             contain version information, the System.Diagnostics.FileVersionInfo contains only the name of 
             the file requested.
        """
        pass

    def ToString(self):
        """
        ToString(self: FileVersionInfo) -> str
        
            Returns a partial list of properties in the System.Diagnostics.FileVersionInfo and their values.
            Returns: A list of the following properties in this class and their values: 
             System.Diagnostics.FileVersionInfo.FileName, System.Diagnostics.FileVersionInfo.InternalName, 
             System.Diagnostics.FileVersionInfo.OriginalFilename, 
             System.Diagnostics.FileVersionInfo.FileVersion, 
             System.Diagnostics.FileVersionInfo.FileDescription, 
             System.Diagnostics.FileVersionInfo.ProductName, 
             System.Diagnostics.FileVersionInfo.ProductVersion, System.Diagnostics.FileVersionInfo.IsDebug, 
             System.Diagnostics.FileVersionInfo.IsPatched, System.Diagnostics.FileVersionInfo.IsPreRelease, 
             System.Diagnostics.FileVersionInfo.IsPrivateBuild, 
             System.Diagnostics.FileVersionInfo.IsSpecialBuild,System.Diagnostics.FileVersionInfo.Language.If 
             the file did not contain version information, this list will contain only the name of the 
             requested file. Boolean values will be false, and all other entries will be null.
        """
        pass

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the comments associated with the file.

Get: Comments(self: FileVersionInfo) -> str

"""

    CompanyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the company that produced the file.

Get: CompanyName(self: FileVersionInfo) -> str

"""

    FileBuildPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the build number of the file.

Get: FileBuildPart(self: FileVersionInfo) -> int

"""

    FileDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description of the file.

Get: FileDescription(self: FileVersionInfo) -> str

"""

    FileMajorPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major part of the version number.

Get: FileMajorPart(self: FileVersionInfo) -> int

"""

    FileMinorPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor part of the version number of the file.

Get: FileMinorPart(self: FileVersionInfo) -> int

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file that this instance of System.Diagnostics.FileVersionInfo describes.

Get: FileName(self: FileVersionInfo) -> str

"""

    FilePrivatePart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file private part number.

Get: FilePrivatePart(self: FileVersionInfo) -> int

"""

    FileVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file version number.

Get: FileVersion(self: FileVersionInfo) -> str

"""

    InternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal name of the file, if one exists.

Get: InternalName(self: FileVersionInfo) -> str

"""

    IsDebug = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the file contains debugging information or is compiled with debugging features enabled.

Get: IsDebug(self: FileVersionInfo) -> bool

"""

    IsPatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the file has been modified and is not identical to the original shipping file of the same version number.

Get: IsPatched(self: FileVersionInfo) -> bool

"""

    IsPreRelease = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the file is a development version, rather than a commercially released product.

Get: IsPreRelease(self: FileVersionInfo) -> bool

"""

    IsPrivateBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the file was built using standard release procedures.

Get: IsPrivateBuild(self: FileVersionInfo) -> bool

"""

    IsSpecialBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the file is a special build.

Get: IsSpecialBuild(self: FileVersionInfo) -> bool

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default language string for the version info block.

Get: Language(self: FileVersionInfo) -> str

"""

    LegalCopyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all copyright notices that apply to the specified file.

Get: LegalCopyright(self: FileVersionInfo) -> str

"""

    LegalTrademarks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the trademarks and registered trademarks that apply to the file.

Get: LegalTrademarks(self: FileVersionInfo) -> str

"""

    OriginalFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name the file was created with.

Get: OriginalFilename(self: FileVersionInfo) -> str

"""

    PrivateBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information about a private version of the file.

Get: PrivateBuild(self: FileVersionInfo) -> str

"""

    ProductBuildPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the build number of the product this file is associated with.

Get: ProductBuildPart(self: FileVersionInfo) -> int

"""

    ProductMajorPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major part of the version number for the product this file is associated with.

Get: ProductMajorPart(self: FileVersionInfo) -> int

"""

    ProductMinorPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor part of the version number for the product the file is associated with.

Get: ProductMinorPart(self: FileVersionInfo) -> int

"""

    ProductName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the product this file is distributed with.

Get: ProductName(self: FileVersionInfo) -> str

"""

    ProductPrivatePart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the private part number of the product this file is associated with.

Get: ProductPrivatePart(self: FileVersionInfo) -> int

"""

    ProductVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of the product this file is distributed with.

Get: ProductVersion(self: FileVersionInfo) -> str

"""

    SpecialBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the special build information for the file.

Get: SpecialBuild(self: FileVersionInfo) -> str

"""



class ICollectData:
    """ Prepares performance data for the performance DLL the system loads when working with performance counters. """
    def CloseData(self):
        """
        CloseData(self: ICollectData)
            Called by the performance DLL's close performance data function.
        """
        pass

    def CollectData(self, id, valueName, data, totalBytes, res):
        """
        CollectData(self: ICollectData, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int) -> IntPtr
        
            Collects the performance data for the performance DLL.
        
            id: The call index.
            valueName: A pointer to a Unicode string list with the requested object identifiers.
            data: A pointer to the data buffer.
            totalBytes: A pointer to a number of bytes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InstanceData(object):
    """
    Holds instance data associated with a performance counter sample.
    
    InstanceData(instanceName: str, sample: CounterSample)
    """
    @staticmethod # known case of __new__
    def __new__(self, instanceName, sample):
        """ __new__(cls: type, instanceName: str, sample: CounterSample) """
        pass

    InstanceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the instance name associated with this instance data.

Get: InstanceName(self: InstanceData) -> str

"""

    RawValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw data value associated with the performance counter sample.

Get: RawValue(self: InstanceData) -> Int64

"""

    Sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the performance counter sample that generated this data.

Get: Sample(self: InstanceData) -> CounterSample

"""



class InstanceDataCollection(DictionaryBase, IDictionary, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.InstanceData objects.
    
    InstanceDataCollection(counterName: str)
    """
    def Contains(self, instanceName):
        """
        Contains(self: InstanceDataCollection, instanceName: str) -> bool
        
            Determines whether a performance instance with a specified name (identified by one of the 
             indexed System.Diagnostics.InstanceData objects) exists in the collection.
        
        
            instanceName: The name of the instance to find in this collection.
            Returns: true if the instance exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: InstanceDataCollection, instances: Array[InstanceData], index: int)
            Copies the items in the collection to the specified one-dimensional array at the specified index.
        
            instances: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The zero-based index value at which to add the new instances.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: DictionaryBase)
            Performs additional custom processes before clearing the contents of the 
             System.Collections.DictionaryBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: DictionaryBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.DictionaryBase instance.
        """
        pass

    def OnGet(self, *args): #cannot find CLR method
        """
        OnGet(self: DictionaryBase, key: object, currentValue: object) -> object
        
            Gets the element with the specified key and value in the System.Collections.DictionaryBase 
             instance.
        
        
            key: The key of the element to get.
            currentValue: The current value of the element associated with key.
            Returns: An System.Object containing the element with the specified key and value.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before removing an element from the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes when validating the element with the specified key and 
             value.
        
        
            key: The key of the element to validate.
            value: The value of the element to validate.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, counterName):
        """ __new__(cls: type, counterName: str) """
        pass

    CounterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the performance counter whose instance data you want to get.

Get: CounterName(self: InstanceDataCollection) -> str

"""

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.DictionaryBase instance.

"""

    InnerHashtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.DictionaryBase instance.

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object and counter registry keys for the objects associated with this instance data.

Get: Keys(self: InstanceDataCollection) -> ICollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw counter values that comprise the instance data for the counter.

Get: Values(self: InstanceDataCollection) -> ICollection

"""



class InstanceDataCollectionCollection(DictionaryBase, IDictionary, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.InstanceDataCollection objects.
    
    InstanceDataCollectionCollection()
    """
    def Contains(self, counterName):
        """
        Contains(self: InstanceDataCollectionCollection, counterName: str) -> bool
        
            Determines whether an instance data collection for the specified counter (identified by one of 
             the indexed System.Diagnostics.InstanceDataCollection objects) exists in the collection.
        
        
            counterName: The name of the performance counter.
            Returns: true if an instance data collection containing the specified counter exists in the collection; 
             otherwise, false.
        """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: InstanceDataCollectionCollection, counters: Array[InstanceDataCollection], index: int)
            Copies an array of System.Diagnostics.InstanceDataCollection instances to the collection, at the 
             specified index.
        
        
            counters: An array of System.Diagnostics.InstanceDataCollection instances (identified by the counters they 
             contain) to add to the collection.
        
            index: The location at which to add the new instances.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: DictionaryBase)
            Performs additional custom processes before clearing the contents of the 
             System.Collections.DictionaryBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: DictionaryBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.DictionaryBase instance.
        """
        pass

    def OnGet(self, *args): #cannot find CLR method
        """
        OnGet(self: DictionaryBase, key: object, currentValue: object) -> object
        
            Gets the element with the specified key and value in the System.Collections.DictionaryBase 
             instance.
        
        
            key: The key of the element to get.
            currentValue: The current value of the element associated with key.
            Returns: An System.Object containing the element with the specified key and value.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before removing an element from the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.DictionaryBase instance.
        
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes when validating the element with the specified key and 
             value.
        
        
            key: The key of the element to validate.
            value: The value of the element to validate.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.DictionaryBase instance.

"""

    InnerHashtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.DictionaryBase instance.

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object and counter registry keys for the objects associated with this instance data collection.

Get: Keys(self: InstanceDataCollectionCollection) -> ICollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the instance data values that comprise the collection of instances for the counter.

Get: Values(self: InstanceDataCollectionCollection) -> ICollection

"""



class MonitoringDescriptionAttribute(DescriptionAttribute, _Attribute):
    """
    Specifies a description for a property or event.
    
    MonitoringDescriptionAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets description text associated with the item monitored.

Get: Description(self: MonitoringDescriptionAttribute) -> str

"""

    DescriptionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string stored as the description.

"""



class OverflowAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how to handle entries in an event log that has reached its maximum file size.
    
    enum OverflowAction, values: DoNotOverwrite (-1), OverwriteAsNeeded (0), OverwriteOlder (1)
    """
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

    DoNotOverwrite = None
    OverwriteAsNeeded = None
    OverwriteOlder = None
    value__ = None


class PerformanceCounter(Component, IComponent, IDisposable, ISupportInitialize):
    """
    Represents a Windows NT performance counter component.
    
    PerformanceCounter()
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, machineName: str)
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str)
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, readOnly: bool)
    PerformanceCounter(categoryName: str, counterName: str)
    PerformanceCounter(categoryName: str, counterName: str, readOnly: bool)
    """
    def BeginInit(self):
        """
        BeginInit(self: PerformanceCounter)
            Begins the initialization of a System.Diagnostics.PerformanceCounter instance used on a form or 
             by another component. The initialization occurs at runtime.
        """
        pass

    def Close(self):
        """
        Close(self: PerformanceCounter)
            Closes the performance counter and frees all the resources allocated by this performance counter 
             instance.
        """
        pass

    @staticmethod
    def CloseSharedResources():
        """
        CloseSharedResources()
            Frees the performance counter library shared state allocated by the counters.
        """
        pass

    def Decrement(self):
        """
        Decrement(self: PerformanceCounter) -> Int64
        
            Decrements the associated performance counter by one through an efficient atomic operation.
            Returns: The decremented counter value.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PerformanceCounter, disposing: bool) """
        pass

    def EndInit(self):
        """
        EndInit(self: PerformanceCounter)
            Ends the initialization of a System.Diagnostics.PerformanceCounter instance that is used on a 
             form or by another component. The initialization occurs at runtime.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def Increment(self):
        """
        Increment(self: PerformanceCounter) -> Int64
        
            Increments the associated performance counter by one through an efficient atomic operation.
            Returns: The incremented counter value.
        """
        pass

    def IncrementBy(self, value):
        """
        IncrementBy(self: PerformanceCounter, value: Int64) -> Int64
        
            Increments or decrements the value of the associated performance counter by a specified amount 
             through an efficient atomic operation.
        
        
            value: The value to increment by. (A negative value decrements the counter.)
            Returns: The new counter value.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NextSample(self):
        """
        NextSample(self: PerformanceCounter) -> CounterSample
        
            Obtains a counter sample, and returns the raw, or uncalculated, value for it.
            Returns: A System.Diagnostics.CounterSample that represents the next raw value that the system obtains 
             for this counter.
        """
        pass

    def NextValue(self):
        """
        NextValue(self: PerformanceCounter) -> Single
        
            Obtains a counter sample and returns the calculated value for it.
            Returns: The next calculated value that the system obtains for this counter.
        """
        pass

    def RemoveInstance(self):
        """
        RemoveInstance(self: PerformanceCounter)
            Deletes the category instance specified by the System.Diagnostics.PerformanceCounter object 
             System.Diagnostics.PerformanceCounter.InstanceName property.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, categoryName=None, counterName=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, machineName: str)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, readOnly: bool)
        __new__(cls: type, categoryName: str, counterName: str)
        __new__(cls: type, categoryName: str, counterName: str, readOnly: bool)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    CategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the performance counter category for this performance counter.

Get: CategoryName(self: PerformanceCounter) -> str

Set: CategoryName(self: PerformanceCounter) = value
"""

    CounterHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description for this performance counter.

Get: CounterHelp(self: PerformanceCounter) -> str

"""

    CounterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the performance counter that is associated with this System.Diagnostics.PerformanceCounter instance.

Get: CounterName(self: PerformanceCounter) -> str

Set: CounterName(self: PerformanceCounter) = value
"""

    CounterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the counter type of the associated performance counter.

Get: CounterType(self: PerformanceCounter) -> PerformanceCounterType

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    InstanceLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the lifetime of a process.

Get: InstanceLifetime(self: PerformanceCounter) -> PerformanceCounterInstanceLifetime

Set: InstanceLifetime(self: PerformanceCounter) = value
"""

    InstanceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an instance name for this performance counter.

Get: InstanceName(self: PerformanceCounter) -> str

Set: InstanceName(self: PerformanceCounter) = value
"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the computer name for this performance counter

Get: MachineName(self: PerformanceCounter) -> str

Set: MachineName(self: PerformanceCounter) = value
"""

    RawValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the raw, or uncalculated, value of this counter.

Get: RawValue(self: PerformanceCounter) -> Int64

Set: RawValue(self: PerformanceCounter) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this System.Diagnostics.PerformanceCounter instance is in read-only mode.

Get: ReadOnly(self: PerformanceCounter) -> bool

Set: ReadOnly(self: PerformanceCounter) = value
"""


    DefaultFileMappingSize = 524288


class PerformanceCounterCategory(object):
    """
    Represents a performance object, which defines a category of performance counters.
    
    PerformanceCounterCategory()
    PerformanceCounterCategory(categoryName: str)
    PerformanceCounterCategory(categoryName: str, machineName: str)
    """
    def CounterExists(self, counterName, categoryName=None, machineName=None):
        """
        CounterExists(counterName: str, categoryName: str, machineName: str) -> bool
        
            Determines whether the specified counter is registered to the specified category on a remote 
             computer.
        
        
            counterName: The name of the performance counter to look for.
            categoryName: The name of the performance counter category, or performance object, with which the specified 
             performance counter is associated.
        
            machineName: The name of the computer on which the performance counter category and its associated counters 
             exist.
        
            Returns: true, if the counter is registered to the specified category on the specified computer; 
             otherwise, false.
        
        CounterExists(counterName: str, categoryName: str) -> bool
        
            Determines whether the specified counter is registered to the specified category on the local 
             computer.
        
        
            counterName: The name of the performance counter to look for.
            categoryName: The name of the performance counter category, or performance object, with which the specified 
             performance counter is associated.
        
            Returns: true, if the counter is registered to the specified category on the local computer; otherwise, 
             false.
        
        CounterExists(self: PerformanceCounterCategory, counterName: str) -> bool
        
            Determines whether the specified counter is registered to this category, which is indicated by 
             the System.Diagnostics.PerformanceCounterCategory.CategoryName and 
             System.Diagnostics.PerformanceCounterCategory.MachineName properties.
        
        
            counterName: The name of the performance counter to look for.
            Returns: true if the counter is registered to the category that is specified by the 
             System.Diagnostics.PerformanceCounterCategory.CategoryName and 
             System.Diagnostics.PerformanceCounterCategory.MachineName properties; otherwise, false.
        """
        pass

    @staticmethod
    def Create(categoryName, categoryHelp, *__args):
        """
        Create(categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory
        
            Registers the custom performance counter category containing the specified counters on the local 
             computer.
        
        
            categoryName: The name of the custom performance counter category to create and register with the system.
            categoryHelp: A description of the custom category.
            counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part 
             of the new category.
        
            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category, 
             or performance object.
        
        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory
        
            Registers the custom performance counter category containing the specified counters on the local 
             computer.
        
        
            categoryName: The name of the custom performance counter category to create and register with the system.
            categoryHelp: A description of the custom category.
            categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values.
            counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part 
             of the new category.
        
            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category, 
             or performance object.
        
        Create(categoryName: str, categoryHelp: str, counterName: str, counterHelp: str) -> PerformanceCounterCategory
        
            Registers a custom performance counter category containing a single counter of type 
             NumberOfItems32 on the local computer.
        
        
            categoryName: The name of the custom performance counter category to create and register with the system.
            categoryHelp: A description of the custom category.
            counterName: The name of a new counter, of type NumberOfItems32, to create as part of the new category.
            counterHelp: A description of the counter that is associated with the new custom category.
            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category, 
             or performance object.
        
        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterName: str, counterHelp: str) -> PerformanceCounterCategory
        
            Registers the custom performance counter category containing a single counter of type 
             System.Diagnostics.PerformanceCounterType.NumberOfItems32 on the local computer.
        
        
            categoryName: The name of the custom performance counter category to create and register with the system.
            categoryHelp: A description of the custom category.
            categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values specifying whether the 
             category is System.Diagnostics.PerformanceCounterCategoryType.MultiInstance, 
             System.Diagnostics.PerformanceCounterCategoryType.SingleInstance, or 
             System.Diagnostics.PerformanceCounterCategoryType.Unknown.
        
            counterName: The name of a new counter to create as part of the new category.
            counterHelp: A description of the counter that is associated with the new custom category.
            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category, 
             or performance object.
        """
        pass

    @staticmethod
    def Delete(categoryName):
        """
        Delete(categoryName: str)
            Removes the category and its associated counters from the local computer.
        
            categoryName: The name of the custom performance counter category to delete.
        """
        pass

    @staticmethod
    def Exists(categoryName, machineName=None):
        """
        Exists(categoryName: str, machineName: str) -> bool
        
            Determines whether the category is registered on the specified computer.
        
            categoryName: The name of the performance counter category to look for.
            machineName: The name of the computer to examine for the category.
            Returns: true if the category is registered; otherwise, false.
        Exists(categoryName: str) -> bool
        
            Determines whether the category is registered on the local computer.
        
            categoryName: The name of the performance counter category to look for.
            Returns: true if the category is registered; otherwise, false.
        """
        pass

    @staticmethod
    def GetCategories(machineName=None):
        """
        GetCategories(machineName: str) -> Array[PerformanceCounterCategory]
        
            Retrieves a list of the performance counter categories that are registered on the specified 
             computer.
        
        
            machineName: The computer to look on.
            Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that 
             are registered on the specified computer.
        
        GetCategories() -> Array[PerformanceCounterCategory]
        
            Retrieves a list of the performance counter categories that are registered on the local computer.
            Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that 
             are registered on the local computer.
        """
        pass

    def GetCounters(self, instanceName=None):
        """
        GetCounters(self: PerformanceCounterCategory, instanceName: str) -> Array[PerformanceCounter]
        
            Retrieves a list of the counters in a performance counter category that contains one or more 
             instances.
        
        
            instanceName: The performance object instance for which to retrieve the list of associated counters.
            Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are 
             associated with the specified object instance of this performance counter category.
        
        GetCounters(self: PerformanceCounterCategory) -> Array[PerformanceCounter]
        
            Retrieves a list of the counters in a performance counter category that contains exactly one 
             instance.
        
            Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are 
             associated with this single-instance performance counter category.
        """
        pass

    def GetInstanceNames(self):
        """
        GetInstanceNames(self: PerformanceCounterCategory) -> Array[str]
        
            Retrieves the list of performance object instances that are associated with this category.
            Returns: An array of strings representing the performance object instance names that are associated with 
             this category or, if the category contains only one performance object instance, a single-entry 
             array that contains an empty string ("").
        """
        pass

    def InstanceExists(self, instanceName, categoryName=None, machineName=None):
        """
        InstanceExists(instanceName: str, categoryName: str, machineName: str) -> bool
        
            Determines whether a specified category on a specified computer contains the specified 
             performance object instance.
        
        
            instanceName: The performance object instance to search for.
            categoryName: The performance counter category to search.
            machineName: The name of the computer on which to look for the category instance pair.
            Returns: true if the category contains the specified performance object instance; otherwise, false.
        InstanceExists(instanceName: str, categoryName: str) -> bool
        
            Determines whether a specified category on the local computer contains the specified performance 
             object instance.
        
        
            instanceName: The performance object instance to search for.
            categoryName: The performance counter category to search.
            Returns: true if the category contains the specified performance object instance; otherwise, false.
        InstanceExists(self: PerformanceCounterCategory, instanceName: str) -> bool
        
            Determines whether the specified performance object instance exists in the category that is 
             identified by this System.Diagnostics.PerformanceCounterCategory object's 
             System.Diagnostics.PerformanceCounterCategory.CategoryName property.
        
        
            instanceName: The performance object instance in this performance counter category to search for.
            Returns: true if the category contains the specified performance object instance; otherwise, false.
        """
        pass

    def ReadCategory(self):
        """
        ReadCategory(self: PerformanceCounterCategory) -> InstanceDataCollectionCollection
        
            Reads all the counter and performance object instance data that is associated with this 
             performance counter category.
        
            Returns: An System.Diagnostics.InstanceDataCollectionCollection that contains the counter and performance 
             object instance data for the category.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, categoryName=None, machineName=None):
        """
        __new__(cls: type)
        __new__(cls: type, categoryName: str)
        __new__(cls: type, categoryName: str, machineName: str)
        """
        pass

    CategoryHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category's help text.

Get: CategoryHelp(self: PerformanceCounterCategory) -> str

"""

    CategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the performance object that defines this category.

Get: CategoryName(self: PerformanceCounterCategory) -> str

Set: CategoryName(self: PerformanceCounterCategory) = value
"""

    CategoryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the performance counter category type.

Get: CategoryType(self: PerformanceCounterCategory) -> PerformanceCounterCategoryType

"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the computer on which this category exists.

Get: MachineName(self: PerformanceCounterCategory) -> str

Set: MachineName(self: PerformanceCounterCategory) = value
"""



class PerformanceCounterCategoryType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates whether the performance counter category can have multiple instances.
    
    enum PerformanceCounterCategoryType, values: MultiInstance (1), SingleInstance (0), Unknown (-1)
    """
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

    MultiInstance = None
    SingleInstance = None
    Unknown = None
    value__ = None


class PerformanceCounterInstanceLifetime(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the lifetime of a performance counter instance.
    
    enum PerformanceCounterInstanceLifetime, values: Global (0), Process (1)
    """
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

    Global = None
    Process = None
    value__ = None


class PerformanceCounterManager(object, ICollectData):
    """
    Prepares performance data for the performance.dll the system loads when working with performance counters.
    
    PerformanceCounterManager()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class PerformanceCounterPermission(ResourcePermissionBase, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Allows control of code access permissions for System.Diagnostics.PerformanceCounter.
    
    PerformanceCounterPermission()
    PerformanceCounterPermission(state: PermissionState)
    PerformanceCounterPermission(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
    PerformanceCounterPermission(permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
    """
    def AddPermissionAccess(self, *args): #cannot find CLR method
        """
        AddPermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Adds a permission entry to the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to add.
        """
        pass

    def Clear(self, *args): #cannot find CLR method
        """
        Clear(self: ResourcePermissionBase)
            Clears the permission of the added permission entries.
        """
        pass

    def GetPermissionEntries(self, *args): #cannot find CLR method
        """
        GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry]
        
            Returns an array of the System.Security.Permissions.ResourcePermissionBaseEntry objects added to 
             this permission.
        
            Returns: An array of System.Security.Permissions.ResourcePermissionBaseEntry objects that were added to 
             this permission.
        """
        pass

    def RemovePermissionAccess(self, *args): #cannot find CLR method
        """
        RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)
            Removes a permission entry from the permission.
        
            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to remove.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
        __new__(cls: type, permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PermissionAccessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an enumeration value that describes the types of access that you are giving the resource.

"""

    PermissionEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of permission entries for this permissions request.

Get: PermissionEntries(self: PerformanceCounterPermission) -> PerformanceCounterPermissionEntryCollection

"""

    TagNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of strings that identify the resource you are protecting.

"""



class PerformanceCounterPermissionAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines access levels used by System.Diagnostics.PerformanceCounter permission classes.
    
    enum (flags) PerformanceCounterPermissionAccess, values: Administer (7), Browse (1), Instrument (3), None (0), Read (1), Write (2)
    """
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

    Administer = None
    Browse = None
    Instrument = None
    None = None
    Read = None
    value__ = None
    Write = None


class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows declaritive performance counter permission checks.
    
    PerformanceCounterPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: PerformanceCounterPermissionAttribute) -> IPermission
        
            Creates the permission based on the requested access levels that are set through the 
             System.Diagnostics.PerformanceCounterPermissionAttribute.PermissionAccess property on the 
             attribute.
        
            Returns: An System.Security.IPermission that represents the created permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action):
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the performance counter category.

Get: CategoryName(self: PerformanceCounterPermissionAttribute) -> str

Set: CategoryName(self: PerformanceCounterPermissionAttribute) = value
"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the computer name for the performance counter.

Get: MachineName(self: PerformanceCounterPermissionAttribute) -> str

Set: MachineName(self: PerformanceCounterPermissionAttribute) = value
"""

    PermissionAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the access levels used in the permissions request.

Get: PermissionAccess(self: PerformanceCounterPermissionAttribute) -> PerformanceCounterPermissionAccess

Set: PermissionAccess(self: PerformanceCounterPermissionAttribute) = value
"""



class PerformanceCounterPermissionEntry(object):
    """
    Defines the smallest unit of a code access security permission that is set for a System.Diagnostics.PerformanceCounter.
    
    PerformanceCounterPermissionEntry(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, permissionAccess, machineName, categoryName):
        """ __new__(cls: type, permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str) """
        pass

    CategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the performance counter category (performance object).

Get: CategoryName(self: PerformanceCounterPermissionEntry) -> str

"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the server on which the category of the performance counter resides.

Get: MachineName(self: PerformanceCounterPermissionEntry) -> str

"""

    PermissionAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the permission access level of the entry.

Get: PermissionAccess(self: PerformanceCounterPermissionEntry) -> PerformanceCounterPermissionAccess

"""



class PerformanceCounterPermissionEntryCollection(CollectionBase, IList, ICollection, IEnumerable):
    """ Contains a strongly typed collection of System.Diagnostics.PerformanceCounterPermissionEntry objects. """
    def Add(self, value):
        """
        Add(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int
        
            Adds a specified System.Diagnostics.PerformanceCounterPermissionEntry to this collection.
        
            value: The System.Diagnostics.PerformanceCounterPermissionEntry object to add.
            Returns: The zero-based index of the added System.Diagnostics.PerformanceCounterPermissionEntry object.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntryCollection)
            Appends a set of specified permission entries to this collection.
        
            value: A System.Diagnostics.PerformanceCounterPermissionEntryCollection that contains the permission 
             entries to add.
        
        AddRange(self: PerformanceCounterPermissionEntryCollection, value: Array[PerformanceCounterPermissionEntry])
            Appends a set of specified permission entries to this collection.
        
            value: An array of type System.Diagnostics.PerformanceCounterPermissionEntry objects that contains the 
             permission entries to add.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> bool
        
            Determines whether this collection contains a specified 
             System.Diagnostics.PerformanceCounterPermissionEntry object.
        
        
            value: The System.Diagnostics.PerformanceCounterPermissionEntry object to find.
            Returns: true if the specified System.Diagnostics.PerformanceCounterPermissionEntry object belongs to 
             this collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: PerformanceCounterPermissionEntryCollection, array: Array[PerformanceCounterPermissionEntry], index: int)
            Copies the permission entries from this collection to an array, starting at a particular index 
             of the array.
        
        
            array: An array of type System.Diagnostics.PerformanceCounterPermissionEntry that receives this 
             collection's permission entries.
        
            index: The zero-based index at which to begin copying the permission entries.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int
        
            Determines the index of a specified permission entry in this collection.
        
            value: The permission entry for which to search.
            Returns: The zero-based index of the specified permission entry, or -1 if the permission entry was not 
             found in the collection.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: PerformanceCounterPermissionEntryCollection, index: int, value: PerformanceCounterPermissionEntry)
            Inserts a permission entry into this collection at a specified index.
        
            index: The zero-based index of the collection at which to insert the permission entry.
            value: The permission entry to insert into this collection.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: PerformanceCounterPermissionEntryCollection)
            Performs additional custom processes after clearing the contents of the collection.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: PerformanceCounterPermissionEntryCollection, index: int, value: object)
            Performs additional custom processes before a new permission entry is inserted into the 
             collection.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the permission entry at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: PerformanceCounterPermissionEntryCollection, index: int, value: object)
            Performs additional custom processes when removing a new permission entry from the collection.
        
            index: The zero-based index at which value can be found.
            value: The permission entry to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: PerformanceCounterPermissionEntryCollection, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the collection.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the permission entry at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry)
            Removes a specified permission entry from this collection.
        
            value: The permission entry to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class PerformanceCounterType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the formula used to calculate the System.Diagnostics.PerformanceCounter.NextValue method for a System.Diagnostics.PerformanceCounter instance.
    
    enum PerformanceCounterType, values: AverageBase (1073939458), AverageCount64 (1073874176), AverageTimer32 (805438464), CounterDelta32 (4195328), CounterDelta64 (4195584), CounterMultiBase (1107494144), CounterMultiTimer (574686464), CounterMultiTimer100Ns (575735040), CounterMultiTimer100NsInverse (592512256), CounterMultiTimerInverse (591463680), CounterTimer (541132032), CounterTimerInverse (557909248), CountPerTimeInterval32 (4523008), CountPerTimeInterval64 (4523264), ElapsedTime (807666944), NumberOfItems32 (65536), NumberOfItems64 (65792), NumberOfItemsHEX32 (0), NumberOfItemsHEX64 (256), RateOfCountsPerSecond32 (272696320), RateOfCountsPerSecond64 (272696576), RawBase (1073939459), RawFraction (537003008), SampleBase (1073939457), SampleCounter (4260864), SampleFraction (549585920), Timer100Ns (542180608), Timer100NsInverse (558957824)
    """
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

    AverageBase = None
    AverageCount64 = None
    AverageTimer32 = None
    CounterDelta32 = None
    CounterDelta64 = None
    CounterMultiBase = None
    CounterMultiTimer = None
    CounterMultiTimer100Ns = None
    CounterMultiTimer100NsInverse = None
    CounterMultiTimerInverse = None
    CounterTimer = None
    CounterTimerInverse = None
    CountPerTimeInterval32 = None
    CountPerTimeInterval64 = None
    ElapsedTime = None
    NumberOfItems32 = None
    NumberOfItems64 = None
    NumberOfItemsHEX32 = None
    NumberOfItemsHEX64 = None
    RateOfCountsPerSecond32 = None
    RateOfCountsPerSecond64 = None
    RawBase = None
    RawFraction = None
    SampleBase = None
    SampleCounter = None
    SampleFraction = None
    Timer100Ns = None
    Timer100NsInverse = None
    value__ = None


class Process(Component, IComponent, IDisposable):
    """
    Provides access to local and remote processes and enables you to start and stop local system processes.
    
    Process()
    """
    def BeginErrorReadLine(self):
        """
        BeginErrorReadLine(self: Process)
            Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardError 
             stream of the application.
        """
        pass

    def BeginOutputReadLine(self):
        """
        BeginOutputReadLine(self: Process)
            Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardOutput 
             stream of the application.
        """
        pass

    def CancelErrorRead(self):
        """
        CancelErrorRead(self: Process)
            Cancels the asynchronous read operation on the redirected 
             System.Diagnostics.Process.StandardError stream of an application.
        """
        pass

    def CancelOutputRead(self):
        """
        CancelOutputRead(self: Process)
            Cancels the asynchronous read operation on the redirected 
             System.Diagnostics.Process.StandardOutput stream of an application.
        """
        pass

    def Close(self):
        """
        Close(self: Process)
            Frees all the resources that are associated with this component.
        """
        pass

    def CloseMainWindow(self):
        """
        CloseMainWindow(self: Process) -> bool
        
            Closes a process that has a user interface by sending a close message to its main window.
            Returns: true if the close message was successfully sent; false if the associated process does not have a 
             main window or if the main window is disabled (for example if a modal dialog is being shown).
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Process, disposing: bool)
            Release all resources used by this process.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    @staticmethod
    def EnterDebugMode():
        """
        EnterDebugMode()
            Puts a System.Diagnostics.Process component in state to interact with operating system processes 
             that run in a special mode by enabling the native property SeDebugPrivilege on the current 
             thread.
        """
        pass

    @staticmethod
    def GetCurrentProcess():
        """
        GetCurrentProcess() -> Process
        
            Gets a new System.Diagnostics.Process component and associates it with the currently active 
             process.
        
            Returns: A new System.Diagnostics.Process component associated with the process resource that is running 
             the calling application.
        """
        pass

    @staticmethod
    def GetProcessById(processId, machineName=None):
        """
        GetProcessById(processId: int) -> Process
        
            Returns a new System.Diagnostics.Process component, given the identifier of a process on the 
             local computer.
        
        
            processId: The system-unique identifier of a process resource.
            Returns: A System.Diagnostics.Process component that is associated with the local process resource 
             identified by the processId parameter.
        
        GetProcessById(processId: int, machineName: str) -> Process
        
            Returns a new System.Diagnostics.Process component, given a process identifier and the name of a 
             computer on the network.
        
        
            processId: The system-unique identifier of a process resource.
            machineName: The name of a computer on the network.
            Returns: A System.Diagnostics.Process component that is associated with a remote process resource 
             identified by the processId parameter.
        """
        pass

    @staticmethod
    def GetProcesses(machineName=None):
        """
        GetProcesses(machineName: str) -> Array[Process]
        
            Creates a new System.Diagnostics.Process component for each process resource on the specified 
             computer.
        
        
            machineName: The computer from which to read the list of processes.
            Returns: An array of type System.Diagnostics.Process that represents all the process resources running on 
             the specified computer.
        
        GetProcesses() -> Array[Process]
        
            Creates a new System.Diagnostics.Process component for each process resource on the local 
             computer.
        
            Returns: An array of type System.Diagnostics.Process that represents all the process resources running on 
             the local computer.
        """
        pass

    @staticmethod
    def GetProcessesByName(processName, machineName=None):
        """
        GetProcessesByName(processName: str, machineName: str) -> Array[Process]
        
            Creates an array of new System.Diagnostics.Process components and associates them with all the 
             process resources on a remote computer that share the specified process name.
        
        
            processName: The friendly name of the process.
            machineName: The name of a computer on the network.
            Returns: An array of type System.Diagnostics.Process that represents the process resources running the 
             specified application or file.
        
        GetProcessesByName(processName: str) -> Array[Process]
        
            Creates an array of new System.Diagnostics.Process components and associates them with all the 
             process resources on the local computer that share the specified process name.
        
        
            processName: The friendly name of the process.
            Returns: An array of type System.Diagnostics.Process that represents the process resources running the 
             specified application or file.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def Kill(self):
        """
        Kill(self: Process)
            Immediately stops the associated process.
        """
        pass

    @staticmethod
    def LeaveDebugMode():
        """
        LeaveDebugMode()
            Takes a System.Diagnostics.Process component out of the state that lets it interact with 
             operating system processes that run in a special mode.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnExited(self, *args): #cannot find CLR method
        """
        OnExited(self: Process)
            Raises the System.Diagnostics.Process.Exited event.
        """
        pass

    def Refresh(self):
        """
        Refresh(self: Process)
            Discards any information about the associated process that has been cached inside the process 
             component.
        """
        pass

    def Start(self, *__args):
        """
        Start(fileName: str) -> Process
        
            Starts a process resource by specifying the name of a document or application file and 
             associates the resource with a new System.Diagnostics.Process component.
        
        
            fileName: The name of a document or application file to run in the process.
            Returns: A new System.Diagnostics.Process component that is associated with the process resource, or 
             null, if no process resource is started (for example, if an existing process is reused).
        
        Start(fileName: str, arguments: str) -> Process
        
            Starts a process resource by specifying the name of an application and a set of command-line 
             arguments, and associates the resource with a new System.Diagnostics.Process component.
        
        
            fileName: The name of an application file to run in the process.
            arguments: Command-line arguments to pass when starting the process.
            Returns: A new System.Diagnostics.Process component that is associated with the process, or null, if no 
             process resource is started (for example, if an existing process is reused).
        
        Start(startInfo: ProcessStartInfo) -> Process
        
            Starts the process resource that is specified by the parameter containing process start 
             information (for example, the file name of the process to start) and associates the resource 
             with a new System.Diagnostics.Process component.
        
        
            startInfo: The System.Diagnostics.ProcessStartInfo that contains the information that is used to start the 
             process, including the file name and any command-line arguments.
        
            Returns: A new System.Diagnostics.Process component that is associated with the process resource, or null 
             if no process resource is started (for example, if an existing process is reused).
        
        Start(self: Process) -> bool
        
            Starts (or reuses) the process resource that is specified by the 
             System.Diagnostics.Process.StartInfo property of this System.Diagnostics.Process component and 
             associates it with the component.
        
            Returns: true if a process resource is started; false if no new process resource is started (for example, 
             if an existing process is reused).
        
        Start(fileName: str, userName: str, password: SecureString, domain: str) -> Process
        
            Starts a process resource by specifying the name of an application, a user name, a password, and 
             a domain and associates the resource with a new System.Diagnostics.Process component.
        
        
            fileName: The name of an application file to run in the process.
            userName: The user name to use when starting the process.
            password: A System.Security.SecureString that contains the password to use when starting the process.
            domain: The domain to use when starting the process.
            Returns: A new System.Diagnostics.Process component that is associated with the process resource, or null 
             if no process resource is started (for example, if an existing process is reused).
        
        Start(fileName: str, arguments: str, userName: str, password: SecureString, domain: str) -> Process
        
            Starts a process resource by specifying the name of an application, a set of command-line 
             arguments, a user name, a password, and a domain and associates the resource with a new 
             System.Diagnostics.Process component.
        
        
            fileName: The name of an application file to run in the process.
            arguments: Command-line arguments to pass when starting the process.
            userName: The user name to use when starting the process.
            password: A System.Security.SecureString that contains the password to use when starting the process.
            domain: The domain to use when starting the process.
            Returns: A new System.Diagnostics.Process component that is associated with the process resource, or null 
             if no process resource is started (for example, if an existing process is reused).
        """
        pass

    def ToString(self):
        """
        ToString(self: Process) -> str
        
            Formats the process's name as a string, combined with the parent component type, if applicable.
            Returns: The System.Diagnostics.Process.ProcessName, combined with the base component's 
             System.Object.ToString return value.
        """
        pass

    def WaitForExit(self, milliseconds=None):
        """
        WaitForExit(self: Process)
            Instructs the System.Diagnostics.Process component to wait indefinitely for the associated 
             process to exit.
        
        WaitForExit(self: Process, milliseconds: int) -> bool
        
            Instructs the System.Diagnostics.Process component to wait the specified number of milliseconds 
             for the associated process to exit.
        
        
            milliseconds: The amount of time, in milliseconds, to wait for the associated process to exit. The maximum is 
             the largest possible value of a 32-bit integer, which represents infinity to the operating 
             system.
        
            Returns: true if the associated process has exited; otherwise, false.
        """
        pass

    def WaitForInputIdle(self, milliseconds=None):
        """
        WaitForInputIdle(self: Process) -> bool
        
            Causes the System.Diagnostics.Process component to wait indefinitely for the associated process 
             to enter an idle state. This overload applies only to processes with a user interface and, 
             therefore, a message loop.
        
            Returns: true if the associated process has reached an idle state.
        WaitForInputIdle(self: Process, milliseconds: int) -> bool
        
            Causes the System.Diagnostics.Process component to wait the specified number of milliseconds for 
             the associated process to enter an idle state. This overload applies only to processes with a 
             user interface and, therefore, a message loop.
        
        
            milliseconds: A value of 1 to System.Int32.MaxValue that specifies the amount of time, in milliseconds, to 
             wait for the associated process to become idle. A value of 0 specifies an immediate return, and 
             a value of -1 specifies an infinite wait.
        
            Returns: true if the associated process has reached an idle state; otherwise, false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BasePriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base priority of the associated process.

Get: BasePriority(self: Process) -> int

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    EnableRaisingEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the System.Diagnostics.Process.Exited event should be raised when the process terminates.

Get: EnableRaisingEvents(self: Process) -> bool

Set: EnableRaisingEvents(self: Process) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    ExitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value that the associated process specified when it terminated.

Get: ExitCode(self: Process) -> int

"""

    ExitTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time that the associated process exited.

Get: ExitTime(self: Process) -> DateTime

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the native handle of the associated process.

Get: Handle(self: Process) -> IntPtr

"""

    HandleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of handles opened by the process.

Get: HandleCount(self: Process) -> int

"""

    HasExited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the associated process has been terminated.

Get: HasExited(self: Process) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier for the associated process.

Get: Id(self: Process) -> int

"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the computer the associated process is running on.

Get: MachineName(self: Process) -> str

"""

    MainModule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the main module for the associated process.

Get: MainModule(self: Process) -> ProcessModule

"""

    MainWindowHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle of the main window of the associated process.

Get: MainWindowHandle(self: Process) -> IntPtr

"""

    MainWindowTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the caption of the main window of the process.

Get: MainWindowTitle(self: Process) -> str

"""

    MaxWorkingSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowable working set size for the associated process.

Get: MaxWorkingSet(self: Process) -> IntPtr

Set: MaxWorkingSet(self: Process) = value
"""

    MinWorkingSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum allowable working set size for the associated process.

Get: MinWorkingSet(self: Process) -> IntPtr

Set: MinWorkingSet(self: Process) = value
"""

    Modules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the modules that have been loaded by the associated process.

Get: Modules(self: Process) -> ProcessModuleCollection

"""

    NonpagedSystemMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the nonpaged system memory size allocated to this process.

Get: NonpagedSystemMemorySize(self: Process) -> int

"""

    NonpagedSystemMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of nonpaged system memory allocated for the associated process.

Get: NonpagedSystemMemorySize64(self: Process) -> Int64

"""

    PagedMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paged memory size.

Get: PagedMemorySize(self: Process) -> int

"""

    PagedMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of paged memory allocated for the associated process.

Get: PagedMemorySize64(self: Process) -> Int64

"""

    PagedSystemMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paged system memory size.

Get: PagedSystemMemorySize(self: Process) -> int

"""

    PagedSystemMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of pageable system memory allocated for the associated process.

Get: PagedSystemMemorySize64(self: Process) -> Int64

"""

    PeakPagedMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the peak paged memory size.

Get: PeakPagedMemorySize(self: Process) -> int

"""

    PeakPagedMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum amount of memory in the virtual memory paging file used by the associated process.

Get: PeakPagedMemorySize64(self: Process) -> Int64

"""

    PeakVirtualMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the peak virtual memory size.

Get: PeakVirtualMemorySize(self: Process) -> int

"""

    PeakVirtualMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum amount of virtual memory used by the associated process.

Get: PeakVirtualMemorySize64(self: Process) -> Int64

"""

    PeakWorkingSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the peak working set size for the associated process.

Get: PeakWorkingSet(self: Process) -> int

"""

    PeakWorkingSet64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum amount of physical memory used by the associated process.

Get: PeakWorkingSet64(self: Process) -> Int64

"""

    PriorityBoostEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the associated process priority should temporarily be boosted by the operating system when the main window has the focus.

Get: PriorityBoostEnabled(self: Process) -> bool

Set: PriorityBoostEnabled(self: Process) = value
"""

    PriorityClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the overall priority category for the associated process.

Get: PriorityClass(self: Process) -> ProcessPriorityClass

Set: PriorityClass(self: Process) = value
"""

    PrivateMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the private memory size.

Get: PrivateMemorySize(self: Process) -> int

"""

    PrivateMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of private memory allocated for the associated process.

Get: PrivateMemorySize64(self: Process) -> Int64

"""

    PrivilegedProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the privileged processor time for this process.

Get: PrivilegedProcessorTime(self: Process) -> TimeSpan

"""

    ProcessName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the process.

Get: ProcessName(self: Process) -> str

"""

    ProcessorAffinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the processors on which the threads in this process can be scheduled to run.

Get: ProcessorAffinity(self: Process) -> IntPtr

Set: ProcessorAffinity(self: Process) = value
"""

    Responding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the user interface of the process is responding.

Get: Responding(self: Process) -> bool

"""

    SafeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SafeHandle(self: Process) -> SafeProcessHandle

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Terminal Services session identifier for the associated process.

Get: SessionId(self: Process) -> int

"""

    StandardError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a stream used to read the error output of the application.

Get: StandardError(self: Process) -> StreamReader

"""

    StandardInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a stream used to write the input of the application.

Get: StandardInput(self: Process) -> StreamWriter

"""

    StandardOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a stream used to read the output of the application.

Get: StandardOutput(self: Process) -> StreamReader

"""

    StartInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the properties to pass to the System.Diagnostics.Process.Start method of the System.Diagnostics.Process.

Get: StartInfo(self: Process) -> ProcessStartInfo

Set: StartInfo(self: Process) = value
"""

    StartTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time that the associated process was started.

Get: StartTime(self: Process) -> DateTime

"""

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object used to marshal the event handler calls that are issued as a result of a process exit event.

Get: SynchronizingObject(self: Process) -> ISynchronizeInvoke

Set: SynchronizingObject(self: Process) = value
"""

    Threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of threads that are running in the associated process.

Get: Threads(self: Process) -> ProcessThreadCollection

"""

    TotalProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total processor time for this process.

Get: TotalProcessorTime(self: Process) -> TimeSpan

"""

    UserProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user processor time for this process.

Get: UserProcessorTime(self: Process) -> TimeSpan

"""

    VirtualMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the process's virtual memory.

Get: VirtualMemorySize(self: Process) -> int

"""

    VirtualMemorySize64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of the virtual memory allocated for the associated process.

Get: VirtualMemorySize64(self: Process) -> Int64

"""

    WorkingSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the associated process's physical memory usage.

Get: WorkingSet(self: Process) -> int

"""

    WorkingSet64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of physical memory allocated for the associated process.

Get: WorkingSet64(self: Process) -> Int64

"""


    ErrorDataReceived = None
    Exited = None
    OutputDataReceived = None


class ProcessModule(Component, IComponent, IDisposable):
    """ Represents a.dll or .exe file that is loaded into a particular process. """
    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ToString(self):
        """
        ToString(self: ProcessModule) -> str
        
            Converts the name of the module to a string.
            Returns: The value of the System.Diagnostics.ProcessModule.ModuleName property.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the memory address where the module was loaded.

Get: BaseAddress(self: ProcessModule) -> IntPtr

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    EntryPointAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the memory address for the function that runs when the system loads and runs the module.

Get: EntryPointAddress(self: ProcessModule) -> IntPtr

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full path to the module.

Get: FileName(self: ProcessModule) -> str

"""

    FileVersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets version information about the module.

Get: FileVersionInfo(self: ProcessModule) -> FileVersionInfo

"""

    ModuleMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of memory that is required to load the module.

Get: ModuleMemorySize(self: ProcessModule) -> int

"""

    ModuleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the process module.

Get: ModuleName(self: ProcessModule) -> str

"""



class ProcessModuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.ProcessModule objects.
    
    ProcessModuleCollection(processModules: Array[ProcessModule])
    """
    def Contains(self, module):
        """
        Contains(self: ProcessModuleCollection, module: ProcessModule) -> bool
        
            Determines whether the specified process module exists in the collection.
        
            module: A System.Diagnostics.ProcessModule instance that indicates the module to find in this collection.
            Returns: true if the module exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ProcessModuleCollection, array: Array[ProcessModule], index: int)
            Copies an array of System.Diagnostics.ProcessModule instances to the collection, at the 
             specified index.
        
        
            array: An array of System.Diagnostics.ProcessModule instances to add to the collection.
            index: The location at which to add the new instances.
        """
        pass

    def IndexOf(self, module):
        """
        IndexOf(self: ProcessModuleCollection, module: ProcessModule) -> int
        
            Provides the location of a specified module within the collection.
        
            module: The System.Diagnostics.ProcessModule whose index is retrieved.
            Returns: The zero-based index that defines the location of the module within the 
             System.Diagnostics.ProcessModuleCollection.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, processModules):
        """
        __new__(cls: type)
        __new__(cls: type, processModules: Array[ProcessModule])
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class ProcessPriorityClass(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the priority that the system associates with a process. This value, together with the priority value of each thread of the process, determines each thread's base priority level.
    
    enum ProcessPriorityClass, values: AboveNormal (32768), BelowNormal (16384), High (128), Idle (64), Normal (32), RealTime (256)
    """
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

    AboveNormal = None
    BelowNormal = None
    High = None
    Idle = None
    Normal = None
    RealTime = None
    value__ = None


class ProcessStartInfo(object):
    """
    Specifies a set of values that are used when you start a process.
    
    ProcessStartInfo()
    ProcessStartInfo(fileName: str)
    ProcessStartInfo(fileName: str, arguments: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, fileName=None, arguments=None):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, arguments: str)
        """
        pass

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the set of command-line arguments to use when starting the application.

Get: Arguments(self: ProcessStartInfo) -> str

Set: Arguments(self: ProcessStartInfo) = value
"""

    CreateNoWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to start the process in a new window.

Get: CreateNoWindow(self: ProcessStartInfo) -> bool

Set: CreateNoWindow(self: ProcessStartInfo) = value
"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the domain to use when starting the process.

Get: Domain(self: ProcessStartInfo) -> str

Set: Domain(self: ProcessStartInfo) = value
"""

    Environment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Environment(self: ProcessStartInfo) -> IDictionary[str, str]

"""

    EnvironmentVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets search paths for files, directories for temporary files, application-specific options, and other similar information.

Get: EnvironmentVariables(self: ProcessStartInfo) -> StringDictionary

"""

    ErrorDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether an error dialog box is displayed to the user if the process cannot be started.

Get: ErrorDialog(self: ProcessStartInfo) -> bool

Set: ErrorDialog(self: ProcessStartInfo) = value
"""

    ErrorDialogParentHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window handle to use when an error dialog box is shown for a process that cannot be started.

Get: ErrorDialogParentHandle(self: ProcessStartInfo) -> IntPtr

Set: ErrorDialogParentHandle(self: ProcessStartInfo) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the application or document to start.

Get: FileName(self: ProcessStartInfo) -> str

Set: FileName(self: ProcessStartInfo) = value
"""

    LoadUserProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the Windows user profile is to be loaded from the registry.

Get: LoadUserProfile(self: ProcessStartInfo) -> bool

Set: LoadUserProfile(self: ProcessStartInfo) = value
"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a secure string that contains the user password to use when starting the process.

Get: Password(self: ProcessStartInfo) -> SecureString

Set: Password(self: ProcessStartInfo) = value
"""

    PasswordInClearText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PasswordInClearText(self: ProcessStartInfo) -> str

Set: PasswordInClearText(self: ProcessStartInfo) = value
"""

    RedirectStandardError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the error output of an application is written to the System.Diagnostics.Process.StandardError stream.

Get: RedirectStandardError(self: ProcessStartInfo) -> bool

Set: RedirectStandardError(self: ProcessStartInfo) = value
"""

    RedirectStandardInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the input for an application is read from the System.Diagnostics.Process.StandardInput stream.

Get: RedirectStandardInput(self: ProcessStartInfo) -> bool

Set: RedirectStandardInput(self: ProcessStartInfo) = value
"""

    RedirectStandardOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the output of an application is written to the System.Diagnostics.Process.StandardOutput stream.

Get: RedirectStandardOutput(self: ProcessStartInfo) -> bool

Set: RedirectStandardOutput(self: ProcessStartInfo) = value
"""

    StandardErrorEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the preferred encoding for error output.

Get: StandardErrorEncoding(self: ProcessStartInfo) -> Encoding

Set: StandardErrorEncoding(self: ProcessStartInfo) = value
"""

    StandardOutputEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the preferred encoding for standard output.

Get: StandardOutputEncoding(self: ProcessStartInfo) -> Encoding

Set: StandardOutputEncoding(self: ProcessStartInfo) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user name to be used when starting the process.

Get: UserName(self: ProcessStartInfo) -> str

Set: UserName(self: ProcessStartInfo) = value
"""

    UseShellExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to use the operating system shell to start the process.

Get: UseShellExecute(self: ProcessStartInfo) -> bool

Set: UseShellExecute(self: ProcessStartInfo) = value
"""

    Verb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the verb to use when opening the application or document specified by the System.Diagnostics.ProcessStartInfo.FileName property.

Get: Verb(self: ProcessStartInfo) -> str

Set: Verb(self: ProcessStartInfo) = value
"""

    Verbs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of verbs associated with the type of file specified by the System.Diagnostics.ProcessStartInfo.FileName property.

Get: Verbs(self: ProcessStartInfo) -> Array[str]

"""

    WindowStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window state to use when the process is started.

Get: WindowStyle(self: ProcessStartInfo) -> ProcessWindowStyle

Set: WindowStyle(self: ProcessStartInfo) = value
"""

    WorkingDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial directory for the process to be started.

Get: WorkingDirectory(self: ProcessStartInfo) -> str

Set: WorkingDirectory(self: ProcessStartInfo) = value
"""



class ProcessThread(Component, IComponent, IDisposable):
    """ Represents an operating system process thread. """
    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ResetIdealProcessor(self):
        """
        ResetIdealProcessor(self: ProcessThread)
            Resets the ideal processor for this thread to indicate that there is no single ideal processor. 
             In other words, so that any processor is ideal.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BasePriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base priority of the thread.

Get: BasePriority(self: ProcessThread) -> int

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    CurrentPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current priority of the thread.

Get: CurrentPriority(self: ProcessThread) -> int

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier of the thread.

Get: Id(self: ProcessThread) -> int

"""

    IdealProcessor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the preferred processor for this thread to run on.

Set: IdealProcessor(self: ProcessThread) = value
"""

    PriorityBoostEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the operating system should temporarily boost the priority of the associated thread whenever the main window of the thread's process receives the focus.

Get: PriorityBoostEnabled(self: ProcessThread) -> bool

Set: PriorityBoostEnabled(self: ProcessThread) = value
"""

    PriorityLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the priority level of the thread.

Get: PriorityLevel(self: ProcessThread) -> ThreadPriorityLevel

Set: PriorityLevel(self: ProcessThread) = value
"""

    PrivilegedProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of time that the thread has spent running code inside the operating system core.

Get: PrivilegedProcessorTime(self: ProcessThread) -> TimeSpan

"""

    ProcessorAffinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the processors on which the associated thread can run.

Set: ProcessorAffinity(self: ProcessThread) = value
"""

    StartAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the memory address of the function that the operating system called that started this thread.

Get: StartAddress(self: ProcessThread) -> IntPtr

"""

    StartTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time that the operating system started the thread.

Get: StartTime(self: ProcessThread) -> DateTime

"""

    ThreadState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of this thread.

Get: ThreadState(self: ProcessThread) -> ThreadState

"""

    TotalProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total amount of time that this thread has spent using the processor.

Get: TotalProcessorTime(self: ProcessThread) -> TimeSpan

"""

    UserProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of time that the associated thread has spent running code inside the application.

Get: UserProcessorTime(self: ProcessThread) -> TimeSpan

"""

    WaitReason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reason that the thread is waiting.

Get: WaitReason(self: ProcessThread) -> ThreadWaitReason

"""



class ProcessThreadCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Provides a strongly typed collection of System.Diagnostics.ProcessThread objects.
    
    ProcessThreadCollection(processThreads: Array[ProcessThread])
    """
    def Add(self, thread):
        """
        Add(self: ProcessThreadCollection, thread: ProcessThread) -> int
        
            Appends a process thread to the collection.
        
            thread: The thread to add to the collection.
            Returns: The zero-based index of the thread in the collection.
        """
        pass

    def Contains(self, thread):
        """
        Contains(self: ProcessThreadCollection, thread: ProcessThread) -> bool
        
            Determines whether the specified process thread exists in the collection.
        
            thread: A System.Diagnostics.ProcessThread instance that indicates the thread to find in this collection.
            Returns: true if the thread exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ProcessThreadCollection, array: Array[ProcessThread], index: int)
            Copies an array of System.Diagnostics.ProcessThread instances to the collection, at the 
             specified index.
        
        
            array: An array of System.Diagnostics.ProcessThread instances to add to the collection.
            index: The location at which to add the new instances.
        """
        pass

    def IndexOf(self, thread):
        """
        IndexOf(self: ProcessThreadCollection, thread: ProcessThread) -> int
        
            Provides the location of a specified thread within the collection.
        
            thread: The System.Diagnostics.ProcessThread whose index is retrieved.
            Returns: The zero-based index that defines the location of the thread within the 
             System.Diagnostics.ProcessThreadCollection.
        """
        pass

    def Insert(self, index, thread):
        """
        Insert(self: ProcessThreadCollection, index: int, thread: ProcessThread)
            Inserts a process thread at the specified location in the collection.
        
            index: The zero-based index indicating the location at which to insert the thread.
            thread: The thread to insert into the collection.
        """
        pass

    def Remove(self, thread):
        """
        Remove(self: ProcessThreadCollection, thread: ProcessThread)
            Deletes a process thread from the collection.
        
            thread: The thread to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, processThreads):
        """
        __new__(cls: type)
        __new__(cls: type, processThreads: Array[ProcessThread])
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class ProcessWindowStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specified how a new window should appear when the system starts a process.
    
    enum ProcessWindowStyle, values: Hidden (1), Maximized (3), Minimized (2), Normal (0)
    """
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

    Hidden = None
    Maximized = None
    Minimized = None
    Normal = None
    value__ = None


class SourceFilter(TraceFilter):
    """
    Indicates whether a listener should trace a message based on the source of a trace.
    
    SourceFilter(source: str)
    """
    def ShouldTrace(self, cache, source, eventType, id, formatOrMessage, args, data1, data):
        """
        ShouldTrace(self: SourceFilter, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: Array[object], data1: object, data: Array[object]) -> bool
        
            Determines whether the trace listener should trace the event.
        
            cache: An object that represents the information cache for the trace event.
            source: The name of the source.
            eventType: One of the enumeration values that identifies the event type.
            id: A trace identifier number.
            formatOrMessage: The format to use for writing an array of arguments or a message to write.
            args: An array of argument objects.
            data1: A trace data object.
            data: An array of trace data objects.
            Returns: true if the trace should be produced; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source):
        """ __new__(cls: type, source: str) """
        pass

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the trace source.

Get: Source(self: SourceFilter) -> str

Set: Source(self: SourceFilter) = value
"""



class SourceLevels(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the levels of trace messages filtered by the source switch and event type filter.
    
    enum (flags) SourceLevels, values: ActivityTracing (65280), All (-1), Critical (1), Error (3), Information (15), Off (0), Verbose (31), Warning (7)
    """
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

    ActivityTracing = None
    All = None
    Critical = None
    Error = None
    Information = None
    Off = None
    value__ = None
    Verbose = None
    Warning = None


class SourceSwitch(Switch):
    """
    Provides a multilevel switch to control tracing and debug output without recompiling your code.
    
    SourceSwitch(name: str)
    SourceSwitch(displayName: str, defaultSwitchValue: str)
    """
    def ShouldTrace(self, eventType):
        """
        ShouldTrace(self: SourceSwitch, eventType: TraceEventType) -> bool
        
            Determines if trace listeners should be called, based on the trace event type.
        
            eventType: One of the System.Diagnostics.TraceEventType values.
            Returns: True if the trace listeners should be called; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str)
        __new__(cls: type, displayName: str, defaultSwitchValue: str)
        """
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of the switch.

Get: Level(self: SourceSwitch) -> SourceLevels

Set: Level(self: SourceSwitch) = value
"""

    SwitchSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current setting for this switch.

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the switch.

"""



class StackFrame(object):
    """
    Provides information about a System.Diagnostics.StackFrame, which represents a function call on the call stack for the current thread.
    
    StackFrame()
    StackFrame(fNeedFileInfo: bool)
    StackFrame(skipFrames: int)
    StackFrame(skipFrames: int, fNeedFileInfo: bool)
    StackFrame(fileName: str, lineNumber: int)
    StackFrame(fileName: str, lineNumber: int, colNumber: int)
    """
    def GetFileColumnNumber(self):
        """
        GetFileColumnNumber(self: StackFrame) -> int
        
            Gets the column number in the file that contains the code that is executing. This information is 
             typically extracted from the debugging symbols for the executable.
        
            Returns: The file column number, or 0 (zero) if the file column number cannot be determined.
        """
        pass

    def GetFileLineNumber(self):
        """
        GetFileLineNumber(self: StackFrame) -> int
        
            Gets the line number in the file that contains the code that is executing. This information is 
             typically extracted from the debugging symbols for the executable.
        
            Returns: The file line number, or 0 (zero) if the file line number cannot be determined.
        """
        pass

    def GetFileName(self):
        """
        GetFileName(self: StackFrame) -> str
        
            Gets the file name that contains the code that is executing. This information is typically 
             extracted from the debugging symbols for the executable.
        
            Returns: The file name, or null if the file name cannot be determined.
        """
        pass

    def GetILOffset(self):
        """
        GetILOffset(self: StackFrame) -> int
        
            Gets the offset from the start of the Microsoft intermediate language (MSIL) code for the method 
             that is executing. This offset might be an approximation depending on whether or not the 
             just-in-time (JIT) compiler is generating debugging code. The generation of this debugging 
             information is controlled by the System.Diagnostics.DebuggableAttribute.
        
            Returns: The offset from the start of the MSIL code for the method that is executing.
        """
        pass

    def GetMethod(self):
        """
        GetMethod(self: StackFrame) -> MethodBase
        
            Gets the method in which the frame is executing.
            Returns: The method in which the frame is executing.
        """
        pass

    def GetNativeOffset(self):
        """
        GetNativeOffset(self: StackFrame) -> int
        
            Gets the offset from the start of the native just-in-time (JIT)-compiled code for the method 
             that is being executed. The generation of this debugging information is controlled by the 
             System.Diagnostics.DebuggableAttribute class.
        
            Returns: The offset from the start of the JIT-compiled code for the method that is being executed.
        """
        pass

    def ToString(self):
        """
        ToString(self: StackFrame) -> str
        
            Builds a readable representation of the stack trace.
            Returns: A readable representation of the stack trace.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, fNeedFileInfo: bool)
        __new__(cls: type, skipFrames: int)
        __new__(cls: type, skipFrames: int, fNeedFileInfo: bool)
        __new__(cls: type, fileName: str, lineNumber: int)
        __new__(cls: type, fileName: str, lineNumber: int, colNumber: int)
        """
        pass

    OFFSET_UNKNOWN = -1


class StackTrace(object):
    """
    Represents a stack trace, which is an ordered collection of one or more stack frames.
    
    StackTrace()
    StackTrace(fNeedFileInfo: bool)
    StackTrace(skipFrames: int)
    StackTrace(skipFrames: int, fNeedFileInfo: bool)
    StackTrace(e: Exception)
    StackTrace(e: Exception, fNeedFileInfo: bool)
    StackTrace(e: Exception, skipFrames: int)
    StackTrace(e: Exception, skipFrames: int, fNeedFileInfo: bool)
    StackTrace(frame: StackFrame)
    StackTrace(targetThread: Thread, needFileInfo: bool)
    """
    def GetFrame(self, index):
        """
        GetFrame(self: StackTrace, index: int) -> StackFrame
        
            Gets the specified stack frame.
        
            index: The index of the stack frame requested.
            Returns: The specified stack frame.
        """
        pass

    def GetFrames(self):
        """
        GetFrames(self: StackTrace) -> Array[StackFrame]
        
            Returns a copy of all stack frames in the current stack trace.
            Returns: An array of type System.Diagnostics.StackFrame representing the function calls in the stack 
             trace.
        """
        pass

    def ToString(self):
        """
        ToString(self: StackTrace) -> str
        
            Builds a readable representation of the stack trace.
            Returns: A readable representation of the stack trace.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, fNeedFileInfo: bool)
        __new__(cls: type, skipFrames: int)
        __new__(cls: type, skipFrames: int, fNeedFileInfo: bool)
        __new__(cls: type, e: Exception)
        __new__(cls: type, e: Exception, fNeedFileInfo: bool)
        __new__(cls: type, e: Exception, skipFrames: int)
        __new__(cls: type, e: Exception, skipFrames: int, fNeedFileInfo: bool)
        __new__(cls: type, frame: StackFrame)
        __new__(cls: type, targetThread: Thread, needFileInfo: bool)
        """
        pass

    FrameCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of frames in the stack trace.

Get: FrameCount(self: StackTrace) -> int

"""


    METHODS_TO_SKIP = 0


class Stopwatch(object):
    """
    Provides a set of methods and properties that you can use to accurately measure elapsed time.
    
    Stopwatch()
    """
    @staticmethod
    def GetTimestamp():
        """
        GetTimestamp() -> Int64
        
            Gets the current number of ticks in the timer mechanism.
            Returns: A long integer representing the tick counter value of the underlying timer mechanism.
        """
        pass

    def Reset(self):
        """
        Reset(self: Stopwatch)
            Stops time interval measurement and resets the elapsed time to zero.
        """
        pass

    def Restart(self):
        """
        Restart(self: Stopwatch)
            Stops time interval measurement, resets the elapsed time to zero, and starts measuring elapsed 
             time.
        """
        pass

    def Start(self):
        """
        Start(self: Stopwatch)
            Starts, or resumes, measuring elapsed time for an interval.
        """
        pass

    @staticmethod
    def StartNew():
        """
        StartNew() -> Stopwatch
        
            Initializes a new System.Diagnostics.Stopwatch instance, sets the elapsed time property to zero, 
             and starts measuring elapsed time.
        
            Returns: A System.Diagnostics.Stopwatch that has just begun measuring elapsed time.
        """
        pass

    def Stop(self):
        """
        Stop(self: Stopwatch)
            Stops measuring elapsed time for an interval.
        """
        pass

    Elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total elapsed time measured by the current instance.

Get: Elapsed(self: Stopwatch) -> TimeSpan

"""

    ElapsedMilliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total elapsed time measured by the current instance, in milliseconds.

Get: ElapsedMilliseconds(self: Stopwatch) -> Int64

"""

    ElapsedTicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total elapsed time measured by the current instance, in timer ticks.

Get: ElapsedTicks(self: Stopwatch) -> Int64

"""

    IsRunning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Diagnostics.Stopwatch timer is running.

Get: IsRunning(self: Stopwatch) -> bool

"""


    Frequency = None
    IsHighResolution = True


class SwitchAttribute(Attribute, _Attribute):
    """
    Identifies a switch used in an assembly, class, or member.
    
    SwitchAttribute(switchName: str, switchType: Type)
    """
    @staticmethod
    def GetAll(assembly):
        """
        GetAll(assembly: Assembly) -> Array[SwitchAttribute]
        
            Returns all switch attributes for the specified assembly.
        
            assembly: The assembly to check for switch attributes.
            Returns: An array that contains all the switch attributes for the assembly.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, switchName, switchType):
        """ __new__(cls: type, switchName: str, switchType: Type) """
        pass

    SwitchDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the description of the switch.

Get: SwitchDescription(self: SwitchAttribute) -> str

Set: SwitchDescription(self: SwitchAttribute) = value
"""

    SwitchName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the display name of the switch.

Get: SwitchName(self: SwitchAttribute) -> str

Set: SwitchName(self: SwitchAttribute) = value
"""

    SwitchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the switch.

Get: SwitchType(self: SwitchAttribute) -> Type

Set: SwitchType(self: SwitchAttribute) = value
"""



class SwitchLevelAttribute(Attribute, _Attribute):
    """
    Identifies the level type for a switch.
    
    SwitchLevelAttribute(switchLevelType: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, switchLevelType):
        """ __new__(cls: type, switchLevelType: Type) """
        pass

    SwitchLevelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type that determines whether a trace should be written.

Get: SwitchLevelType(self: SwitchLevelAttribute) -> Type

Set: SwitchLevelType(self: SwitchLevelAttribute) = value
"""



class ThreadPriorityLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the priority level of a thread.
    
    enum ThreadPriorityLevel, values: AboveNormal (1), BelowNormal (-1), Highest (2), Idle (-15), Lowest (-2), Normal (0), TimeCritical (15)
    """
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

    AboveNormal = None
    BelowNormal = None
    Highest = None
    Idle = None
    Lowest = None
    Normal = None
    TimeCritical = None
    value__ = None


class ThreadState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the current execution state of the thread.
    
    enum ThreadState, values: Initialized (0), Ready (1), Running (2), Standby (3), Terminated (4), Transition (6), Unknown (7), Wait (5)
    """
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

    Initialized = None
    Ready = None
    Running = None
    Standby = None
    Terminated = None
    Transition = None
    Unknown = None
    value__ = None
    Wait = None


class ThreadWaitReason(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the reason a thread is waiting.
    
    enum ThreadWaitReason, values: EventPairHigh (7), EventPairLow (8), ExecutionDelay (4), Executive (0), FreePage (1), LpcReceive (9), LpcReply (10), PageIn (2), PageOut (12), Suspended (5), SystemAllocation (3), Unknown (13), UserRequest (6), VirtualMemory (11)
    """
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

    EventPairHigh = None
    EventPairLow = None
    ExecutionDelay = None
    Executive = None
    FreePage = None
    LpcReceive = None
    LpcReply = None
    PageIn = None
    PageOut = None
    Suspended = None
    SystemAllocation = None
    Unknown = None
    UserRequest = None
    value__ = None
    VirtualMemory = None


class Trace(object):
    """ Provides a set of methods and properties that help you trace the execution of your code. This class cannot be inherited. """
    @staticmethod
    def Assert(condition, message=None, detailMessage=None):
        """
        Assert(condition: bool, message: str, detailMessage: str)
            Checks for a condition; if the condition is false, outputs two specified messages and displays a 
             message box that shows the call stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the specified messages are not 
             sent and the message box is not displayed.
        
            message: The message to send to the System.Diagnostics.Trace.Listeners collection.
            detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.
        Assert(condition: bool, message: str)
            Checks for a condition; if the condition is false, outputs a specified message and displays a 
             message box that shows the call stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, the specified message is not 
             sent and the message box is not displayed.
        
            message: The message to send to the System.Diagnostics.Trace.Listeners collection.
        Assert(condition: bool)
            Checks for a condition; if the condition is false, displays a message box that shows the call 
             stack.
        
        
            condition: The conditional expression to evaluate. If the condition is true, a failure message is not sent 
             and the message box is not displayed.
        """
        pass

    @staticmethod
    def Close():
        """
        Close()
            Flushes the output buffer, and then closes the System.Diagnostics.Trace.Listeners.
        """
        pass

    @staticmethod
    def Fail(message, detailMessage=None):
        """
        Fail(message: str, detailMessage: str)
            Emits an error message, and a detailed error message.
        
            message: A message to emit.
            detailMessage: A detailed message to emit.
        Fail(message: str)
            Emits the specified error message.
        
            message: A message to emit.
        """
        pass

    @staticmethod
    def Flush():
        """
        Flush()
            Flushes the output buffer, and causes buffered data to be written to the 
             System.Diagnostics.Trace.Listeners.
        """
        pass

    @staticmethod
    def Indent():
        """
        Indent()
            Increases the current System.Diagnostics.Trace.IndentLevel by one.
        """
        pass

    @staticmethod
    def Refresh():
        """
        Refresh()
            Refreshes the trace configuration data.
        """
        pass

    @staticmethod
    def TraceError(*__args):
        """
        TraceError(format: str, *args: Array[object])
            Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified array of objects and formatting information.
        
        
            format: A format string that contains zero or more format items, which correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        TraceError(message: str)
            Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified message.
        
        
            message: The informative message to write.
        """
        pass

    @staticmethod
    def TraceInformation(*__args):
        """
        TraceInformation(format: str, *args: Array[object])
            Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified array of objects and formatting information.
        
        
            format: A format string that contains zero or more format items, which correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        TraceInformation(message: str)
            Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified message.
        
        
            message: The informative message to write.
        """
        pass

    @staticmethod
    def TraceWarning(*__args):
        """
        TraceWarning(format: str, *args: Array[object])
            Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified array of objects and formatting information.
        
        
            format: A format string that contains zero or more format items, which correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        TraceWarning(message: str)
            Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners 
             collection using the specified message.
        
        
            message: The informative message to write.
        """
        pass

    @staticmethod
    def Unindent():
        """
        Unindent()
            Decreases the current System.Diagnostics.Trace.IndentLevel by one.
        """
        pass

    @staticmethod
    def Write(*__args):
        """
        Write(message: str, category: str)
            Writes a category name and a message to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        Write(value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Trace.Listeners collection.
        
        
            value: An System.Object name is sent to the System.Diagnostics.Trace.Listeners.
            category: A category name used to organize the output.
        Write(message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.
        
            message: A message to write.
        Write(value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection.
        
        
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
        """
        pass

    @staticmethod
    def WriteIf(condition, *__args):
        """
        WriteIf(condition: bool, message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            message: A message to write.
            category: A category name used to organize the output.
        WriteIf(condition: bool, value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
            category: A category name used to organize the output.
        WriteIf(condition: bool, message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if 
             a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            message: A message to write.
        WriteIf(condition: bool, value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
        """
        pass

    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine(message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection.
        
        
            message: A message to write.
            category: A category name used to organize the output.
        WriteLine(value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Trace.Listeners collection.
        
        
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
            category: A category name used to organize the output.
        WriteLine(message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.
        
            message: A message to write.
        WriteLine(value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection.
        
        
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
        """
        pass

    @staticmethod
    def WriteLineIf(condition, *__args):
        """
        WriteLineIf(condition: bool, message: str, category: str)
            Writes a category name and message to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            message: A message to write.
            category: A category name used to organize the output.
        WriteLineIf(condition: bool, value: object, category: str)
            Writes a category name and the value of the object's System.Object.ToString method to the trace 
             listeners in the System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
            category: A category name used to organize the output.
        WriteLineIf(condition: bool, message: str)
            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if 
             a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            message: A message to write.
        WriteLineIf(condition: bool, value: object)
            Writes the value of the object's System.Object.ToString method to the trace listeners in the 
             System.Diagnostics.Trace.Listeners collection if a condition is true.
        
        
            condition: true to cause a message to be written; otherwise, false.
            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
        """
        pass

    AutoFlush = False
    CorrelationManager = None
    IndentLevel = 0
    IndentSize = 4
    Listeners = None
    UseGlobalLock = True


class TraceEventCache(object):
    """
    Provides trace event data specific to a thread and a process.
    
    TraceEventCache()
    """
    Callstack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the call stack for the current thread.

Get: Callstack(self: TraceEventCache) -> str

"""

    DateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date and time at which the event trace occurred.

Get: DateTime(self: TraceEventCache) -> DateTime

"""

    LogicalOperationStack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the correlation data, contained in a stack.

Get: LogicalOperationStack(self: TraceEventCache) -> Stack

"""

    ProcessId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier of the current process.

Get: ProcessId(self: TraceEventCache) -> int

"""

    ThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique identifier for the current managed thread.

Get: ThreadId(self: TraceEventCache) -> str

"""

    Timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of ticks in the timer mechanism.

Get: Timestamp(self: TraceEventCache) -> Int64

"""



class TraceEventType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the type of event that has caused the trace.
    
    enum TraceEventType, values: Critical (1), Error (2), Information (8), Resume (2048), Start (256), Stop (512), Suspend (1024), Transfer (4096), Verbose (16), Warning (4)
    """
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
    Error = None
    Information = None
    Resume = None
    Start = None
    Stop = None
    Suspend = None
    Transfer = None
    value__ = None
    Verbose = None
    Warning = None


class TraceLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies what messages to output for the System.Diagnostics.Debug, System.Diagnostics.Trace and System.Diagnostics.TraceSwitch classes.
    
    enum TraceLevel, values: Error (1), Info (3), Off (0), Verbose (4), Warning (2)
    """
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

    Error = None
    Info = None
    Off = None
    value__ = None
    Verbose = None
    Warning = None


class TraceListenerCollection(object, IList, ICollection, IEnumerable):
    """ Provides a thread-safe list of System.Diagnostics.TraceListener objects. """
    def Add(self, listener):
        """
        Add(self: TraceListenerCollection, listener: TraceListener) -> int
        
            Adds a System.Diagnostics.TraceListener to the list.
        
            listener: A System.Diagnostics.TraceListener to add to the list.
            Returns: The position at which the new listener was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: TraceListenerCollection, value: TraceListenerCollection)
            Adds the contents of another System.Diagnostics.TraceListenerCollection to the list.
        
            value: Another System.Diagnostics.TraceListenerCollection whose contents are added to the list.
        AddRange(self: TraceListenerCollection, value: Array[TraceListener])
            Adds an array of System.Diagnostics.TraceListener objects to the list.
        
            value: An array of System.Diagnostics.TraceListener objects to add to the list.
        """
        pass

    def Clear(self):
        """
        Clear(self: TraceListenerCollection)
            Clears all the listeners from the list.
        """
        pass

    def Contains(self, listener):
        """
        Contains(self: TraceListenerCollection, listener: TraceListener) -> bool
        
            Checks whether the list contains the specified listener.
        
            listener: A System.Diagnostics.TraceListener to find in the list.
            Returns: true if the listener is in the list; otherwise, false.
        """
        pass

    def CopyTo(self, listeners, index):
        """
        CopyTo(self: TraceListenerCollection, listeners: Array[TraceListener], index: int)
            Copies a section of the current System.Diagnostics.TraceListenerCollection list to the specified 
             array at the specified index.
        
        
            listeners: An array of type System.Array to copy the elements into.
            index: The starting index number in the current list to copy from.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TraceListenerCollection) -> IEnumerator
        
            Gets an enumerator for this list.
            Returns: An enumerator of type System.Collections.IEnumerator.
        """
        pass

    def IndexOf(self, listener):
        """
        IndexOf(self: TraceListenerCollection, listener: TraceListener) -> int
        
            Gets the index of the specified listener.
        
            listener: A System.Diagnostics.TraceListener to find in the list.
            Returns: The index of the listener, if it can be found in the list; otherwise, -1.
        """
        pass

    def Insert(self, index, listener):
        """
        Insert(self: TraceListenerCollection, index: int, listener: TraceListener)
            Inserts the listener at the specified index.
        
            index: The position in the list to insert the new System.Diagnostics.TraceListener.
            listener: A System.Diagnostics.TraceListener to insert in the list.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: TraceListenerCollection, name: str)
            Removes from the collection the first System.Diagnostics.TraceListener with the specified name.
        
            name: The name of the System.Diagnostics.TraceListener to remove from the list.
        Remove(self: TraceListenerCollection, listener: TraceListener)
            Removes from the collection the specified System.Diagnostics.TraceListener.
        
            listener: A System.Diagnostics.TraceListener to remove from the list.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: TraceListenerCollection, index: int)
            Removes from the collection the System.Diagnostics.TraceListener at the specified index.
        
            index: The zero-based index of the System.Diagnostics.TraceListener to remove from the list.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of listeners in the list.

Get: Count(self: TraceListenerCollection) -> int

"""



class TraceOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies trace data options to be written to the trace output.
    
    enum (flags) TraceOptions, values: Callstack (32), DateTime (2), LogicalOperationStack (1), None (0), ProcessId (8), ThreadId (16), Timestamp (4)
    """
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

    Callstack = None
    DateTime = None
    LogicalOperationStack = None
    None = None
    ProcessId = None
    ThreadId = None
    Timestamp = None
    value__ = None


class TraceSource(object):
    """
    Provides a set of methods and properties that enable applications to trace the execution of code and associate trace messages with their source.
    
    TraceSource(name: str)
    TraceSource(name: str, defaultLevel: SourceLevels)
    """
    def Close(self):
        """
        Close(self: TraceSource)
            Closes all the trace listeners in the trace listener collection.
        """
        pass

    def Flush(self):
        """
        Flush(self: TraceSource)
            Flushes all the trace listeners in the trace listener collection.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceSource) -> Array[str]
        
            Gets the custom attributes supported by the trace source.
            Returns: A string array naming the custom attributes supported by the trace source, or null if there are 
             no custom attributes.
        """
        pass

    def TraceData(self, eventType, id, data):
        """
        TraceData(self: TraceSource, eventType: TraceEventType, id: int, *data: Array[object])
            Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners 
             collection using the specified event type, event identifier, and trace data array.
        
        
            eventType: One of the enumeration values that specifies the event type of the trace data.
            id: A numeric identifier for the event.
            data: An object array containing the trace data.
        TraceData(self: TraceSource, eventType: TraceEventType, id: int, data: object)
            Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners 
             collection using the specified event type, event identifier, and trace data.
        
        
            eventType: One of the enumeration values that specifies the event type of the trace data.
            id: A numeric identifier for the event.
            data: The trace data.
        """
        pass

    def TraceEvent(self, eventType, id, *__args):
        """
        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, format: str, *args: Array[object])
            Writes a trace event to the trace listeners in the System.Diagnostics.TraceSource.Listeners 
             collection using the specified event type, event identifier, and argument array and format.
        
        
            eventType: One of the enumeration values that specifies the event type of the trace data.
            id: A numeric identifier for the event.
            format: A composite format string (see Remarks) that contains text intermixed with zero or more format 
             items, which correspond to objects in the args array.
        
            args: An object array containing zero or more objects to format.
        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, message: str)
            Writes a trace event message to the trace listeners in the 
             System.Diagnostics.TraceSource.Listeners collection using the specified event type, event 
             identifier, and message.
        
        
            eventType: One of the enumeration values that specifies the event type of the trace data.
            id: A numeric identifier for the event.
            message: The trace message to write.
        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int)
            Writes a trace event message to the trace listeners in the 
             System.Diagnostics.TraceSource.Listeners collection using the specified event type and event 
             identifier.
        
        
            eventType: One of the enumeration values that specifies the event type of the trace data.
            id: A numeric identifier for the event.
        """
        pass

    def TraceInformation(self, *__args):
        """
        TraceInformation(self: TraceSource, format: str, *args: Array[object])
            Writes an informational message to the trace listeners in the 
             System.Diagnostics.TraceSource.Listeners collection using the specified object array and 
             formatting information.
        
        
            format: A composite format string (see Remarks) that contains text intermixed with zero or more format 
             items, which correspond to objects in the args array.
        
            args: An array containing zero or more objects to format.
        TraceInformation(self: TraceSource, message: str)
            Writes an informational message to the trace listeners in the 
             System.Diagnostics.TraceSource.Listeners collection using the specified message.
        
        
            message: The informative message to write.
        """
        pass

    def TraceTransfer(self, id, message, relatedActivityId):
        """
        TraceTransfer(self: TraceSource, id: int, message: str, relatedActivityId: Guid)
            Writes a trace transfer message to the trace listeners in the 
             System.Diagnostics.TraceSource.Listeners collection using the specified numeric identifier, 
             message, and related activity identifier.
        
        
            id: A numeric identifier for the event.
            message: The trace message to write.
            relatedActivityId: A structure that identifies the related activity.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, defaultLevel=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, defaultLevel: SourceLevels)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom switch attributes defined in the application configuration file.

Get: Attributes(self: TraceSource) -> StringDictionary

"""

    Listeners = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of trace listeners for the trace source.

Get: Listeners(self: TraceSource) -> TraceListenerCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the trace source.

Get: Name(self: TraceSource) -> str

"""

    Switch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the source switch value.

Get: Switch(self: TraceSource) -> SourceSwitch

Set: Switch(self: TraceSource) = value
"""



class TraceSwitch(Switch):
    """
    Provides a multilevel switch to control tracing and debug output without recompiling your code.
    
    TraceSwitch(displayName: str, description: str)
    TraceSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, displayName, description, defaultSwitchValue=None):
        """
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, defaultSwitchValue: str)
        """
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the trace level that determines the messages the switch allows.

Get: Level(self: TraceSwitch) -> TraceLevel

Set: Level(self: TraceSwitch) = value
"""

    SwitchSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current setting for this switch.

"""

    TraceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the switch allows error-handling messages.

Get: TraceError(self: TraceSwitch) -> bool

"""

    TraceInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the switch allows informational messages.

Get: TraceInfo(self: TraceSwitch) -> bool

"""

    TraceVerbose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the switch allows all messages.

Get: TraceVerbose(self: TraceSwitch) -> bool

"""

    TraceWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the switch allows warning messages.

Get: TraceWarning(self: TraceSwitch) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the switch.

"""



class XmlWriterTraceListener(TextWriterTraceListener, IDisposable):
    """
    Directs tracing or debugging output as XML-encoded data to a System.IO.TextWriter or to a System.IO.Stream, such as a System.IO.FileStream.
    
    XmlWriterTraceListener(stream: Stream)
    XmlWriterTraceListener(stream: Stream, name: str)
    XmlWriterTraceListener(writer: TextWriter)
    XmlWriterTraceListener(writer: TextWriter, name: str)
    XmlWriterTraceListener(filename: str)
    XmlWriterTraceListener(filename: str, name: str)
    """
    def Close(self):
        """
        Close(self: XmlWriterTraceListener)
            Closes the System.Diagnostics.TextWriterTraceListener.Writer for this listener so that it no 
             longer receives tracing or debugging output.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextWriterTraceListener, disposing: bool)
            Disposes this System.Diagnostics.TextWriterTraceListener object.
        
            disposing: true to release managed resources; if false, 
             System.Diagnostics.TextWriterTraceListener.Dispose(System.Boolean) has no effect.
        """
        pass

    def Fail(self, message, detailMessage=None):
        """
        Fail(self: XmlWriterTraceListener, message: str, detailMessage: str)
            Writes trace information including an error message and a detailed error message to the file or 
             stream.
        
        
            message: The error message to write.
            detailMessage: The detailed error message to append to the error message.
        """
        pass

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]
        
            Gets the custom attributes supported by the trace listener.
            Returns: A string array naming the custom attributes supported by the trace listener, or null if there 
             are no custom attributes.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])
            Writes trace information, data objects, and event information to the file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack 
             trace information.
        
            source: The source name.
            eventType: One of the System.Diagnostics.TraceEventType values.
            id: A numeric identifier for the event.
            data: An array of data objects to emit.
        TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)
            Writes trace information, a data object, and event information to the file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack 
             trace information.
        
            source: The source name.
            eventType: One of the System.Diagnostics.TraceEventType values.
            id: A numeric identifier for the event.
            data: A data object to emit.
        """
        pass

    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)
            Writes trace information, a message, and event information to the file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack 
             trace information.
        
            source: The source name.
            eventType: One of the System.Diagnostics.TraceEventType values.
            id: A numeric identifier for the event.
            message: The message to write.
        TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])
            Writes trace information, a formatted message, and event information to the file or stream.
        
            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack 
             trace information.
        
            source: The source name.
            eventType: One of the System.Diagnostics.TraceEventType values.
            id: A numeric identifier for the event.
            format: A format string that contains zero or more format items that correspond to objects in the args 
             array.
        
            args: An object array containing zero or more objects to format.
        """
        pass

    def TraceTransfer(self, eventCache, source, id, message, relatedActivityId):
        """
        TraceTransfer(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid)
            Writes trace information including the identity of a related activity, a message, and event 
             information to the file or stream.
        
        
            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack 
             trace information.
        
            source: The source name.
            id: A numeric identifier for the event.
            message: A trace message to write.
            relatedActivityId: A System.Guid structure that identifies a related activity.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: XmlWriterTraceListener, message: str)
            Writes a verbatim message without any additional context information to the file or stream.
        
            message: The message to write.
        """
        pass

    def WriteIndent(self, *args): #cannot find CLR method
        """
        WriteIndent(self: TraceListener)
            Writes the indent to the listener you create when you implement this class, and resets the 
             System.Diagnostics.TraceListener.NeedIndent property to false.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: XmlWriterTraceListener, message: str)
            Writes a verbatim message without any additional context information followed by the current 
             line terminator to the file or stream.
        
        
            message: The message to write.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, name: str)
        __new__(cls: type, writer: TextWriter)
        __new__(cls: type, writer: TextWriter, name: str)
        __new__(cls: type, filename: str)
        __new__(cls: type, filename: str, name: str)
        """
        pass

    NeedIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to indent the output.

"""



# variables with complex values


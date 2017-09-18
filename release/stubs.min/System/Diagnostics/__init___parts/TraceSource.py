class TraceSource(object):
 """
 Provides a set of methods and properties that enable applications to trace the execution of code and associate trace messages with their source.

 

 TraceSource(name: str)

 TraceSource(name: str,defaultLevel: SourceLevels)
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
 def GetSupportedAttributes(self,*args):
  """
  GetSupportedAttributes(self: TraceSource) -> Array[str]

  

   Gets the custom attributes supported by the trace source.

   Returns: A string array naming the custom attributes supported by the trace source,or null if there are 

    no custom attributes.
  """
  pass
 def TraceData(self,eventType,id,data):
  """
  TraceData(self: TraceSource,eventType: TraceEventType,id: int,*data: Array[object])

   Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners 

    collection using the specified event type,event identifier,and trace data array.

  

  

   eventType: One of the enumeration values that specifies the event type of the trace data.

   id: A numeric identifier for the event.

   data: An object array containing the trace data.

  TraceData(self: TraceSource,eventType: TraceEventType,id: int,data: object)

   Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners 

    collection using the specified event type,event identifier,and trace data.

  

  

   eventType: One of the enumeration values that specifies the event type of the trace data.

   id: A numeric identifier for the event.

   data: The trace data.
  """
  pass
 def TraceEvent(self,eventType,id,*__args):
  """
  TraceEvent(self: TraceSource,eventType: TraceEventType,id: int,format: str,*args: Array[object])

   Writes a trace event to the trace listeners in the System.Diagnostics.TraceSource.Listeners 

    collection using the specified event type,event identifier,and argument array and format.

  

  

   eventType: One of the enumeration values that specifies the event type of the trace data.

   id: A numeric identifier for the event.

   format: A composite format string (see Remarks) that contains text intermixed with zero or more format 

    items,which correspond to objects in the args array.

  

   args: An object array containing zero or more objects to format.

  TraceEvent(self: TraceSource,eventType: TraceEventType,id: int,message: str)

   Writes a trace event message to the trace listeners in the 

    System.Diagnostics.TraceSource.Listeners collection using the specified event type,event 

    identifier,and message.

  

  

   eventType: One of the enumeration values that specifies the event type of the trace data.

   id: A numeric identifier for the event.

   message: The trace message to write.

  TraceEvent(self: TraceSource,eventType: TraceEventType,id: int)

   Writes a trace event message to the trace listeners in the 

    System.Diagnostics.TraceSource.Listeners collection using the specified event type and event 

    identifier.

  

  

   eventType: One of the enumeration values that specifies the event type of the trace data.

   id: A numeric identifier for the event.
  """
  pass
 def TraceInformation(self,*__args):
  """
  TraceInformation(self: TraceSource,format: str,*args: Array[object])

   Writes an informational message to the trace listeners in the 

    System.Diagnostics.TraceSource.Listeners collection using the specified object array and 

    formatting information.

  

  

   format: A composite format string (see Remarks) that contains text intermixed with zero or more format 

    items,which correspond to objects in the args array.

  

   args: An array containing zero or more objects to format.

  TraceInformation(self: TraceSource,message: str)

   Writes an informational message to the trace listeners in the 

    System.Diagnostics.TraceSource.Listeners collection using the specified message.

  

  

   message: The informative message to write.
  """
  pass
 def TraceTransfer(self,id,message,relatedActivityId):
  """
  TraceTransfer(self: TraceSource,id: int,message: str,relatedActivityId: Guid)

   Writes a trace transfer message to the trace listeners in the 

    System.Diagnostics.TraceSource.Listeners collection using the specified numeric identifier,

    message,and related activity identifier.

  

  

   id: A numeric identifier for the event.

   message: The trace message to write.

   relatedActivityId: A structure that identifies the related activity.
  """
  pass
 @staticmethod
 def __new__(self,name,defaultLevel=None):
  """
  __new__(cls: type,name: str)

  __new__(cls: type,name: str,defaultLevel: SourceLevels)
  """
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the custom switch attributes defined in the application configuration file.



Get: Attributes(self: TraceSource) -> StringDictionary



"""

 Listeners=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of trace listeners for the trace source.



Get: Listeners(self: TraceSource) -> TraceListenerCollection



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the trace source.



Get: Name(self: TraceSource) -> str



"""

 Switch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the source switch value.



Get: Switch(self: TraceSource) -> SourceSwitch



Set: Switch(self: TraceSource)=value

"""



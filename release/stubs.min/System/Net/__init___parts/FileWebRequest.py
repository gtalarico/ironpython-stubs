class FileWebRequest(WebRequest,ISerializable):
 """ Provides a file system implementation of the System.Net.WebRequest class. """
 def Abort(self):
  """
  Abort(self: FileWebRequest)

   Cancels a request to an Internet resource.
  """
  pass
 def BeginGetRequestStream(self,callback,state):
  """
  BeginGetRequestStream(self: FileWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous request for a System.IO.Stream object to use to write data.

  

   callback: The System.AsyncCallback delegate.

   state: An object that contains state information for this request.

   Returns: An System.IAsyncResult that references the asynchronous request.
  """
  pass
 def BeginGetResponse(self,callback,state):
  """
  BeginGetResponse(self: FileWebRequest,callback: AsyncCallback,state: object) -> IAsyncResult

  

   Begins an asynchronous request for a file system resource.

  

   callback: The System.AsyncCallback delegate.

   state: An object that contains state information for this request.

   Returns: An System.IAsyncResult that references the asynchronous request.
  """
  pass
 def EndGetRequestStream(self,asyncResult):
  """
  EndGetRequestStream(self: FileWebRequest,asyncResult: IAsyncResult) -> Stream

  

   Ends an asynchronous request for a System.IO.Stream instance that the application uses to write 

    data.

  

  

   asyncResult: An System.IAsyncResult that references the pending request for a stream.

   Returns: A System.IO.Stream object that the application uses to write data.
  """
  pass
 def EndGetResponse(self,asyncResult):
  """
  EndGetResponse(self: FileWebRequest,asyncResult: IAsyncResult) -> WebResponse

  

   Ends an asynchronous request for a file system resource.

  

   asyncResult: An System.IAsyncResult that references the pending request for a response.

   Returns: A System.Net.WebResponse that contains the response from the file system resource.
  """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: FileWebRequest,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

   streamingContext: A System.Runtime.Serialization.StreamingContext  that specifies the destination for this 

    serialization.
  """
  pass
 def GetRequestStream(self):
  """
  GetRequestStream(self: FileWebRequest) -> Stream

  

   Returns a System.IO.Stream object for writing data to the file system resource.

   Returns: A System.IO.Stream for writing data to the file system resource.
  """
  pass
 def GetResponse(self):
  """
  GetResponse(self: FileWebRequest) -> WebResponse

  

   Returns a response to a file system request.

   Returns: A System.Net.WebResponse that contains the response from the file system resource.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
 ConnectionGroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the connection group for the request. This property is reserved for future use.



Get: ConnectionGroupName(self: FileWebRequest) -> str



Set: ConnectionGroupName(self: FileWebRequest)=value

"""

 ContentLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the content length of the data being sent.



Get: ContentLength(self: FileWebRequest) -> Int64



Set: ContentLength(self: FileWebRequest)=value

"""

 ContentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the content type of the data being sent. This property is reserved for future use.



Get: ContentType(self: FileWebRequest) -> str



Set: ContentType(self: FileWebRequest)=value

"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the credentials that are associated with this request. This property is reserved for future use.



Get: Credentials(self: FileWebRequest) -> ICredentials



Set: Credentials(self: FileWebRequest)=value

"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of the name/value pairs that are associated with the request. This property is reserved for future use.



Get: Headers(self: FileWebRequest) -> WebHeaderCollection



"""

 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the protocol method used for the request. This property is reserved for future use.



Get: Method(self: FileWebRequest) -> str



Set: Method(self: FileWebRequest)=value

"""

 PreAuthenticate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to preauthenticate a request. This property is reserved for future use.



Get: PreAuthenticate(self: FileWebRequest) -> bool



Set: PreAuthenticate(self: FileWebRequest)=value

"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the network proxy to use for this request. This property is reserved for future use.



Get: Proxy(self: FileWebRequest) -> IWebProxy



Set: Proxy(self: FileWebRequest)=value

"""

 RequestUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Uniform Resource Identifier (URI) of the request.



Get: RequestUri(self: FileWebRequest) -> Uri



"""

 Timeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the length of time until the request times out.



Get: Timeout(self: FileWebRequest) -> int



Set: Timeout(self: FileWebRequest)=value

"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Always throws a System.NotSupportedException.



Get: UseDefaultCredentials(self: FileWebRequest) -> bool



Set: UseDefaultCredentials(self: FileWebRequest)=value

"""



class WebClient(Component,IComponent,IDisposable):
 """
 Provides common methods for sending data to and receiving data from a resource identified by a URI.

 

 WebClient()
 """
 def CancelAsync(self):
  """
  CancelAsync(self: WebClient)

   Cancels a pending asynchronous operation.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)

   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def DownloadData(self,address):
  """
  DownloadData(self: WebClient,address: Uri) -> Array[Byte]

  

   Downloads the resource with the specified URI as a System.Byte array.

  

   address: The URI represented by the System.Uri  object,from which to download data.

   Returns: A System.Byte array containing the downloaded resource.

  DownloadData(self: WebClient,address: str) -> Array[Byte]

  

   Downloads the resource with the specified URI as a System.Byte array.

  

   address: The URI from which to download data.

   Returns: A System.Byte array containing the downloaded resource.
  """
  pass
 def DownloadDataAsync(self,address,userToken=None):
  """
  DownloadDataAsync(self: WebClient,address: Uri,userToken: object)

   Downloads the specified resource as a System.Byte array. This method does not block the calling 

    thread.

  

  

   address: A System.Uri containing the URI to download.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  DownloadDataAsync(self: WebClient,address: Uri)

   Downloads the specified resource as a System.Byte array. This method does not block the calling 

    thread.

  

  

   address: A System.Uri containing the URI to download.
  """
  pass
 def DownloadDataTaskAsync(self,address):
  """
  DownloadDataTaskAsync(self: WebClient,address: Uri) -> Task[Array[Byte]]

  DownloadDataTaskAsync(self: WebClient,address: str) -> Task[Array[Byte]]
  """
  pass
 def DownloadFile(self,address,fileName):
  """
  DownloadFile(self: WebClient,address: Uri,fileName: str)

   Downloads the resource with the specified URI to a local file.

  

   address: The URI specified as a System.String,from which to download data.

   fileName: The name of the local file that is to receive the data.

  DownloadFile(self: WebClient,address: str,fileName: str)

   Downloads the resource with the specified URI to a local file.

  

   address: The URI from which to download data.

   fileName: The name of the local file that is to receive the data.
  """
  pass
 def DownloadFileAsync(self,address,fileName,userToken=None):
  """
  DownloadFileAsync(self: WebClient,address: Uri,fileName: str,userToken: object)

   Downloads,to a local file,the resource with the specified URI. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to download.

   fileName: The name of the file to be placed on the local computer.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  DownloadFileAsync(self: WebClient,address: Uri,fileName: str)

   Downloads,to a local file,the resource with the specified URI. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to download.

   fileName: The name of the file to be placed on the local computer.
  """
  pass
 def DownloadFileTaskAsync(self,address,fileName):
  """
  DownloadFileTaskAsync(self: WebClient,address: Uri,fileName: str) -> Task

  DownloadFileTaskAsync(self: WebClient,address: str,fileName: str) -> Task
  """
  pass
 def DownloadString(self,address):
  """
  DownloadString(self: WebClient,address: Uri) -> str

  

   Downloads the requested resource as a System.String. The resource to download is specified as a 

    System.Uri.

  

  

   address: A System.Uri object containing the URI to download.

   Returns: A System.String containing the requested resource.

  DownloadString(self: WebClient,address: str) -> str

  

   Downloads the requested resource as a System.String. The resource to download is specified as a 

    System.String containing the URI.

  

  

   address: A System.String containing the URI to download.

   Returns: A System.String containing the requested resource.
  """
  pass
 def DownloadStringAsync(self,address,userToken=None):
  """
  DownloadStringAsync(self: WebClient,address: Uri,userToken: object)

   Downloads the specified string to the specified resource. This method does not block the calling 

    thread.

  

  

   address: A System.Uri containing the URI to download.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  DownloadStringAsync(self: WebClient,address: Uri)

   Downloads the resource specified as a System.Uri. This method does not block the calling thread.

  

   address: A System.Uri containing the URI to download.
  """
  pass
 def DownloadStringTaskAsync(self,address):
  """
  DownloadStringTaskAsync(self: WebClient,address: Uri) -> Task[str]

  DownloadStringTaskAsync(self: WebClient,address: str) -> Task[str]
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def GetWebRequest(self,*args):
  """
  GetWebRequest(self: WebClient,address: Uri) -> WebRequest

  

   Returns a System.Net.WebRequest object for the specified resource.

  

   address: A System.Uri that identifies the resource to request.

   Returns: A new System.Net.WebRequest object for the specified resource.
  """
  pass
 def GetWebResponse(self,*args):
  """
  GetWebResponse(self: WebClient,request: WebRequest,result: IAsyncResult) -> WebResponse

  

   Returns the System.Net.WebResponse for the specified System.Net.WebRequest using the specified 

    System.IAsyncResult.

  

  

   request: A System.Net.WebRequest that is used to obtain the response.

   result: An System.IAsyncResult object obtained from a previous call to 

    System.Net.WebRequest.BeginGetResponse(System.AsyncCallback,System.Object) .

  

   Returns: A System.Net.WebResponse containing the response for the specified System.Net.WebRequest.

  GetWebResponse(self: WebClient,request: WebRequest) -> WebResponse

  

   Returns the System.Net.WebResponse for the specified System.Net.WebRequest.

  

   request: A System.Net.WebRequest that is used to obtain the response.

   Returns: A System.Net.WebResponse containing the response for the specified System.Net.WebRequest.
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
 def OnDownloadDataCompleted(self,*args):
  """
  OnDownloadDataCompleted(self: WebClient,e: DownloadDataCompletedEventArgs)

   Raises the System.Net.WebClient.DownloadDataCompleted event.

  

   e: A System.Net.DownloadDataCompletedEventArgs object that contains event data.
  """
  pass
 def OnDownloadFileCompleted(self,*args):
  """
  OnDownloadFileCompleted(self: WebClient,e: AsyncCompletedEventArgs)

   Raises the System.Net.WebClient.DownloadFileCompleted event.

  

   e: An System.ComponentModel.AsyncCompletedEventArgs object containing event data.
  """
  pass
 def OnDownloadProgressChanged(self,*args):
  """
  OnDownloadProgressChanged(self: WebClient,e: DownloadProgressChangedEventArgs)

   Raises the System.Net.WebClient.DownloadProgressChanged event.

  

   e: A System.Net.DownloadProgressChangedEventArgs object containing event data.
  """
  pass
 def OnDownloadStringCompleted(self,*args):
  """
  OnDownloadStringCompleted(self: WebClient,e: DownloadStringCompletedEventArgs)

   Raises the System.Net.WebClient.DownloadStringCompleted event.

  

   e: A System.Net.DownloadStringCompletedEventArgs object containing event data.
  """
  pass
 def OnOpenReadCompleted(self,*args):
  """
  OnOpenReadCompleted(self: WebClient,e: OpenReadCompletedEventArgs)

   Raises the System.Net.WebClient.OpenReadCompleted event.

  

   e: A System.Net.OpenReadCompletedEventArgs  object containing event data.
  """
  pass
 def OnOpenWriteCompleted(self,*args):
  """
  OnOpenWriteCompleted(self: WebClient,e: OpenWriteCompletedEventArgs)

   Raises the System.Net.WebClient.OpenWriteCompleted event.

  

   e: A System.Net.OpenWriteCompletedEventArgs object containing event data.
  """
  pass
 def OnUploadDataCompleted(self,*args):
  """
  OnUploadDataCompleted(self: WebClient,e: UploadDataCompletedEventArgs)

   Raises the System.Net.WebClient.UploadDataCompleted event.

  

   e: A System.Net.UploadDataCompletedEventArgs  object containing event data.
  """
  pass
 def OnUploadFileCompleted(self,*args):
  """
  OnUploadFileCompleted(self: WebClient,e: UploadFileCompletedEventArgs)

   Raises the System.Net.WebClient.UploadFileCompleted event.

  

   e: An System.Net.UploadFileCompletedEventArgs object containing event data.
  """
  pass
 def OnUploadProgressChanged(self,*args):
  """
  OnUploadProgressChanged(self: WebClient,e: UploadProgressChangedEventArgs)

   Raises the System.Net.WebClient.UploadProgressChanged event.

  

   e: An System.Net.UploadProgressChangedEventArgs object containing event data.
  """
  pass
 def OnUploadStringCompleted(self,*args):
  """
  OnUploadStringCompleted(self: WebClient,e: UploadStringCompletedEventArgs)

   Raises the System.Net.WebClient.UploadStringCompleted event.

  

   e: An System.Net.UploadStringCompletedEventArgs  object containing event data.
  """
  pass
 def OnUploadValuesCompleted(self,*args):
  """
  OnUploadValuesCompleted(self: WebClient,e: UploadValuesCompletedEventArgs)

   Raises the System.Net.WebClient.UploadValuesCompleted event.

  

   e: A System.Net.UploadValuesCompletedEventArgs  object containing event data.
  """
  pass
 def OnWriteStreamClosed(self,*args):
  """ OnWriteStreamClosed(self: WebClient,e: WriteStreamClosedEventArgs) """
  pass
 def OpenRead(self,address):
  """
  OpenRead(self: WebClient,address: Uri) -> Stream

  

   Opens a readable stream for the data downloaded from a resource with the URI specified as a 

    System.Uri

  

  

   address: The URI specified as a System.Uri from which to download data.

   Returns: A System.IO.Stream used to read data from a resource.

  OpenRead(self: WebClient,address: str) -> Stream

  

   Opens a readable stream for the data downloaded from a resource with the URI specified as a 

    System.String.

  

  

   address: The URI specified as a System.String from which to download data.

   Returns: A System.IO.Stream used to read data from a resource.
  """
  pass
 def OpenReadAsync(self,address,userToken=None):
  """
  OpenReadAsync(self: WebClient,address: Uri,userToken: object)

   Opens a readable stream containing the specified resource. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to retrieve.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  OpenReadAsync(self: WebClient,address: Uri)

   Opens a readable stream containing the specified resource. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to retrieve.
  """
  pass
 def OpenReadTaskAsync(self,address):
  """
  OpenReadTaskAsync(self: WebClient,address: Uri) -> Task[Stream]

  OpenReadTaskAsync(self: WebClient,address: str) -> Task[Stream]
  """
  pass
 def OpenWrite(self,address,method=None):
  """
  OpenWrite(self: WebClient,address: str,method: str) -> Stream

  

   Opens a stream for writing data to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the data.

   method: The method used to send the data to the resource. If null,the default is POST for http and STOR 

    for ftp.

  

   Returns: A System.IO.Stream used to write data to the resource.

  OpenWrite(self: WebClient,address: Uri,method: str) -> Stream

  

   Opens a stream for writing data to the specified resource,by using the specified method.

  

   address: The URI of the resource to receive the data.

   method: The method used to send the data to the resource. If null,the default is POST for http and STOR 

    for ftp.

  

   Returns: A System.IO.Stream used to write data to the resource.

  OpenWrite(self: WebClient,address: str) -> Stream

  

   Opens a stream for writing data to the specified resource.

  

   address: The URI of the resource to receive the data.

   Returns: A System.IO.Stream used to write data to the resource.

  OpenWrite(self: WebClient,address: Uri) -> Stream

  

   Opens a stream for writing data to the specified resource.

  

   address: The URI of the resource to receive the data.

   Returns: A System.IO.Stream used to write data to the resource.
  """
  pass
 def OpenWriteAsync(self,address,method=None,userToken=None):
  """
  OpenWriteAsync(self: WebClient,address: Uri,method: str,userToken: object)

   Opens a stream for writing data to the specified resource,using the specified method. This 

    method does not block the calling thread.

  

  

   address: The URI of the resource to receive the data.

   method: The method used to send the data to the resource. If null,the default is POST for http and STOR 

    for ftp.

  

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes

  

  OpenWriteAsync(self: WebClient,address: Uri,method: str)

   Opens a stream for writing data to the specified resource. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to receive the data.

   method: The method used to send the data to the resource. If null,the default is POST for http and STOR 

    for ftp.

  

  OpenWriteAsync(self: WebClient,address: Uri)

   Opens a stream for writing data to the specified resource. This method does not block the 

    calling thread.

  

  

   address: The URI of the resource to receive the data.
  """
  pass
 def OpenWriteTaskAsync(self,address,method=None):
  """
  OpenWriteTaskAsync(self: WebClient,address: str,method: str) -> Task[Stream]

  OpenWriteTaskAsync(self: WebClient,address: Uri,method: str) -> Task[Stream]

  OpenWriteTaskAsync(self: WebClient,address: str) -> Task[Stream]

  OpenWriteTaskAsync(self: WebClient,address: Uri) -> Task[Stream]
  """
  pass
 def UploadData(self,address,*__args):
  """
  UploadData(self: WebClient,address: str,method: str,data: Array[Byte]) -> Array[Byte]

  

   Uploads a data buffer to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the data.

   method: The HTTP method used to send the data to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The data buffer to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadData(self: WebClient,address: Uri,method: str,data: Array[Byte]) -> Array[Byte]

  

   Uploads a data buffer to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the data.

   method: The HTTP method used to send the data to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The data buffer to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadData(self: WebClient,address: str,data: Array[Byte]) -> Array[Byte]

  

   Uploads a data buffer to a resource identified by a URI.

  

   address: The URI of the resource to receive the data.

   data: The data buffer to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadData(self: WebClient,address: Uri,data: Array[Byte]) -> Array[Byte]

  

   Uploads a data buffer to a resource identified by a URI.

  

   address: The URI of the resource to receive the data.

   data: The data buffer to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.
  """
  pass
 def UploadDataAsync(self,address,*__args):
  """
  UploadDataAsync(self: WebClient,address: Uri,method: str,data: Array[Byte],userToken: object)

   Uploads a data buffer to a resource identified by a URI,using the specified method and 

    identifying token.

  

  

   address: The URI of the resource to receive the data.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The data buffer to send to the resource.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  UploadDataAsync(self: WebClient,address: Uri,method: str,data: Array[Byte])

   Uploads a data buffer to a resource identified by a URI,using the specified method. This method 

    does not block the calling thread.

  

  

   address: The URI of the resource to receive the data.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The data buffer to send to the resource.

  UploadDataAsync(self: WebClient,address: Uri,data: Array[Byte])

   Uploads a data buffer to a resource identified by a URI,using the POST method. This method does 

    not block the calling thread.

  

  

   address: The URI of the resource to receive the data.

   data: The data buffer to send to the resource.
  """
  pass
 def UploadDataTaskAsync(self,address,*__args):
  """
  UploadDataTaskAsync(self: WebClient,address: str,method: str,data: Array[Byte]) -> Task[Array[Byte]]

  UploadDataTaskAsync(self: WebClient,address: Uri,method: str,data: Array[Byte]) -> Task[Array[Byte]]

  UploadDataTaskAsync(self: WebClient,address: str,data: Array[Byte]) -> Task[Array[Byte]]

  UploadDataTaskAsync(self: WebClient,address: Uri,data: Array[Byte]) -> Task[Array[Byte]]
  """
  pass
 def UploadFile(self,address,*__args):
  """
  UploadFile(self: WebClient,address: str,method: str,fileName: str) -> Array[Byte]

  

   Uploads the specified local file to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the file.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   fileName: The file to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadFile(self: WebClient,address: Uri,method: str,fileName: str) -> Array[Byte]

  

   Uploads the specified local file to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the file.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   fileName: The file to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadFile(self: WebClient,address: str,fileName: str) -> Array[Byte]

  

   Uploads the specified local file to a resource with the specified URI.

  

   address: The URI of the resource to receive the file. For example,ftp://localhost/samplefile.txt.

   fileName: The file to send to the resource. For example,"samplefile.txt".

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadFile(self: WebClient,address: Uri,fileName: str) -> Array[Byte]

  

   Uploads the specified local file to a resource with the specified URI.

  

   address: The URI of the resource to receive the file. For example,ftp://localhost/samplefile.txt.

   fileName: The file to send to the resource. For example,"samplefile.txt".

   Returns: A System.Byte array containing the body of the response from the resource.
  """
  pass
 def UploadFileAsync(self,address,*__args):
  """
  UploadFileAsync(self: WebClient,address: Uri,method: str,fileName: str,userToken: object)

   Uploads the specified local file to the specified resource,using the POST method. This method 

    does not block the calling thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   method: The HTTP method used to send the data to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   fileName: The file to send to the resource.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  UploadFileAsync(self: WebClient,address: Uri,method: str,fileName: str)

   Uploads the specified local file to the specified resource,using the POST method. This method 

    does not block the calling thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   method: The HTTP method used to send the data to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   fileName: The file to send to the resource.

  UploadFileAsync(self: WebClient,address: Uri,fileName: str)

   Uploads the specified local file to the specified resource,using the POST method. This method 

    does not block the calling thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   fileName: The file to send to the resource.
  """
  pass
 def UploadFileTaskAsync(self,address,*__args):
  """
  UploadFileTaskAsync(self: WebClient,address: str,method: str,fileName: str) -> Task[Array[Byte]]

  UploadFileTaskAsync(self: WebClient,address: Uri,method: str,fileName: str) -> Task[Array[Byte]]

  UploadFileTaskAsync(self: WebClient,address: str,fileName: str) -> Task[Array[Byte]]

  UploadFileTaskAsync(self: WebClient,address: Uri,fileName: str) -> Task[Array[Byte]]
  """
  pass
 def UploadString(self,address,*__args):
  """
  UploadString(self: WebClient,address: str,method: str,data: str) -> str

  

   Uploads the specified string to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the file. This URI must identify a resource that can accept a 

    request sent with the method method.

  

   method: The HTTP method used to send the string to the resource. If null,the default is POST for http 

    and STOR for ftp.

  

   data: The string to be uploaded.

   Returns: A System.String containing the response sent by the server.

  UploadString(self: WebClient,address: Uri,method: str,data: str) -> str

  

   Uploads the specified string to the specified resource,using the specified method.

  

   address: The URI of the resource to receive the file. This URI must identify a resource that can accept a 

    request sent with the method method.

  

   method: The HTTP method used to send the string to the resource. If null,the default is POST for http 

    and STOR for ftp.

  

   data: The string to be uploaded.

   Returns: A System.String containing the response sent by the server.

  UploadString(self: WebClient,address: str,data: str) -> str

  

   Uploads the specified string to the specified resource,using the POST method.

  

   address: The URI of the resource to receive the string. For Http resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   data: The string to be uploaded.

   Returns: A System.String containing the response sent by the server.

  UploadString(self: WebClient,address: Uri,data: str) -> str

  

   Uploads the specified string to the specified resource,using the POST method.

  

   address: The URI of the resource to receive the string. For Http resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   data: The string to be uploaded.

   Returns: A System.String containing the response sent by the server.
  """
  pass
 def UploadStringAsync(self,address,*__args):
  """
  UploadStringAsync(self: WebClient,address: Uri,method: str,data: str,userToken: object)

   Uploads the specified string to the specified resource. This method does not block the calling 

    thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The string to be uploaded.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  UploadStringAsync(self: WebClient,address: Uri,method: str,data: str)

   Uploads the specified string to the specified resource. This method does not block the calling 

    thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The string to be uploaded.

  UploadStringAsync(self: WebClient,address: Uri,data: str)

   Uploads the specified string to the specified resource. This method does not block the calling 

    thread.

  

  

   address: The URI of the resource to receive the file. For HTTP resources,this URI must identify a 

    resource that can accept a request sent with the POST method,such as a script or ASP page.

  

   data: The string to be uploaded.
  """
  pass
 def UploadStringTaskAsync(self,address,*__args):
  """
  UploadStringTaskAsync(self: WebClient,address: str,method: str,data: str) -> Task[str]

  UploadStringTaskAsync(self: WebClient,address: Uri,method: str,data: str) -> Task[str]

  UploadStringTaskAsync(self: WebClient,address: str,data: str) -> Task[str]

  UploadStringTaskAsync(self: WebClient,address: Uri,data: str) -> Task[str]
  """
  pass
 def UploadValues(self,address,*__args):
  """
  UploadValues(self: WebClient,address: str,method: str,data: NameValueCollection) -> Array[Byte]

  

   Uploads the specified name/value collection to the resource identified by the specified URI,

    using the specified method.

  

  

   address: The URI of the resource to receive the collection.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadValues(self: WebClient,address: Uri,method: str,data: NameValueCollection) -> Array[Byte]

  

   Uploads the specified name/value collection to the resource identified by the specified URI,

    using the specified method.

  

  

   address: The URI of the resource to receive the collection.

   method: The HTTP method used to send the file to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadValues(self: WebClient,address: str,data: NameValueCollection) -> Array[Byte]

  

   Uploads the specified name/value collection to the resource identified by the specified URI.

  

   address: The URI of the resource to receive the collection.

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.

  UploadValues(self: WebClient,address: Uri,data: NameValueCollection) -> Array[Byte]

  

   Uploads the specified name/value collection to the resource identified by the specified URI.

  

   address: The URI of the resource to receive the collection.

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

   Returns: A System.Byte array containing the body of the response from the resource.
  """
  pass
 def UploadValuesAsync(self,address,*__args):
  """
  UploadValuesAsync(self: WebClient,address: Uri,method: str,data: NameValueCollection,userToken: object)

   Uploads the data in the specified name/value collection to the resource identified by the 

    specified URI,using the specified method. This method does not block the calling thread,and 

    allows the caller to pass an object to the method that is invoked when the operation completes.

  

  

   address: The URI of the resource to receive the collection. This URI must identify a resource that can 

    accept a request sent with the method method.

  

   method: The HTTP method used to send the string to the resource. If null,the default is POST for http 

    and STOR for ftp.

  

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

   userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 

    completes.

  

  UploadValuesAsync(self: WebClient,address: Uri,method: str,data: NameValueCollection)

   Uploads the data in the specified name/value collection to the resource identified by the 

    specified URI,using the specified method. This method does not block the calling thread.

  

  

   address: The URI of the resource to receive the collection. This URI must identify a resource that can 

    accept a request sent with the method method.

  

   method: The method used to send the string to the resource. If null,the default is POST for http and 

    STOR for ftp.

  

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.

  UploadValuesAsync(self: WebClient,address: Uri,data: NameValueCollection)

   Uploads the data in the specified name/value collection to the resource identified by the 

    specified URI. This method does not block the calling thread.

  

  

   address: The URI of the resource to receive the collection. This URI must identify a resource that can 

    accept a request sent with the default method. See remarks.

  

   data: The System.Collections.Specialized.NameValueCollection to send to the resource.
  """
  pass
 def UploadValuesTaskAsync(self,address,*__args):
  """
  UploadValuesTaskAsync(self: WebClient,address: Uri,data: NameValueCollection) -> Task[Array[Byte]]

  UploadValuesTaskAsync(self: WebClient,address: Uri,method: str,data: NameValueCollection) -> Task[Array[Byte]]

  UploadValuesTaskAsync(self: WebClient,address: str,data: NameValueCollection) -> Task[Array[Byte]]

  UploadValuesTaskAsync(self: WebClient,address: str,method: str,data: NameValueCollection) -> Task[Array[Byte]]
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AllowReadStreamBuffering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllowReadStreamBuffering(self: WebClient) -> bool



Set: AllowReadStreamBuffering(self: WebClient)=value

"""

 AllowWriteStreamBuffering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllowWriteStreamBuffering(self: WebClient) -> bool



Set: AllowWriteStreamBuffering(self: WebClient)=value

"""

 BaseAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base URI for requests made by a System.Net.WebClient.



Get: BaseAddress(self: WebClient) -> str



Set: BaseAddress(self: WebClient)=value

"""

 CachePolicy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the application's cache policy for any resources obtained by this WebClient instance using System.Net.WebRequest objects.



Get: CachePolicy(self: WebClient) -> RequestCachePolicy



Set: CachePolicy(self: WebClient)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the network credentials that are sent to the host and used to authenticate the request.



Get: Credentials(self: WebClient) -> ICredentials



Set: Credentials(self: WebClient)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Encoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the System.Text.Encoding used to upload and download strings.



Get: Encoding(self: WebClient) -> Encoding



Set: Encoding(self: WebClient)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Headers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a collection of header name/value pairs associated with the request.



Get: Headers(self: WebClient) -> WebHeaderCollection



Set: Headers(self: WebClient)=value

"""

 IsBusy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether a Web request is in progress.



Get: IsBusy(self: WebClient) -> bool



"""

 Proxy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the proxy used by this System.Net.WebClient object.



Get: Proxy(self: WebClient) -> IWebProxy



Set: Proxy(self: WebClient)=value

"""

 QueryString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a collection of query name/value pairs associated with the request.



Get: QueryString(self: WebClient) -> NameValueCollection



Set: QueryString(self: WebClient)=value

"""

 ResponseHeaders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of header name/value pairs associated with the response.



Get: ResponseHeaders(self: WebClient) -> WebHeaderCollection



"""

 UseDefaultCredentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.



Get: UseDefaultCredentials(self: WebClient) -> bool



Set: UseDefaultCredentials(self: WebClient)=value

"""


 DownloadDataCompleted=None
 DownloadFileCompleted=None
 DownloadProgressChanged=None
 DownloadStringCompleted=None
 OpenReadCompleted=None
 OpenWriteCompleted=None
 UploadDataCompleted=None
 UploadFileCompleted=None
 UploadProgressChanged=None
 UploadStringCompleted=None
 UploadValuesCompleted=None
 WriteStreamClosed=None


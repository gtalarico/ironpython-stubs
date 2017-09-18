class HtmlDocument(object):
 """ Provides top-level programmatic access to an HTML document hosted by the System.Windows.Forms.WebBrowser control. """
 def AttachEventHandler(self,eventName,eventHandler):
  """
  AttachEventHandler(self: HtmlDocument,eventName: str,eventHandler: EventHandler)

   Adds an event handler for the named HTML DOM event.

  

   eventName: The name of the event you want to handle.

   eventHandler: The managed code that handles the event.
  """
  pass
 def CreateElement(self,elementTag):
  """
  CreateElement(self: HtmlDocument,elementTag: str) -> HtmlElement

  

   Creates a new HtmlElement of the specified HTML tag type.

  

   elementTag: The name of the HTML element to create.

   Returns: A new element of the specified tag type.
  """
  pass
 def DetachEventHandler(self,eventName,eventHandler):
  """
  DetachEventHandler(self: HtmlDocument,eventName: str,eventHandler: EventHandler)

   Removes an event handler from a named event on the HTML DOM.

  

   eventName: The name of the event you want to cease handling.

   eventHandler: The managed code that handles the event.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HtmlDocument,obj: object) -> bool

  

   obj: The object to compare with the current object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def ExecCommand(self,command,showUI,value):
  """
  ExecCommand(self: HtmlDocument,command: str,showUI: bool,value: object)

   Executes the specified command against the document.

  

   command: The name of the command to execute.

   showUI: Whether or not to show command-specific dialog boxes or message boxes to the user.

   value: The value to assign using the command. Not applicable for all commands.
  """
  pass
 def Focus(self):
  """
  Focus(self: HtmlDocument)

   Sets user input focus on the current document.
  """
  pass
 def GetElementById(self,id):
  """
  GetElementById(self: HtmlDocument,id: str) -> HtmlElement

  

   Retrieves a single System.Windows.Forms.HtmlElement using the element's ID attribute as a search 

    key.

  

  

   id: The ID attribute of the element to retrieve.

   Returns: Returns the first object with the same ID attribute as the specified value,or null if the id 

    cannot be found.
  """
  pass
 def GetElementFromPoint(self,point):
  """
  GetElementFromPoint(self: HtmlDocument,point: Point) -> HtmlElement

  

   Retrieves the HTML element located at the specified client coordinates.

  

   point: The x,y position of the element on the screen,relative to the top-left corner of the document.

   Returns: The System.Windows.Forms.HtmlElement at the specified screen location in the document.
  """
  pass
 def GetElementsByTagName(self,tagName):
  """
  GetElementsByTagName(self: HtmlDocument,tagName: str) -> HtmlElementCollection

  

   Retrieve a collection of elements with the specified HTML tag.

  

   tagName: The name of the HTML tag for the System.Windows.Forms.HtmlElement objects you want to retrieve.

   Returns: The collection of elements who tag name is equal to the tagName argument.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HtmlDocument) -> int

   Returns: A hash code for the current System.Object.
  """
  pass
 def InvokeScript(self,scriptName,args=None):
  """
  InvokeScript(self: HtmlDocument,scriptName: str) -> object

  

   Executes an Active Scripting function defined in an HTML page.

  

   scriptName: The name of the script method to invoke.

   Returns: The object returned by the Active Scripting call.

  InvokeScript(self: HtmlDocument,scriptName: str,args: Array[object]) -> object

  

   Executes an Active Scripting function defined in an HTML page.

  

   scriptName: The name of the script method to invoke.

   args: The arguments to pass to the script method.

   Returns: The object returned by the Active Scripting call.
  """
  pass
 def OpenNew(self,replaceInHistory):
  """
  OpenNew(self: HtmlDocument,replaceInHistory: bool) -> HtmlDocument

  

   Gets a new System.Windows.Forms.HtmlDocument to use with the 

    System.Windows.Forms.HtmlDocument.Write(System.String) method.

  

  

   replaceInHistory: Whether the new window's navigation should replace the previous element in the navigation 

    history of the DOM.

  

   Returns: A new document for writing.
  """
  pass
 def Write(self,text):
  """
  Write(self: HtmlDocument,text: str)

   Writes a new HTML page.

  

   text: The HTML text to write into the document.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 ActiveElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides the System.Windows.Forms.HtmlElement which currently has user input focus.



Get: ActiveElement(self: HtmlDocument) -> HtmlElement



"""

 ActiveLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.Color of a hyperlink when clicked by a user.



Get: ActiveLinkColor(self: HtmlDocument) -> Color



Set: ActiveLinkColor(self: HtmlDocument)=value

"""

 All=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an instance of System.Windows.Forms.HtmlElementCollection,which stores all System.Windows.Forms.HtmlElement objects for the document.



Get: All(self: HtmlDocument) -> HtmlElementCollection



"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the HTML document.



Get: BackColor(self: HtmlDocument) -> Color



Set: BackColor(self: HtmlDocument)=value

"""

 Body=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.HtmlElement for the BODY tag.



Get: Body(self: HtmlDocument) -> HtmlElement



"""

 Cookie=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the HTTP cookies associated with this document.



Get: Cookie(self: HtmlDocument) -> str



Set: Cookie(self: HtmlDocument)=value

"""

 DefaultEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the encoding used by default for the current document.



Get: DefaultEncoding(self: HtmlDocument) -> str



"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string describing the domain of this document for security purposes.



Get: Domain(self: HtmlDocument) -> str



Set: Domain(self: HtmlDocument)=value

"""

 DomDocument=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unmanaged interface pointer for this System.Windows.Forms.HtmlDocument.



Get: DomDocument(self: HtmlDocument) -> object



"""

 Encoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character encoding for this document.



Get: Encoding(self: HtmlDocument) -> str



Set: Encoding(self: HtmlDocument)=value

"""

 Focused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the document has user input focus.



Get: Focused(self: HtmlDocument) -> bool



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text color for the document.



Get: ForeColor(self: HtmlDocument) -> Color



Set: ForeColor(self: HtmlDocument)=value

"""

 Forms=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all of the <FORM> elements in the document.



Get: Forms(self: HtmlDocument) -> HtmlElementCollection



"""

 Images=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all image tags in the document.



Get: Images(self: HtmlDocument) -> HtmlElementCollection



"""

 LinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of hyperlinks.



Get: LinkColor(self: HtmlDocument) -> Color



Set: LinkColor(self: HtmlDocument)=value

"""

 Links=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of all the hyperlinks within this HTML document.



Get: Links(self: HtmlDocument) -> HtmlElementCollection



"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the direction of text in the current document.



Get: RightToLeft(self: HtmlDocument) -> bool



Set: RightToLeft(self: HtmlDocument)=value

"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text value of the <TITLE> tag in the current HTML document.



Get: Title(self: HtmlDocument) -> str



Set: Title(self: HtmlDocument)=value

"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URL describing the location of this document.



Get: Url(self: HtmlDocument) -> Uri



"""

 VisitedLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Color of links to HTML pages that the user has already visited.



Get: VisitedLinkColor(self: HtmlDocument) -> Color



Set: VisitedLinkColor(self: HtmlDocument)=value

"""

 Window=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.HtmlWindow associated with this document.



Get: Window(self: HtmlDocument) -> HtmlWindow



"""


 Click=None
 ContextMenuShowing=None
 Focusing=None
 LosingFocus=None
 MouseDown=None
 MouseLeave=None
 MouseMove=None
 MouseOver=None
 MouseUp=None
 Stop=None


class HtmlWindow(object):
 """ Represents the logical window that contains one or more instances of System.Windows.Forms.HtmlDocument. """
 def Alert(self,message):
  """
  Alert(self: HtmlWindow,message: str)

   Displays a message box.

  

   message: The System.String to display in the message box.
  """
  pass
 def AttachEventHandler(self,eventName,eventHandler):
  """
  AttachEventHandler(self: HtmlWindow,eventName: str,eventHandler: EventHandler)

   Adds an event handler for the named HTML DOM event.

  

   eventName: The name of the event you want to handle.

   eventHandler: A reference to the managed code that handles the event.
  """
  pass
 def Close(self):
  """
  Close(self: HtmlWindow)

   Closes the window.
  """
  pass
 def Confirm(self,message):
  """
  Confirm(self: HtmlWindow,message: str) -> bool

  

   Displays a dialog box with a message and buttons to solicit a yes/no response.

  

   message: The text to display to the user.

   Returns: true if the user clicked Yes; false if the user clicked No or closed the dialog box.
  """
  pass
 def DetachEventHandler(self,eventName,eventHandler):
  """
  DetachEventHandler(self: HtmlWindow,eventName: str,eventHandler: EventHandler)

   Removes the named event handler.

  

   eventName: The name of the event you want to handle.

   eventHandler: A reference to the managed code that handles the event.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HtmlWindow,obj: object) -> bool

  

   Tests the object for equality against the current object.

  

   obj: The object to test.

   Returns: true if the objects are equal; otherwise,false.
  """
  pass
 def Focus(self):
  """
  Focus(self: HtmlWindow)

   Puts the focus on the current window.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HtmlWindow) -> int

   Returns: System.Int32
  """
  pass
 def MoveTo(self,*__args):
  """
  MoveTo(self: HtmlWindow,point: Point)

   Moves the window to the specified coordinates on the screen.

  

   point: The x- and y-coordinates of the window's upper-left corner.

  MoveTo(self: HtmlWindow,x: int,y: int)

   Moves the window to the specified coordinates on the screen.

  

   x: The x-coordinate of the window's upper-left corner.

   y: The y-coordinate of the window's upper-left corner.
  """
  pass
 def Navigate(self,*__args):
  """
  Navigate(self: HtmlWindow,urlString: str)

   Displays or downloads the new content located at the specified URL.

  

   urlString: The resource to display,described by a Uniform Resource Locator.

  Navigate(self: HtmlWindow,url: Uri)

   Displays a new document in the current window.

  

   url: The location,specified as a System.Uri,of the document or object to display in the current 

    window.
  """
  pass
 def Open(self,*__args):
  """
  Open(self: HtmlWindow,url: Uri,target: str,windowOptions: str,replaceEntry: bool) -> HtmlWindow

  

   Displays a file in the named window.

  

   url: The Uniform Resource Locator that describes the location of the file to load.

   target: The name of the window in which to open the resource. This can be a developer-supplied name,or 

    one of the following special values:_blank: Opens url in a new window. Works the same as a call 

    to System.Windows.Forms.HtmlWindow.OpenNew(System.String,System.String)._media: Opens url in the 

    Media bar. _parent: Opens url in the window that created the current window._search: Opens url 

    in the Search bar._self: Opens url in the current window. _top: If called against a window 

    belonging to a FRAME element,opens url in the window hosting its FRAMESET. Otherwise,acts the 

    same as _self.

  

   windowOptions: A comma-delimited string consisting of zero or more of the following options in the form 

    name=value. Except for the left,top,height,and width options,which take arbitrary integers,

    each option accepts yes or 1,and no or 0,as valid values.channelmode: Used with the deprecated 

    channels technology of Internet Explorer 4.0. Default is no.directories: Whether the window 

    should display directory navigation buttons. Default is yes. height: The height of the window's 

    client area,in pixels. The minimum is 100; attempts to open a window smaller than this will 

    cause the window to open according to The Internet Explorer defaults. left: The left 

    (x-coordinate) position of the window,relative to the upper-left corner of the user's screen,

    in pixels. Must be a positive integer.location: Whether to display the Address bar,which 

    enables users to navigate the window to a new URL. Default is yes. menubar: Whether to display 

    menus on the new window. Default is yes.resizable: Whether the window can be resized by the 

    user. Default is yes.scrollbars: Whether the window has horizontal and vertical scroll bars. 

    Default is yes.status: Whether the window has a status bar at the bottom. Default is 

    yes.titlebar: Whether the title of the current page is displayed. Setting this option to no has 

    no effect within a managed application; the title bar will always appear.toolbar: Whether 

    toolbar buttons such as Back,Forward,and Stop are visible. Default is yes.top: The top 

    (y-coordinate) position of the window,relative to the upper-left corner of the user's screen,

    in pixels. Must be a positive integer.width: The width of the window's client area,in pixels. 

    The minimum is 100; attempts to open a window smaller than this will cause the window to open 

    according to The Internet Explorer defaults.

  

   replaceEntry: Whether url replaces the current window's URL in the navigation history. This will effect the 

    operation of methods on the System.Windows.Forms.HtmlHistory class.

  

   Returns: An System.Windows.Forms.HtmlWindow representing the new window,or the previously created window 

    named by the target parameter.

  

  Open(self: HtmlWindow,urlString: str,target: str,windowOptions: str,replaceEntry: bool) -> HtmlWindow

  

   Displays a file in the named window.

  

   urlString: The Uniform Resource Locator that describes the location of the file to load.

   target: The name of the window in which to open the resource. This may be a developer-supplied name,or 

    one of the following special values:_blank: Opens url in a new window. Works the same as a call 

    to System.Windows.Forms.HtmlWindow.OpenNew(System.String,System.String)._media: Opens url in the 

    Media bar. _parent: Opens url in the window that created the current window._search: Opens url 

    in the Search bar._self: Opens url in the current window. _top: If called against a window 

    belonging to a FRAME element,opens url in the window hosting its FRAMESET. Otherwise,acts the 

    same as _self.

  

   windowOptions: A comma-delimited string consisting of zero or more of the following options in the form 

    name=value. Except for the left,top,height,and width options,which take arbitrary integers,

    each option accepts yes or 1,and no or 0,as valid values.channelmode: Used with the deprecated 

    channels technology of Internet Explorer 4.0. Default is no.directories: Whether the window 

    should display directory navigation buttons. Default is yes. height: The height of the window's 

    client area,in pixels. The minimum is 100; attempts to open a window smaller than this will 

    cause the window to open according to the Internet Explorer defaults. left: The left 

    (x-coordinate) position of the window,relative to the upper-left corner of the user's screen,

    in pixels. Must be a positive integer.location: Whether to display the Address bar,which 

    enables users to navigate the window to a new URL. Default is yes. menubar: Whether to display 

    menus on the new window. Default is yes.resizable: Whether the window can be resized by the 

    user. Default is yes.scrollbars: Whether the window has horizontal and vertical scroll bars. 

    Default is yes.status: Whether the window has a status bar at the bottom. Default is 

    yes.titlebar: Whether the title of the current page is displayed. Setting this option to no has 

    no effect within a managed application; the title bar will always appear.toolbar: Whether 

    toolbar buttons such as Back,Forward,and Stop are visible. Default is yes.top: The top 

    (y-coordinate) position of the window,relative to the upper-left corner of the user's screen,

    in pixels. Must be a positive integer.width: The width of the window's client area,in pixels. 

    The minimum is 100; attempts to open a window smaller than this will cause the window to open 

    according to the Internet Explorer defaults.

  

   replaceEntry: Whether url replaces the current window's URL in the navigation history. This will effect the 

    operation of methods on the System.Windows.Forms.HtmlHistory class.

  

   Returns: An System.Windows.Forms.HtmlWindow representing the new window,or the previously created window 

    named by the target parameter.
  """
  pass
 def OpenNew(self,*__args):
  """
  OpenNew(self: HtmlWindow,url: Uri,windowOptions: str) -> HtmlWindow

  

   Displays a file in a new window.

  

   url: The Uniform Resource Locator that describes the location of the file to load.

   windowOptions: A comma-delimited string consisting of zero or more of the following options in the form 

    name=value. See 

    System.Windows.Forms.HtmlWindow.Open(System.String,System.String,System.String,System.Boolean) 

    for a full description of the valid options.

  

   Returns: An System.Windows.Forms.HtmlWindow representing the new window.

  OpenNew(self: HtmlWindow,urlString: str,windowOptions: str) -> HtmlWindow

  

   Displays a file in a new window.

  

   urlString: The Uniform Resource Locator that describes the location of the file to load.

   windowOptions: A comma-delimited string consisting of zero or more of the following options in the form 

    name=value. See 

    System.Windows.Forms.HtmlWindow.Open(System.String,System.String,System.String,System.Boolean) 

    for a full description of the valid options.

  

   Returns: An System.Windows.Forms.HtmlWindow representing the new window.
  """
  pass
 def Prompt(self,message,defaultInputValue):
  """
  Prompt(self: HtmlWindow,message: str,defaultInputValue: str) -> str

  

   Shows a dialog box that displays a message and a text box to the user.

  

   message: The message to display to the user.

   defaultInputValue: The default value displayed in the text box.

   Returns: A System.String representing the text entered by the user.
  """
  pass
 def RemoveFocus(self):
  """
  RemoveFocus(self: HtmlWindow)

   Takes focus off of the current window.
  """
  pass
 def ResizeTo(self,*__args):
  """
  ResizeTo(self: HtmlWindow,size: Size)

   Changes the size of the window to the specified dimensions.

  

   size: A System.Drawing.Size describing the desired width and height of the window,in pixels. Must be 

    100 pixels or more in both dimensions.

  

  ResizeTo(self: HtmlWindow,width: int,height: int)

   Changes the size of the window to the specified dimensions.

  

   width: Describes the desired width of the window,in pixels. Must be 100 pixels or more.

   height: Describes the desired height of the window,in pixels. Must be 100 pixels or more.
  """
  pass
 def ScrollTo(self,*__args):
  """
  ScrollTo(self: HtmlWindow,point: Point)

   Moves the window to the specified coordinates.

  

   point: The x- and y-coordinates,relative to the top-left corner of the current window,toward which 

    the page should scroll.

  

  ScrollTo(self: HtmlWindow,x: int,y: int)

   Scrolls the window to the designated position.

  

   x: The x-coordinate,relative to the top-left corner of the current window,toward which the page 

    should scroll.

  

   y: The y-coordinate,relative to the top-left corner of the current window,toward which the page 

    should scroll.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the HTML document contained within the window.



Get: Document(self: HtmlWindow) -> HtmlDocument



"""

 DomWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unmanaged interface wrapped by this class.



Get: DomWindow(self: HtmlWindow) -> object



"""

 Frames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a reference to each of the FRAME elements defined within the Web page.



Get: Frames(self: HtmlWindow) -> HtmlWindowCollection



"""

 History=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object containing the user's most recently visited URLs.



Get: History(self: HtmlWindow) -> HtmlHistory



"""

 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this window is open or closed.



Get: IsClosed(self: HtmlWindow) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the window.



Get: Name(self: HtmlWindow) -> str



Set: Name(self: HtmlWindow)=value

"""

 Opener=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a reference to the window that opened the current window.



Get: Opener(self: HtmlWindow) -> HtmlWindow



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window which resides above the current one in a page containing frames.



Get: Parent(self: HtmlWindow) -> HtmlWindow



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position of the window's client area on the screen.



Get: Position(self: HtmlWindow) -> Point



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the current window.



Get: Size(self: HtmlWindow) -> Size



Set: Size(self: HtmlWindow)=value

"""

 StatusBarText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text displayed in the status bar of a window.



Get: StatusBarText(self: HtmlWindow) -> str



Set: StatusBarText(self: HtmlWindow)=value

"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the URL corresponding to the current item displayed in the window.



Get: Url(self: HtmlWindow) -> Uri



"""

 WindowFrameElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frame element corresponding to this window.



Get: WindowFrameElement(self: HtmlWindow) -> HtmlElement



"""


 Error=None
 GotFocus=None
 Load=None
 LostFocus=None
 Resize=None
 Scroll=None
 Unload=None


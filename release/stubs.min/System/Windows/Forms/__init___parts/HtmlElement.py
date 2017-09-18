class HtmlElement(object):
 """ Represents an HTML element inside of a Web page. """
 def AppendChild(self,newElement):
  """
  AppendChild(self: HtmlElement,newElement: HtmlElement) -> HtmlElement

  

   Adds an element to another element's subtree.

  

   newElement: The System.Windows.Forms.HtmlElement to append to this location in the tree.

   Returns: The element after it has been added to the tree.
  """
  pass
 def AttachEventHandler(self,eventName,eventHandler):
  """
  AttachEventHandler(self: HtmlElement,eventName: str,eventHandler: EventHandler)

   Adds an event handler for a named event on the HTML Document Object Model (DOM).

  

   eventName: The name of the event you want to handle.

   eventHandler: The managed code that handles the event.
  """
  pass
 def DetachEventHandler(self,eventName,eventHandler):
  """
  DetachEventHandler(self: HtmlElement,eventName: str,eventHandler: EventHandler)

   Removes an event handler from a named event on the HTML Document Object Model (DOM).

  

   eventName: The name of the event you want to handle.

   eventHandler: The managed code that handles the event.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HtmlElement,obj: object) -> bool

  

   Tests if the supplied object is equal to the current element.

  

   obj: The object to test for equality.

   Returns: true if obj is an System.Windows.Forms.HtmlElement; otherwise,false.
  """
  pass
 def Focus(self):
  """
  Focus(self: HtmlElement)

   Puts user input focus on the current element.
  """
  pass
 def GetAttribute(self,attributeName):
  """
  GetAttribute(self: HtmlElement,attributeName: str) -> str

  

   Retrieves the value of the named attribute on the element.

  

   attributeName: The name of the attribute. This argument is case-insensitive.

   Returns: The value of this attribute on the element,as a System.String value. If the specified attribute 

    does not exist on this element,returns an empty string.
  """
  pass
 def GetElementsByTagName(self,tagName):
  """
  GetElementsByTagName(self: HtmlElement,tagName: str) -> HtmlElementCollection

  

   Retrieves a collection of elements represented in HTML by the specified HTML tag.

  

   tagName: The name of the tag whose System.Windows.Forms.HtmlElement objects you wish to retrieve.

   Returns: An System.Windows.Forms.HtmlElementCollection containing all elements whose HTML tag name is 

    equal to tagName.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HtmlElement) -> int

   Returns: A hash code for the current System.Object.
  """
  pass
 def InsertAdjacentElement(self,orient,newElement):
  """
  InsertAdjacentElement(self: HtmlElement,orient: HtmlElementInsertionOrientation,newElement: HtmlElement) -> HtmlElement

  

   Insert a new element into the Document Object Model (DOM).

  

   orient: Where to insert this element in relation to the current element.

   newElement: The new element to insert.

   Returns: The System.Windows.Forms.HtmlElement that was just inserted. If insertion failed,this will 

    return null.
  """
  pass
 def InvokeMember(self,methodName,parameter=None):
  """
  InvokeMember(self: HtmlElement,methodName: str,*parameter: Array[object]) -> object

  

   Executes a function defined in the current HTML page by a scripting language.

  

   methodName: The name of the property or method to invoke.

   parameter: A list of parameters to pass.

   Returns: The element returned by the function,represented as an System.Object. If this System.Object is 

    another HTML element,and you have a reference to the unmanaged MSHTML library added to your 

    project,you can cast it to its appropriate unmanaged interface.

  

  InvokeMember(self: HtmlElement,methodName: str) -> object

  

   Executes an unexposed method on the underlying DOM element of this element.

  

   methodName: The name of the property or method to invoke.

   Returns: The element returned by this method,represented as an System.Object. If this System.Object is 

    another HTML element,and you have a reference to the unmanaged MSHTML library added to your 

    project,you can cast it to its appropriate unmanaged interface.
  """
  pass
 def RaiseEvent(self,eventName):
  """
  RaiseEvent(self: HtmlElement,eventName: str)

   Causes the named event to call all registered event handlers.

  

   eventName: The name of the event to raise.
  """
  pass
 def RemoveFocus(self):
  """
  RemoveFocus(self: HtmlElement)

   Removes focus from the current element,if that element has focus.
  """
  pass
 def ScrollIntoView(self,alignWithTop):
  """
  ScrollIntoView(self: HtmlElement,alignWithTop: bool)

   Scrolls through the document containing this element until the top or bottom edge of this 

    element is aligned with the document's window.

  

  

   alignWithTop: If true,the top of the object will be displayed at the top of the window. If false,the bottom 

    of the object will be displayed at the bottom of the window.
  """
  pass
 def SetAttribute(self,attributeName,value):
  """
  SetAttribute(self: HtmlElement,attributeName: str,value: str)

   Sets the value of the named attribute on the element.

  

   attributeName: The name of the attribute to set.

   value: The new value of this attribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 All=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Windows.Forms.HtmlElementCollection of all elements underneath the current element.



Get: All(self: HtmlElement) -> HtmlElementCollection



"""

 CanHaveChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element can have child elements.



Get: CanHaveChildren(self: HtmlElement) -> bool



"""

 Children=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Windows.Forms.HtmlElementCollection of all children of the current element.



Get: Children(self: HtmlElement) -> HtmlElementCollection



"""

 ClientRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the client area of the element in the HTML document.



Get: ClientRectangle(self: HtmlElement) -> Rectangle



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.HtmlDocument to which this element belongs.



Get: Document(self: HtmlElement) -> HtmlDocument



"""

 DomElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an unmanaged interface pointer for this element.



Get: DomElement(self: HtmlElement) -> object



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the user can input data into this element.



Get: Enabled(self: HtmlElement) -> bool



Set: Enabled(self: HtmlElement)=value

"""

 FirstChild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the next element below this element in the document tree.



Get: FirstChild(self: HtmlElement) -> HtmlElement



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a label by which to identify the element.



Get: Id(self: HtmlElement) -> str



Set: Id(self: HtmlElement)=value

"""

 InnerHtml=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the HTML markup underneath this element.



Get: InnerHtml(self: HtmlElement) -> str



Set: InnerHtml(self: HtmlElement)=value

"""

 InnerText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text assigned to the element.



Get: InnerText(self: HtmlElement) -> str



Set: InnerText(self: HtmlElement)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the element.



Get: Name(self: HtmlElement) -> str



Set: Name(self: HtmlElement)=value

"""

 NextSibling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the next element at the same level as this element in the document tree.



Get: NextSibling(self: HtmlElement) -> HtmlElement



"""

 OffsetParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element from which System.Windows.Forms.HtmlElement.OffsetRectangle is calculated.



Get: OffsetParent(self: HtmlElement) -> HtmlElement



"""

 OffsetRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of an element relative to its parent.



Get: OffsetRectangle(self: HtmlElement) -> Rectangle



"""

 OuterHtml=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current element's HTML code.



Get: OuterHtml(self: HtmlElement) -> str



Set: OuterHtml(self: HtmlElement)=value

"""

 OuterText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current element's text.



Get: OuterText(self: HtmlElement) -> str



Set: OuterText(self: HtmlElement)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current element's parent element.



Get: Parent(self: HtmlElement) -> HtmlElement



"""

 ScrollLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance between the edge of the element and the left edge of its content.



Get: ScrollLeft(self: HtmlElement) -> int



Set: ScrollLeft(self: HtmlElement)=value

"""

 ScrollRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the dimensions of an element's scrollable region.



Get: ScrollRectangle(self: HtmlElement) -> Rectangle



"""

 ScrollTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance between the edge of the element and the top edge of its content.



Get: ScrollTop(self: HtmlElement) -> int



Set: ScrollTop(self: HtmlElement)=value

"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a comma-delimited list of styles for the current element.



Get: Style(self: HtmlElement) -> str



Set: Style(self: HtmlElement)=value

"""

 TabIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location of this element in the tab order.



Get: TabIndex(self: HtmlElement) -> Int16



Set: TabIndex(self: HtmlElement)=value

"""

 TagName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the HTML tag.



Get: TagName(self: HtmlElement) -> str



"""


 Click=None
 DoubleClick=None
 Drag=None
 DragEnd=None
 DragLeave=None
 DragOver=None
 Focusing=None
 GotFocus=None
 KeyDown=None
 KeyPress=None
 KeyUp=None
 LosingFocus=None
 LostFocus=None
 MouseDown=None
 MouseEnter=None
 MouseLeave=None
 MouseMove=None
 MouseOver=None
 MouseUp=None


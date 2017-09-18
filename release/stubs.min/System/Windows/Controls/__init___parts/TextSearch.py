class TextSearch(DependencyObject):
 """ Enables a user to quickly access items in a set by typing prefixes of strings. """
 @staticmethod
 def GetText(element):
  """
  GetText(element: DependencyObject) -> str

  

   Returns the string to that identifies the specified item.

  

   element: The element from which the property value is read.

   Returns: The string that identifies the specified item.
  """
  pass
 @staticmethod
 def GetTextPath(element):
  """
  GetTextPath(element: DependencyObject) -> str

  

   Returns the name of the property that identifies an item in the specified element's collection.

  

   element: The element from which the property value is read.

   Returns: The name of the property that identifies the item to the user.
  """
  pass
 @staticmethod
 def SetText(element,text):
  """
  SetText(element: DependencyObject,text: str)

   Writes the System.Windows.Controls.TextSearch.Text�attached property value to the specified 

    element.

  

  

   element: The element to which the property value is written.

   text: The string that identifies the item.
  """
  pass
 @staticmethod
 def SetTextPath(element,path):
  """
  SetTextPath(element: DependencyObject,path: str)

   Writes the System.Windows.Controls.TextSearch.TextPath�attached property to the specified 

    element.

  

  

   element: The element to which the property value is written.

   path: The name of the property that identifies an item.
  """
  pass
 TextPathProperty=None
 TextProperty=None


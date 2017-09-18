class LayoutInformation(object):
 """ Defines methods that provide additional information about the layout state of an element. """
 @staticmethod
 def GetLayoutClip(element):
  """
  GetLayoutClip(element: FrameworkElement) -> Geometry

  

   Returns a System.Windows.Media.Geometry that represents the visible region of an element.

  

   element: The System.Windows.FrameworkElement whose layout clip is desired.

   Returns: A System.Windows.Media.Geometry that represents the visible region of an element.
  """
  pass
 @staticmethod
 def GetLayoutExceptionElement(dispatcher):
  """
  GetLayoutExceptionElement(dispatcher: Dispatcher) -> UIElement

  

   Returns a System.Windows.UIElement that was being processed by the layout engine at the moment 

    of an unhandled exception.

  

  

   dispatcher: The System.Windows.Threading.Dispatcher object that defines the scope of the operation. There is 

    one dispatcher per layout engine instance.

  

   Returns: A System.Windows.UIElement that was being processed by the layout engine at the moment of an 

    unhandled exception.
  """
  pass
 @staticmethod
 def GetLayoutSlot(element):
  """
  GetLayoutSlot(element: FrameworkElement) -> Rect

  

   Returns a System.Windows.Rect that represents the layout partition that is reserved for a child 

    element.

  

  

   element: The System.Windows.FrameworkElement whose layout slot is desired.

   Returns: A System.Windows.Rect that represents the layout slot of the element.
  """
  pass
 __all__=[
  'GetLayoutClip',
  'GetLayoutExceptionElement',
  'GetLayoutSlot',
 ]


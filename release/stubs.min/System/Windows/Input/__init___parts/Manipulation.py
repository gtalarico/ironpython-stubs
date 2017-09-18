class Manipulation(object):
 """ Contains methods to get and update information about a manipulation. """
 @staticmethod
 def AddManipulator(element,manipulator):
  """
  AddManipulator(element: UIElement,manipulator: IManipulator)
   Associates a System.Windows.Input.IManipulator object with the specified 
    element.
  
  
   element: The element to associate the manipulator with.
   manipulator: The object that provides the position of the input that creates or is added to 
    a manipulation.
  """
  pass
 @staticmethod
 def CompleteManipulation(element):
  """
  CompleteManipulation(element: UIElement)
   Completes the active manipulation on the specified element. When called,
    manipulation input is no longer tracked and inertia on the specified element 
    stops.
  
  
   element: The element on which to complete manipulation.
  """
  pass
 @staticmethod
 def GetManipulationContainer(element):
  """
  GetManipulationContainer(element: UIElement) -> IInputElement
  
   Gets the container that defines the coordinates for the manipulation.
  
   element: The element on which there is an active manipulation.
   Returns: The container that defines the coordinate space.
  """
  pass
 @staticmethod
 def GetManipulationMode(element):
  """
  GetManipulationMode(element: UIElement) -> ManipulationModes
  
   Gets the System.Windows.Input.ManipulationModes for the specified element.
  
   element: The element for which to get the manipulation mode.
   Returns: One of the enumeration values.
  """
  pass
 @staticmethod
 def GetManipulationPivot(element):
  """
  GetManipulationPivot(element: UIElement) -> ManipulationPivot
  
   Returns an object that describes how a rotation occurs with one point of user 
    input.
  
  
   element: The element on which there is a manipulation.
   Returns: An object that describes how a rotation occurs with one point of user input.
  """
  pass
 @staticmethod
 def IsManipulationActive(element):
  """
  IsManipulationActive(element: UIElement) -> bool
  
   Gets a value that indicates whether a manipulation is associated with the 
    specified element.
  
  
   element: The element to check.
   Returns: true if a manipulation is associated with the specified element; otherwise,
    false.
  """
  pass
 @staticmethod
 def RemoveManipulator(element,manipulator):
  """
  RemoveManipulator(element: UIElement,manipulator: IManipulator)
   Removes the association between the specified System.Windows.Input.IManipulator 
    object and the element.
  
  
   element: The element to remove the associated manipulator from.
   manipulator: The object that provides the position of the input.
  """
  pass
 @staticmethod
 def SetManipulationContainer(element,container):
  """
  SetManipulationContainer(element: UIElement,container: IInputElement)
   Sets the element that defines the coordinates for the manipulation of the 
    specified element.
  
  
   element: The element with which the manipulation is associated.
   container: The container that defines the coordinate space.
  """
  pass
 @staticmethod
 def SetManipulationMode(element,mode):
  """
  SetManipulationMode(element: UIElement,mode: ManipulationModes)
   Sets the mode of manipulation for the specified element.
  
   element: The element on which to set the manipulation mode.
   mode: The new manipulation mode.
  """
  pass
 @staticmethod
 def SetManipulationParameter(element,parameter):
  """
  SetManipulationParameter(element: UIElement,parameter: ManipulationParameters2D)
   Adds parameters to the manipulation of the specified element.
  
   element: The element that has the manipulation that the parameter is added to.
   parameter: The parameter to add.
  """
  pass
 @staticmethod
 def SetManipulationPivot(element,pivot):
  """
  SetManipulationPivot(element: UIElement,pivot: ManipulationPivot)
   Sets the pivot of the single-point manipulation of the specified element.
  
   element: The element that has an active manipulation.
   pivot: An object that describes the pivot.
  """
  pass
 @staticmethod
 def StartInertia(element):
  """
  StartInertia(element: UIElement)
   Stops the manipulation and begins inertia on the specified element.
  
   element: The element on which to begin inertia.
  """
  pass
 __all__=[
  'AddManipulator',
  'CompleteManipulation',
  'GetManipulationContainer',
  'GetManipulationMode',
  'GetManipulationPivot',
  'IsManipulationActive',
  'RemoveManipulator',
  'SetManipulationContainer',
  'SetManipulationMode',
  'SetManipulationParameter',
  'SetManipulationPivot',
  'StartInertia',
 ]


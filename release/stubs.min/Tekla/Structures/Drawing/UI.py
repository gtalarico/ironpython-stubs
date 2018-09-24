# encoding: utf-8
# module Tekla.Structures.Drawing.UI calls itself UI
# from Tekla.Structures.Drawing,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DrawingObjectSelector(object):
 # no doc
 def GetSelected(self):
  """ GetSelected(self: DrawingObjectSelector) -> DrawingObjectEnumerator """
  pass
 def SelectObject(self,DrawingObject):
  """ SelectObject(self: DrawingObjectSelector,DrawingObject: DrawingObject) -> bool """
  pass
 def SelectObjects(self,DrawingObjects,ExtendSelection):
  """ SelectObjects(self: DrawingObjectSelector,DrawingObjects: ArrayList,ExtendSelection: bool) -> bool """
  pass
 def UnselectAllObjects(self):
  """ UnselectAllObjects(self: DrawingObjectSelector) -> bool """
  pass
 def UnselectObject(self,DrawingObject):
  """ UnselectObject(self: DrawingObjectSelector,DrawingObject: DrawingObject) -> bool """
  pass
 def UnselectObjects(self,DrawingObjects):
  """ UnselectObjects(self: DrawingObjectSelector,DrawingObjects: ArrayList) -> bool """
  pass

class DrawingSelector(object):
 # no doc
 def GetSelected(self):
  """ GetSelected(self: DrawingSelector) -> DrawingEnumerator """
  pass

class Events(MarshalByRefObject):
 """ Events() """
 def InitializeLifetimeService(self):
  """ InitializeLifetimeService(self: Events) -> object """
  pass
 def OnDrawingEditorClose(self,EventName,Parameters):
  """ OnDrawingEditorClose(self: Events,EventName: str,*Parameters: Array[object]) """
  pass
 def OnDrawingEditorOpen(self,EventName,Parameters):
  """ OnDrawingEditorOpen(self: Events,EventName: str,*Parameters: Array[object]) """
  pass
 def OnDrawingListSelectionChanged(self,EventName,Parameters):
  """ OnDrawingListSelectionChanged(self: Events,EventName: str,*Parameters: Array[object]) """
  pass
 def OnDrawingLoaded(self,EventName,Parameters):
  """ OnDrawingLoaded(self: Events,EventName: str,*Parameters: Array[object]) """
  pass
 def OnSelectionChange(self,EventName,Parameters):
  """ OnSelectionChange(self: Events,EventName: str,*Parameters: Array[object]) """
  pass
 def Register(self):
  """ Register(self: Events) """
  pass
 def UnRegister(self):
  """ UnRegister(self: Events) """
  pass
 DrawingEditorClosed=None
 DrawingEditorClosedDelegate=None
 DrawingEditorOpened=None
 DrawingEditorOpenedDelegate=None
 DrawingListSelectionChanged=None
 DrawingListSelectionChangedDelegate=None
 DrawingLoaded=None
 DrawingLoadedDelegate=None
 SelectionChange=None
 SelectionChangeDelegate=None


class Picker(object):
 # no doc
 def IsInteractive(self):
  """ IsInteractive(self: Picker) -> bool """
  pass
 def PickObject(self,prompt,*__args):
  """
  PickObject(self: Picker,prompt: str) -> (DrawingObject,ViewBase,Point)
  PickObject(self: Picker,prompt: str,typeFilter: Array[Type]) -> (DrawingObject,ViewBase,Point)
  PickObject(self: Picker,prompt: str) -> (DrawingObject,ViewBase)
  PickObject(self: Picker,prompt: str) -> Tuple[DrawingObject,ViewBase]
  """
  pass
 def PickObjectAndPoint(self,prompt):
  """ PickObjectAndPoint(self: Picker,prompt: str) -> Tuple[DrawingObject,ViewBase,Point] """
  pass
 def PickPoint(self,prompt,pickedPoint=None,pickedView=None):
  """
  PickPoint(self: Picker,prompt: str) -> Tuple[Point,ViewBase]
  PickPoint(self: Picker,prompt: str) -> (Point,ViewBase)
  """
  pass
 def PickPoints(self,*__args):
  """
  PickPoints(self: Picker,prompts: StringList) -> (PointList,ViewBase)
  PickPoints(self: Picker,prompts: StringList) -> Tuple[PointList,ViewBase]
  PickPoints(self: Picker,numberOfPicks: int,prompts: StringList) -> (PointList,ViewBase)
  PickPoints(self: Picker,numberOfPicks: int,prompts: StringList) -> Tuple[PointList,ViewBase]
  """
  pass
 def PickThreePoints(self,firstPrompt,secondPrompt,thirdPrompt,firstPickedPoint,secondPickedPoint,thirdPickedPoint,pickedView):
  """ PickThreePoints(self: Picker,firstPrompt: str,secondPrompt: str,thirdPrompt: str) -> (Point,Point,Point,ViewBase) """
  pass
 def PickTwoPoints(self,firstPrompt,secondPrompt,firstPickedPoint,secondPickedPoint,pickedView):
  """ PickTwoPoints(self: Picker,firstPrompt: str,secondPrompt: str) -> (Point,Point,ViewBase) """
  pass


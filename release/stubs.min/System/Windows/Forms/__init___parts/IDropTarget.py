class IDropTarget:
 """ Defines mouse events. """
 def OnDragDrop(self,e):
  """
  OnDragDrop(self: IDropTarget,e: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragDrop event.

  

   e: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragEnter(self,e):
  """
  OnDragEnter(self: IDropTarget,e: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragEnter event.

  

   e: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,e):
  """
  OnDragLeave(self: IDropTarget,e: EventArgs)

   Raises the System.Windows.Forms.Control.DragLeave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,e):
  """
  OnDragOver(self: IDropTarget,e: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragOver event.

  

   e: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

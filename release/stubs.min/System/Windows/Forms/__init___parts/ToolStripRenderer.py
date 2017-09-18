class ToolStripRenderer(object):
 """ Handles the painting functionality for System.Windows.Forms.ToolStrip objects. """
 @staticmethod
 def CreateDisabledImage(normalImage):
  """
  CreateDisabledImage(normalImage: Image) -> Image

  

   Creates a gray-scale copy of a given image.

  

   normalImage: The image to be copied.

   Returns: An System.Drawing.Image that is a copy of the given image,but with a gray-scale color matrix.
  """
  pass
 def DrawArrow(self,e):
  """
  DrawArrow(self: ToolStripRenderer,e: ToolStripArrowRenderEventArgs)

   Draws an arrow on a System.Windows.Forms.ToolStripItem.

  

   e: A System.Windows.Forms.ToolStripArrowRenderEventArgs that contains data to draw the arrow.
  """
  pass
 def DrawButtonBackground(self,e):
  """
  DrawButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStripButton.

  

   e: The System.Windows.Forms.ToolStripItemRenderEventArgs that contains data to draw the button's 

    background.
  """
  pass
 def DrawDropDownButtonBackground(self,e):
  """
  DrawDropDownButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStripDropDownButton.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the data to draw the drop-down 

    button's background.
  """
  pass
 def DrawGrip(self,e):
  """
  DrawGrip(self: ToolStripRenderer,e: ToolStripGripRenderEventArgs)

   Draws a move handle on a System.Windows.Forms.ToolStrip.

  

   e: A System.Windows.Forms.ToolStripGripRenderEventArgs that contains the data to draw the move 

    handle.
  """
  pass
 def DrawImageMargin(self,e):
  """
  DrawImageMargin(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Draws the space around an image on a System.Windows.Forms.ToolStrip.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the data to draw the space around 

    the image.
  """
  pass
 def DrawItemBackground(self,e):
  """
  DrawItemBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStripItem.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the data to draw the 

    background of the item.
  """
  pass
 def DrawItemCheck(self,e):
  """
  DrawItemCheck(self: ToolStripRenderer,e: ToolStripItemImageRenderEventArgs)

   Draws an image on a System.Windows.Forms.ToolStripItem that indicates the item is in a selected 

    state.

  

  

   e: A System.Windows.Forms.ToolStripItemImageRenderEventArgs that contains the data to draw the 

    selected image.
  """
  pass
 def DrawItemImage(self,e):
  """
  DrawItemImage(self: ToolStripRenderer,e: ToolStripItemImageRenderEventArgs)

   Draws an image on a System.Windows.Forms.ToolStripItem.

  

   e: A System.Windows.Forms.ToolStripItemImageRenderEventArgs that contains the data to draw the 

    image.
  """
  pass
 def DrawItemText(self,e):
  """
  DrawItemText(self: ToolStripRenderer,e: ToolStripItemTextRenderEventArgs)

   Draws text on a System.Windows.Forms.ToolStripItem.

  

   e: A System.Windows.Forms.ToolStripItemTextRenderEventArgs that contains the data to draw the text.
  """
  pass
 def DrawLabelBackground(self,e):
  """
  DrawLabelBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStripLabel.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the data to draw the 

    background for the label.
  """
  pass
 def DrawMenuItemBackground(self,e):
  """
  DrawMenuItemBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStripMenuItem.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the data to draw the 

    background for the menu item.
  """
  pass
 def DrawOverflowButtonBackground(self,e):
  """
  DrawOverflowButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background for an overflow button.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def DrawSeparator(self,e):
  """
  DrawSeparator(self: ToolStripRenderer,e: ToolStripSeparatorRenderEventArgs)

   Draws a System.Windows.Forms.ToolStripSeparator.

  

   e: A System.Windows.Forms.ToolStripSeparatorRenderEventArgs that contains the data to draw the 

    System.Windows.Forms.ToolStripSeparator.
  """
  pass
 def DrawSplitButton(self,e):
  """
  DrawSplitButton(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws a System.Windows.Forms.ToolStripSplitButton.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def DrawStatusStripSizingGrip(self,e):
  """
  DrawStatusStripSizingGrip(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Draws a sizing grip.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def DrawToolStripBackground(self,e):
  """
  DrawToolStripBackground(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Draws the background for a System.Windows.Forms.ToolStrip.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the data to draw the background 

    for the System.Windows.Forms.ToolStrip.
  """
  pass
 def DrawToolStripBorder(self,e):
  """
  DrawToolStripBorder(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Draws the border for a System.Windows.Forms.ToolStrip.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the data to draw the border for 

    the System.Windows.Forms.ToolStrip.
  """
  pass
 def DrawToolStripContentPanelBackground(self,e):
  """
  DrawToolStripContentPanelBackground(self: ToolStripRenderer,e: ToolStripContentPanelRenderEventArgs)

   Draws the background of the System.Windows.Forms.ToolStripContentPanel.

  

   e: A System.Windows.Forms.ToolStripContentPanelRenderEventArgs that contains the event data.
  """
  pass
 def DrawToolStripPanelBackground(self,e):
  """
  DrawToolStripPanelBackground(self: ToolStripRenderer,e: ToolStripPanelRenderEventArgs)

   Draws the background of the System.Windows.Forms.ToolStripPanel.

  

   e: A System.Windows.Forms.ToolStripPanelRenderEventArgs that contains the event data.
  """
  pass
 def DrawToolStripStatusLabelBackground(self,e):
  """
  DrawToolStripStatusLabelBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Draws the background of the System.Windows.Forms.ToolStripStatusLabel.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def Initialize(self,*args):
  """
  Initialize(self: ToolStripRenderer,toolStrip: ToolStrip)

   When overridden in a derived class,provides for custom initialization of the given 

    System.Windows.Forms.ToolStrip.

  

  

   toolStrip: The System.Windows.Forms.ToolStrip to be initialized.
  """
  pass
 def InitializeContentPanel(self,*args):
  """
  InitializeContentPanel(self: ToolStripRenderer,contentPanel: ToolStripContentPanel)

   Initializes the specified System.Windows.Forms.ToolStripContentPanel.

  

   contentPanel: The System.Windows.Forms.ToolStripContentPanel.
  """
  pass
 def InitializeItem(self,*args):
  """
  InitializeItem(self: ToolStripRenderer,item: ToolStripItem)

   When overridden in a derived class,provides for custom initialization of the given 

    System.Windows.Forms.ToolStripItem.

  

  

   item: The System.Windows.Forms.ToolStripItem to be initialized.
  """
  pass
 def InitializePanel(self,*args):
  """
  InitializePanel(self: ToolStripRenderer,toolStripPanel: ToolStripPanel)

   Initializes the specified System.Windows.Forms.ToolStripPanel.

  

   toolStripPanel: The System.Windows.Forms.ToolStripPanel.
  """
  pass
 def OnRenderArrow(self,*args):
  """
  OnRenderArrow(self: ToolStripRenderer,e: ToolStripArrowRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderArrow event.

  

   e: A System.Windows.Forms.ToolStripArrowRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderButtonBackground(self,*args):
  """
  OnRenderButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderButtonBackground event.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderDropDownButtonBackground(self,*args):
  """
  OnRenderDropDownButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderDropDownButtonBackground event.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderGrip(self,*args):
  """
  OnRenderGrip(self: ToolStripRenderer,e: ToolStripGripRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderGrip event.

  

   e: A System.Windows.Forms.ToolStripGripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderImageMargin(self,*args):
  """
  OnRenderImageMargin(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Draws the item background.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderItemBackground(self,*args):
  """
  OnRenderItemBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the 

    System.Windows.Forms.ToolStripSystemRenderer.OnRenderItemBackground(System.Windows.Forms.ToolStri

    pItemRenderEventArgs) event.

  

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderItemCheck(self,*args):
  """
  OnRenderItemCheck(self: ToolStripRenderer,e: ToolStripItemImageRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderItemCheck event.

  

   e: A System.Windows.Forms.ToolStripItemImageRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderItemImage(self,*args):
  """
  OnRenderItemImage(self: ToolStripRenderer,e: ToolStripItemImageRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderItemImage event.

  

   e: A System.Windows.Forms.ToolStripItemImageRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderItemText(self,*args):
  """
  OnRenderItemText(self: ToolStripRenderer,e: ToolStripItemTextRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderItemText event.

  

   e: A System.Windows.Forms.ToolStripItemTextRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderLabelBackground(self,*args):
  """
  OnRenderLabelBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderLabelBackground event.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderMenuItemBackground(self,*args):
  """
  OnRenderMenuItemBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderMenuItemBackground event.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderOverflowButtonBackground(self,*args):
  """
  OnRenderOverflowButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderOverflowButtonBackground event.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderSeparator(self,*args):
  """
  OnRenderSeparator(self: ToolStripRenderer,e: ToolStripSeparatorRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderSeparator event.

  

   e: A System.Windows.Forms.ToolStripSeparatorRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderSplitButtonBackground(self,*args):
  """
  OnRenderSplitButtonBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the 

    System.Windows.Forms.ToolStripRenderer.OnRenderSplitButtonBackground(System.Windows.Forms.ToolStr

    ipItemRenderEventArgs) event.

  

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderStatusStripSizingGrip(self,*args):
  """
  OnRenderStatusStripSizingGrip(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderStatusStripSizingGrip event.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderToolStripBackground(self,*args):
  """
  OnRenderToolStripBackground(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderToolStripBackground event.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderToolStripBorder(self,*args):
  """
  OnRenderToolStripBorder(self: ToolStripRenderer,e: ToolStripRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderToolStripBorder event.

  

   e: A System.Windows.Forms.ToolStripRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderToolStripContentPanelBackground(self,*args):
  """
  OnRenderToolStripContentPanelBackground(self: ToolStripRenderer,e: ToolStripContentPanelRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderToolStripContentPanelBackground event.

  

   e: A System.Windows.Forms.ToolStripContentPanelRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderToolStripPanelBackground(self,*args):
  """
  OnRenderToolStripPanelBackground(self: ToolStripRenderer,e: ToolStripPanelRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderToolStripPanelBackground event.

  

   e: A System.Windows.Forms.ToolStripPanelRenderEventArgs that contains the event data.
  """
  pass
 def OnRenderToolStripStatusLabelBackground(self,*args):
  """
  OnRenderToolStripStatusLabelBackground(self: ToolStripRenderer,e: ToolStripItemRenderEventArgs)

   Raises the System.Windows.Forms.ToolStripRenderer.RenderToolStripStatusLabelBackground event.

  

   e: A System.Windows.Forms.ToolStripItemRenderEventArgs that contains the event data.
  """
  pass
 def ScaleArrowOffsetsIfNeeded(self,*args):
  """ ScaleArrowOffsetsIfNeeded() """
  pass
 Offset2X=2
 Offset2Y=2
 RenderArrow=None
 RenderButtonBackground=None
 RenderDropDownButtonBackground=None
 RenderGrip=None
 RenderImageMargin=None
 RenderItemBackground=None
 RenderItemCheck=None
 RenderItemImage=None
 RenderItemText=None
 RenderLabelBackground=None
 RenderMenuItemBackground=None
 RenderOverflowButtonBackground=None
 RenderSeparator=None
 RenderSplitButtonBackground=None
 RenderStatusStripSizingGrip=None
 RenderToolStripBackground=None
 RenderToolStripBorder=None
 RenderToolStripContentPanelBackground=None
 RenderToolStripPanelBackground=None
 RenderToolStripStatusLabelBackground=None


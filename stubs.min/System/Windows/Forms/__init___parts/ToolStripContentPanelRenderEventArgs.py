class ToolStripContentPanelRenderEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ToolStripContentPanel.RendererChanged event.
    
    ToolStripContentPanelRenderEventArgs(g: Graphics, contentPanel: ToolStripContentPanel)
    """
    @staticmethod # known case of __new__
    def __new__(self, g, contentPanel):
        """ __new__(cls: type, g: Graphics, contentPanel: ToolStripContentPanel) """
        pass

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object to use for drawing.

Get: Graphics(self: ToolStripContentPanelRenderEventArgs) -> Graphics

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the event was handled.

Get: Handled(self: ToolStripContentPanelRenderEventArgs) -> bool

Set: Handled(self: ToolStripContentPanelRenderEventArgs) = value
"""

    ToolStripContentPanel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Forms.ToolStripContentPanel affected by the click.

Get: ToolStripContentPanel(self: ToolStripContentPanelRenderEventArgs) -> ToolStripContentPanel

"""



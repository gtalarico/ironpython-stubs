class TemplateBindingExpression(Expression):
    """ Describes a run-time instance of a System.Windows.TemplateBindingExtension. """
    TemplateBindingExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.TemplateBindingExtension object of this expression instance.

Get: TemplateBindingExtension(self: TemplateBindingExpression) -> TemplateBindingExtension

"""



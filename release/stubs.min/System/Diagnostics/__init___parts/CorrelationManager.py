class CorrelationManager(object):
 """ Correlates traces that are part of a logical transaction. """
 def StartLogicalOperation(self,operationId=None):
  """
  StartLogicalOperation(self: CorrelationManager)

   Starts a logical operation on a thread.

  StartLogicalOperation(self: CorrelationManager,operationId: object)

   Starts a logical operation with the specified identity on a thread.

  

   operationId: An object identifying the operation.
  """
  pass
 def StopLogicalOperation(self):
  """
  StopLogicalOperation(self: CorrelationManager)

   Stops the current logical operation.
  """
  pass
 ActivityId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the identity for a global activity.



Get: ActivityId(self: CorrelationManager) -> Guid



Set: ActivityId(self: CorrelationManager)=value

"""

 LogicalOperationStack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the logical operation stack from the call context.



Get: LogicalOperationStack(self: CorrelationManager) -> Stack



"""



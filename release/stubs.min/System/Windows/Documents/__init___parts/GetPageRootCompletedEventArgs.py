class GetPageRootCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Windows.Documents.PageContent.GetPageRootCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Documents.FixedPage content asynchronously requested by System.Windows.Documents.PageContent.GetPageRootAsync(System.Boolean).

Get: Result(self: GetPageRootCompletedEventArgs) -> FixedPage

"""



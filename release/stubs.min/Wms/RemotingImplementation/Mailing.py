# encoding: utf-8
# module Wms.RemotingImplementation.Mailing calls itself Mailing
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class FileLocationMailAttachment(object):
 """
 FileLocationMailAttachment(filepath: str)
 FileLocationMailAttachment(filepath: str,sendAsFilename: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return FileLocationMailAttachment()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetContentBytes(self):
  """ GetContentBytes(self: FileLocationMailAttachment) -> Array[Byte] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,filepath,sendAsFilename=None):
  """
  __new__(cls: type,filepath: str)
  __new__(cls: type,filepath: str,sendAsFilename: str)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Filename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filename(self: FileLocationMailAttachment) -> str

"""



class IMailAttachment:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IMailAttachment()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetContentBytes(self):
  """ GetContentBytes(self: IMailAttachment) -> Array[Byte] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Filename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filename(self: IMailAttachment) -> str

"""



class IMailer:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IMailer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def SendHtmlAsync(self,args,bodyHtml):
  """ SendHtmlAsync(self: IMailer,args: SendMailArgs,bodyHtml: str) -> Task """
  pass
 def SendRazorFileAsync(self,args,razorTemplateFilepath,razorTemplateData):
  """ SendRazorFileAsync(self: IMailer,args: SendMailArgs,razorTemplateFilepath: str,razorTemplateData: object) -> Task """
  pass
 def SendRazorStringAsync(self,args,razorTemplateString,razorTemplateData):
  """ SendRazorStringAsync(self: IMailer,args: SendMailArgs,razorTemplateString: str,razorTemplateData: object) -> Task """
  pass
 def SendTextAsync(self,args,bodyText):
  """ SendTextAsync(self: IMailer,args: SendMailArgs,bodyText: str) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class MailAttachment(object):
 """ MailAttachment(filename: str,filecontent: Array[Byte]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailAttachment()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetContentBytes(self):
  """ GetContentBytes(self: MailAttachment) -> Array[Byte] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,filename,filecontent):
  """ __new__(cls: type,filename: str,filecontent: Array[Byte]) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Filename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filename(self: MailAttachment) -> str

Set: Filename(self: MailAttachment)=value
"""



class MailerBase(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailerBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def SendHtmlAsync(self,args,bodyHtml):
  """ SendHtmlAsync(self: MailerBase,args: SendMailArgs,bodyHtml: str) -> Task """
  pass
 def SendMail(self,*args):
  """ SendMail(self: MailerBase,args: SendMailArgs,body: str,bodyIsHtml: bool) -> Task """
  pass
 def SendRazorFileAsync(self,args,razorTemplateFilepath,razorTemplateData):
  """ SendRazorFileAsync(self: MailerBase,args: SendMailArgs,razorTemplateFilepath: str,razorTemplateData: object) -> Task """
  pass
 def SendRazorStringAsync(self,args,razorTemplateString,razorTemplateData):
  """ SendRazorStringAsync(self: MailerBase,args: SendMailArgs,razorTemplateString: str,razorTemplateData: object) -> Task """
  pass
 def SendTextAsync(self,args,bodyText):
  """ SendTextAsync(self: MailerBase,args: SendMailArgs,bodyText: str) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class MailerException(Exception):
 """
 MailerException()
 MailerException(message: str)
 MailerException(message: str,innerException: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailerException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class MailgunException(MailerException):
 """
 MailgunException(message: str)
 MailgunException(message: str,innerException: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailgunException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message,innerException=None):
  """
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  """
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class MailgunMailer(MailerBase):
 """ MailgunMailer(settings: MailgunSettings) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailgunMailer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def SendMail(self,*args):
  """ SendMail(self: MailgunMailer,args: SendMailArgs,body: str,bodyIsHtml: bool) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,settings):
  """ __new__(cls: type,settings: MailgunSettings) """
  pass
 ApiEndpoint=property(lambda self: object(),lambda self,v: None,lambda self: None)



class MailgunResponse(object):
 """ MailgunResponse() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailgunResponse()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: MailgunResponse) -> str

Set: Id(self: MailgunResponse)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: MailgunResponse) -> str

Set: Message(self: MailgunResponse)=value
"""



class MailgunSettings(object):
 """ MailgunSettings() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MailgunSettings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 MailgunApiKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MailgunApiKey(self: MailgunSettings) -> str

Set: MailgunApiKey(self: MailgunSettings)=value
"""

 MailgunBaseUrl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MailgunBaseUrl(self: MailgunSettings) -> str

Set: MailgunBaseUrl(self: MailgunSettings)=value
"""

 MailgunDefaultSender=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MailgunDefaultSender(self: MailgunSettings) -> str

Set: MailgunDefaultSender(self: MailgunSettings)=value
"""

 MailgunDomainBoxwise=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MailgunDomainBoxwise(self: MailgunSettings) -> str

Set: MailgunDomainBoxwise(self: MailgunSettings)=value
"""



class SendMailArgs(object):
 """ SendMailArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SendMailArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AddressesBcc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AddressesBcc(self: SendMailArgs) -> List[str]

Set: AddressesBcc(self: SendMailArgs)=value
"""

 AddressesCc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AddressesCc(self: SendMailArgs) -> List[str]

Set: AddressesCc(self: SendMailArgs)=value
"""

 AddressFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AddressFrom(self: SendMailArgs) -> str

Set: AddressFrom(self: SendMailArgs)=value
"""

 AddressTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AddressTo(self: SendMailArgs) -> str

Set: AddressTo(self: SendMailArgs)=value
"""

 Attachments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Attachments(self: SendMailArgs) -> List[IMailAttachment]

Set: Attachments(self: SendMailArgs)=value
"""

 Subject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Subject(self: SendMailArgs) -> str

Set: Subject(self: SendMailArgs)=value
"""



class SynchronousMailExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SynchronousMailExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def SendHtml(mailer,args,bodyHtml):
  """ SendHtml(mailer: IMailer,args: SendMailArgs,bodyHtml: str) """
  pass
 @staticmethod
 def SendRazorFile(mailer,args,razorTemplateFilepath,razorTemplateData):
  """ SendRazorFile(mailer: IMailer,args: SendMailArgs,razorTemplateFilepath: str,razorTemplateData: object) """
  pass
 @staticmethod
 def SendRazorString(mailer,args,razorTemplateString,razorTemplateData):
  """ SendRazorString(mailer: IMailer,args: SendMailArgs,razorTemplateString: str,razorTemplateData: object) """
  pass
 @staticmethod
 def SendText(mailer,args,bodyText):
  """ SendText(mailer: IMailer,args: SendMailArgs,bodyText: str) """
  pass
 __all__=[
  'SendHtml',
  'SendRazorFile',
  'SendRazorString',
  'SendText',
 ]



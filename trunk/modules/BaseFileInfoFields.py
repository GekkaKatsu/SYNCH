from modules.SizeUtils import ConvertBytes

from models.FileInfo import FileInfo

class BaseFileInfoFields(dict):
	def __init__(self,fileInformation,dict=None,):
		self.data = {}    
		if dict is not None: self.update(dict)
		self["File Name:"] = fileInformation.blob.filename
		self["Creation Date:"] = fileInformation.uploaded_at
		self["Uploaded by:"] = fileInformation.uploaded_by
		self["Size:"] = ConvertBytes(fileInformation.blob.size)

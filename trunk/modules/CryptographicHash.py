import hashlib

class md5HashSum():
    def valueToHash(self,value):
        return hashlib.md5(value).hexdigest() 
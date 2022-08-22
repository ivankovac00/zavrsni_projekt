# definirana klasa za blokove koja sadrzi broj bloka, prethodni hash, podatke, timestamp
import json
from datetime import datetime
import hashlib

class Block:

    def __init__(self, index, data, prevHash):
        self.index = index
        self.data = data
        self.prevHash = prevHash
        self.timestamp = datetime.now()
        self.hash = self.getHash()
    
# definirana metoda za hashiranje
    
    def getHash(self):
        hash = hashlib.sha256()
        hash.update(
            str(self.data).encode('utf-8') +
            str(self.prevHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.index).encode('utf-8')
        )
        return hash.hexdigest()
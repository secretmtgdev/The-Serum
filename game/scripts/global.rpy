init python:
    class GameManager:
        def __init__(self):
            self._element= ""
            self._realm = ""

        # Getters 
        @property
        def element(self):
            return self._element

        @property
        def realm(self):
            return self._realm

        # Setters
        @element.setter
        def element(self, element):
            self._element = element

        @realm.setter
        def realm(self, realm):
            self._realm = realm

        # Deleters
        @element.deleter
        def element(self):
            del self._element
        
        @realm.deleter
        def realm(self):
            del self._realm
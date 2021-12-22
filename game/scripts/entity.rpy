init python:
    class Entity:
        def __init__(self):
            self._name = ""
            self._stats = {}
        
        # Getters
        @property
        def name(self):
            return self._name

        @property
        def stats(self):
            return self._stats

        # Setters
        @name.setter
        def name(self, name):
            self._name = name        

        @stats.setter
        def stats(self, stats):
            self._stats = stats

        # Deleters
        @name.deleter
        def name(self):
            del self._name
        
        @stats.deleter
        def stats(self):
            del self._stats
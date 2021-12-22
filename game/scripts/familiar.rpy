init python:
    class Familiar:
        def __init__(self, name, ability):
            self._name = name
            self._ability = ability

        # Getters
        @property
        def name(self):
            return self._name

        @property
        def ability(self):
            return self._ability
        
        # Setters
        @name.setter
        def name(self, name):
            self._name = name
        
        @ability.setter
        def ability(self, ability):
            self._ability = ability

        # Deleters
        @name.deleter
        def name(self):
            del self._name
        
        @ability.deleter
        def ability(self):
            del self._ability
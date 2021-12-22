init python:
    class Player(Entity):
        def __init__(self):
            # Python v3 makes use of zero arg constructor
            # Renpy is on Python v2 and thus we need to supply
            # the baseClass and self as parameters: https://tinyurl.com/2bd79zka
            super(Entity, self).__init__()
            self._familiar = {}

        # Getters
        @property
        def familiar(self):
            return self._familiar

        # Setters
        @familiar.setter
        def familiar(self, familiar):
            self._familiar = familiar

        # Deleters
        @familiar.deleter
        def familiar(self):
            del self._familiar
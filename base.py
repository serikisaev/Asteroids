import abc


class Thing:
    @abc.abstractmethod
    def draw(self, surface):
        ...

    @abc.abstractmethod
    def update(self, dt):
        ...

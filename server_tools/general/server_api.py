
from abc import ABC, abstractmethod

class ServerAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # In case we wish to use these functions later
    # @abstractmethod
    # def connect(self):
    #     pass

    # @abstractmethod
    # def send_data(self, data):
    #     pass

    # @abstractmethod
    # def receive_data(self):
    #     pass

    # @abstractmethod
    # def disconnect(self):
    #     pass

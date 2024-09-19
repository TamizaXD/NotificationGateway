from abc import ABC, abstractmethod
class MessageService(ABC):
    @abstractmethod
    def send_message(self,name, phone_number, message_body):
        pass


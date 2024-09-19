from inspect import getmembers, isclass, isabstract
import notification_gateway.message_methods

class MessageFactory(object):
    message_implementations = {}

    def __init__(self):
        self.load_message_methods()

    def load_message_methods(self):
        implementations = getmembers(notification_gateway.message_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, notification_gateway.message_methods.MessageService):
                self.message_implementations[name] = _type
    
    def createMessage(self, message_type):
        if message_type in self.message_implementations:
            return self.message_implementations[message_type]()
        else:
            raise ValueError (f"{message_type} is not implemented yet!")
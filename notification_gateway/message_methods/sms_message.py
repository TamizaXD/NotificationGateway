import requests
from .message_service import MessageService
from notification_gateway.methods.get_doc_name import get_customer, get_alawael_url
from notification_gateway.data.web_status_code import STATUS_CODE_MAP


class SMS(MessageService):
    def send_message(self, name, phone_number, message_body, base64 = None):

        getOrganization = get_customer(name).organization
        getUserName = get_customer(name).provider_name
        url = get_alawael_url()

        data = {
           "orgName" : getOrganization,
           "userName" :  getUserName,
           "password" :  "FinTechaSys@1777789",
           "mobileNo":  phone_number, 
           "text":  message_body,
           "coding":  2
        }
        response = requests.get(url, params=data)
        print(f"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR{response}RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        status = STATUS_CODE_MAP.get(response.status_code, 'Failed')
        return status
import requests
import urllib.parse
from notification_gateway.notification_gateway.doctype.lago_customer.lago_customer import current_usage
from notification_gateway.methods.get_doc_name import get_customer, get_wppconnect_url
from .message_service import MessageService
from notification_gateway.data.web_status_code import STATUS_CODE_MAP

class Whatsapp(MessageService):
    def send_message(self, name, phone_number, message_body, base64):

        if current_usage() == 5:
            print("You have consumed all your messages")
        else:       
            url = get_wppconnect_url()
            baseUrl = urllib.parse.urljoin(url, get_customer(name).session)
            status = 'Failed'

            url = f"{baseUrl}/send-message"
            data = {
                "phone": phone_number,
                "isGroup":False,
                "isNewsletter": False,
                "message": message_body
            }
            headers = { 
                "Authorization": f"Bearer {get_customer(name).auth_token_wam}",
                "Content-Type": "application/json; charset=utf-8",
            }
            if base64: #if the whatsapp message has an image both the url and data are updated

                base64_prefix = "data:image/jpeg;base64,"
                full_base64 = f'{base64_prefix}{base64}'

                url = f"{baseUrl}/send-image"
                data.update({"base64": full_base64})

            response = requests.post(url, json=data, headers=headers)
            status = STATUS_CODE_MAP.get(response.status_code, 'Failed')
            
            return status
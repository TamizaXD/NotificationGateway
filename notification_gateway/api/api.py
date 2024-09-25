import frappe
from notification_gateway.methods.get_doc_name import get_customer


@frappe.whitelist(allow_guest=False)
def send_message(name, message, base64 = None):
    """
    Submits a wallet payment.

    :param name: The name of the wallet payment to submit.
    :type name: str
    :param password: The password to confirm the transaction.
    :type password: str
    :return: The submitted wallet payment document.
    :rtype: frappe.model.document.Document
    """
    #name, message, and base64 are parameters passed through Postman

    getSender = get_customer(name).customer_detail
    getMessageServiceType = get_customer(name).service_type
    getMessageService =  get_customer(name).service_type
    method = 'notification_gateway.methods.add_to_message.add_to_message_dt'
    
    frappe.enqueue(method,    
                   name = name,
                   sender = getSender,
                   message = message,
                   message_time = frappe.utils.now(), 
                   message_service_type = getMessageServiceType, 
                   message_type = getMessageService,
                   message_status = 'Pending',
                   base64 = base64
                )
    return { #test in Postman 
        "status": "Message queued for sending",
        "Sender": getSender,
        "Message": message,
        "Message Service Type": getMessageServiceType
    }

# http://127.0.0.1:8001/api/method/notification_gateway.api.api.send_message

# + GET /api/v2/method/Sales Order/make_sales_invoice

# http://127.0.0.1:8001/api/v2/send_message
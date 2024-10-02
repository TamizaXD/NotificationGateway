# Copyright (c) 2024, mohammed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from notification_gateway.notification_gateway.doctype.lago_customer.lago_customer import current_usage, make_event 
from notification_gateway.methods.get_doc_name import get_customer

class MessageService(Document):
	pass

@frappe.whitelist(allow_guest=False)
def send_message(name, message, base64 = None):

	getSender = get_customer(name).customer_detail
	getMessageServiceType = get_customer(name).service_type
	getMessageService = get_customer(name).service_type
	method = 'notification_gateway.methods.add_to_message.add_to_message_dt'
	
	if current_usage() <= 10:
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
		
		# make_event()
	# return { #test in Postman 
    #     "status": "Message queued for sending",
    #     "Sender": getSender,
    #     "Message": message,
    #     "Message Service Type": getMessageServiceType
    # }
# http://127.0.0.1:8001/api/v2/method/Message Service/send_message
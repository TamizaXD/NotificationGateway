import frappe
from notification_gateway.methods.message_log import add_to_message_log_dt, add_to_frappe
from notification_gateway.methods.get_doc_name import get_customer
from notification_gateway.methods.clean_number import remove_non_numeric
from notification_gateway.classes.message_factory import MessageFactory

def add_to_message_dt(name, sender, message, message_time, message_service_type, message_type, message_status, base64):

    message_dt = frappe.get_doc({
        'doctype': 'Message',
        'sender': sender,
        'message': message,
        'timestamp': message_time,
        'message_service_type': message_service_type,                               
        'message_type': message_type,
        'status': message_status,
        'base64': base64
    })

    add_to_frappe(message_dt)
    
    getReceiverPhoneNumber = remove_non_numeric(get_customer(name).receiver_phone_number) 
    getSenderPhoneNumber = remove_non_numeric(get_customer(name).phone_number) #change it to the sender instead??

    messageFactory = MessageFactory()
    msg = messageFactory.createMessage(message_type)
    status = msg.send_message(name, getReceiverPhoneNumber, message ,base64)

    update_message_status(message_dt.name, status)
    add_to_message_log_dt(getSenderPhoneNumber, getReceiverPhoneNumber, frappe.utils.now(), message, message_status, message_dt.name, base64)

def update_message_status(name, status):
    frappe.db.set_value('Message', f'{name}','status', f'{status}') #updataing the the message status from 'Pending' to the new status like 'Completed' or 'Failed'
    frappe.db.commit()
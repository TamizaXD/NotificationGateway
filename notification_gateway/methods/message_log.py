import frappe

def add_to_message_log_dt(sender_number, receiver_number, timestamp, message, status, message_link , base64 = None): 

    target_doctype = frappe.get_doc({
        'doctype': 'Message Log',
        'sender_number': sender_number,
        'receiver_number': receiver_number,
        'timestamp': timestamp,
        'message': message,
        'status':status,
        'message_link': message_link,
        'message_image': base64
    })

    add_to_frappe(target_doctype) # this function ensures the record is being inserted and saved in the Message Log Doctype

def add_to_frappe(target):
    target.insert()
    frappe.db.commit()
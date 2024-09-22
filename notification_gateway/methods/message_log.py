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
    # update_message_status(target_doctype.name, )

    return target_doctype.name

def add_to_frappe(target):
    target.insert()
    frappe.db.commit()

def update_message_status(name, status):
    frappe.db.set_value('Message', f'{name}','status', f'{status}') #updataing the the message status from 'Pending' to the new status like 'Completed' or 'Failed'
    frappe.db.commit()
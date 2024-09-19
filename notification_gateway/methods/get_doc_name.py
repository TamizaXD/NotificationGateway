import frappe 

get_customer = lambda customer_name: frappe.get_doc("Message Service", customer_name) # lambda function that returns the whole record based on its name in the Doctype

def get_wppconnect_url():
    config = frappe.get_doc("Message Configuration")
    wppconnectURL = config.wppconnect_url
    return wppconnectURL

def get_alawael_url():
    config = frappe.get_doc("Message Configuration")
    alawael_url = config.alawael_url
    return alawael_url
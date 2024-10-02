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

def get_lago_url():
    config = frappe.get_doc("Lago Configuration")
    lago_url = config.lago_customer_endpoint
    return lago_url

def get_lagp_key():
    config = frappe.get_doc("Lago Configuration")
    lago_key = config.lago_api_key
    return lago_key
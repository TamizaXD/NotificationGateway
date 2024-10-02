# Copyright (c) 2024, mohammed and contributors
# For license information, please see license.txt

import frappe, requests
from notification_gateway.methods.get_doc_name import get_lago_url, get_lagp_key
from frappe.model.document import Document

class LagoCustomer(Document):
	def before_save(self):
		self.legal_name = f"{self.first_name} {self.last_name}"
		add_new_customer(self)

@frappe.whitelist(allow_guest=False)
def add_new_customer(self):

	url = get_lago_url()
	headers = {
		"Authorization": f"Bearer {get_lagp_key()}",
        "Content-Type": "application/json",
	}
	data = {
		"customer": {
      		"external_id":self.name,
      		"legal_name": self.legal_name,
      		"name": self.first_name,
      		"phone": self.phone_number
    	}
	}
	try:
		requests.post(url, json=data, headers=headers)
	except Exception as e:
		print(f"ERROR: {e}")

@frappe.whitelist(allow_guest=True)
def current_usage():

	url = f"{get_lago_url()}/lago-ctm-288/current_usage"
	headers = {
		"Authorization": f"Bearer {get_lagp_key()}",
        "Content-Type": "application/json",
	}
	data = {
		"external_subscription_id" : "145e9ac6-cbae-45cf-834c-13071f461618"
	}
	try:
		response = requests.get(url, params=data, headers=headers).json()
		events_count = response['customer_usage']['charges_usage'][0]['events_count']

		return events_count
	except Exception as e:
		frappe.msgprint(f"ERROR: {e}")

@frappe.whitelist(allow_guest=True)
def make_event():
	
	uage = current_usage() + 1
	url = "http://localhost:3000/api/v1/events"
	headers = {
		"Authorization": f"Bearer {get_lagp_key()}",
        "Content-Type": "application/json",
	}
	data = {
		"event": {
          "transaction_id": f"00{uage}",
          "external_subscription_id": "145e9ac6-cbae-45cf-834c-13071f461618",
          "code": "sms10",
          "properties": {
            "count": 10
          }
      }
	}
	try:
		response = requests.post(url, json=data, headers=headers)
		return response.json()
	except Exception as e:
		pass

# 	return count

@frappe.whitelist(allow_guest=True)
def adjust_plan():

	url = "http://localhost:3000/api/v1/plans/sms10"
	headers = {
		"Authorization": f"Bearer {get_lagp_key()}",
        "Content-Type": "application/json",
	}
	
	data = {
		"plan":{
        	"amount_cents": get_plan() - 100
    	}
	}
	try:
		response = requests.put(url, json=data, headers=headers).json()
		amount_used = response['plan']["amount_cents"]
		return amount_used
	except Exception as e:
		pass

@frappe.whitelist(allow_guest=True)
def get_plan():

	url = "http://localhost:3000/api/v1/plans/sms10"
	headers = {
		"Authorization": f"Bearer {get_lagp_key()}",
        "Content-Type": "application/json",
	}
	try:
		response = requests.get(url, headers=headers).json()
		amount = response['plan']["amount_cents"]
		return amount
	except Exception as e:
		pass
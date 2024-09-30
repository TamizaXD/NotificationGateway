# Copyright (c) 2024, mohammed and contributors
# For license information, please see license.txt

import frappe, requests
from frappe.model.document import Document

class LagoCustomer(Document):
	def before_save(self):
		self.legal_name = f"{self.first_name} {self.last_name}"
		add_new_customer(self)

@frappe.whitelist(allow_guest=False)
def add_new_customer(self):

	url = "http://localhost:3000/api/v1/customers"
	headers = {
		"Authorization": "Bearer 4b72ccc6-441e-42d7-bcc0-e32c2bbeb501",
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
		frappe.msgprint("Customer Created")
	except Exception as e:
		frappe.msgprint("Customer is not Created")
		print(f"ERROR: {e}")
	

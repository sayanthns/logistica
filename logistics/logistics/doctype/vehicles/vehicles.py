# Copyright (c) 2023, siva and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Vehicles(Document):
	def validate(self):
		frappe.db.set_value("Drivers",{'name':self.current_driver},'status','Vehicle Assigned')	
		frappe.db.set_value("Drivers",{'name':self.current_driver},'current_vehicle',self.name)

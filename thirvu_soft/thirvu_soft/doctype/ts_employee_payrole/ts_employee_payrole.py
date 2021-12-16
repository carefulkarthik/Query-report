# Copyright (c) 2021, Navin S R and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import date

class TsEmployee_payrole(Document):
	def validate(self):
		#a=self.ts_enddate - self.ts_startdate
		#self.ts_totaldays=a.days
		if self.ts_totaldays >=25 :

			bp={"Team member":8000 ,"Team lead":8000,"Tech lead":25000,"House keeping":18000}
			self.ts_basicpay=bp[self.ts_employee_designation]
		elif self.ts_totaldays: 
			bp={"Team member":6000 ,"Team lead":6000,"Tech lead":20000,"House keeping":14000}
			self.ts_basicpay=bp[self.ts_employee_designation]

		

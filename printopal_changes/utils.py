from __future__ import unicode_literals

import frappe
from frappe import _
import json


def get_tax_breakup_for_cgst_sgst(doc):
	tax_breakups = []
	if doc.doctype == 'Sales Invoice':
		taxes = {}
		for tax in doc.items:
			if tax.item_tax_template and tax.item_tax_rate:
				tax_rate = json.loads(tax.item_tax_rate)
				rate = sum(float(val) for key,val in tax_rate.items())
				if not rate in taxes:
					taxes[rate] = 0
				taxes[rate] += 	tax.amount

		tax_template = frappe._dict({"taxable_amount": 0, "crate": 0, "camount": 0, "srate": 0, "samount": 0, "total_tax_amount": 0})
		for tax,amount in taxes.items():
			temp = tax_template.copy()
			temp.taxable_amount = amount
			tax_rate = (tax)/2
			tax_amount = (tax*amount)/100
			half_amount = (tax_amount)/2
			temp.crate = tax_rate
			temp.camount = half_amount
			temp.srate = tax_rate
			temp.samount = half_amount
			temp.total_tax_amount = tax_amount
			tax_breakups.append(temp)

	return tax_breakups

def get_item_gst_value(item):
	rate = 0
	if item.item_tax_template and item.item_tax_rate:
		tax_rate = json.loads(item.item_tax_rate)
		rate = sum(float(val) for key,val in tax_rate.items())

	return int(rate) if rate else 0
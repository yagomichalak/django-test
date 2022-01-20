import datetime
from typing import List, Dict, Union, Any
import json

def format_date(data_json) -> List[Dict[str, Union[str, int, datetime.datetime]]]:
	""" Formats the date from a json object. """
	#new_data_list: List[Dict[str, Union[str, int, datetime.datetime]]] = []


	for row in data_json:

		print(type(row))

		row_date = row['product_url__created_at']
		row_date_formatted = eval(row_date)#.strftime('%y-%m-%d %H:%M:%S')
		row['product_url__created_at'] = row_date_formatted

		#new_data_list.append(row)



	return data_json


def group_products(data_json) -> Dict[str, Union[str, int, datetime.datetime]]:
	""" Group duplicate products. """

	new_data_list: List[List[Dict[str, Union[str, int, datetime.datetime]]]] = []

	products: Dict[str, List[Any]] = {}

	for row in data_json:
		#print(row)
		print()

		if row['product_url'] in products:
			products[row['product_url']].append(row)
		else:
			products[row['product_url']] = [row]



	return products
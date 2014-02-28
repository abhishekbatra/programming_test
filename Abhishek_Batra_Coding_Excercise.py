#!/usr/bin/python
"""Q)  Consider Share prices for a N number of companies given for each month since year     
         1990 in a CSV file.  Format of the file is as below with first line as header.
 

Year,Month,Company A, Company B,Company C, .............Company N
1990, Jan, 10, 15, 20, , ..........,50
1990, Feb, 10, 15, 20, , ..........,50
.
.
.
.
2013, Sep, 50, 10, 15............500



a) List for each Company year and month in which the share price was highest.
b) Submit a unit test with sample data to support your solution."""

import csv
import unittest

def getHighestPrices(filename):
	with open(filename) as f:
		reader = csv.reader(f)
		highest_dict = dict()
		
		names = next(reader)[2:]

		for name in names:
			highest_dict[name] = (0, 0, 0)
			
		for row in reader:
			year, month = row[:2]
			for name, price in zip(names, map(int, row[2:])):
				if highest_dict[name][0] < price:
					highest_dict[name] = (price, year, month)
				
	return highest_dict

class StandardTest(unittest.TestCase):
	
	def test_sample(self):
		result = getHighestPrices("sample.csv")
		self.assertEqual(result["company 3"][0], 3600)
		
def main():
	print getHighestPrices("sample.csv")
	
if __name__ == '__main__':
	unittest.main()

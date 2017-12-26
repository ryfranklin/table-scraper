import csv
import urllib2
from BeautifulSoup import BeautifulSoup
import re

#uses uplopen to open the url.  
page = urllib2.urlopen("http://www.phoenixconcerts.net/")
soup = BeautifulSoup(page)

#Searches tag elements.  use 'attrs' to search for classes.
table  = soup.find('tbody')

list_of_rows = []
for row in table.findAll('tr')[1:]:
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('none', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)


outfile = open("./concert_list.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Event", "Date", "Venue", "Ticket"])
writer.writerows(list_of_rows)






import csv
from bs4 import BeautifulSoup as sp
from urllib.request import urlopen
import sys

def main(deptID):
# def main():

	

	base_url= 'http://jamiahamdard.edu/Department/Department_FacultyList.aspx?nDeptID='
	url = base_url + deptID

	with open('Department-Faculty-List.csv','w',newline='') as out_file:	
		csvwriter = csv.writer(out_file, delimiter=",")
		row = ["Name","Designation","Email ID"]
		csvwriter.writerow(row)


	#Storing the above url in html for using the scaper.
		url_client = urlopen(url)
		full_html = url_client.read()
		parsed_html = sp(full_html,'html.parser')
		url_client.close()
		faculty_table = parsed_html.find("table", {"class" : "table"}).find("tbody")
		faculty_rows = faculty_table.findAll("tr")

		for i in range(len(faculty_rows)):
			faculty_items = faculty_rows[i].findAll("td")

			try:
				name = faculty_items[1].text.strip()
			except AttributeError:
				name = "Not Available"

			try:
				designation = faculty_items[2].text.strip()
			except AttributeError:
				designation = "Not Available"	

			try:
				email = faculty_items[3].text.strip()
			except AttributeError:
				email = "Not Available"

			row = [name,designation,email]
			print (row)
			csvwriter.writerow(row)	
				

			#print("name = ", faculty_items[1].text)
			# for j in range(len(faculty_items)):
			# 	print(faculty_items[j])
			# try:
				
			# except AttributeError:
			# 	name = "Not available"
			# print ("name = ", name)

# print("Welcome to Department Faculty list generator!\n"
# 	 "______________________________________________\n")
# print("Choose your School from the following:\n")
# print("1. School of Chemical & Life Sciences\n"
# 	  "2. School of Unani Medical Education & Research\n"
# 	  "3. School of Pharmaceutial Education & Research\n"
# 	  "4. School of Nursing Sciences and Allied Health\n"
# 	  "5. School of Interdisciplinary Studies\n"
# 	  "6. School of Management and Business Studies\n")


# user_input = int(input("Enter your choice: "))
# print(user_input)
# if (user_input==1):
# 	ID='eo'
# elif(user_input==2):
# 	ID='is'
# elif(user_input==3):
# 	ID='ga'	
# else:	

# 	print("Your choice is incorrect")	



if __name__ == '__main__':
	main(ID)
	
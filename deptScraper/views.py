from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import csv, sys, os
from bs4 import BeautifulSoup as sp
from urllib.request import urlopen



def index(request):
	return render(request,'index.html')

#------------------------------------------Website Crawler Script------------------------------------------# 

def make_file(deptID):
	base_url= 'http://jamiahamdard.edu/Department/Department_FacultyList.aspx?nDeptID='
	url = base_url + deptID
	#print("url = ",url)
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
			#print (row)
			csvwriter.writerow(row)	
				
#fetching form data
def fetch_data(request):
	value=request.POST.get('school','default')
	value1=request.POST.get('dept1','default')
	value2=request.POST.get('dept2','default')
	value3=request.POST.get('dept3','default')
	value4=request.POST.get('dept4','default')
	value5=request.POST.get('dept5','default')
	value6=request.POST.get('dept6','default')
	value7=request.POST.get('dept7','default')
	value8=request.POST.get('dept8','default')
	value9=request.POST.get('dept9','default')



	if (value1 != "Choose your Department"):
		make_file(value1)
	elif (value2 != "Choose your Department"):
		make_file(value2)	#pass argument to python script
	elif (value3 != "Choose your Department"):
		make_file(value3)#pass argument to python script
	elif (value4 != "Choose your Department"):
		make_file(value4)#pass argument to python script
	elif (value5 != "Choose your Department"):
		make_file(value5)#pass argument to python script			
	elif (value6 != "Choose your Department"):
		make_file(value6)#pass argument to python script
	elif (value7 != "Choose your Department"):
		make_file(value7)#pass argument to python script
	elif (value8 != "Choose your Department"):
		make_file(value8)#pass argument to python script
	elif (value9 != "Choose your Department"):
		make_file(value9)#pass argument to python script
	else:
		("Choose the department")

	path = os.getcwd()+ '/Department-Faculty-List.csv' 
	print("Sending file...")
	response = FileResponse(open(path, 'rb'),as_attachment=True)
	os.remove(path)
	return response			

#About.html
def about(request):
 	return render(request,'about.html')

	
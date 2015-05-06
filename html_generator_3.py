'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Chapter 2 - Crate HTML document
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Psuedo Code for my Program 

#1 - HTML_informaiton 

Created an Input function called "HTML_informaiton" that houses the values that I want to use in my HTML document.

Note: There are a total of 4 list with 2 values per list. So each list will have value for our title and value for our description. 




#2 - Extract_HTML_info (HTML_informaiton )

Created "Extract_HTML_info" program that uses input variable "HTML_informaiton" values






#3 - Execute HTML_informaiton  program

"Execute HTML_informaiton" then executes to extracts and seperate my values in "HTML_informaiton" by using  funciton while loop steps through the values. 

Note:

Example: First Loop example
	
count= 0, starts at 0 because when grabing the information form HTML_informaiton it starts at 0
number = len(text) = 4, number of list in  the input varaible text (text = HTML_informaiton = 4)

while 0<4: (while loop is true as since 4 is greater than 0)
				
    a = text[0]                #  a = p[0] = save first list value in nest_loop list = [Title: HTML , Description: Hypertext Markup Language forms the structure of webpages],
	title =  test[0]                   #  title  = extract the title string = Title:HTML , grab the string value 
	description =  text[1]             #  description = estract strin = Description: Hypertext Markup Language forms the structure of webpages
    concept = title + description  #  concept = concatinaiotn of two string = Title:HTML Description: Hypertext Markup Language forms the structure of webpages





#4 - Small program within "while_program" 

A Small program exectures to extract informaiton for HTML: 
	
	
		Ex - Continue with first while loop: 
			
        #5.def get_title(concept):         ---> finds title information and stores it in the variable called  "title" 
                                           ---> title  = HTML Description

		#6. def get_description(concept):  ---> finds title description information and stores it in the variable "description"
		                                   ---> description = Hypertext Markup Language forms the structure of webpages
		
        #7. get_description(concept):      ---> uses the "title" and "description" information to populate through out our HTML document 
										    --->  prints of the html code using variable "title" and "description" to populate the HTML Code
										    <div class="concept">
											  												  	       <div class="concept-title">
											
											  													          HTML 
											  													       </div>
											
											  												  	       <div class="concept-description">
											
											  													       HTML stands for Hypertext Marup Language. HTML documents form the majority of the content on the web. HTML documents contain text content which describes "what you see" and markup which describes "how it looks
											  													       </div>
											  </div>
										




#8 - Order repeated in the while loop. 

The order is repeated with, "count=count+1" keeping track the next count for the next loop of html informaiton and also helps identify the next value in our nester list input.  




What I fixed in my 3rd attempt: 
1. Included more HTML informaiton 
2. Removed hard code in get_title(concept) & get_description(concept):
3. included similar HTML body information even thought this was supposed to show a simple HTML program per example in class
4. Renamed variables and functions to better explaine what they do


'''


#******************************************************************************************************************************************************************************

#3. Call the program "Extract_HTML_info" that executes to extract title and description information. New variable text = HTML_informaiton  = holds our list of input variables

def Extract_HTML_info (text): 
	count = 0       # i =0, starts count at 0. We'll use i to count in our while loop & select information from out list. (Note: List starts at 0 ... 4)
	number = len(text)  # n = len(p) = len(HTML_informaiton) = 4, we have a number of 4 elements our list with 2 pairs of information per list.   
	
	
	print '''<!DOCTYPE html>'''
	print '''<html>  '''
	print '''<body>'''
	
	while count< number:   # while n is greater then i is true the loop will keep running
		    
	
			a = text[count]      # a = saves the list information
			title =  a[0]        # title = a[0] = grabs the title string information from the list
			description =  a[1]  #description = a[1] = grabs the description string information fromt the list 
			
			concept = title + description  #concept = title + description = created a concatination string of the title and description information
			
			
			
			#4.  Small program within "while_program"
			#########################################################
			title = get_title(concept)                             #title =  input the concept in the program get_title and return the title info to variable 'title'
			description = get_description(concept)                 #description = input concept in the program ger_description and return the description info to variable 'description'
			concept_html = generate_concept_HTML(title, description)  #concept_html = generate html output with title variable and description variable
			
			#########################################################
						
			
			#8.  Order repeated and keeps counts 
			count = count + 1
		
	
	print "       "
	print "</body>"
	print "</html>"


#******************************************************************************************************************************************************************************
	
	
#5. Small Program - get_title, gets title information from concept variable
def get_title(concept):
	start = concept.find(" ")          #start = find location for the first space "  "
	end = concept.find("Description:") #endl = find location for the word "Description:"
	
	title = concept [start : end]   # title = give the information next to the word title in our list
	return  title                   # return the new variable called "title'
	
#6.	Small Program - get_description, gets description from concept variable
def get_description(concept):
	start_1 = concept.find(":", 9)    #start_1 = find location for the second space "  " so we set a range of 9 to go beyond the first space " "
	description = concept[start_1 + 1: ]   # description = give the information next to the word description and beyond the word
	return   description				# return the new variable called "description'
	
#7.Small Program - generate_concept_HTML , gets title & description and outputs there values in my HTML document. 
def generate_concept_HTML(title, description):
	
	
	
	  html_1 = '''
	  <div class="concept">
	  						<div class="concept-title">
	
	  						''' + title

	  html_2 = '''
	  						</div>
	
	  						<div class="concept-description">
	
	  						''' + description

	  html_3 = '''
	  						</div>
	  </div>'''

	  html_all = html_1 + html_2 + html_3  # html_all = holds the 3 string information 
	  print html_all					    #print html_all , prints the HTML document



  
# 1. Created input variable called "HTML_informaiton" that takes in a list of inputs that will used to populate our HTML document output
HTML_informaiton  = [


['Title: HTML', 'Description: HTML stands for Hypertext Marup Language. HTML documents form the majority of the content on the web. HTML documents contain text content which describes "what you see" and markup which describes "how it looks"'],

['Title: How the Web Works', 'Description: The web is a bunch of computers that communicate with each other. When a person goes to a web page like www.google.com, their computer sends a HTTP Request to a server. The server finds the appropriate HTML document and sends it back to the users computer where a web browser interprets the page and displays it on the users screen.'],

['Title: Tags and Elements', 'Description: HTML documents are made of HTML elements. When writing HTML, we tell browsers the type of each element by using HTML tags.'],

['Title: Why Computers are Stupid', 'Description: Computers are stupid because they interpret instructions literally. This makes them very unforgiving since a small mistake by a programmer can cause huge problems.']


		            ]
		


# 2. Created "Extract_HTML_info" program that uses input variable "HTML_informaiton"
Extract_HTML_info (HTML_informaiton)


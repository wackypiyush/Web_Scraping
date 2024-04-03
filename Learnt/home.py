from bs4 import BeautifulSoup

#--------------------------------------------
# with open('home.html',"r") as f:
#     content=f.read()

#     print(content)
#--------------------------------------------

#--------------------------------------------
# with open('home.html',"r") as f:
#      content=f.read()

#      soup=BeautifulSoup(content, 'lxml')
#      print(soup.prettify())
#--------------------------------------------

#--------------------------------------------
# with open('home.html',"r") as f:
#     content=f.read()
    
#     soup=BeautifulSoup(content, 'lxml')
#     tag=soup.find('h5')
#     print(tag,"\n")
    
#     tags=soup.find_all('h5')
#     print(tags) 
#     print()   
#     for t in tags:
#         print(t.text)
#--------------------------------------------

#--------------------------------------------
# with open('home.html',"r") as f:
#     content=f.read()
    
#     soup=BeautifulSoup(content, 'lxml')
#     course_cards=soup.find_all('div',class_='card')
#     for course in course_cards:
#         course_name=course.h5.text
#         course_cost=course.a.text.split()[-1]
#         print(f'{course_name} costs {course_cost}' )
#--------------------------------------------

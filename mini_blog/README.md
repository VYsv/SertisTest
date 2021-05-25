# Sertis
## Back-end  test

### Requirement
- python3
- pip install django
- pip install djangorestframework
   
### Quick Start
- py manage.py makemigrations
- py manage.py migrate
- py manage.py runserver

### Overview
#### Add new card:
PATH: /blog/post  
Request Content: JSON with name, status, content, category and author fields  

---

#### Edit card:
PATH: /blog/<blog_id>/edit  
Request Content: JSON with edited card name, status, content, category and author fields  

---

#### Delete card
PATH: /blog/<blog_id>/delete  
Request Content: JSON with name and author is fine  

**I don't understand edit part a bit that if request content is all edited so you can only pick the card by author and changed it? that make no sense so I assume that when you edit the card you have to enter to the card first, so we can get the id of the card that we gonna edit and check the author after picked the card
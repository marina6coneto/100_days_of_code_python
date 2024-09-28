from bs4 import BeautifulSoup

with open ('day_45/website.html') as file:
    contents = file.read()
   
   
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
# print(soup.a)

# all_anchor_tag = soup.find_all(name='a')
# print(all_anchor_tag)

# all_anchor_tag = soup.find_all(name='a')
# for tag in all_anchor_tag:
#     print(tag.get('href'))
    
# heading = soup.find(name='h1', id='name')
# print(heading)

# seaction_heading = soup.find(name='h3', class_='heading')
# print(seaction_heading)
# print(seaction_heading.get_text())

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

classes = soup.select('.heading')
print(classes)
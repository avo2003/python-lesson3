from bs4 import BeautifulSoup
html_atag="""<html><body><p>Test html a tag example</p>
<a href='http://www.packtpub.com'>Home</a>
<a href='http://www.packtpub.com/books'>Books</a>
</body>
</html>"""
soup = BeautifulSoup(html_atag,features="html.parser")
atag = soup.a
print (atag)
tagname = atag.name
print(tagname)
print (atag['href'])
first_a_string = atag.string
print(first_a_string)

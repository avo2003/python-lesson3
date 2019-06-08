from bs4 import BeautifulSoup
with open ("foo.html","r") as foo_file:
	soup_foo = BeautifulSoup(foo_file, features="html.parser")
	print(soup_foo)

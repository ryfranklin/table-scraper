
import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.bash.academy/")
html = page.read()
soup = BeautifulSoup(html)

print soup.prettify() 





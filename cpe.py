
from bs4 import BeautifulSoup # pip install beautifulsoup4 lxml
import urllib2
# http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3-20151001-003305.xml
soup = BeautifulSoup(urllib2.urlopen("http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3-20151001-003305.xml"), "lxml-xml")
# cpe:{part}:{vendor}:{product}:{version}
for tag in soup.find_all("cpe-item"):
	mcpe = tag["name"].split(":")
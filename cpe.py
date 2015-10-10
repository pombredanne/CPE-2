import psycopg2
from bs4 import BeautifulSoup
# pip install beautifulsoup4 lxml
import urllib2


class CPE:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.xmllocation = "http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/" \
                           "official-cpe-dictionary_v2.3-20151001-003305.xml"

    def connect(self, host, dbname, user, passwd):
        conn_string = "host=%s dbname=%s user=%s password=%s" % (host, dbname, user, passwd)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def commitdb(self):
        self.conn.commit()

    def initdb(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS CPE
            (
              id serial primary key,
              part text,
              vendor text,
              product text,
              version text
            )""")
        self.commitdb()

    def insert_cpe(self, part, vendor, product, version):
        self.cursor.execute("INSERT INTO CPE (part, vendor, product, version) VALUES (%s, %s, %s, %s)",
                            (part, vendor, product, version))

    def load_remote_xml(self):
        soup = BeautifulSoup(urllib2.urlopen(
            self.xmllocation),
            "lxml")
        # cpe:{part}:{vendor}:{product}:{version}
        for tag in soup.find_all("cpe-item"):
            mcpe = tag["name"].split(":")
            (part, vendor, product, version) = (mcpe[1], mcpe[2], mcpe[3], mcpe[4])
            self.insert_cpe(part, vendor, product, version)
            # print CPE.tostring(part, vendor, product, version)
        self.commitdb()

    @staticmethod
    def tostring(part, vendor, product, version):
        return part + ":" + vendor + ":" + product + ":" + version

if "__main__" == __name__:
    cpe = CPE()
    cpe.connect('localhost', 'test', 'tfairane', '')
    cpe.initdb()
    cpe.load_remote_xml()
    cpe.close()

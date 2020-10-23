import requests,time
from datetime import datetime
# import datetime

def mediviahouses(city, status, beds, size = 0):
    print("\nSearching for houses in "+city+".")
    url = "https://medivia.online/community/houses/legacy/%s/%s" % (city, status)
    
    page = requests.get(url, {'User-Agent': 'Mozilla/5.0'}).text

    headsplit = '''                        <div class="med-width-33">Current auction</div>
                    </strong>
                </li>'''

    tailsplit = '''                            
            </ul>
        </div>
	</div>
</div>'''

    page = page.split(headsplit)[1]
    page = page.split(tailsplit)[0]
    page = page.split('href="')
    page = page[1:]

    house_urls = []
    for house in page:
        houseurl = house[0:22]
        if "house" in houseurl:
            fullurl = "https://medivia.online"+houseurl
            house_urls.append(fullurl)


    for hurl in house_urls:
        page = requests.get(hurl, {'User-Agent': 'Mozilla/5.0'}).text
        page = page.split('<div class="title">')[1]
        endsplit = '''    </div>
</div>'''
        page = page.split(endsplit)[0]

        name_server = page.split('</div>')[0]
        name = name_server.split(' on')[0]
        server = name_server.split('on ')[1]
        hsize = page.split('The house has a size of <b>')[1].split('</b> square meters')[0]
        rent = page.split('The monthly rent is <b>')[1].split('</b>')[0]
        nrbeds = page.split('The house has <b>')[1].split('</b>')[0]
        
        if status == "rented":
            try:
                last_pay = page.split('The rent has been paid until')[1].split(', ',1)[1].split('. <br>')[0]
                last_pay = datetime.strptime(last_pay, '%b %d, %Y %I:%M %p')
            except:
                last_pay = datetime.now()

            today = datetime.now()
            if last_pay < today:
                if int(nrbeds) >= beds:
                    print(name+" has not payed rent since "+str(last_pay)+".\n"+hurl+"\nThis house has "+str(beds)+" or more beds and rent: "+rent+" gp.\n")

        if status == "available":
            if int(nrbeds) >= beds:
                print("This house has "+nrbeds+" beds: "+hurl)

            if int(hsize) >= size:
                print("This house is "+hsize+" sqm large: "+hurl)
                


min_size = 150
min_bed = 3
status = "available"
cities = ["mittenhoff", "eschen", "arak", "thoris", "osaris", "garrogat", "abukir", "icenhaal", "yehsha"]
for city in cities:
    mediviahouses("mittenhoff", status, min_bed, min_size)
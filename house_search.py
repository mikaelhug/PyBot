import requests,time
from datetime import date

def mediviahouses(city, status, beds):
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


    for hurl in house_urls[0:1]:
        page = requests.get(hurl, {'User-Agent': 'Mozilla/5.0'}).text
        page = page.split('<div class="title">')[1]
        endsplit = '''    </div>
</div>'''
        page = page.split(endsplit)[0]

        name_server = page.split('</div>')[0]
        name = name_server.split(' on')[0]
        server = name_server.split('on ')[1]
        rent = page.split('The monthly rent is <b>')[1].split('</b>')[0]
        beds = page.split('The house has <b>')[1].split('</b>')[0]

        # print(page)

        print(name)
        print(server)
        print(rent)
        print(beds)
        
        if status == "rented":
            last_pay = page.split('The rent has been paid until')[1].split(', ',1)[1].split('. <br>')[0]
            last_pay = last_pay.rsplit(' ',2)[0]
            last_pay = date.strptime(last_pay, '%b %d, %Y')
            today = datetime.today().date()
            if last_pay < today:
                print("not payed rent")
            print(last_pay)
            print(datetime.today().date())

        # page = page.split('</b>  door')[0]
        # nrbeds = page.split('</b>')[0]
        # # time.sleep(0.2)

        # if int(nrbeds) >= beds:
        #     print(hurl)


# mediviahouses("yehsha", "available", 3)
mediviahouses("yehsha", "rented", 3)

# mediviahouses("mittenhoff")
# mediviahouses("eschen")
# mediviahouses("arak")
# mediviahouses("thoris")
# mediviahouses("osaris")
# mediviahouses("garrogat")
# mediviahouses("abukir")
# mediviahouses("icenhaal")
# mediviahouses("yehsha")

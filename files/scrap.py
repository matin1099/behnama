
#Scraping and getting image
import requests
import bs4
import  datetime

class scrap:
    def __init__(self, url:str, header:dict) -> None:
        print("init run!")
        self.link = url
        print("link run!")
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        #self.header = dict(header)
        self.grab (self.link, self.header)
        print("grab run!")

    

    def grab(self,url,headers):
        try:
            print("1")
            req = requests.get(self.link, headers=self.header)
            if req.status_code == 200 :
                print("2")
                print("Request respond Successfully.")
                raw_html = bs4.BeautifulSoup(req.text,"lxml")
                pt_url = raw_html.select("img")[1]["src"] 
                try:
                    pt_bimg = requests.get(pt_url,headers=self.header)
                    pt_bimg = requests.get(pt_url,headers=self.header)
                    if pt_bimg.status_code == 200 :
                        print("image recived.")
                        self.save_img(pt_bimg.content)
                        
                except:
                    print("URL is good.CANNOT TAKE IMAGE.")

            elif req.status_code == 403:
                print("we got forbidon. CHANGE HEADER!")
            
            else:
                print("somthing happend, perhaps Internet???")
        except:
            print("Can NOT connect to website. CHECK URL MAUALLY.\n HTTPS ERR Code:\t{}".format(req.status_code))
        

    def save_img(self, img_context):

        self.name_gen =datetime.datetime.now().strftime(format="%d-%m-%Y-__-%H-%M")+".png"
        f = open(self.name_gen, "wb")
        f.write(img_context)
        f.close()
        print("image created")
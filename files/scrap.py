
#Scraping and getting image
import requests
import bs4
import  datetime

class scrap:
    def __init__(self, url:str, header:dict) -> None:
        #Getting url and setting header for grub
        print("init run!")
        self.link = url
        print("link run!")
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.grab (self.link, self.header)
        print("grab run!")

    

    def grab(self,url,headers):
        try:
            #start request
            req = requests.get(self.link, headers=self.header)
            if req.status_code == 200 :
                #try to find Price table (pt) url
                print("Request respond Successfully.")
                raw_html = bs4.BeautifulSoup(req.text,"lxml")
                pt_url = raw_html.select("img")[1]["src"] 
                try:
                    #try to get url (DOUBLE TIME REQ SOMETIMES IT WONT WORK FOR FIST TIME!)
                    pt_bimg = requests.get(pt_url,headers=self.header)
                    pt_bimg = requests.get(pt_url,headers=self.header)
                    # save image if PT binery getted
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
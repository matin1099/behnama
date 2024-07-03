
#Scraping and getting image
import requests
import bs4
import  datetime

from  loguru import logger

from files.sound import notification_scrap
class Scrap:
    def __init__(self, url:str, previous_url:str) -> None:
        #Getting url and setting header for grub
        self.link = url
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        logger.success("Scraper initiated successfully")


    

    def grab(self, old_url):
        """grab and save new image

        Args:
            old_url (str): old Url

        Returns:
            _type_: _description_
        """
        try:
            #start request
            req = requests.get(self.link, headers=self.header)
            if req.status_code == 200 :
                #try to find Price table (pt) url
                logger.trace("Request respond Successfully.")
                raw_html = bs4.BeautifulSoup(req.text,"lxml")
                pt_url = raw_html.select("img")[1]["src"] 
                logger.trace("Picture url found")
                
                #Check IF url Changed.
                if self.check(old_url,pt_url):

                    try:
                        logger.info("Start to get new picture.")
                        #try to get url (DOUBLE TIME REQ SOMETIMES IT WONT WORK FOR FIST TIME!)
                        pt_bimg = requests.get(pt_url,headers=self.header)
                        pt_bimg = requests.get(pt_url,headers=self.header)
                        # save image if PT binery getted
                        if pt_bimg.status_code == 200 :
                            logger.trace("image recived.")
                            name = self.save_img(pt_bimg.content)
                            return  pt_url, name
                            
                    except:
                        logger.critical("URL is good.CANNOT TAKE IMAGE.")

            elif req.status_code == 403:
                logger.critical("we got forbidon. CHANGE HEADER!")
            
            else:
                logger.critical("somthing happend, perhaps Internet???")
        except:
            logger.critical("Can NOT connect to website. CHECK URL MAUALLY.\n HTTPS ERR Code:\t{}".format(req.status_code))
        

    def save_img(self, img_context):
        
        self.name_gen =datetime.datetime.now().strftime(format="%d-%m-%Y-__-%H-%M")+".png"
        f = open(self.name_gen, "wb")
        f.write(img_context)
        f.close()
        logger.trace("image created")
        return self.name_gen

    def check(self,old_url, new_url):
        return old_url != new_url
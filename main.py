from files.cfg import Cfg
from files.scrap import Scrap
from files.spotter import Spotter


import time
import shutil
import os



def archiver(old_image_name) -> None :

    shutil.move(old_image_name, './archive/')


if "archive" not in os.listdir():
    print("create folder")
    os.mkdir("archive")
else:
    print("there is folder")

config = Cfg().read_cfg()
tehran_pakhsh, ahora, yaran = config[0]["tehranPakhsh"], config[0]["ahora"], config[0]["yaran"]
halt = config[1]
prev = config[2]
old_image=config[3]

#call for scrap tehranPakhsh
tehran_pakhsh_scraper = Scrap(tehran_pakhsh,previous_url=prev["tehranPakhsh"])


while True:

    new_url,new_img=tehran_pakhsh_scraper.grab(prev["tehranPakhsh"])
    if new_img != old_image["tehranPakhsh"]:
        Spotter().spot(old_image["tehranPakhsh"], new_img)
        archiver(old_image["tehranPakhsh"])

        Cfg().change_info("prev_url","tehranPakhsh",new_url)
        Cfg().change_info("prev_image_name","tehranPakhsh",new_img)


        config = Cfg().read_cfg()
        prev = config[2]
        old_image=config[3]
        print("reach_to halt")
        time.sleep(halt)
#tehran_pakhsh_scraper = scrap(tehran_pakhsh,header)
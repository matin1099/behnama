from files.cfg import Cfg
from files.scrap import Scrap
from files.spotter import Spotter


from  loguru import logger

import time
import shutil
import os



def archiver(old_image_name) -> None :

    shutil.move(old_image_name, './archive/')
    logger.info("{} had archived.")


if "archive" not in os.listdir():
    logger.trace("Createing archive folder.")
    os.mkdir("archive")
else:
    logger.info("Found archive folder.")
#Log output
logger.add("logs.log")


config = Cfg().read_cfg()
tehran_pakhsh,  yaran = config[0]["tehranPakhsh"],  config[0]["yaran"]
halt = config[1]
prev = config[2]
old_image=config[3]
logger.success("Reading config successfully.")

#call for scrap tehranPakhsh
tehran_pakhsh_scraper = Scrap(tehran_pakhsh,previous_url=prev["tehranPakhsh"])
logger.trace("Initiated TehranPakhsh scraper.")
#
#
##
"""yaran_scraper = Scrap(yaran,previous_url=prev["yaran"])
logger.trace("Initiated Mobile Yaran scraper.")
"""

while True:
    logger.info("Start to Scrap tehran pakhsh")
    info =tehran_pakhsh_scraper.grab(prev["tehranPakhsh"])
    if info != None:
        new_url , new_img = info[0],info[1] 

        if new_img != old_image["tehranPakhsh"]:
            logger.info("New image!")
            Spotter().spot(old_image["tehranPakhsh"], new_img)
            archiver(old_image["tehranPakhsh"])

            Cfg().change_info("prev_url","tehranPakhsh",new_url)
            Cfg().change_info("prev_image_name","tehranPakhsh",new_img)
            logger.trace("Change Config.json parameters with new ones.")

            config = Cfg().read_cfg()
            prev = config[2]
            old_image=config[3]
            logger.trace("Read config for new run.")
    logger.info(f"Halt for {halt} secends")
    time.sleep(halt)


""" logger.info("Start to Scrap Yaran")
    info = yaran_scraper.grab(prev["tehranPakhsh"])
    if info != None:
        new_url , new_img = info[0],info[1] 

        if new_img != old_image["yaran"]:
            logger.info("New image!")
            Spotter().spot(old_image["yaran"], new_img)
            archiver(old_image["yaran"])

            Cfg().change_info("prev_url","yaran",new_url)
            Cfg().change_info("prev_image_name","yaran",new_img)
            logger.trace("Change Config.json parameters with new ones.")

            config = Cfg().read_cfg()
            prev = config[2]
            old_image=config[3]
            logger.trace("Read config for new run.")"""
    

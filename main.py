from files.cfg import Cfg
from files.scrap import Scrap
from files.spotter import Spotter

"""TODO
    make scrap check if link changed.(perv link in json)
    returning name of new image for spotter
    making spotter remain prev one
    making old pics go to another dir
    making cfg json file to write old names
"""
config = Cfg().read_cfg()
tehran_pakhsh, ahora, yaran = config[0]["tehranPakhsh"], config[0]["ahora"], config[0]["yaran"]
header = config[1]
halt = config[2]
prev = config[3]
old_image=config[4]
print(old_image)
print(old_image["tehranPakhsh"])
#call for scrap tehranPakhsh
tehran_pakhsh_scraper = Scrap(tehran_pakhsh,previous_url=prev["tehranPakhsh"])


#while True:

new_url,new_img=tehran_pakhsh_scraper.grab(prev["tehranPakhsh"])
if new_img != old_image["tehrabPakhsh"]:
    Spotter().spot(old_image["tehrabPakhsh"], new_img)
    #change json file image old name with new_image
    #change json file oldurl with new_url
#tehran_pakhsh_scraper = scrap(tehran_pakhsh,header)




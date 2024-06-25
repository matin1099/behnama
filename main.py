from files.cfg import Cfg
from files.scrap import scrap
from files.spotter import spotter

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
print(prev)
print(type(prev))
#call for scrap tehranPakhsh
#tehran_pakhsh_scraper = scrap(tehran_pakhsh,header)




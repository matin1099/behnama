import json
class Cfg:
    def __init__(self,nothing="none") -> None:

        with open("Config.json", "r") as jf:
            self.data= json.load(jf)
            print ("config find SUCCESSFUL.")
            jf.close()

            
            

    def read_cfg(self) -> dict:
            urls = self.data["scrap_url"]
            halt = self.data["halt"]
            prev_url = self.data["prev_url"]
            old_image = self.data["prev_image_name"]
            print("config read Successfuly")
            return urls, halt, prev_url,old_image

    def change_image_info(self,section:str, website:str, new_info:str) -> None:
        self.data[section][website] = new_info if website != "" else self.data[section] = new_info
        with open("Config.json","w") as jf:
             updating = json.dump(self.data,jf)
             jf.close()
        print("json Updated")
        

    def __str__(self) -> str:
         return(
              f"""Context of Config:
              URLS:
              TehranPakhsh:\t{self.data["scrap_url"]["tehranPakhsh"]}
              Ahora:\t{self.data["scrap_url"]["ahora"]}
              Yaran:\t{self.data["scrap_url"]["yaran"]}
              
              REQUEST HEADER:
              {self.data["req_header"]}
              
              TIME FOR HALT:
              {self.data["halt"]}"""
         )

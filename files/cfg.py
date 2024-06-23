import json
class Cfg:
    def __init__(self,nothing="none") -> None:

        with open("Config.json", "r") as jf:
            self.data= json.load(jf)
            print ("config find SUCCESSFUL.")
            jf.close()

            
            

    def read_cfg(self) -> None:
            urls = self.data["scrap_url"]
            header = self.data["req_header"]
            halt = self.data["halt"]
            print("config read Successfuly")
            return urls, header, halt

    def change_cfg(self) -> None:
        pass

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
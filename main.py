import time
class Malumot:
    def __init__(self,person,tong,abet,kechgipayt,kuchqurun):
        self.person = person
        self.tong = tong
        self.abet = abet
        self.kechgipayt = kechgipayt
        self.kuchqurun = kuchqurun
        self.tongpayt()
    def tongpayt(self):
        print(f"Soat {self.tong} va {self.person} uyg'ondi , yuzini yuvdi tishini yuvdi va ovqatlandi")
        time.sleep(2)
        print("Uydagi ishlarni qildi")
        self.abetpayt()
    def abetpayt(self):
        time.sleep(2)
        print(f"Soat {self.abet} va {self.person},abet tayyorlab ovqatlandi")
        time.sleep(2)
        print(f"{self.person} ovqatlanib dasturxonni yig'di")
        time.sleep(2)
        print(f"{self.person} dasturxonni yig'ib dam oldi")
        self.kechgi()
    def kechgi(self):
        time.sleep(2)
        print(f"Soat {self.kechgipayt} va {self.person},kechgi dasturxon tayyorlab ovqatlandi")
        time.sleep(2)
        print(f"{self.person} ovqatlanib dasturxonni yig'di")
        time.sleep(2)
        print(f"{self.person} dasturxonni yig'ib dars qilishga o'tirdi")
        self.kech()
    def kech(self):
        time.sleep(2)
        print(f"Soat {self.kuchqurun} va {self.person} joy solib uxladi")
obj = Malumot("Bunyodbek",7,13,18,23)

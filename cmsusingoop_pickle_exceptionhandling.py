""" remaining section =
     1-  data is not sort
     2- exception handiling is not include
     3- restiction on input are there  """

#BLL
import json
import pickle
class costumer:
    listcos = []
    def __init__(self):
        self.id = 0
        self.name = 0
        self.cont_no = 0
        self.email = 0
        self.address = 0

    def addCostumer(self):#function add costumer
        costumer.listcos.append(self)

    def searchCostumer(self):#function for search costumer
        for e in costumer.listcos:
            if e.id == self.id:
                self.name = e.name
                self.cont_no = e.cont_no
                self.email = e.email
                self.address = e.address
            return 1
        return 0
    @staticmethod
    def showCostumer(cos):
        print("id ",cos.id,"name ",cos.name,"cont_no ",cos.cont_no,"email",cos.email,"address",cos.address)

    def modifyCostumer(self):
        for e in costumer.listcos:
            if e.id ==self.id:

                e.name = self.name
                e.cont_no = self.cont_no
                e.email  = self.email
                e.address = self.address
            return 1
        return 0

    def deleteCostumer(self):
        for e in costumer.listcos:
            if e.id == self.id:
                 costumer.listcos.remove(e)
                 break

    def displayCostumer(self):
        for e in costumer.listcos:
            if e.id == self.id:
                self.name = e.name
                self.cont_no = e.count_no
                self.email = e.email
                self.address = e.address


    @staticmethod
    def saveinpickle():#to sve data in pickle form
            costumerinbytes = pickle.dumps(costumer.listcos)
            f = open("D:\\costumerusingtkinter.txt", "wb")#append mood nhi chal raha
            f.write( costumerinbytes)
            f.close()

    @staticmethod
    def loadthroughpickle():# to load data from pickle
        f = open("D:\\costumerusingtkinter.txt","rb")
        datainbytes = f.read()
        costumer.listcos = pickle.loads( datainbytes)
        f.close()

#"""json is acepted by all laungage"""
    @staticmethod
    def convertcostumerintodict(cus):#convert object into dict
        return cus.__dict__

    @staticmethod
    def convertdictintiobject(dict):#convert dict into object
        cus = costumer
        for e in dict.items():
            cus.__setattr__(e[0],e[1])
        return cus

    @staticmethod
    def saveinjsonfile():#json data ko dictionary me save karta to obect ko pahle dict me convert karana padega
        jsonlist = json.dumps(costumer.listcos,default = costumer.convertcostumerintodict)
        f = open("D:\\jsoncostumer.txt","w")
        f.write(jsonlist)
        f.close()

    @staticmethod
    def loadthroughjson():
        f = open("D:\\jsoncostumer.txt","r")
        listinjson = f.read()
        costumer.listcos = json.loads(listinjson,object_hook = costumer.convertdictintiobject)


#PL
if __name__ == "__main__":
    while(True):
        print("enter 1 for add,2 for serach,3 for modify,4 for delete,5 for disply,6 for save in pickle,7 for load in pickle,8 save in json,9 for load in json,10 for exit")
        ch = input("enter the choice")
        if ch =="1":#add code
         try:
                cos = costumer()
                cos.id = input("enter id")
                cos.name = input("enter name")
                cos.cont_no = input("enter mobile no")
                cos.email= input("enter email")
                cos.address = input("enter address")
                cos.addCostumer()
                print("costumer add successfully")
         except Exception as ex:
             print(ex)

        elif ch =="2":#search code
            try:
                cos = costumer()
                cos.id = input("enter id ")
                flag = cos.searchCostumer()
                if flag == 0:
                    print("coatumer not fount")
                else:
                    costumer.showCostumer(cos)
            except Exception as ex:
                print(ex)

        elif ch =="3":# modify costumer
            try:
                cos = costumer()
                cos.id = input("enter id")
                cos.name = input("enter name")
                cos.cont_no = input("enter mobile no")
                cos.email = input("enter email")
                cos.address = input("enter address")
                flag = cos.modifyCostumer()
                if flag == 0:
                    print("costumer not fount ")
                else :
                    print("costumer modify successfully")
            except Exception as ex:
                print(ex)

        elif ch =="4":#delete costumer
            try:
                cos = costumer()
                cos.id = input("enter id ")
                cos.deleteCostumer()
                print("costumer deleted successfully")
            except Exception as ex:
                print(ex)

        elif ch == "5":#display costumer
             for e in costumer.listcos:
                 costumer.showCostumer(e)


        elif ch =="6":#to save file in pickle
            costumer.saveinpickle()
            print("costumer save in picklefile successfully")


        elif ch =="7":#toload datafrom picklefile
            costumer.loadthroughpickle()
            print("costumer load in picklefile successfully")


        elif ch =="8":# to sve in json
            costumer.saveinjsonfile()
            print("costumer save in jsonfile successfully")


        elif ch == "9":#to losd from json
             costumer.loadthroughjson()
             print("costumer load in jsonfile successfully")


        elif ch =="10":
            print("invaild choice")

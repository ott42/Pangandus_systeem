#Parent Class : User
#Has a function to show user details
#Child Class : Bank
#Stores details about the account balance
#Stores details about the amount
#Allows for deposits, withdraw,view_balance
#Parent class

class User(): #klass mille nimi on user
    def __init__(self,name,age,gender): #kolm erinevat argumenti mida kasutatakse objekti vanuse, nime ja soo atribuutide väärtuste määäramiseks
        self.name = name #kasutaja määrab endale nime
        self.age = age #kasutaja määrab endale vanuse
        self.gender = gender #kasutaja määrab endale soo
        
    def show_details(self): #temal on õigus igale objektile üleval pool, liige kasutajaklassis
        print("Personal Details") #see rida koodi väljastab personaalseid detaile
        print("")
        print("Name ", self.name) #see rida koodi väljastab nime
        print("Age  ", self.age) #see rida koodi väljastab vanuse
        print("Gender ", self.gender) #see rida koodi väljastab soo
        

#Child Class
class Bank(User): #panga klass
    def __init__(self,name,age,gender): #kolm erinevat argumenti mida kasutatakse objektide nime, vanuse ja soo atribuutide väärtusteks 
        super().__init__(name,age,gender)#see rida koodi kutsub vanema klassi, hetkel kasutajaklassi, meetodi __init__ ja edastab sellele nime, vanuse ja soo argumendid
        self.balance = 0 #see rida koodi rahasumma on 0, mis ise on määratud
    
    def deposit(self,amount): #see rida koodi määratleb meetodi nimega deposit, mis on panga klassi liige. Meetodil on kaks parameetrit, self ja kogus/summa
        self.amount = amount #see rida koodi määrab objekti koguse/summa atribuudi väärtuse koguse/summa parameetri väärtuseks
        self.balance = self.balance + amount #rida teeb objekti suurema tasakaalu atribuudi väärtust kogsuse/summa parameetri väärtuse jagu
        print("Account balance has been updated : £", self.balance) #rida väljastab teadaande, et konto saldot on uunedatud koos konto hetkese jäägiga
        
    def withdraw(self,amount): #see rida koodi määrab meetodi nimega väljastus, mis on panga klassi liige. Mõlemal meetodil on kaks parameetrit: self ja kogus/summa
        self.amount = amount #see rida koodi määrab objekti koguse/summa atribuudi väärtuse koguse/summa parameetri väärtuseks
        if self.amount > self.balance: #see rida koodi teeb kindlaks, kas olemasoleva summa väärtus on suurem kui saldo väärtus. Kui see on tõene, tähendab see et kontol ei ole raha väljastamise lõpuleviimiseks piisavalt raha
            print("Insufficient Funds / Balance Available : £", self.balance) #see rida koodi prindib teate, et kontol ei ole piisavalt raha ja konto praeguse saldo
        else: #juhul kui atribuudi summa väärtus on väiksem kui atribuudi saldo väärtusest, siis käivitatakse järgnev plokk "else"
            self.balance = self.balance - self.amount #see rida koodi vähendab konto saldo atribuudi väärtust koguse/summa atribuudi väärtuse võrra
            print("Account balance has been updated : £", self.balance) #see rida koodi väljastab teate, et konto saldot on värskendatud koos konto hetkese jäägiga
            
    def view_balance(self): #see rida koodi määratleb meetodi "view_balance" ehk kuva summa, mis on panga klassi liige
        self.show_details() #see rida koodi väljastab välja teated
        print("Account balance has been updated : £", self.balance) #see rida koodi väljastab teate, et konto saldot on värskendatud koos konto hetkese jäägiga



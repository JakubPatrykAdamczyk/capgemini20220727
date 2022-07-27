    
class Employer:
    def __init__(self,f_name,l_name,age,job,salary,bonus):
        
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.job=job
        self.salary=salary
        self.bonus=bonus
        self.total_salary=int(self.salary)+int(self.bonus)
    
    def applybonus(self,bonus):
        self.bonus=bonus
        self.total_salary=int(self.salary)+int(self.bonus)
   
    def invoice(self):
        invn=str(self.f_name)+str(self.l_name)+".txt"
        f=open(invn,"w")
        f.write("name: " +self.f_name+ 
            "\nsurname: "+ self.l_name+
            "\nsalary: "+str(self.salary)+
            "\nbonus: "+str(self.bonus)+
            "\nsum: "+str(self.total_salary))
    
    
class Departament:
    def __init__(self,name):
        self.name=name
        self.users=[]
        
    def display_employers(self):
        for i in range(len(self.users)):
            print(self.users[i].f_name+" "+self.users[i].l_name)
        
    def add_employers(self,f_name,l_name,age,job,salary,bonus):
        self.users.append(Employer(f_name,l_name,age,job,salary,bonus))
    
    def applybonusall(self,bonus):
        for i in range(len(self.users)):
            self.users[i].applybonus(bonus)
    
    def searchname(self,name):
        for i in range(len(self.users)):
            if name==self.users[i].f_name:
                print(str(name)+" is "+ str(i))
    
    def searchsurname(self,name):
        for i in range(len(self.users)):
            if name==self.users[i].l_name:
                print(str(name)+" is "+ str(i))
    
    def searchemp(self,f_name,l_name):
        for i in range(len(self.users)):
            if f_name==self.users[i].f_name and l_name==self.users[i].l_name:
                print(str(f_name)+" "+str(l_name) +" is "+ str(i))

        


class Company:
    def __init__(self,name):
        self.name=name
        self.dep=[]
    
    def add_department(self,name):
        self.dep.append(Departament(name))
        

    def display_departaments(self):
          for i in range(len(self.dep)):
                print(self.dep[i].name)
    def save(self):
        f=open("employer.txt","w")
        for i in range(len(self.dep)):
            for j in range(len(self.dep[i].users)):
                f.write(self.dep[i].users[j].f_name+" "+self.dep[i].users[j].l_name +" "+str(self.dep[i].users[j].salary)+ " "+str(self.dep[i].users[j].bonus)+ "\n")

            
c=Company("JA")                                                     #creat company
c.add_department("IT")                                              #add departament
c.display_departaments()                                            #show departament

c.dep[0].add_employers("Jan","Kowalski",25,"IT",7000,0)             #add Employer
c.dep[0].users[0].applybonus(1000)                                  #addbonus to Employer
c.dep[0].applybonusall(1000)                                        #apply bonus to all Employer
c.dep[0].display_employers()                                        #show Employer

c.save()                                                            #save to file
c.dep[0].users[0].invoice()                                         #make invoice
c.dep[0].searchemp("Jan","Kowalski")                                #search name and surname (code ofert search by onlny name or onlny surname)





del c.dep[0].users[0]                                               #delete Employer
c.dep[0].display_employers()                                        #show Employer is delete

# c.display_departaments()
del c.dep[0]                                                        #delete departament
c.display_departaments()                                            #show departament is delete
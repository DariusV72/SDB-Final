from Domain.applicant import Applicant
from Domain.job import Job


class Repository:
    """
    Functie care se ocupa de operatiile CRUD pentru entitatile din aplicatie
    """
    def __init__(self) -> None:
        """
        Constructor pentru clasa repository
        """
        self._entities_list = []
    
    def find_position_of_entity(self, entity):
        """
        Functie folosita in aflarea pozitiei unei entitatil intr-o lista
        :param entity: (object) entitatea data
        :return: (int) pozitia entitatii in lista sau -1 daca aceasta nu se regaseste in lista
        """
        for i in range(len(self._entities_list)):
            if self._entities_list[i] == entity:
                return i
        return -1

    def add(self, entity):
        """
        Functie folosita in adaugarea unei entitati in lista
        :param entity: (object) entitatea data
        :return:
        """
        if self.find_position_of_entity(entity) != -1:
                raise Exception("Exista deja!")
        self._entities_list.append(entity)

    def delete(self, entity):
        """
        Functie folosita in stergerea unei entitati dintr-o lista
        Ridicam o eroare in cazul in care entitatea nu exista
        :param entity: (object) entitatea data
        :return:
        """
        position = self.find_position_of_entity(entity)
        if position == -1:
            raise Exception("Nu exista!")
        
        del self._entities_list[position]

    def get_all(self) -> list:
        """
        Functie care returneaza lista de entitati
        :return: (list) lista de entitati
        """
        return self._entities_list
    
    def __print_commands(self):
        print("1. Modificare titlu")
        print("2. Modificare departament")
        print("3. Modificare salar")
        print("4. Modificare ani de experienta ceruti")
        print("5. Modificare numar de locuri disponibile")
        print("0. Inchidere functionalitate")
    
    def update(self, job_id):
        """
        Functie care citeste id-ul unui job si permite modificarea datelor acestuia
        """
        list_of_jobs = self.get_all()
        entity : Job
        found = False
            #id_requested = input("Introduceti ID-ul jobului la care doriti sa faceti modificari")
        for i in range(len(list_of_jobs)):
            entity = list_of_jobs[i]
            if job_id == entity.get_id():
                found = True
                while True:
                    command = input("Introduceti comanda dorita pentru a modifica datele sau 0 pentru a inchide functionalitatea: ")
                    if int(command) == 1:
                        new_title = input("Introduceti noul titlu al jobului: ")
                        entity._title = new_title
                    elif int(command) == 2:
                        new_department = input("Introduceti noul departament caruia ii apartine jobul: ")
                        entity._department = new_department
                    elif int(command) == 3:
                        new_salary = input("Introduceti noul salariu: ")
                        while True:
                            if int(new_salary) is not ValueError and int(new_salary) > 0:
                                entity._salary = int(new_salary)
                                break
                            else:
                                print("Salariul trebuie sa fie o valoare numerica mai mare ca 0! (ex. 123)")
                                new_salary = input("Introduceti noul salariu: ")
                    elif int(command) == 4:
                        new_years_requirement = input("Introduceti noua valoare a anilor de experienta ceruti")
                        while True:
                            if int(new_years_requirement) is not ValueError and int(new_years_requirement) >= 0:
                                entity._years_of_experience_req = int(new_years_requirement)
                                break
                            else:
                                print("Anii de experienta trebuie sa fie o valoare numerica de cel putin 0!")
                                new_years_requirement = input("Introduceti noua valoare a anilor de experienta ceruti")
                    elif int(command) == 5:
                        new_positions_available = input("Introduceti noul numar de pozitii disponibile: ")
                        while True:
                            if int(new_positions_available) is not ValueError and int(new_positions_available) >= 0:
                                entity._number_of_positions_available = int(new_positions_available)
                                break
                            else:
                                print("Numarul de pozitii disponibile trebuie sa fie o valoare numerica cel putin 0!")
                                new_positions_available = input("Introduceti noul numar de pozitii disponibile: ")
                    elif int(command) == 0:
                        break
                    else:
                        print("Comanda nerecunoscuta! Incercati din nou.")
        if found == False:
            print("ID-ul introdus nu este asociat niciunui job din lista actuala de joburi!")
    
    def sort_by_department(self, job_department):
        """
        Functie care afiseaza toate joburile ce apartin unui departament dat ca parametru
        :param job_department: (str) departamentul caruia ii apartin joburile afisate
        """
        list_of_jobs = self.get_all()
        entity : Job
        found = False
        for job in range(len(list_of_jobs)):
            entity = list_of_jobs[job]
            if job_department == entity.get_department():
                found = True
                print(entity)
        if found == False:
            print("Nu exista vreun job in lista actuala care sa aiba asociat departamentul introdus!")
    
    
    def sort_by_salary(self):
        """
        Functie care sorteaza descrescator lista de salarii
        :return salary_list: (list) lista de salarii sortate
        """
        salary_list = []
        entity : Job
        list_of_jobs = self.get_all()
        for i in range(len(list_of_jobs)):
            entity = list_of_jobs[i]
            if entity.get_salary() not in salary_list:
                salary_list.append(entity.get_salary())
        
        salary_list.sort(reverse=True)
        return salary_list
    
    def sort_by_years_required(self):
        """
        Functie care sorteaza crescator anii de experienta ceruti
        :return years_list: (list) lista cu ani sortati
        """
        years_list = []
        entity : Job
        list_of_jobs = self.get_all()
        for i in range(len(list_of_jobs)):
            entity = list_of_jobs[i]
            if entity.get_years_of_experience_req() not in years_list:
                years_list.append(entity.get_years_of_experience_req())
        
        years_list.sort()
        return years_list
    
   
        

        
   


            
            
                
                







    
        
    
                

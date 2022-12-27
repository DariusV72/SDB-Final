class Job:
    """
    Clasa ce retine entitatea de baza in aplicatie, job
    """
    def __init__(self, id, title, department, salary, years_of_experience_req, number_of_positions_available, list_of_applicants: list):
        """
        Constructor pentru clasa Job
        :param id: (str) id-ul jobului - nu mai mult de 10 caractere
        :param title: (str) titlul jobului
        :param department: (str) numele departamentului in cadrul caruia se regaseste jobul
        :param salary: (int) salariul
        :param years_of_experience_req: (int) anii de experienta necesari
        :param number_of_positions_available: (int) numarul de locuri disponibile pt aplicanti
        :param list_of_applicant: (list) lista de aplicanti ai unui job
        """
        self._id = id
        self._title = title
        self._department = department
        self._salary = salary
        self._years_of_experience_req = years_of_experience_req
        self._number_of_positions_available = number_of_positions_available
        self._list_of_applicants = list_of_applicants
    
    def get_id(self):
        """
        Getter pentru ID
        :return: (str) id-ul jobului
        """
        return self._id
    
    def set_id(self, new_id):
        """
        Setter pentru id
        :param new_id: (str) noul id al jobului
        """
        self._id = new_id
    
    def get_title(self):
        """
        Getter pentru titlu
        :return: (str) titlul jobului
        """
        return self._title
    
    def set_title(self, new_title):
        """
        Setter pentru titlu
        :param new_title: (str) noul titlu al jobului
        """
        self._title = new_title
    
    def get_department(self):
        """
        Getter pentru departamentul jobului
        :return: (str) numele departamentului la care este inregistrat jobul
        """
        return self._department

    def set_department(self, new_department):
        """
        Setter oentru departament
        :param new_department: (str) noul departament
        """
        self._department = new_department
    
    #Observatie: Setterul exista pentru rarele cazuri in care este necesara schimbarea departamentului unui job

    def get_salary(self):
        """
        Getter pentru salariu
        :return: (int) salariul oferit
        """
        return self._salary

    def set_salary(self, new_salary):
        """
        Setter pentru salariu
        :param new_salary: (int) noul salariu
        """
        self._salary = new_salary

    def get_years_of_experience_req(self):
        """
        Getter pentru anii de experienta necesari
        :return: (int) anii de experienta necesari
        """
        return self._years_of_experience_req
    
    def set_years_of_experience_req(self, new_years_requirement):
        """
        Setter pentru anii de experienta necesari
        :param new_years_requirement: (int) noua valoare a anilor de experienta necesari
        """
        self._years_of_experience_req = new_years_requirement

    def get_number_of_positions_available(self):
        """
        Getter pentru numarul de pozitii disponibile
        :return: (int) numarul de pozitii disponibile
        """
        return self._number_of_positions_available

    def set_number_of_positions_available(self, new_number_of_positions):
        """
        Setter pentru numarul de pozitii disponibile
        :param new_number_of_positions: (int) noul numar de pozitii disponibile
        """
        self._number_of_positions_available = new_number_of_positions
    
    def get_list_of_applicants(self):
        """
        Getter pentru lista de aplicanti ai unui job
        :return: (list) lista de aplicanti
        """
        return self._list_of_applicants
    
    def set_list_of_applicants(self, new_list_of_applicants):
        """
        Setter pentru lista de aplicanti
        :param new_list_of_applicants: (list) noua lista de aplicanti
        """
        self._list_of_applicants = new_list_of_applicants

    
    def __eq__(self, job):
        """
        Verifica egalitatea id-urilor a 2 obiecte de tip Job
        :param job: (Job) jobul cu care se compara cel curent, self
        :return: (bool) True daca id-urile coincid, altfel false
        """
        return self.get_id() == job.get_id()
    
    def __str__(self):
        """
        Suprascrierea functiei str() pentru a converti un job la un string, sau pentru a-l afisa/printa
        :return: (str) un string ce contine valorile atributelor unui job
        """
        return self._id + " " + self._title + " " + self._department + " " + str(self._salary) + " " + str(self._years_of_experience_req) + " " + str(self._number_of_positions_available) + " " + str(self._list_of_applicants)
        
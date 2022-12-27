from Domain.job import Job
from Repository.repository import Repository

class Job_services:
    """
    Clasa ce ofera functionalitati pentru aplicatie, in ceea ce priveste operatiile cu joburi
    """
    def __init__(self, job_list: Repository):
        """
        Constructor pt obiecte de tip Job_services
        :param job_list: (Repository) repository-ul de joburi
        """
        self._job_list = []
        self._job_list = job_list
        self._job_list.add(Job("1d10","Operator de retea" ,"Securitate", 2500, 3, 14, ["Varu Sandel"] ))
        self._job_list.add(Job("2453rt", "Receptioner", "Relatii cu clientii", 3100, 1, 6, []))
        self._job_list.add(Job("10br24", "Administrator de sistem linux","abc", 4500, 7, 3, []))
        self._job_list.add(Job("12qaz32", "Tester", "Debugging", 3000, 6, 7, []))
    
    
    def add_job(self, id, title, department, salary, years_of_experience_req, number_of_positions_available, list_of_applicants):
        """
        Functie care creaza si adauga un job in repository-ul de joburi
        :param id: (str) id-ul jobului - nu mai mult de 10 caractere
        :param title: (str) titlul jobului
        :param department: (str) numele departamentului in cadrul caruia se regaseste jobul
        :param salary: (int) salariul
        :param years_of_experience_req: (int) anii de experienta necesari
        :param number_of_positions_available: (int) numarul de locuri disponibile pt aplicanti
        """
        self._job_list.add(Job(id, title, department, salary, years_of_experience_req, number_of_positions_available, list_of_applicants))
    
    def delete_job(self, id):
        """
        Functie ce sterge un job identificat dupa id
        :param id: (str) id-ul jobului ce se doreste a fi sters
        """
        self._job_list.delete(Job(id, "", "", 0, 0, 0, []))
    
    def get_all_jobs(self):
        """
        Functie ce returneaza toata lista de joburi
        :return: (list) lista de joburi
        """
        return self._job_list.get_all()
    
    def salary_sorted_reversed(self):
        """
        Functie  care afiseaza joburile ordonate descrescator dupa salariu
        """
        sorted_salary = self._job_list.sort_by_salary()
        list_of_jobs = self.get_all_jobs()
        entity : Job
        for j in range(len(sorted_salary)):
            for i in range(len(list_of_jobs)):
                entity = list_of_jobs[i]
                if entity.get_salary() == sorted_salary[j]:
                    print(entity)
    
    def view_all_jobs_with_applicants(self):
        """
        Functie care afiseaza joburile cu aplicanti, ordonate in ordine descrescatoare dupa salariu
        """
        sorted_salary = self._job_list.sort_by_salary()
        list_of_jobs = self.get_all_jobs()
        entity : Job
        for j in range(len(sorted_salary)):
            for i in range(len(list_of_jobs)):
                entity = list_of_jobs[i]
                if len(entity.get_list_of_applicants()) is not 0 and entity.get_salary() == sorted_salary[j]:
                    print(entity)
    
    def sorted_by_years(self, years_max : int):
        """
        Functie care afiseaza joburile ordonate crescator dupa anii de experienta ceruti
        """
        sorted_years = self._job_list.sort_by_years_required()
        list_of_jobs = self.get_all_jobs()
        entity : Job
        for j in sorted_years:
            for i in list_of_jobs:
                entity = i
                if entity.get_years_of_experience_req() == j and entity.get_years_of_experience_req() <= years_max:
                    print(entity)
    
    def view_all_applicants_of_1_job(self, job_id):
        """
        Functie care afiseaza toti aplicantii unui job
        """
        entity : Job
        list_of_jobs = self.get_all_jobs()
        for j in range(len(list_of_jobs)):
            entity = list_of_jobs[j]
            if entity.get_id() == job_id:
                print(entity.get_list_of_applicants())
                break
    

    
    


from Domain.job import Job
from Services.applicant_statistics import Statistics
from Services.Job_services import Job_services
from Services.Applicant_services import Applicant_Services


class UI:
    """
    Clasa ce se ocupa de interfata aplicatiei
    Gestioneaza operatiile de citire si afisare
    """
    def __init__(self, management_service: Job_services, applicant_service: Applicant_Services, statistics_service: Statistics):
        self._management_service = management_service
        self._applicant_service = applicant_service
        self._statistics_service = statistics_service
    
    def __print_all_jobs(self):
        """
        Functie care afiseaza toate joburile
        """
        print("Lista de joburi: ")
        for job in self._management_service.get_all_jobs():
            print(job)
        
    
    
    def __validate_command(self, command):
        """
        Functie care verifica daca comanda introdusa se poate converti la int
        Ridica o eroare daca parametrul introdus nu se poate converti
        :param: (int) comanda
        """
        try:
            int_command = int(command)
        except:
            raise ValueError("Comanda introdusa nu este valida")
    
    

    def __validate_salary(self, salary):
        """
        Functie ce verifica daca salariul introdus se poate converti la int
        Ridica o eroare daca parametrul introdus nu se poate converti
        :param salary: (int) salar
        """
        try:
            int_salary = int(salary)
        except:
            raise ValueError("Salariul introdus nu este o valoare numerica!")

    def __validate_years_of_experience(self, years):
        """
        Functie ce verifica daca anii introdusi se pot converti la int
        Ridica o eroare daca parametrul introdus nu se poate converti
        :param years: (int) anii ceruti
        """
        try:
            int_years = int(years)
        except:
            raise ValueError("Valoarea introdusa nu este o valoare numerica!")

    def __validate_positions_available(self, positions_available):
        """
        Functie ce verifica daca salariul introdus se poate converti la int
        Ridica o eroare daca parametrul introdus nu se poate converti
        :param salary: (int) salar
        """
        try:
            int_numbers_of_positions = int(positions_available)
        except:
            raise ValueError("Numarul de pozitii introduse nu este o valoare numerica!")
    
    def __salary_sorted(self):
        """
        Functie care apeleaza sortarea descrescatoare a salariilor
        """
        self._management_service.salary_sorted_reversed()

    def __add_job(self):
        """
        Functie care citeste toate datele unui job si le trimite la Job_services pentru a adauga jobul in aplicatie
        """
        id = input("ID-ul jobului (nu mai mult de 10 caractere) este: ")
        while True:
            if len(id) <= 10 and len(id) > 0:
                break
            else:
                print("Numarul de caratere din id depaseste limita de 10")
            id = input("ID-ul jobului (nu mai mult de 10 caractere) este: ")

        title = input("Titlul jobului este: ")

        department = input("Departamentul este: ")

        while True:
            salary = input("Salariul oferit este: ")
            self.__validate_salary(salary)
            if int(salary) < 0:
                print("Valuarea introdusa nu poate fi mai mica decat 0")
            else:
                break

        while True:
            years_of_experience_req = input("Introduceti valoarea dorita: ")
            self.__validate_years_of_experience(years_of_experience_req)
            if int(years_of_experience_req) < 0:
                print("Valoarea anilor de experienta trebuie sa fie cel putin 0, nu mai mica decat 0")
            else:
                break
        

        while True:
            number_of_positions_available = input("Introduceti numarul de pozitii disponibile: ")
            self.__validate_positions_available(number_of_positions_available)
            if int(number_of_positions_available) < 0:
                print("Numarul de pozitii disponibile trebuie sa fie cel putin egal cu 0!")
            else:
                break
        
        list_of_applicants = []
        
        self._management_service.add_job(id, title, department, int(salary), int(years_of_experience_req), int(number_of_positions_available), list_of_applicants)
        print("\nJob adaugat cu succes!")

    def __apply_job(self):
        """
        Functie care permite aplicarea la un job
        """
        id_request = input("Introduceti ID-ul jobului la care doriti sa aplicati: ")
        list_of_all_jobs = self._management_service.get_all_jobs()
        list_of_all_applicants = self._applicant_service.get_all_applicants()
        self._statistics_service.apply_to_job(id_request, list_of_all_jobs, list_of_all_applicants)
    
    def __job_removal(self):
        """
        Functie care citeste id-ul unui job si il scoate din lista
        """
        id = input("ID-ul jobului ce se doreste a fi sters: ")
        self._management_service.delete_job(id)
        print("\nJob sters cu succes!")
    
    def __print_commands_job_modifications(self):
        """
        Functie care afiseaza lista de comenzi pentru modificarea datelor unui job
        """
        print("1. Modificare titlu")
        print("2. Modificare departament")
        print("3. Modificare salar")
        print("4. Modificare ani de experienta ceruti")
        print("5. Modificare numar de locuri disponibile")
        print("0. Inchidere functionalitate")
    
    def __print_main_menu(self):
        """
        Functie care afiseaza comenzile meniul principal
        """
        print("1. Modul angajator")
        print("2. Modul aplicant")
        print("0. Inchidere aplicatie")

    def __print_management_mode_functionalities(self):
        """
        Functie care afiseaza comenzile meniului modului de manager
        """
        print("1. Vizualizarea listei de joburi")
        print("2. Adaugarea unui job in lista de joburi")
        print("3. Eliminarea unui job din lista de joburi")
        print("4. Modificarea datelor unui job din lista de joburi")
        print("5. Vizualizarea tuturor joburilor dintr-un departament introdus")
        print("6. vizualizarea tuturor aplicantilor de la un job")
        print("7. Vizualizarea joburilor care au aplicanti, sortate descrescator dupa valoarea salariului")
        print("0. Intoarcere la meniul principal")

    def __print_applicant_mode_functionalities(self):
        """
        Functie care afiseaza comenzile modului de aplicant
        """
        print("1. Vizualizarea listei de joburi")
        print("2. Vizualizarea tuturor joburilor, sortate descrescator dupa valoarea salariilor")
        print("3. Vizualizarea tuturor joburilor care au experienta ceruta sub un anumit numar de ani")
        print("4. Aplicarea la un job")
        print("0. Intoarcere la meniul principal")
    
    def __update_job(self):
        """
        Functie care trimite id-ul jobului care se doreste a fi updatat
        """
        while True:
            job_id = input("Introduceti ID-ul jobului pe care doriti sa il modificati sau b/B epntru a opri functionalitatea: ")
            if job_id == 'b' or job_id == 'B':
                break
            else:
                self.__print_commands_job_modifications()
                self._management_service._job_list.update(job_id)
    
    def __view_by_department(self):
        """
        Functie care trimite departamentul in cadrul caruia vor sa se vada joburile
        """
        while True:
            department_request = input("Introduceti departamentul caruia vreti sa-i vedeti joburile asociate sau b/B pentru a opri functionalitatea: ")
            if department_request == 'b' or department_request == 'B':
                break
            else:
                self._management_service._job_list.sort_by_department(department_request)
    
    def __view_jobs_with_applicants(self):
        """
        Functie care prezinta joburile cu aplicanti, ordonate descrescator dupa salariu
        """
        self._management_service.view_all_jobs_with_applicants()
    
    def __view_applicants_of_1_job(self):
        """
        Funtie care apeleaza afisarea aplicantilor unui job
        """
        while True:
            job_id = input("Introduceti ID-ul jobului ai cariu aplicanti doriti sa ii vedeti sau b/B pentru a opri functionalitatea: ")
            if self.__validate_id(job_id) == True:
                self._management_service.view_all_applicants_of_1_job(job_id)
                break
            elif job_id == 'b' or job_id == 'B':
                break
            else:
                print("ID-ul introdus nu se afla in actuala lista de joburi")
            

    
    def __view_by_years_of_experience(self):
        """
        Functie care trimite maximul de ani de experienta
        """
        while True:
            years_introduced = input("Introduceti anii de experienta pe care ii aveti pentru a putea filtra lista(valoare numerica cel putin egala cu 0) sau b/B pentru a opri funtionalitatea: ")
            if years_introduced == 'b' or years_introduced == 'B':
                break
            else:
                self.__validate_years_of_experience(years_introduced)
                if int(years_introduced) >= 0:
                    self._management_service.sorted_by_years(int(years_introduced))
                else:
                    print("Valoarea introdusa trebuie sa fie pozitiva! ")
    
    def __validate_id(self, id_in_question):
        """
        Functie care verifica daca ID-ul introdus este asociat vreunui job din lista
        """
        entity:Job
        list_of_jobs = self._management_service.get_all_jobs()
        for i in range(len(list_of_jobs)):
            entity = list_of_jobs[i]
            if entity.get_id() == id_in_question:
                return True
        return False
    
    
    def run(self):
        """
        Functie pentru afisarea si rularea unui meniu cu optiuni
        """
        while True:
            print("\033[H\033[J", end="")
            self.__print_main_menu()
            command_main_menu = input("Introduceti comanda asociata modului pe care doriti sa il accesati sau 0 pentru a opri aplicatia: ")
            self.__validate_command(command_main_menu)
            if int(command_main_menu) == 1:
                print("\033[H\033[J", end="")
                while True:
                    
                    self.__print_management_mode_functionalities()
                    command_management_mode = input("Introduceti comanda asociata optiunii pe care doriti sa o accesati sau 0 pentru a reveni la meniul principal: ")
                    self.__validate_command(command_management_mode)
                    if int(command_management_mode) == 1:
                        print("\033[H\033[J", end="")
                        self.__print_all_jobs()
                    elif int(command_management_mode) == 2:
                        print("\033[H\033[J", end="")
                        self.__add_job()
                    elif int(command_management_mode) == 3:
                        print("\033[H\033[J", end="")
                        self.__job_removal()
                    elif int(command_management_mode) == 4:
                        print("\033[H\033[J", end="")
                        self.__update_job()
                    elif int(command_management_mode) == 5:
                        print("\033[H\033[J", end="")
                        self.__view_by_department()
                    elif int(command_management_mode) == 6:
                        print("\033[H\033[J", end="")
                        self.__view_applicants_of_1_job()
                    elif int(command_management_mode) == 7:
                        print("\033[H\033[J", end="")
                        self.__view_jobs_with_applicants()
                        
                    elif int(command_management_mode) == 0:
                        break
                    else:
                        print("Comanda nerecunoscuta!")
            
            elif int(command_main_menu) == 2:
                print("\033[H\033[J", end="")
                while True:
                    
                    self.__print_applicant_mode_functionalities()
                    command_applicant_mode = input("Introduceti comanda asociata optiunii pe care doriti sa o accesati sau 0 pentru a reveni la meniul principal: ")
                    self.__validate_command(command_applicant_mode)
                    if int(command_applicant_mode) == 1:
                        print("\033[H\033[J", end="")
                        self.__print_all_jobs()
                    elif int(command_applicant_mode) == 2:
                        print("\033[H\033[J", end="")
                        self.__salary_sorted()
                    elif int(command_applicant_mode) == 3:
                        print("\033[H\033[J", end="")
                        self.__view_by_years_of_experience()
                    elif int(command_applicant_mode) ==4:
                        print("\033[H\033[J", end="")
                        self.__apply_job()
                    elif int(command_applicant_mode) == 0:
                        break
                    else:
                        print("Comanda nerecunoscuta!") 
            
            elif int(command_main_menu) == 0:
                break

            else:
                print("Comanda nerecunoscuta!")



                


    


            





    
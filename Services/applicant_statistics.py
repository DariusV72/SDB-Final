from Services.Applicant_services import Applicant_Services
from Services.Job_services import Job_services
from Domain.applicant import Applicant
from Domain.job import Job


class Statistics:
    """
    Functie care se ocupa cu aplicarea la un job a unui aplicant
    """
    def __init__(self, list_of_applicants: Applicant_Services, list_of_jobs: Job_services):
        self._list_of_applicants = list_of_applicants
        self._list_of_jobs = list_of_jobs
    

    def apply_to_job(self, id_job_desired: str, list_of_all_jobs: list, list_of_all_applicants: list):
        """
        Funtie de aplicarea la un job a unui aplicant
        """
        entity_applicant : Applicant
        entity_job : Job
        list_of_jobs = list_of_all_jobs
        list_of_applicants = list_of_all_applicants
        found_applicant = False
        found_job = False
        
        for i in range(len(list_of_jobs)):
            entity_job = list_of_jobs[i]
            if entity_job.get_id() == id_job_desired:
                found_job = True
                if entity_job.get_number_of_positions_available() == 0:
                    print("Nu mai sunt pozitii disponibile pe acest post")
                    break
                else:
                    name = input("Introduceti-va numele: ")
                    for j in range(len(list_of_applicants)):
                        entity_applicant = list_of_applicants[j]
                        if entity_applicant.get_name() == name:
                            print("Numele aplicantului este deja inregistrat, nu va mai fi necesara reintroducerea datelor")
                            found_applicant = True
                            break
                    if found_applicant == True:
                        entity_applicant._list_of_job_ids.add(id_job_desired)
                        entity_job._list_of_applicants.append(entity_applicant.get_name())
                        entity_job._number_of_positions_available = entity_job._number_of_positions_available - 1 
                        break
                    else:
                        cv_link = input("Introduceti linkul catre CV-ul dumneavoastra: ")
                        new_job_id_list = set()
                        new_job_id_list.add(id_job_desired)
                        list_of_applicants.append(Applicant(name, cv_link, new_job_id_list))
                        entity_job._list_of_applicants.append(name)
                        entity_job._number_of_positions_available = entity_job._number_of_positions_available - 1 
        if found_job == False:
            print("ID-ul introdus nu este asociat niciunui job din lista actuala")
                    
        
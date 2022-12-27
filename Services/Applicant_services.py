from Domain.applicant import Applicant
from Repository.repository import Repository

class Applicant_Services:
    def __init__(self, applicant_repository: Repository):
        self._applicant_repository = []
        self._applicant_repository = applicant_repository
        self._applicant_repository.add(Applicant("Varu Sandel", "https://random.CV.link", {"1d10", "10br24"}))
        self._applicant_repository.add(Applicant("Popa Marcel", "https://random.Cv.link.2", {"12qaz32"}))
    
    def get_all_applicants(self):
        """
        Functie care returneaza toata lista de aplicanti
        :return: (list) lista de aplicanti
        """
        return self._applicant_repository.get_all()
    
    
        

        

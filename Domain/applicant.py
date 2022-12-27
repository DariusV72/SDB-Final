class Applicant:
    def __init__(self, name, CV_link, list_of_job_ids: set):
        """
        Constructor pentru clasa Applicant
        :param name: (str) numele aplicantului
        :param CV_link: (str) linkul catre CV-ul aplicantului
        :param list_of_job_ids: (list) lista de id-uri a joburilor la care a aplicat
        """
        self._name = name
        self._CV_link = CV_link
        self._list_of_job_ids = list_of_job_ids
    
    def get_name(self):
        """
        Getter pentru numele aplicantului
        :return: (str) numele aplicantului
        """
        return self._name
    
    def get_CV_link(self):
        """
        Getter pentru linkul CV-ului aplicantului
        :return: (str) linkul CV-ului
        """
        return self._CV_link
    
    def get_list_of_job_ids(self):
        """
        Getter pentru lista de id-uri ale joburilor la care a aplicat aplicantul
        :return: (list) lista de id-uri a joburilor
        """
        return self._list_of_job_ids

    def set_list_of_job_ids(self, new_list_of_job_ids):
        """
        Setter pentru lista de id-uri ale joburilor la care a aplicat aplicantul
        :param new_list_of_jobs: (list) noua lista de id-uri a joburilor
        """
        self._list_of_job_ids = new_list_of_job_ids
        
    def __eq__(self, applicant):
        """
        Verifica egalitatea numelor a 2 aplicanti
        :param applicant: (Applicant) aplicantul cu care se compara cel curent, self
        :return:True daca cele 2 nume sunt identice, altfel false
        """
        return self.get_name() == applicant.get_name()
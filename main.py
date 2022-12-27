from tracemalloc import Statistic
from UI.ui import UI
from Repository.repository import Repository
from Services.Job_services import Job_services
from Services.Applicant_services import Applicant_Services
from Services.applicant_statistics import Statistics

job_repository = Repository()
applicant_repository = Repository()

management_service = Job_services(job_repository)
applicant_service = Applicant_Services(applicant_repository)
applicant_statistics = Statistics(management_service, applicant_service)

console = UI(management_service, applicant_service, applicant_statistics)
console.run()



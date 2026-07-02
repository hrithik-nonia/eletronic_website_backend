import json
import os

APPLICATION_FILE = "app/data/job_portal.json"

def read_applicants() -> list:
    if not os.path.exists(APPLICATION_FILE):
        return []
    with open(APPLICATION_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)
    

def write_application(applications: list):
    with open(APPLICATION_FILE, "w") as f:
        json.dump(applications, f, indent=2)


def add_application(application: dict) -> dict:
    applications = read_applicants()
    applications.append(application)
    write_application(applications)
    return application
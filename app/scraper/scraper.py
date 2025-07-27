from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path
import os

dotenv_path = Path(__file__).parents[1] / ".env"
load_dotenv(dotenv_path=dotenv_path)
APIKEY = os.getenv("APIKEY")
url = os.getenv("JOBSURL")
auth = HTTPBasicAuth(APIKEY,"")

def jobs_run_scraper():
	requests.get()
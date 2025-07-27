from dotenv import load_dotenv
import requests
from pathlib import Path

dotenv_path = Path(__file__).parents[1] / ".env"
load_dotenv(dotenv_path=dotenv_path)

def jobs_run_scraper():
	requests.get()
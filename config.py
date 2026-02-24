import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "35943485")

API_HASH = os.environ.get("API_HASH", "185886afadce6add3777d63e61ed3257")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8515491658:AAEDk3m7A-ww648kWXFQrYlyL8epJQXbCW0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1003663695128") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://mfhussainakbar_db:294753618@cluster0.mwn0tlj.mongodb.net/?appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6178309871').split()]

PORT = os.environ.get("PORT", "8080")


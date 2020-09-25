import os
import dotenv
import dns


dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")
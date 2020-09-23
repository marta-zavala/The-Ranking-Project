from src.app import app
from src.config import PORT
import src.controllers.lab_controller
import src.controllers.student_controller


app.run("0.0.0.0", PORT, debug=True)

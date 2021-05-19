from app import app as application
from db import db
from Weed.resources.create_db import filldb_weed
from Disease.resources.create_db import filldb_disease

db.init_app(application)

if __name__ == "__main__":
    application.run()

@application.before_first_request
def create_tables():
    db.create_all()
    filldb_weed()
    filldb_disease()

from flask import Flask 


from flask_migrate import Migrate


#factory
def create_app(): 
    app = Flask(__name__)

    app.config['TEMPLATES_AUTO_RELOAD'] = True

# database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate (app, models.db)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    #register pet blueprint
    from . import fact
    app.register_blueprint(fact.bp)
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app    



    # return the app
    return app



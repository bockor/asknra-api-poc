from flask import Flask
from app.security import token_required


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'mysecretkey'

    from . import security
    app.register_blueprint(security.bp)

    from . import netz
    app.register_blueprint(netz.bp, url_prefix='/api')

    from . import sitez
    app.register_blueprint(sitez.bp, url_prefix='/api')
    
    @app.route('/')
    def index():
         return("<h3><b>hello ... only html overhere !</b></h3>")

    @app.route('/nra-only')
    @token_required('admin')
    def onlyadmins():
        return 'Only NRA route'

    @app.route('/users-only')
    @token_required('user')
    def onlyusers():
        return 'Only users route'
    
    
    return app
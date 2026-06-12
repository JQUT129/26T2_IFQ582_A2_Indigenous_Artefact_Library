from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.debug = True
    app.secret_key = 'cf328bcd52ad6563951eac59206f1d29c5c809215d78653fa900932a471143ae'

    # register blueprints
    from . import views
    app.register_blueprint(views.bp)

    # error handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template("error_pages/404.html"), 404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template("error_pages/500.html"), 500

    return app




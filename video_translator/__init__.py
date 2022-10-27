from flask import Flask,render_template,jsonify,request

def create_app(root):
    app = Flask(__name__,root_path = root,template_folder= r'templates',static_folder = r'static')
    
    #register the blueprints
    from .upload import upload
    from .home import home
    app.register_blueprint(home,root_path = root,prefix_url = '/')
    app.register_blueprint(upload,root_path = root,prefix_url = '/')
    return app
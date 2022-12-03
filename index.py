from config import *
from auth.signup import *
from auth.login import *
from auth.verification import *


app.register_blueprint(signup, url_prefix = '/signup')
app.register_blueprint(login, url_prefix = '/login')
app.register_blueprint(verification, url_prefix = '/verification')


@app.route('/')
def home():
    return 'Home View'



if __name__ == '__main__':
    app.run(port=5000,debug=True)
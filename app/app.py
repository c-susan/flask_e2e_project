from flask import Flask, render_template, url_for, redirect, session
import pandas as pd
from sqlalchemy import create_engine, text 
import os
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from oauth.db_functions import update_or_create_user
from flask_session import Session
import sentry_sdk

sentry_sdk.init(
    dsn="https://826f9a57f816daf5c766b02699963c0c@o4504980167524352.ingest.sentry.io/4506373742657536",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Load the environment variables from the .env file
load_dotenv()

# Database connection settings for the MySQL Connection 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
engine = create_engine(
        connection_string,
        connect_args=connect_args)

## Connection settings for the Goolge OAuth
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)

app.secret_key = os.urandom(12)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
oauth = OAuth(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/air')
def air():
    df = pd.read_csv('https://raw.githubusercontent.com/c-susan/flask_e2e_project/main/data/cleaned_air_quality.csv').sample(50)
    data = df.values
    return render_template('air.html', data=data)


@app.route('/sql')
def sql():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data
        query = text('SELECT * FROM geo_area_id')

        result = connection.execute(query)

        # Fetch all rows of data
        db_data = result.fetchall()

    return render_template('sql.html', data2=db_data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-1039191608401-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
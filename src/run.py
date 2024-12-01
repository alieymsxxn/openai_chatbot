from app import create_app

def run_app():
    '''Initialize and run the Flask application.

    This function creates the Flask app instance and starts the server.
    It is configured to run in production mode by default, with options
    to specify the host and port.
    '''
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)  # Set debug to False for production

if __name__ == '__main__':
    run_app()
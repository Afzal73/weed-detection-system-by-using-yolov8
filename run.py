from web.app import app

if __name__ == "__main__":
    # This allows running with python run.py for development
    app.run(host='0.0.0.0', port=5000, debug=True)

# For production, run with:
# gunicorn -w 4 -b 0.0.0.0:5000 run:app 
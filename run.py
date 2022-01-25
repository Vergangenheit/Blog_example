from flask_blog import create_app

try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    print('No ".env" file or python-dotenv not installed... Using default env variables...')

app = create_app()

if __name__ == '__main__':
	app.run(debug=True)

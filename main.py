from website.templates import create_app    # imports the function 'create_app' from the folder 'website' of the app '__init__'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
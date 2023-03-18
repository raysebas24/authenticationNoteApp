from website import create_app    # imports the function 'create_app' from the folder 'website.templates' of the app '__init__'
print("[main]")

app = create_app()
print("[main]: created 'create_app()'")

if __name__ == '__main__':
    print("[main]: main()\n")
    # 'debug=True' will automaticlly reload if code change
    app.run(debug=True)
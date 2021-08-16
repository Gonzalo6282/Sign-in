from website import create_app

# Run application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

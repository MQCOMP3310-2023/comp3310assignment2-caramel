from project import create_app

if __name__ == '__main__':
  app = create_app()
  app.run(host = '0.0.0.0', port = 8000, debug=False )

# Running the app in debugger mode can be vulnerable, 
# therefore debugger mode is turned off.

API_CLIENT_ID = "7qgiaitv90g4vmq8e9rpnlgtim"
API_USERNAME = "ace.stratton@berkeley.edu"
API_PASSWORD = "Meteorite0509!"

# Throw an error if the user has not set the API_USERNAME and API_PASSWORD
if API_USERNAME == "" or API_PASSWORD == "":
    raise Exception("Please set the API_USERNAME and API_PASSWORD in the cfg/access_cfg.py file.")

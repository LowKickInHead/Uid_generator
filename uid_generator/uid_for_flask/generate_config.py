import configparser

config_file = configparser.ConfigParser()

config_file["Api_settings"] = {
    "port": ":3000",
    "host": "http://127.0.0.1",
    "url": "/api/main"

}

with open("settings.ini", 'w', encoding='utf-8') as file:
    config_file.write(file)
print("[INFO] Config file 'settings.ini' was created")

read_file = open('settings.ini')
content = read_file.read()
print(content)

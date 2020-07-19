from configparser import ConfigParser

def read_config_data(section, key):
    config = ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)

def read_login_elements(section, key):
    config = ConfigParser()
    config.read("./ConfigurationFiles/Locators_loginpage.cfg")
    return config.get(section, key)
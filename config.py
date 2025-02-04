import configparser 

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = configparser.ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    # check if section exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db
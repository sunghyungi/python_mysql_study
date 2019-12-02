from configparser import ConfigParser


def read_db_config(filename="Config.ini", section="mysql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        for item in parser.items(section):
            db[item[0]] = item[1]
    else:
        raise Exception('{} not found in the {} file'.format(section, filename))
    return db

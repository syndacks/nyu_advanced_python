class Config(object):
    base_dir = '/home/dacks/Code/nyu_advanced_python/week4/'

    def __init__(self):
        self.store_data('config.csv')
        self.configdict = {}
        # we'll want to open the csv and create a key by enumerating and then storing the values as the three items in the CSV

    def store_data(self, custom_path):
        """sets the path of the file we are going to be retrieving data from"""
        self.dir = Config.base_dir + '/' + custom_path
        with open(self.dir) as csv_data:
            lines = csv_data.readlines()
        keys = lines[0].split(',')
        values = lines[1].split(',')
        self.configdict = dict(zip(keys, values))

    def get(self, keyname, value):
        """returns the value found for this keyname in the dictionary we stored
        in the instance in the constructor. If the key can't be found, it raises
        a KeyError exception"""

    def set(self, keyname, value):
        """adds the key and value to the instance's dictionary, and then writes
        the entire key/value set back to the file"""

    def _write_data(self):
        """does the work of opening the file and writing each key and value in
        the dictionary to the file."""





my_config = Config()

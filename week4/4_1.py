import csv


class Config(object):
    base_dir = '/Users/dacks/sites/nyu_advanced_python/week4/config.csv'

    def __init__(self, base_dir):
        self.configdict = {}
        self.store_data(base_dir)

    def store_data(self, custom_path):
        """sets the path of the file we are going to be retrieving data from"""
        self.dir = custom_path
        with open(self.dir) as csv_data:
            lines = csv_data.read().splitlines()
            csv_data.close()
        keys = lines[0].split(',')
        values = lines[1].split(',')
        self.configdict = dict(zip(keys, values))

    def get(self, keyname):
        """returns the value found for this keyname in the dictionary we stored
        in the instance in the constructor. If the key can't be found, it raises
        a KeyError exception"""
        try:
            value = self.configdict[keyname]
            print "get value: ", value

            return value
        except KeyError:
            print "No value for given tryname: " + keyname
            exit()

    def set(self, keyname, value, overwrite):
        """adds the key and value to the instance's dictionary, and then writes
        the entire key/value set back to the file"""
        if overwrite is True:
            self.configdict[keyname] = value

        elif overwrite is False:
            try:
                if self.configdict[keyname]:
                    print "The key '" + keyname + "' already exists, and overwrite is set to False. Exiting"
                    exit()
            except KeyError:
                self.configdict[keyname] = value

        self._write_data(self.configdict)

    def _write_data(self, dict_to_write):
        """private method for opening the file and writing each key and value in
        the dictionary to the file. Called by self.set"""
        with open(self.dir, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(dict_to_write.keys())
            writer.writerow(dict_to_write.values())


my_config = Config(Config.base_dir)
my_config.set('foo', 'bar', True)

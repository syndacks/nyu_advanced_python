import csv


class Config(object):
    base_dir = '/home/dacks/Code/nyu_advanced_python/week4/'

    def __init__(self):
        self.configdict = {}
        self.store_data('config.csv')

    def store_data(self, custom_path):
        """sets the path of the file we are going to be retrieving data from"""
        self.dir = Config.base_dir + '/' + custom_path
        with open(self.dir) as csv_data:
            lines = csv_data.readlines()
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
            return value
        except KeyError:
            print "No value for given tryname: " + keyname
            exit()


    def set(self, keyname, value):
        """adds the key and value to the instance's dictionary, and then writes
        the entire key/value set back to the file"""
        print self.configdict
        self.configdict[keyname] = value
        print self.configdict

        with open(self.dir, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.configdict.keys())
            writer.writerow(self.configdict.values())


    def _write_data(self):
        """does the work of opening the file and writing each key and value in
        the dictionary to the file."""





my_config = Config()
my_config.set('foo', 'bar')

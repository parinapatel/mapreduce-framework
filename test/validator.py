import string
import os
import unittest


# os.chdir("/home/parin/CLionProjects/AOS/aos4/test")


class Map_reduce():
    def __init__(self):
        self.d = dict()
        self.output = dict()

    def read_config(self, filepath='/home/parin/CLionProjects/AOS/aos4/test/config.ini'):
        var = {}
        with open(filepath, 'r') as fw:
            for line in fw.read().split('\n'):
                var.update({
                    line.split('=', 1)[0]: line.split('=', 1)[1]
                })
        return var

    def find_occrunce(self, fil):
        with open(fil, 'r') as text:
            for line in text:
                # Remove the leading spaces and newline character
                line = line.strip()
                # Remove the punctuation marks from the line
                line = line.translate(line.maketrans("", "", string.punctuation))

                # Split the line into words
                words = line.split(" ")

                # Iterate over each word in line
                for word in words:
                    # Check if the word is already in dictionary
                    if word in self.d:
                        # Increment count of word by 1
                        self.d[word] = self.d[word] + 1
                    else:
                        # Add the word to dictionary with count 1
                        self.d[word] = 1

    def read_output(self, fil):
        with open(fil, 'r') as text:
            for line in text:
                self.output.update({
                    line.split(" ")[0]: int(line.split(" ")[1])
                })


class ValidateMapReduce(unittest.TestCase):

    def test_dict_size_fast(self):
        """
        Dict are equal , fast one
        """
        self.maxDiff = None
        self.mr = Map_reduce()
        self.config = self.mr.read_config()
        for files in self.config['input_files'].split(','):
            self.mr.find_occrunce(files)
        for files in os.listdir(self.config["output_dir"]):
            self.mr.read_output(self.config["output_dir"] + "/" + files)
        self.assertTrue (self.mr.d == self.mr.output )

    def test_validate_output(self):
        """
        Dict are equal , detailed.
        """
        self.maxDiff = None
        self.mr = Map_reduce()
        self.config = self.mr.read_config()
        for files in self.config['input_files'].split(','):
            self.mr.find_occrunce(files)
        for files in os.listdir(self.config["output_dir"]):
            self.mr.read_output(self.config["output_dir"] + "/" + files)
        self.assertDictEqual(self.mr.d, self.mr.output)

    def test_validate_file_count(self):
        """
        output has correct number of files.
        """
        self.mr = Map_reduce()
        self.config = self.mr.read_config()
        self.assertEqual(int(self.config["n_output_files"]), len(os.listdir(self.config["output_dir"])))

    def test_diff_should_be_none(self):
        """
        Keys are same.
        """
        self.mr = Map_reduce()
        self.config = self.mr.read_config()
        for files in self.config['input_files'].split(','):
            self.mr.find_occrunce(files)
        for files in os.listdir(self.config["output_dir"]):
            self.mr.read_output(self.config["output_dir"] + "/" + files)
        # value = {k: self.mr.output[k] for k in set(self.mr.output) - set(self.mr.d)}
        self.assertListEqual(sorted(list(self.mr.output.keys())), sorted(list(self.mr.d.keys())))


if __name__ == '__main__':
    unittest.main(failfast=True)

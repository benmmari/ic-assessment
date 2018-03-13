from nameko.rpc import rpc
import math
import zlib


class AssessmentService(object):
    name = 'assessment_service'

    string_dictionary = {}

    @rpc
    def one(self, number_list):
        squared_number_list = []
        for number in number_list:
            squared_number_list.append(int(math.pow(number, 2)))
        return squared_number_list

    @rpc
    def two(self, string_list):
        for string in string_list:
            self.string_dictionary[string] = zlib.compress(string)
        return self.string_dictionary

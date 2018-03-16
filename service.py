from nameko.rpc import rpc
import math
import zlib


class AssessmentService(object):
    name = 'assessment_service'

    string_dictionary_decoded_key = {}
    string_dictionary_encoded_key = {}

    @rpc
    def one(self, number_list):
        squared_number_list = []
        for number in number_list:
            squared_number_list.append(int(math.pow(number, 2)))
        return squared_number_list

    @rpc
    def two(self, string_list):
        for string in string_list:
            compressed_string = str(zlib.compress(string.encode('utf-8')))
            self.string_dictionary_decoded_key[string] = compressed_string
            self.string_dictionary_encoded_key[compressed_string] = string
        return (self.string_dictionary_decoded_key)

    @rpc
    def three(self, compressed_string):
        if compressed_string in self.string_dictionary_encoded_key:
            return self.string_dictionary_encoded_key[compressed_string]
        else:
            return "The coresponding string has not yet been compressed"

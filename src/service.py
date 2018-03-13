from nameko.rpc import rpc
import math


class AssessmentService(object):
    name = 'assessment_service'

    @rpc
    def one(self, number_list):
        squared_number_list = []
        for number in number_list:
            squared_number_list.append(int(math.pow(number, 2)))
        return squared_number_list

import os
import grpc
import sys
import random
import string
#from sendenums_pb2_grpc import DoStuffStub
#from sendenums_pb2 import StuffRequest
#from RfmxNr_pb2 import Nr
from RfmxNr_pb2 import *
from RfmxPolicy_pb2 import *
from RfmxNrResults_pb2 import *
from RfsgNr_pb2 import *
from OranRUServiceDef_pb2_grpc import *
from OranRUServiceDef_pb2 import *
#from RfmxNrSubBlock_pb2 import *
from importlib import import_module
from google.protobuf.struct_pb2 import NullValue
from waferslim.converters import convert_arg, convert_result, StrConverter
import json
from google.protobuf.json_format import MessageToJson

_STR_CONVERTER = StrConverter()

x = os.listdir()
for f in x:
    last6 = f[-6:]
    if f[-6:] == 'pb2.py':
        f = f[:-3]
        st = f"from {f} import *"
        exec(st)

class ProtobufMessage:

    #method to parse data object and populate gRPC request
    @staticmethod  #creating as static method to mirror Mark's C# code
    def create_instance(request):

        if request == []:
            return

        #cycle through protobuf object attributes
        for att in request.DESCRIPTOR.fields_by_name:
            if att in request.DESCRIPTOR.fields_by_name:
                data_attribute = request.DESCRIPTOR.fields_by_name[att]

                if att == 'Policy':
                    #setattr(request, att, data_attribute.default_value)
                    p_handle = getattr(request, att)
                    p_handle.SetInParent()


                if att == 'Instr':
                    pass

                #enums are type = 14
                if data_attribute.type == 14:
                    setattr(request, att, 500)

                #nested data type = 11
                elif data_attribute.type == 11:

                    # repeated fields need to be populated with at least one value
                    if data_attribute.label == 3:
                        obj_name = 'Nr' + att
                        sub_req = eval(obj_name)()
                        new_req = ProtobufMessage.create_instance(sub_req)
                        prop = getattr(request, att)
                        prop.append(new_req)

                    #if not a built-in type, it is an actual nested message - make recursive call to populate it
                    elif type(data_attribute).__module__ != 'builtins':
                        #else:
                            ProtobufMessage.create_instance(getattr(request, att))

        return request

class Calc:
    def __init__(self):
        self._A = 0
        self._B = 0

    @convert_arg(to_type=int)
    def setA(self, A):
        self._A = A

    @convert_arg(to_type=int)
    def setB(self, B):
        self._B = B

    @convert_result(using=_STR_CONVERTER)
    def multiply(self):
        return self._A * self._B

    def execute(self):
        print('Execute function')

    def reset(self):
        print('Reset function')


class Grpc:

    def __init__(self):
        self.Reply = 'default reply'
        self.req = ProtobufMessage.create_instance(Nr())

    #def setReply(self, reply):
        #pass

    #def viewReply(self):
        #return self.Reply

    #def setArgument(self, argument):
        #pass

    def create_default_nr_request(self):
        NrRequest = ProtobufMessage.create_instance(Nr())
        self.req = NrRequest
        return 'Active Request is: NrRequest'

    def set_double_property_by_name(self, prop, val):
        p = self.retrieve_property(prop)
        p.value = float(val)
        return self.retrieve_property(prop).value

    def set_int_property_by_name(self, prop, val):
        p = self.retrieve_property(prop)
        p.value = int(val)
        return self.retrieve_property(prop).value

    def set_string_property_by_name(self, prop, val):
        p = self.retrieve_property(prop)
        p.value = val
        return self.retrieve_property(prop).value

    def set_bool_property_by_name(self, prop, val):
        p = self.retrieve_property(prop)
        p.value = eval(val)
        return self.retrieve_property(prop).value

    #@convert_result(using=_STR_CONVERTER)
    def set_enum_property_by_name(self, prop, val):
        ins = 'self.req.' + prop + ' = ' + str(val)
        exec(ins)
        #p = self.retrieve_property(prop)
        #p = 0
        #ins = 'self.req.' + prop + ' = ' + val
        #exec(ins)
        return self.retrieve_property(prop)

    #need this method to descend embedded messages
    def retrieve_property(self, prop):
        levels = prop.split('.')
        att = self.req
        for i in range(len(levels)):
            if '[' in levels[i]: #if this is a repeated field
                levels[i] = levels[i][:-3]
                att = getattr(att, levels[i])
                att = att[0]
            else:
                att = getattr(att, levels[i])
        return att

    def get_double_property_by_name(self, prop):
        att = getattr(self.req, prop)
        return att.value

    def get_enum_property_by_name(self, prop):
        att = getattr(self.req, prop)
        return att

    def get_request_json_string(self):
        out = MessageToJson(self.req)
        return out

    def launch_rfmx_nr(self):
        channel = grpc.insecure_channel('localhost:7132')
        client = OranRuStub(channel)
        response = str(client.ConfigureRfmxNr(self.req))
        return ''.join(response.split())

    def create_default_nr_result_request(self):
        res = ProtobufMessage.create_instance(NrResults())
        self.req = res
        return 'Active Request is: NrResults'






#

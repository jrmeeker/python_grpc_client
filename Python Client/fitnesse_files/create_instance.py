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

x = os.listdir()
for f in x:
    last6 = f[-6:]
    if f[-6:] == 'pb2.py':
        f = f[:-3]
        st = f"from {f} import *"
        exec(st)

#method to parse data object and populate gRPC request
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
                    new_req = create_instance(sub_req)
                    prop = getattr(request, att)
                    prop.append(new_req)

                #if not a built-in type, it is an actual nested message - make recursive call to populate it
                elif type(data_attribute).__module__ != 'builtins':
                    #if 'google' in data_attribute.message_type.full_name:
                        #p_handle = getattr(request, att)
                        #p_handle.SetInParent()
                        #setattr(request, att, NullValue.NULL_VALUE)
                        #data_attribute.message_type = 'google.protobuf.NullValue'
                        #data_attribute = NullValue.NULL_VALUE
                    #else:
                        create_instance(getattr(request, att))




            #else:
                #setattr(request, att, NullValue.NULL_VALUE)
                #request = NullValue.NULL_VALUE



    return request

############### START ##########################################################

#instantiate reqest object
#req = StuffRequest()
req = Nr()

#parse data object and populate the gRPC request
create_instance(req)

req.Policy.Signal.value = 'something'

#open channel and establish client
#channel = grpc.insecure_channel("localhost:50051") -- toy
channel = grpc.insecure_channel("localhost:7132")

#client = DoStuffStub(channel) -- toy
client = OranRuStub(channel)

#send request over rpc
#x = client.ProcessEnums(req)
response = client.ConfigureRfmxNr(req)

#print reply from server
print('.\n.\n.\nResponse from server:  ', end='')
print(str(response))
print('\n\n\n')

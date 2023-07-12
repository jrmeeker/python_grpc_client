@echo OFF

FOR %%x IN (*.*) DO python -m grpc_tools.protoc -I. -I./Instr -I./NR -I./SpecAn --python_out=. --grpc_python_out=. %%x
PAUSE
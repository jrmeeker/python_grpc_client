

from waferslim.converters import convert_arg, convert_result, StrConverter

_STR_CONVERTER = StrConverter()

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


class GrpcRfmxNrFixture:

    ActiveRequest = '' #placeholder for ActiveRequest

    def __init__(self):
        self.Reply = ''
        self.Inst = InstrRequest()
        self.Nr = NrRequest()
        self.NrResults = NrResults()
        self.Wlan = WLanRequest()
        self.RfsgNr = RfsgRequest()
        self.Playback = PlaybackRequest()
        self.Clients = [X410InstrClient(), X410InstrClient(), X410InstrClient(), X410InstrClient()]
        self.OranClients = [OranClient(), OranClient(), OranClient(), OranClient()]
        self.WlanResults = WlanResults()
        self.ActiveRequest = ActiveRequest()

    ###skipping a bunch of methods from c# code

    def CreateDefaultNrRequest(self):
        NrRequest = create_instance(Nr())
        ActiveRequest = NrRequest
        return 'Active Request is: NrRequest'

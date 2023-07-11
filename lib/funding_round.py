class FundingRound:

    all = []

    def __init__(self, startup, vc, round_type, investment):
        self.startup = startup
        self._venture_capitalist = vc
        self.type = round_type
        self.investment = investment
        FundingRound.all.append(self)

    @property
    def startup (self):
        return self._startup
    
    @startup.setter
    def startup (self, value):
        from .startup import Startup
        if hasattr(self, '_startup'):
            raise Exception
        else :
            if isinstance(value, Startup):
                self._startup = value
            else:
                raise Exception

    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    def set_investment(self, number):
        if type(number) == float and number >= 0.0:
            self._investment = number
        else:
            raise Exception

    def get_investment(self):
        return self._investment 
    
    investment = property(get_investment, set_investment)
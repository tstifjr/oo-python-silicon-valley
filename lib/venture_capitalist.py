from .funding_round import FundingRound

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(self):
        return [element for element in VentureCapitalist.all if element.total_worth > 1000000000]

    def offer_contract(self, startup, inv_type, amount):
        FundingRound(startup, self, inv_type, amount)

    @property
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if self == fr.venture_capitalist]
    
    def portfolio (self):
        return list ({fr.startup for fr in self.funding_rounds})
    
    def biggest_investment(self):
        return max(self.funding_rounds, key = lambda fr : fr.investment)
    
    def invested(self, domain):
        
        total = sum ( [fr.investment for fr in self.funding_rounds if fr.startup.domain == domain])
        if total == 0 :
            return "Not invested in domain"
        else :
            return total
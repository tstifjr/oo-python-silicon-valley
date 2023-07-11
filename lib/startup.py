from .funding_round import FundingRound

class Startup:
   all = []
   def __init__(self, name, founder, domain):
      self.name = name
      self.founder = founder 
      self._domain = domain
      Startup.all.append(self)
    
   def get_founder(self):
      return self._founder
   
   def set_founder(self, founder):
      if hasattr(self, '_founder'):
         raise Exception("founder is set")
      else :
         self._founder = founder

   founder = property(get_founder, set_founder)

   @property
   def domain(self):
      return self._domain
   
   def pivot(self, domain, name):
      self.name = name
      self._domain = domain

   @classmethod
   def find_by_founder(self, founder):
      return next((startups for startups in Startup.all if founder == startups.founder), "No founder with that name")

   @classmethod
   def domains(self):
      return [startups.domain for startups in Startup.all]
   
   def sign_contract(self, vc_object, inv_type, amount):
      FundingRound(self, vc_object, inv_type, amount)

   @property
   def funding_rounds_list(self):
      return [fr for fr in FundingRound.all if fr.startup == self]
   
   @property
   def num_funding_rounds(self):
      return len(self.funding_rounds_list)
   
   @property 
   def total_funds(self):
      return sum([fr.investment for fr in self.funding_rounds_list])
   
   @property 
   def investors(self):
      return list ( {fr.venture_capitalist for fr in self.funding_rounds_list} )
   
   @property 
   def big_investors(self):
      from .venture_capitalist import VentureCapitalist
      return [investor for investor in self.investors if investor in VentureCapitalist.tres_commas_club()]
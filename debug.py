from lib import *

# code here
# e.g.
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
s2 = Startup( 'Hooli', 'Gavin Belson', 'www.hooli.com' )
s3 = Startup("PiperChat", "Richard Hendricks", "www.piperchat.com")
vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
vc2 = VentureCapitalist("Russ Hannamen", 2900000000)
fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.01 )
fr2 = FundingRound( s1, vc2, 'Pre-Seed', 300000.01 )
fr3 = FundingRound( s1, vc2, 'Pre-Seed', 100000.01 )
fr4 = FundingRound( s1, vc1, 'Pre-Seed', 700000.01 )






# do not remove
import ipdb; ipdb.set_trace()

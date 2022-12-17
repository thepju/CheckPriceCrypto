import cryptocompare
from songline import Sendline
#token = 'ROzrmuBthClg6T69txx73WxWZRsqL7OU2RiQoojCfmF'
token = 'xHn41EW5iQNSG0yNFhaxlZUKsdqIpSb1uQVvhq3aQF1'
messenger = Sendline(token)

ac = ['DOGE','BNB','BTC'] #ac = allcryptocurrency

unit = ['THB']
getP = cryptocompare.get_price(ac,unit)

doge = getP['DOGE']['THB']
bnb = getP['BNB']['THB']
emoji = '\U0001F972'

djib = doge*( 203.11/1.5188 + 60.39/1.5189 + 697.66/1.5189 + 238.84/1.5189 + 993.88/2.242 ) 
dname = doge*(  500/1.8096 + 302.49/2.13 )
dnut = doge*( 2000/2.24 )
dogeJib = format(djib,'.1f')
dogeName = format(dname,'.1f')
dogeNut = format(dnut,'.1f')

bjib = bnb*(2400/19143 + 1000/18100 )
bnut = bnb*(500/18999.57 + 700/17585.98 )
bname = bnb*(1500/17600 )
bnbJib = format(bjib,'.1f')
bnbNut = format(bnut,'.1f')
bnbName = format(bname,'.1f')


text = f"""
#------------##------------#
#DOGE--------##BNB---------#
#PRICE:{doge:.2f}--##PRICE:{bnb:.0f}#
#JIB (2200)----##JIB (3400)--#
#NOW:{dogeJib}-##NOW:{bnbJib}#
#NAME (800)--##NAME (1500)-#
#NOW:{dogeName}--##NOW:{bnbName}-# 
#NUT (2000)---##NUT (1200)--#
#NOW:{dogeNut}-##NOW:{bnbNut}--#
#------------{emoji}{emoji}------------#
"""
#----------------------------------main----------------------------------
messenger.sendtext(text)

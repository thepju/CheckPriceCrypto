import requests
from pprint import pprint
import time 


from songline import Sendline
token = 'ROzrmuBthClg6T69txx73WxWZRsqL7OU2RiQoojCfmF'
messenger = Sendline(token)


API_HOST = 'https://api.bitkub.com'

mycoin = ['THB_BTC','THB_DOGE']

response = requests.get(API_HOST + '/api/market/ticker')
result = response.json()

n_doge_name = 276.28888766+142.0140845 #418.3
n_doge_jib = 790.04572625+0.0012227+443.30062444#1233.3076884 ถอน2126.2076884
n_doge_nut = 892.85714285 #892.9
#print(n_doge_nut+n_doge_name+n_doge_jib-418.3)
for c in mycoin :
	sym = c 
	data = result[sym]
	last = data['last']
	#print(sym,last)
	
	#if c == 'THB_ETH' :
	#	bene_name = (n_eth_name*last)-300
	if c == 'THB_BTC' :
		txt_btc = 'BTC PRICE NOW: '+ str(last) + '\n'+'---------------------------'+ '\n' 
	if c == 'THB_DOGE' :
		bene_jib = last*n_doge_jib - 1200 - 1000 # ทุนจิ๊บ
		bene_name = last*n_doge_name - 802.49 # ทุนเนม
		bene_nut = last*n_doge_nut - 2000 # ทุนนัด

		txt_doge = 'DOGE PRICE NOW: ' + str(last) + '\n'+'---------------------------'+ '\n' 
		txt_jib = 'JIB TOTAL: '+str(last*n_doge_jib)+ '\n'
		txt_nut = 'NUT TOTAL: '+str(last*n_doge_nut)+ '\n'
		txt_name = 'NAME TOTAL: '+str(last*n_doge_name)+ '\n'
		if bene_name>0 :	txt_name = txt_name + 'NAME BENEFIT:' + str(bene_name)+ '\n' + '---------------------------'+ '\n' 
		else :	txt_name = txt_name + 'NAME LOSS: ' + str(bene_name)+ '\n'+ '---------------------------'+ '\n' 
		if bene_nut>0 :	txt_nut = txt_nut + 'NUT BENEFIT: ' + str(bene_nut)+ '\n'+ '---------------------------'+ '\n' 
		else :	txt_nut = txt_nut + 'NUT LOSS: ' + str(bene_nut)+ '\n'+ '---------------------------'+ '\n' 
		if bene_jib>0 :	txt_jib = txt_jib + 'JIB BENEFIT: ' + str(bene_jib)+ '\n'+ '---------------------------'+ '\n' 
		else :	txt_jib = txt_jib + 'JIB LOSS: ' + str(bene_jib)+ '\n'+ '---------------------------'+ '\n' 

alltxt = txt_btc + txt_doge+txt_name+txt_jib+txt_nut+'***รอราคา DOGE 1$***'+'\n'+'***เดินทางมาแล้ว'+str(int((last/30)*100))+'%***'
#print(alltxt)	


#------------------------------------		
#messenger.sendtext('\n'+txt_eth+'\n'+txt_doge+ '\n' +alltxt+'\n'+'***รอราคา DOGE 1$ ก่อนนะ!!***')


#messenger.sticker(527,2)


"""
def textprice(ac,c):
	text = ''
 	for i in ac :
  		text = text + i + ': '
  		for j in c :
   			text = text + str(getP[i][j]) +''
 	return text """

import cryptocompare
ac = ['BTC','DOGE','BNB'] #ac = allcryptocurrency
c = ['THB']
getP = cryptocompare.get_price(ac,c)
bnb = getP[ac[2]][c[0]]
bnut = (bnb/18999.57)*500 + (bnb/17585.98)*700
bnbnut = format( bnut ,'.2f') 
bnbjib = format((bnb/19143)*2400+(bnb/18100)*1000,'.2f') 
bnbname = format((bnb/17600)*1500,'.2f')
text = 'BNBNut(1200): ' + str(bnbnut) +'\n' + 'BNBJib(3400): ' +str(bnbjib) +'\n' + 'BNBName(1500): ' +str(bnbname)
#print(text)
messenger.sendtext( alltxt + '\n' + text +'\n'+ 'BNB NOW: '+str(bnb) )
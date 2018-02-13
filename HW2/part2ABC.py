


letter_frequency = { 'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 
				'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.996, 'j': 0.153, 
				'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 
				'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't':9.056, 
				'u':2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 
				'z': 0.074 };

frequency = {	'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
				'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
				'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
				'y': 0, 'z': 0 };

plaintext = 'ethicslawanduniversitypoliciestodefendasystemyouneedt'\
			'obeabletothinklikeanattackerandthatincludesunderstand'\
			'ingtechniquesthatcanbeusedtocompromisesecurityhowever'\
			'usingthosetechniquesintherealworldmayviolatethelawort'\
			'heuniversitysrulesanditmaybeunethicalundersomecircums'\
			'tancesevenprobingforweaknessesmayresultinseverepenalt'\
			'iesuptoandincludingexpulsioncivilfinesandjailtimeourp'\
			'olicyineecsisthatyoumustrespecttheprivacyandpropertyr'\
			'ightsofothersatalltimesorelseyouwillfailthecourseacti'\
			'nglawfullyandethicallyisyourresponsibilitycarefullyre'\
			'adthecomputerfraudandabuseactcfaaafederalstatutethatb'\
			'roadlycriminalizescomputerintrusionthisisoneofseveral'\
			'lawsthatgovernhackingunderstandwhatthelawprohibitsyou'\
			'dontwanttoenduplikethisguyifindoubtwecanreferyoutoana'\
			'ttorneypleasereviewitsspoliciesonresponsibleuseoftech'\
			'nologyresourcesandcaenspolicydocumentsforguidelinesco'\
			'ncerningproperuseofinformationtechnologyatumaswellast'\
			'heengineeringhonorcodeasmembersoftheuniversitycommuni'\
			'tyyouarerequiredtoabidebyt'
			
			
alphapet = 'abcdefghijklmnopqrstuvwxyz'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'





#var calculator function
def var_calculator(frq):
  u=0.0
  for i in alphapet:
    u=u+frq[i]
  u=u/26
 
 
    ###find var###
  var = 0.0;
  for i in alphapet:
  	var = var + (frq[i] -u)**2

  var = var/26

  return var



 ### encrypt Message function
def encryptMessage(myKey, myMessage):
   
   translated = []
   s=""
   keyIndex = 0
   myKey=myKey.upper()
   myMessage=myMessage.upper()
   
   
   for letter in myMessage :
     temp_index=LETTERS.index(letter)
     temp_key=LETTERS.index(myKey[keyIndex])
     num=(temp_key+temp_index)%26
     translated.append(LETTERS[num].lower())
     keyIndex+=1
     if keyIndex == len(myKey):
       keyIndex=0
   for i in translated:
     s=s+i
  
   return s   

   
  
  
def PartA():
  print("Part A")
  var=var_calculator(letter_frequency)
  return var
  

def PartB(massage):
  if massage==plaintext:
    print("Part B")
  for l in alphapet:
    c=massage.count(l)
    frequency[l] = c/len(massage)
    frequency[l]= frequency[l]*100
  var=var_calculator(frequency)
  return var
  



def PartC():
  key=["yz","xyz","wxyz","vwxyz","uvwxyz"]
  print("Part C:")
  for i in key :
    encrypted=encryptMessage(i, plaintext)
    print("key:")
    print(i)
    print("var")
    print(PartB(encrypted))
    
    print(encrypted)
   # print(PartB(encrypted))
  return "done"
    
    
    
print(PartA()) 
print(PartB(plaintext))
print(PartC())
  
  



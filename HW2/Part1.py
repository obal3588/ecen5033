 # Obaid Alqahtani 
 


#from sets import Set
from collections import Counter
import re







  
#ciphertext
ciphertext = "DFSAWSXSOJSBMJUVYAUETUWWPDRUTHOOBSWUSWSQMHVSMQRVJFQOCHGFNAOYLGRUWIYLRK"\
			"ISJCHWVOQYZIXYJFXADVKJSMNDPCFRUOYIITOLTHWDPFYRHRVSOFWBMKJGUMRYKDCHDWVL"\
			"DHCYJEEEOHLOCQJBAAUSKPQIWVXYBHIGHVTPAYEKIZOTFFHRTFCZLGZVSGUCLIJBBXHKMT"\
			"IOLPUICBHYOWSMBFCZXWRTDYNWWZOWHQRVDBHCZQWVDILTWCJVQBLVHRUOWZQJZESHELEC"\
			"JHSODXRJBNPJVZUMUFWLVOHCNDXZPBUYGRFOFYAXHZBHCZQQFESLYFVPQHIRUEGIMCYWII"\
			"TSWEVXYFRCDFMGMWHPVSWNONSHQRUWWDFSDQINPUWTJSHNHEEESFPFXIJQUWHRXJBYPUME"\
			"HAIOHVEDFSAWSXSOJSBMJISUGLPPCOMPGSENONSHQRUWWLOXYFCLJDRUDCGAXXVSGWTHRT"\
			"FDLLFXZDSWCBTKPULLSLZDOFRRVZUVGDDVVESMTJRVEOLZXRUDCGAXXRUWIYDPYBFXYHWJ"\
			"BGMFPTKJCHDPEBJBADXGYBZAZUMKIAMSDVUUCVCHEBJBJCDGKJQYMBEEZOXGHVJBFSTWMJ"\
			"UVYZUIKJQUWOCGPGMTEPVUCVCHEBTIWSDWPTHYXEYKJHCDLRWFOMTEPVUCXZVSSZOHJNRF"\
			"XBJCDGKJQUWPIROGWCBTKPZIRBVVMONPGXVDVHZOSXZVUDUEZTSXLQYDCSLZIPVHOFTVWL"\
			"FGNSHICFQNCRRZDTLZQXZFFZZXRUBHCZQARTWHGRPMFRCYDGRTSCYWLVVBCEHHJUONPVAY"\
			"JQBBXIJUWIYHHNISNSHVIFEOTUMEHGODSITUSXNUMDJBUWVXFQFIGLHVUVYTUHVDFSAWMF"\
			"OYYJVXFMOQPQJFSQYXHRKJGOYFSETHCEXXZPBUWWLVFTZLUKLFRNSDXKIWMTVEMJCFLWMF"\
			"OCZEKIIJUBERJEPHVPLRXGCLNHHKPWHNUMDJBUEHSEFGYWIEJHWPPQMEUVYQLJKIOGPQHD";

# I assum it is not would be more than 16 letters
max_lenth=16 


# from part 2 
frequency_letter = { 'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 
				'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06996, 'J': 0.00153, 
				'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 
				'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 
				'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 
				'Z': 0.00074 };



def reset_letter():
	
	reset_letter = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
					'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
					'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
					'Y': 0, 'Z': 0 };
	return reset_letter
			


			
# fsctors calculator function 		
    
def factor_numbers(number):
	back_arr = []
	for i in range(2, number + 1):
	   if ( number % i == 0 ):
	   	back_arr.append(i)
	return back_arr
	

# shift letter by shift_numberi

def shift( letter, shift_number ):
	alphapet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	temp= (alphapet.index(letter)+ ( shift_number % 26) ) % 26 
	return alphapet[ temp]	
	





#I USED THIS THIS reference:http://inventwithpython.com/hacking/chapter21.html 
#accourding to the thery 
#1- N is the lenth of keyword , so the N should be  one of the cipthertext lenth massage 
# 2- the number of the letter between two comman letter is called distance



#GET THE FACTOR 
factorList = factor_numbers( max_lenth );





def RepeatSequencesAndKeylenth(text):
  #Associative array  that HAS ALL KEYS THA ARE sequences
    spaces_sequences = {} 
 
  # we want to go through the ciphertext ,and find 3- letter sequence that repeted N time
  # this for loop will go up to the begist value of lenth factor 
  # it will shift the text compare it to the orginal up to 16 in this case 
    for seq_lenth  in range(3, factorList[-1]) :
      for sequence_start in range( 0, max_lenth - seq_lenth ):
        
         # store 3 letter sequence 
         #reference:http://inventwithpython.com/hacking/chapter21.html 
        
         temp_substring = text[sequence_start : sequence_start + seq_lenth ]
        
         for i in range(sequence_start + seq_lenth, len(text) - seq_lenth):
           if text[i:i + seq_lenth] == temp_substring:
              
              if temp_substring not in spaces_sequences:
              
                spaces_sequences[temp_substring]=[]
              spaces_sequences[temp_substring].append(i - sequence_start)
              
              
              
              #######
      # distances
    factor_list = {}
    test = [];
    for temp_substring, list_of_distances in spaces_sequences.items():
      for distance in list_of_distances:
        for factor in range(2, factorList[-1]):
          if distance % factor == 0:
                if temp_substring not in factor_list:
                    factor_list[temp_substring] = [];

                test.append(factor);
    counter = Counter(test);
    keylenth= counter.most_common(1)[0][0];
    


          
    
    return keylenth



def guss_letter_key(ciphertext,key):
  alphapet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  
  forma_text=re.findall('.......', ciphertext);
  check=''
  key_word=''
  
					
  for guss_lett in range(0, key):

    letterCount =reset_letter();
    for keyword in forma_text:
		    check = check + keyword[guss_lett]
		
		
    shift_num=0
    temp_var=0.0
    var = 2.0
    
    
    for j in range(0, 26):
        for i in alphapet:
        	letterCount[i] = check.count(shift(i,j))/(check.__len__()*1.0)
        for i in alphapet:
          temp_var = temp_var + (letterCount[i] - frequency_letter[i]) ** 2
        temp_var = temp_var / 26
        

        if ( temp_var < var ):
          var=temp_var
          shift_num=j
          
        temp_var=0.0

	
	
    key_word=key_word+alphapet[shift_num]	
    check=''
  return key_word






##########Main##########################  
k=RepeatSequencesAndKeylenth(ciphertext)
print("keylenth :")
print(k)
print(guss_letter_key(ciphertext,k))







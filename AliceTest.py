
from cqc.pythonLib import CQCConnection, qubit
import random
from cqc.cqcHeader import CQC_TP_HELLO


def main():
	# Initialize  the  connection
	with  CQCConnection("Alice") as  Alice:
    		# Generate a key
    		k = random.randint(0, 1)
    		
    		#print(k)
    
    		# Create a qubit
    		q = qubit(Alice)
    	
    
    		#Encode  the  key in the  qubit
    		if k == 1:
        		q.X()
        		
        		print(q.X())
        
    		#Send  qubit  to Bob (via  Eve)
    		Alice.sendQubit(q,"Eve")
    
    		# Encode  and  send a classical  message m to Bob
    		m=1
    		enc=(m+k)%2
    		Alice.sendClassical("Bob",enc)
    		print("Alice  send  the  message m={} to Bob".format(m))
    
main()    

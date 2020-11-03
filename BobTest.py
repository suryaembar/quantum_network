
from cqc.pythonLib import CQCConnection, qubit

import random
from cqc.cqcHeader import CQC_TP_HELLO

def main():

	# Initialize  the  connection
	with  CQCConnection("Bob") as Bob:
    		# Receive  qubit  from  Alice (via  Eve)
    		q = Bob.recvQubit ()
    		
    		# Retreive  key
    		k = q.measure ()
    		
    		#Receive  classical  encoded  message  from  Alice
    		enc = Bob.recvClassical ()[0]
    		
    		# Calculate  message
    		m = (enc + k) % 2
    		
    		print("Bob  retrived  the  message m={}  from  Alice.".format(m))
########################################################################################### 		
main()

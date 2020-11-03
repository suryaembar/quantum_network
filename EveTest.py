
from cqc.pythonLib import CQCConnection


def main():
	# Initialize  the  connection
	with  CQCConnection("Eve") as Eve:
    		# Receive  qubit  from  Alice
    		q = Eve.recvQubit ()
    		# Forward  the  qubit  to Bob
    		Eve.sendQubit(q, "Bob")
    		
main()

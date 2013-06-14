import sys
import codecs

result = "Your unicode string here"
# Replacement for print string
sys.stdout.write((result + "\n").encode('utf8'))        
sys.stdout.flush()
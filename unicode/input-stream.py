import sys
import codecs

reader = codecs.getreader("utf-8")(sys.stdin)
line = reader.readline().strip()
while line:
    # Your code here
    
    # Don't forget this final line, otherwise your code will stuck forever
    line = reader.readline().strip()
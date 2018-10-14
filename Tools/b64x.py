#!/usr/bin/env python
import base64

print "Base64 multi decoder."
print "Please enter the string you want to decode:"
inp_string = raw_input()
print "How many times does it need to be decoded?"
times = raw_input ()
times = int(times)
for i in range(times):
    inp_string = base64.b64decode(inp_string)

out_string = inp_string.decode('UTF-8')
print(out_string)
import urllib

import re
name="https://www.linkedin.com/"
ab="mynetwork"
bc="/invite-connect/connections/"
final=name+urllib.urlencode(bc)
print(final)

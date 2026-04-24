from time import time
from datetime import datetime

seconds = time()
current_date = datetime.now()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))

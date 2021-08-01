import csv
from io import StringIO

import dotenv
import os
#
# dir(dotenv.load_dotenv())
#
# print(os.getenv('LOGGING_LEVEL'))


s = StringIO.StringIO('1, "text1,text2", "text3, text4", a, b, c')
print(list(csv.reader(s, skipinitialspace=True)))
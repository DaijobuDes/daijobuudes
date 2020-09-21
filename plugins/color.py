from datetime import datetime

consoletime = datetime.now()
debuginfo = f'{consoletime}\u001b[36;1m [DEBUG/INFO] \u001b[0m'
infolow = f'{consoletime}\u001b[37;1m [INFO/LOW] \u001b[0m'
warnlow = f'{consoletime}\u001b[33;1m [WARN/LOW] \u001b[0m'
warnhigh = f'{consoletime}\u001b[33;1m [WARN/HIGH] \u001b[0m'
errorsevere = f'{consoletime}\u001b[31;1m [ERROR/SEVERE] \u001b[0m'


# class Color():

#     def __init__(self):
#         super().__init__()

#     def debuginfo(self):
#         return f'{consoletime}\u001b[36;1m [DEBUG/INFO] \u001b[0m'

#     def infolow(self):
#         return f'{consoletime}\u001b[37;1m [INFO/LOW] \u001b[0m'

#     def warnlow(self):
#         return f'{consoletime}\u001b[33;1m [WARN/LOW] \u001b[0m'

#     def warnhigh(self):
#         return f'{consoletime}\u001b[33;1m [WARN/HIGH] \u001b[0m'

#     def errorsevere(self):
#         return f'{consoletime}\u001b[31;1m [ERROR/SEVERE] \u001b[0m'

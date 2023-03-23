

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex,log)
print(result[1]) 


#grep thon /usr/share/dict/words
#grep -i python /usr/share/dict/words
#grep l.rts /usr/share/dict/words
#grep ^fruit /usr/share/dict/words
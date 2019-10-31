import os
import errno
import socket

filelist = os.listdir("/home/data")
filelist_str = ""

for file in filelist:
    if ".txt" not in file:
        filelist.remove(file)

for file in filelist:
        filelist_str = file + ", " + filelist_str

filelist_str = filelist_str[:-2]
filelist_str = ".TXT FILES AT /HOME/DATA\n" + filelist_str + "\n"

print(filelist_str)

######

file_dict = {}
total_words = 0

for file in filelist:
    num_words = 0
    with open(("/home/data/" + file), 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
            total_words += len(words)
    file_dict[file] = num_words


numwords_str = "WORDCOUNT\n"
for key in file_dict:
    numwords_str = numwords_str + key + ": "
    numwords_str = numwords_str + str(file_dict[key]) + "\n" 
print(numwords_str)

######

totalwords_str = "TOTAL # OF WORDS IN ALL FILES\n" + str(total_words) + "\n"
print(totalwords_str)

######

max_word = 0
max_word_key = ""

for key in file_dict:
    
    if file_dict[key] > max_word:
        max_word = file_dict[key]
        max_word_key = key
    
maxword_str = "MAXIMUM # OF WORDS\n" + max_word_key + ": " + str(max_word) + "\n"

print(maxword_str)

######

try: 
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name) 
except: 
    print("Unable to get Hostname and IP") 

ip_str = "IP ADDRESS\n" + str(host_ip)
print(ip_str)

######

filename = "/home/output/result.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write(filelist_str + "\n" + numwords_str + "\n" + totalwords_str + "\n" + maxword_str + "\n" + ip_str)

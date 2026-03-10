from collections import Counter

logfile = open("access.log", "r")

ip_list = []
page_list = []
error_404 = 0

for line in logfile:
    
    parts = line.split()
    
    ip = parts[0]
    page = parts[6]
    status = parts[8]

    ip_list.append(ip)
    page_list.append(page)

    if status == "404":
        error_404 += 1

print("Total 404 errors:", error_404)

print("Most requested page:", Counter(page_list).most_common(1))

print("Most active IP:", Counter(ip_list).most_common(1))

logins = [
    ("alice", "192.168.1.1"),
    ("bob", "10.0.0.2"),
    ("alice", "192.168.1.2"),
    ("alice", "192.168.1.1"),
    ("bob", "10.0.0.2"),
    ("charlie", "8.8.8.8"),
    ("charlie", "1.1.1.1"),
    ("charlie", "8.8.8.8"),
]

def detect_suspicious(logins):
    
    user_ips = {}
    
    for user, ip in logins:
        
        if user not in user_ips:
            user_ips[user] = []
        user_ips[user].append(ip)
    
    ips_result = []
    
    for user, ips in user_ips.items():
        ip_count = {}
        
        for ip in set(ips):
        
            if ip not in ip_count:
                ip_count[ip] = 1
            else:
                ip_count[ip] += 1
            
            if ips.count(ip) >= 3: 
                ips_result.append(user)
                break
    return ips_result


print(detect_suspicious(logins))

# check again the whole logic and think how it works cuz now I have some problems of understanding it

logins = [
    ("alice", "192.168.1.1"),
    ("bob", "10.0.0.2"),
    ("alice", "192.168.1.2"),
    ("alice", "192.168.1.1"),
    ("bob", "8.8.8.8"),
    ("bob", "192.168.1.1"),
    ("bob", "10.0.0.2"),
    ("charlie", "8.8.8.8"),
    ("charlie", "1.1.1.1"),
    ("charlie", "8.8.8.6"),
    ("charlie", "8.8.8.7"),
    ("charlie", "8.8.8.5"),
    ("alice", "192.168.1.1")
]

def detect_suspicious(logins):
    
    user_ips = {}
    result = {}
    
    for user, ip in logins:
        
        if user not in user_ips:
            user_ips[user] = []
        user_ips[user].append(ip)

    for user, ips in user_ips.items():
        
        ip_count = {}

        #Rule 1 start
        if len(set(ips)) >= 3:
            if user not in result:
                result[user] = []
            result[user].append('Rule 1')
        #Rule 1 end

        #Rule 2 start
        for ip in ips:
    
            if ip not in ip_count:
                ip_count[ip] = 1
            else:
                ip_count[ip] += 1
            
            if ip_count[ip] >= 3: 
                if user not in result:
                    result[user] = []
                result[user].append('Rule 2')
                break
                
        #Rule 2 end
        
        #Rule 3 start
        has_private = False
        has_public = False

        for ip in ips:
            if ip.startswith("192.168.") or ip.startswith("10."):
                has_private = True
            else:
                has_public = True
        
        if has_private and has_public:
            if user not in result:
                result[user] = []
            result[user].append('Rule 3')
        #Rule 3 end
    
    return f"Rules results: {result}"

print(detect_suspicious(logins))

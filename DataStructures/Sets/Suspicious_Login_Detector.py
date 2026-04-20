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
    
    dict_user_ips = {}
    ips_result = set()
    
    for user, ip in logins:
        
        if user not in dict_user_ips:
            dict_user_ips[user] = []
        dict_user_ips[user].append(ip)

    for user, ips in dict_user_ips.items():
        
        ip_count = {}

        #Rule 1 start
        if len(set(ips)) >= 3:
            ips_result.add( (f"Rule 1: {user}") )
        #Rule 1 end

        #Rule 2 start
        for ip in ips:
    
            if ip not in ip_count:
                ip_count[ip] = 1
            else:
                ip_count[ip] += 1
            
            if ip_count[ip] >= 3: 
                ips_result.add((f"Rule 2: {user}"))
                break
        #Rule 2 end
        
        #Rule 3 start
        has_private = False
        has_public = False

        for ip in set(ips):
            if ip.startswith("192.168.") or ip.startswith("10."):
                has_private = True
            else:
                has_public = True
        
        if has_private and has_public:
            ips_result.add((f"Rule 3: {user}"))
        #Rule 3 end
    
    sorted_ips_results = sorted(list(ips_result))
    
    return f"Rules results {sorted_ips_results}"

print(detect_suspicious(logins))

class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        result="IPv4"
        count=0
        for x in IP.split('.'):
            try:
                if int(x) > 255 or int(x)<0:
                    result="Neither"
                elif len(x)>3 or len(x)==0 or (int(x)<10 and len(x)!=1) or (100>int(x)>9  and len(x)!=2):
                    result="Neither"
            except: 
                 result="Neither"
            count+=1
            
        if count!=4: 
            result="Neither"

        IP=IP.split(':') 
        if len(IP)!=8:
            return result
        
        result="IPv6" 
        
        for x in IP:
            try:
                d=int(x, 16)
                if x[0]=="-"  or len(x)>4 or len(x)==0:
                    return "Neither"
            except:
                return "Neither"
            
        return result   
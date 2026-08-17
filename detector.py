import re
from  urllib.parse import urlparse
def check(url):
  score=0
  reasons=[]
  new_url=url if"://" in url else f"http://{url}"
  parsed=urlparse(new_url)

  hostname=(parsed.hostname or "").lower()
  ip=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
  path_query=f"{parsed.path}?{parsed.query}".lower()
  susp=["login","verify","update","secure","account","password","bank","confirm"]
  if len(url)>75:
     score=score+1
     reasons.append("URL is unusually long more than 75 characters")
  if "@" in url:
     score=score+1
     reasons.append("It contains @ symbol")
  if re.fullmatch(ip,hostname):
     score=score+1
     reasons.append("It contains ip address not host name!")   
  for x in susp:
     if x in path_query:
       score=score+1
       reasons.append("It contains suspicious words")
  domain=hostname.split('.')    
  if(len(domain)>3 and not re.fullmatch(ip,hostname)):
      score=score+1
      reasons.append("Excessive subdomains found")  
  result="Suspicious " if score>=3 else "Likely Safe"
  return result,score ,reasons
  
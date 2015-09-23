from piazza_api import Piazza
p=Piazza()
p.user_login('xiayuc@andrew.cmu.edu','Cxy3020840!')
eece210 = p.network("ieby1xzit8r1ki")
post=eece210.get_post(29)
s=post['history'][0]
print s['content']

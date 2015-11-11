

DOMAIN = r'http://bbs.uestc.edu.cn/'
USERNAME=r'xxxx'
PASSWORD=r'xxxx'
USERUID =r'114640'
LOGINFIELD = r'username'

HOMEURL = DOMAIN
LOGINURL= DOMAIN + r'member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LXlmu&inajax=1'
POSTURL = DOMAIN + r'forum.php?mod=post&action=newthread&fid=FID&extra=&topicsubmit=yes'
REPLYURL= DOMAIN + r'forum.php?mod=post&action=reply&fid=25&tid=TID&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'



WATERURL  = DOMAIN + r'forum.php?mod=viewthread&tid=1559009'
WWURL     = DOMAIN + r'forum.php?mod=viewthread&tid=1570810'
#LASTPAGEURL_BASE = DOMAIN + r'forum.php?mod=viewthread&tid=1559009&extra=&page='
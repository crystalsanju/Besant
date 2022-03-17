# random passwrd  generator
import  random 
UC= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LC = 'abcdefghijklmnopqrstuvwxyz'
SB= '#$%&*@'
NB='0123456789'
ps= UC+LC+SB+NB
ln=10
ps=random.sample(ps,ln)
passwd="".join(ps)
print(passwd)

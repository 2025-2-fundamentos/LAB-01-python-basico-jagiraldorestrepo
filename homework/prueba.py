h = 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2'
l = 'jjj:12,bbb:3,hhh:2'

h = h.split(',')



h = [x.split(':')[0] for x in h]
l = [x.split(':')[0] for x in h]

x = h + l
print(x)
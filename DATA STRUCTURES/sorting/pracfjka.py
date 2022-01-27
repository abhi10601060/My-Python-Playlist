import math

# print(((1700*math.sin(5*math.pi/180)+0)**2+(math.cos(5*math.pi/180)*800+300)**2)**(0.5))

# print(((3600*math.sin(5*math.pi/180)+0)**2+(math.cos(5*math.pi/180)*1100+350)**2)**(0.5))

# for h in range (0,501,5):
#     for a in range (5,31,5):
#         act1=(((1700*math.sin(a*math.pi/180)+h)**2+(math.cos(a*math.pi/180)*800+300)**2)**(0.5))
#         print(act1)


for h in range (0,501,5):
    for a in range (5,31,5):
        act2=(((3600*math.sin(a*math.pi/180)+h)**2+(math.cos(a*math.pi/180)*1100+350)**2)**(0.5))
        print (act2)
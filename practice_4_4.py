import math

Rz = 6371

inp_1 = input('Point 1 / [longitude latitude]: ').split(' ')
p_1 = tuple([float(el)*math.pi/180 for el in inp_1])

inp_2 = input('Point 2 / [longitude latitude]: ').split(' ')
p_2 = tuple([float(el)*math.pi/180 for el in inp_2])

cos_d = math.sin(p_1[1]) * math.sin(p_2[1]) + math.cos(p_1[1]) * math.cos(p_2[1]) \
    * math.cos(p_1[0]-p_2[0])
d = math.acos(cos_d)
L = d * Rz

print('Distance: {} km'.format(L))




box_size = [float(el) for el in input('Box size (WxLxH): ').split('x')]
door_size = [float(el) for el in input('Door size (WxH): ').split('x')]

cnt = len(box_size)
while cnt > 0:
    if (box_size[0] <= door_size[0]) and (box_size[1] <= door_size[1]) or \
       (box_size[0] <= door_size[1]) and (box_size[1] <= door_size[0]):
        print('OK')
        break
    else:
        cnt -= 1
    box_size.insert(0, box_size.pop())
if cnt == 0:
    print('Not OK')

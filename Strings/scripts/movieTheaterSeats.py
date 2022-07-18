input_str = input()
inputs = [int(x) for x in input_str.split(' ')]
N, occupied , liked = inputs[0], inputs[1], inputs[2]
occupied_l = []
for i in range(occupied):
    val = input()
    occupied_l.append(val)
liked_l = []
for i in range(liked):
    val = input()
    liked_l.append(val)

for item in zip(occupied_l, liked_l):
    if item[0]== item[1]:
        print('N')
    else:
        print('Y')

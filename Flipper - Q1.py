import sys
rotations = []
box = [1, 2, 3, 4]
previousbox = [0, 0, 0, 0]
rawinput = sys.stdin.readlines()

for i in rawinput[0]:
    rotations.append(i)
print(rawinput)
print(rotations)
for i in rotations:
    previousbox[0] = box[0]
    previousbox[1] = box[1]
    previousbox[2] = box[2]
    previousbox[3] = box[3]
    if i == 'H':
        box[0] = previousbox[2]
        box[1] = previousbox[3]
        box[2] = previousbox[0]
        box[3] = previousbox[1]
    if i == 'V':
        box[0] = previousbox[1]
        box[1] = previousbox[0]
        box[2] = previousbox[3]
        box[3] = previousbox[2]
        
print(str(box[0])+' '+str(box[1])+"\n"+str(box[2])+' '+str(box[3]))

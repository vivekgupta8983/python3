




# Create program will take IP and  it will find out How
# many segment do that IP Address have. 192.168.1.1

# Number of Segments
# Number of element in each Segment

ip = input('please Create program '
           'will take IP Create program '
           'will take IP and  it'
           'will find out How and  it will find out Ho wenter IP: ')
if ip[-1] != '.':
    ip += '.'
print(ip)

segment = 1
element = 0
# char = ''
for char in ip:
    if char == '.':
        print(f'this segment has length={element} segments are {segment}')
        segment += 1
        element  = 0

    else:
        element += 1

# what this code does is it skips segment without '.'
# if char != '.':
#      print(f'this segment has length={element} segments are {segment}')
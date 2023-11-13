# i found a solution to make ascii animation in terminal:
# clear screen, sleep 0.5 second
# inspired by the C donut

payload = "*"
for i in range(10):
    payload+='*'
    print(payload)
    time.sleep(0.5)
    print('\x1b[2J')
    # \x1b is the escape character
    # [2J is to clear the screen

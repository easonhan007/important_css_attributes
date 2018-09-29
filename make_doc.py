file_name = 'all.txt'

with open(file_name) as f:
    content = f.read()
    for line in content.split("\n"):
        times_and_attr = line.strip().split(' ')
        if len(times_and_attr) == 2:
            print('* %s [%s](https://developer.mozilla.org/en-US/docs/Web/CSS/%s)' %(times_and_attr[0], times_and_attr[1], times_and_attr[1]))
            
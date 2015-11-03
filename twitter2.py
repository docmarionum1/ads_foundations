results = {}
with open('results.txt') as f:
        for l in f.readlines():
                if l[0] == '/':
                        continue
                d, c, p = l.split()
                if d not in results:
                        results[d] = {'c': 0, 'p': 0}

                s = 1.*results[d]['c'] + float(c)
                r1 = results[d]['c']/s
                r2 = float(c)/s
                results[d]['p'] = results[d]['p']*r1 + float(p)*r2
                results[d]['c'] = s


for d in results:
        print '%s,%s,%s' % (d, results[d]['c'], results[d]['p'])
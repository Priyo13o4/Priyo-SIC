""" def check_arrangement(b, g)
	arrangment = true
	for i in range(1, n):
		if girls[i] >= boys[i-1] and boys[i] >= girls[i-1]:
			continue # go to the next iteration
		else:
			arrangment = False
			break # Once we know such arrangment is not possible, quit
	if arrangment and (g[0] >= b[0] and g[-1] >= b[-1]) or (b[0] >= g[0] and b[-1] >= g[-1])
		return "yes"

Sudo code : 
    Read T
    output []
    for T times do :
        Read N 
        g[]
        b[]
        read N height of g[]
        read N height of b[]
        sort g[]
        sort b[]
        result = check_arrangement(b,g)
        output.append(result)"""
def pascal_triangle(n):
	res = [[1],[1,1]]
	i = 2
	if n == 1:
		res = [[1]]
		return res
	elif n == 2:
		res = [[1],[1,1]]
		return res
	else:
		while i != n:
			s = []
			p = res[-1]
			s.append(p[0])
			for q in range(i-1):
				s.append(p[q]+p[q+1])
			s.append(p[-1])
			res.append(s)
			i += 1
		return res

print(pascal_triangle(5))
print(pascal_triangle(3))
print(pascal_triangle(2))
print(pascal_triangle(1))
print(pascal_triangle(8))



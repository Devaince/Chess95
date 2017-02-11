


#chess
##turn #nobat
##str mat_i
##str mat_j
##str mat_z
##str mat_t


def pawn(table,turn,i,j,z,t):
#taking
	if(j != t and i != z):
		if(turn % 2 ):
			if(abs(t - j) == 1 and z - i == 1):
				if(table[z][t][0] == "b" ):
					return(1)
				else:
					return(0)
			else:
				return(0)				
		else:	
			if(abs(t - j) == 1 and i - z == 1):
				if(table[z][t][0] == "w" ):
					return(1)
				else:	
					return(0)
			else:
				return(0)
##move straight	
	else:
		if(t == j ):
			if(abs(i - z) == 1):
				if(table[z][t] == "**"):
					return(1)
				else:
					return(0)	
			elif(turn % 2):
				
				if(i == 1 and z - i == 2 and table[i+1][j] == "**"):
					return(1)
				else:
					return(0)
			else:
				if(i == 6 and i - z == 2 and table[i-1][j] == "**"):
					return(1)
				else:
					return(0)
		else:
			return(0)			





def king(table,turn,i,j,z,t):
	if((turn % 2 == 1 and table[z][t][0] == "b") or (turn % 2 == 0 and table[z][t][0] == "w") or (table[z][t] == "**")):
		if(abs(z - i) <= 1 and abs(t - j) <= 1):
			return(1)		
		else: 
			return(0)


def knight(table,turn,i,j,z,t):
	if((turn % 2 == 1 and table[z][t][0] == "b") or (turn % 2 == 0 and table[z][t][0] == "w") or (table[z][t] == "**")):	
		if(z - i == 2 and abs(t - j) == 1):
			return(1)
		elif(i - z == 2 and abs(t - j) == 1):
			return(1)
		elif(i - z == 1 and abs(t - j) == 2):
			return(1)
		elif(z - i == 1 and abs(j - t) == 2):
			return(1)
		else:
			return(0)
	else:
		return(0)
def queen(table,turn,i,j,z,t):
	if(rook(table,turn,i,j,z,t) == 1 or bishop(table,turn,i,j,z,t) == 1):
		return(1)
	else:
		return(0)

def rook(table,turn,i,j,z,t):
	if((turn % 2 == 1 and table[z][t][0] == "b") or (turn % 2 == 0 and table[z][t][0] == "w") or(table[z][t] == "**")):
		if((i == z and j != t) or (i != z and j == t)):
			for x in range(1 , max(abs(z-i),abs(t-j))):
				if(z > i and j == t):
					if(table[i+x][j] != "**"):
						return(0)
				elif(z < i and j == t):
					if(table[i-x][j] != "**"):
						return(0)
				elif(z == i and j < t):
					if(table[i][j+x] != "**"):
						return(0)
				elif(z == i and j > t):
					if(table[i][j-x] != "**"):
						return(0)
			return(1)			
		return(0)
	return(0)	
#harkate rokh
def bishop(table,turn,i,j,z,t):
		if((turn % 2 == 1 and table[z][t][0] == "b") or (turn % 2 == 0 and table[z][t][0] == "w") or(table[z][t] == "**")):
				
				if(abs(t - j) == abs(z -i)):

					for x in range(1,abs(t - j)):
						if(z > i and t > j):
							if(table[i+x][j+x] != "**"):
								return(0)
						elif(z < i and t > j):
							if(table[i-x][j+x] != "**"):
								return(0)									
						elif(z > i and t < j):
							if(table[i+x][j-x] != "**"):
								return(0)		
						elif(z < i and t < j):
							if(table[i-x][j-x] != "**"):

								return(0)
					return(1)
				else:
					return(0)
		else: 
			return(0)
# harkate fil




def check(table,turn,i,j,z,t):
	check_table = [["**" for i in range(8)] for j in range(8)]
	for x in range(8):
		for y in range(8):
			if(table[x][y] == "wk"):
				king_white_x = x
				king_white_y = y
			if(table[x][y] == " bk"):
				king_black_x = x
				king_black_y = y

			check_table[x][y] = table[x][y]
	check_table[z][t] = check_table[i][j]
	check_table[i][j] = "**"

	if(turn % 2 == 0):
		for x in range(8):
			for y in range(8):
				if(check_table[x][y] == "bp"):
					print("####")
					if(pawn(table,turn,x,y,king_white_x,king_white_y)):
						return(1)	
				if(check_table[x][y] == "bn"):	
					if(knight(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "bb"):							
					if(bishop(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "br"):			
					if(rook(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "bq"):			
					if(queen(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "bk"):
					if(king(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				else:
					return(0)		
	else:
		for x in range(8):
			for y in range(8):
				if(check_table[x][y] == "wp"):
					if(pawn(table,turn,x,y,king_white_x,king_white_y)):
						return(1)	
				if(check_table[x][y] == "wn"):	
					if(knight(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "wb"):							
					if(bishop(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "wr"):			
					if(rook(table,turn,x,y,king_white_x,king_white_y)):
						return(1)
				if(check_table[x][y] == "wq"):			
					if(queen(table,turn,x,y,king_white_x,king_white_y)):
						return(1)					
				if(check_table[x][y] == "wk"):
					if(king(table,turn,x,y,king_black_x,king_black_y)):
						return(1)
				else:
					return(0)
# kishhhhh







def move(table,turn,movement_string,i,j,z,t):# az (i,j) be (z,t)
	if(check(table, n,i,j,z,t) and  (n % 2 == 1)):
		print("white will be  checked!!!!")
		return("",0)
	elif(check(table,n,i,j,z,t) and ( n % 2 == 0)):
		print("back is checked!!!!!!")
		return("",0)
	if(turn % 2 == 1 and table[i][j][0] == "b" ):
		print("its not your turn !!!")
		return(movement_string,1)
	if(turn % 2 == 0 and table[i][j][0] == "w" ):
		print("its not youre turn !!!!")
		return(movement_string,1)
	if(table[i][j][1] == "b"):
		if(bishop(table,turn,i,j,z,t)):
			movement_string += table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
			table[z][t] = table[i][j]
			table[i][j] = "**"
			return(movement_string,1)
		else:
			print("error")
			return("",0)
	if(table[i][j][1] == "r"):
		if(rook(table,turn,i,j,z,t)):
			movement_string += table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
			table[z][t] = table[i][j]
			table[i][j] = "**"
			return(movement_string,1)
		else:
			print("error")	
			return("",0)
	if(table[i][j][1] == "q"):
		if(queen(table,turn,i,j,z,t)):
			movement_string += table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
			table[z][t] = table[i][j]
			table[i][j] = "**"
			return(movement_string,1)
		else:
			print("error")
			return("",0)
	if(table[i][j][1] == "n"):
		if(knight(table,turn,i,j,z,t)):
			movement_string += table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
			table[z][t] = table[i][j]
			table[i][j] = "**"
			return(movement_string,1)
		else:
			print("error")
			return("",0)	
	if(table[i][j][1] == "p"):
		if(pawn(table,turn,i,j,z,t)):
			movement_string +=  table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
			table[z][t] = table[i][j]
			table[i][j] = "**"
			return(movement_string,1)
		else:
			print("error")	
			return("",0)
	if(table[i][j][1] == "k"):
		movement_string +=  table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
		table[z][t] = table[i][j]
		table[i][j] = "**"
		return(movement_string,1)
	else:	
		print("######")
		movement_string +=  table[i][j] + str(i) + str(j) + table[z][t] + str(z) + str(t)
		table[z][t] = table[i][j]
		table[i][j] = "**"
		return(movement_string,1)
		
			
# harkat




def show(table): ## neshoon dadane jadval 
	for i in range (8):
		for j in range(8):
			print(table[i][j], end = " ") 
		print()	
	return()


table = [["**" for i in range(8)] for j in range(8)]
for i in range(8):
	table[1][i] = "wp"
	table[6][i] = "bp"
table[0][0] = "wr"	
table[0][7] = "wr"
table[7][0] = "br"
table[7][7] = "br"
# rokh


table[0][1] = "wn"
table[0][6] = "wn"
table[7][1] = "bn"
table[7][6] = "Bn"
# asb

table[0][2] = "wb"
table[0][5] = "wb"
table[7][2] = "bb"
table[7][5] = "bb"
# fil

table[0][3] = "wk"
table[7][3] = "bk"
# shah


table[0][4] = "wq"
table[7][4] = "bq"
#vazir
##def bishop(turn )
##def pawn(turn)
show(table)
movement_string = ""
n = 1
while(n >= 1):
	
	i = int(input())
	j = int(input())
	z = int(input())
	t = int(input())
	movement_string,s = move(table,n , movement_string,i,j,z,t)
	print(n)
	show(table)
	for x in range(1,len(movement_string)):
		if(x % 8 != 0):
			print(movement_string[x-1],end ="" )
		else:
			print()
	print()
	n += s

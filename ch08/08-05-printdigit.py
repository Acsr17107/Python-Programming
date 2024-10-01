LCD = [[ "|||||", 
         "|   |", 
         "|   |", 
         "|   |", 
         "|||||" ], 
         
        ["   | ", 
         "  || ", 
         "   | ", 
         "   | ", 
         " ||||" ], 
         
        ["|||||", 
         "    |", 
         "|||||", 
         "|    ", 
         "|||||" ], 
         
        ["|||||", 
         "    |", 
         "|||||", 
         "    |", 
         "|||||" ], 
         
        ["|   |", 
         "|   |", 
         "|||||", 
         "    |", 
         "    |" ], 
         
        ["|||||", 
         "|    ", 
         "|||||", 
         "    |", 
         "|||||" ]]

# 표준 입력
num = -1
while not (0 <= num <= 5): # 0에서 5 사이만을 입력받기 위해
    num = int(input("0 ~ 5 사이의 숫자 1개 입력 >> "))

# 위 LCD 리스트에서 한 항목인 숫자를 선택
select = LCD[num]
# 선택한 select 숫자인 리스트에서 각각의 항목을 한 줄에 출력
for row in select:
    print(row)
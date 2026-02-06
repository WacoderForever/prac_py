
row1=["⬛","⬛","⬛"]
row2=["⬛","⬛","⬛"]
row3=["⬛","⬛","⬛"]
map=[row1,row2,row3]
pos=input("Enter position to hide your treasure:")
pos=(int)(pos)
row_pos=pos//10
column_pos=pos%10
map[row_pos-1][column_pos-1]="T"
print('\n',row1,'\n',row2,'\n',row3)
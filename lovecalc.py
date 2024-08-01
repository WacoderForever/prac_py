my=input("What is your name?:")
cr=input("What is his/her name?:")
my=my.lower()
cr=cr.lower()
t_count=my.count("t")+cr.count("t")
r_count=my.count("r")+cr.count("r")
u_count=my.count("u")+cr.count("u")
e_count=my.count("e")+cr.count("e")
first=t_count+r_count+u_count+e_count
l_count=my.count("l")+cr.count("l")
o_count=my.count("o")+cr.count("o")
v_count=my.count("v")+my.count("v")
last=l_count+o_count+v_count+e_count
ans=(first*10)+last
print("You two love each other {}%".format(ans))
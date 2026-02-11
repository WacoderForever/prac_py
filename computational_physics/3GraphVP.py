from vpython import *

string = "black:sin^2(x) blue:cos^2(x) cyan:sin(x)*cos(x)"

graph1 = graph(title=string,xtitle='x',ytitle='y',
                width=400, height=400,
                background=color.white,foreground=color.black)

y1 = gcurve(color = color.black)
y2 = gvbars(color = color.blue)
y3 = gdots(color = color.cyan)

for x in arange(-5,5,0.1):
    y1.plot(pos=(x,sin(x)**2))
    y2.plot(pos=(x,cos(x)*cos(x)))
    y3.plot(pos=(x,sin(x)*cos(x)))

from vpython import *

graph1 = graph(align='left',width=400,height=400,
            background=color.white,foreground=color.black)
Plot1 = gcurve(color=color.red)
for x in arange(0,8.1,0.1):
    Plot1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x)))

graph2 = graph(align='right',width=400,height=400,
            background=color.white,foreground=color.black,
            title='2D plot',xtitle='x',ytitle='f(x)')

Plot2 = gdots(color=color.black)

for x in arange(-5,5,0.1):
    Plot2.plot(pos=(x,cos(x)))
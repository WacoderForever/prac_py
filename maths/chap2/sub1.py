from vector_drawing import *
from vectors import *

v=(-1,3)
w=(2,2)

draw(Points(v,w),Arrow(tip=v,color=blue),Arrow(tip=w,color=blue),Arrow(tip=v,tail=w,color=red),
    Arrow(tip=subtract(v,w),color=red),Points(subtract(v,w)))
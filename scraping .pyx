# distutils: language=c++
# distutils: extra_compile_args = ["-O3"]
# cython: language_level=3, boundscheck=False, wraparound=False
# cython: cdivision=True

from libcpp.vector cimport vector #ここでcppのvectorを呼び出している。
ctypedef long long LL
ctypedef vector[LL] vec

import time

start=time.time()

cdef: 
    vec c

for i in range(100000):
  c.push_back(i)

end=time.time()

print(end-start)





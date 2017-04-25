def answer(start, length):
	    result = 0
	    if start % 2 == 0:
	        for i in xrange(length, 0, -1):
	            fe = start+(length*(length-i)) # first elegible element of that row
	            le = start+(length*(length-i))+(i-1) # last elegible element of that row
	            if i % 4 == 1:
	                result ^= le
	            elif i % 4 == 2:
	                if length % 2 == 0:
	                    result ^= 1
	                else:
	                    result ^= le ^ fe
	            elif i % 4 == 3:
	                result ^= le ^ 1
	            else:
	                if length % 2 == 1:
	                    result ^= le ^ fe ^ 1
	    else:
	        for i in xrange(length, 0, -1):
	            fe = start+(length*(length-i)) # first elegible element of that row
	            le = start+(length*(length-i))+(i-1) # last elegible element of that row
	            if i % 4 == 1:
	                result ^= fe
	            elif i % 4 == 2:
	                if length % 2 == 1:
	                    result ^= 1
	                else:
	                    result ^= le ^ fe
	            elif i % 4 == 3:
	                result ^= fe ^ 1
	            else:
	                if length % 2 == 0:
	                    result ^= le ^ fe ^ 1
	    print(result)
	    return result


answer(0, 3)
answer(17, 4)
answer(17, 6)
answer(17, 8)
answer(17, 5)
answer(2, 6)
answer(2, 5)
#answer(2000000000, 1)
#answer(2000000000, 500000000)

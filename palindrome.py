#starting values of variables
x = int(input ())
a = 0
b = 0
c = False

#if the number is negative
if x < 0:
x = str(x) [1:]
x = int(x)
c = True

#algorithm for finding the nearest palindrome
while True:
 b = x
 b = x + a
 if str(b) == str(b)[::-1]:
  break
 b = x - a
 if str(b) == str(b)[::-1]:
  break
 a = a + 1

#if the number is negative
if c:
 b = " - " + str (b)
 b = int (b)

#output
print(b)

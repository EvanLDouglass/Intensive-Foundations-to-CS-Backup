# Homework 2 Feedback:
### Written:
####W2:
answer should be `nickname = dog_name[:num_letters] + "-" + name_suffix`
Adding the `+1` causes the b from Tugboat to be used in the nickname:
```
# Example
dog_name = "Tugboat"
num_letter = 3
name_suffix = "face"
nickname = dog_name[0:num_letter+1] + "-" + name_suffix
print(nickname)
```
this prints: Tugb-face

Pythons slice operator `array[start:end]` vs `array[index]` is a little interesting.
[here's a stack overflow comment, that explains the difference between the index and slice](https://stackoverflow.com/a/4729334)

10/11 correct

_total: 96/100_

### Program:
##### P1:
Nice work! very good testing. The is_pal() function being abstracted from main is very good.

##### P2:
Excellent implementation. One comment might be to consider breaking up your code into more portable functions(you're already thinking along these lines based on your comments in the code), but this is very good. Also lot of character to the user interface!

##### P3:
-Program Correctness: 85, sat, 20, N => $12.00, when it should be $11.00
  This problem stems from line 78-79, I believe. You are adding an extra $1 weekend premium since its after 5pm, which should not be there. There's only a 5pm premium on weekdays.
-Readability: Literals on lines 55, 58, 76, and 78, should be using as constants


---
- Program Correctness : 93/100, for issue on P3
- Readability : 93/100 for literals in P3
- Documentation : 100/100
- Coding Efficiency : 100/100
- Amazing :
_total: 92.54/100_

---
### Grade : 93.232

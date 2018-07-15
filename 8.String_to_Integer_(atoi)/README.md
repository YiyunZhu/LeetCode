<!-- <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script> -->
# 8. String to Integer (atoi)

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**
- Only the space character `' '` is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [$2^(31)$ ,  $$2^(31)-1$$]. If the numerical value is out of the range of representable values, INT_MAX ($$2^(31)-1$$) or INT_MIN ($$-2^(31)$$) is returned.

**Example 1:**
```
Input: "42"
Output: 42
```

**Example 2:**
```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

**Example 3:**
```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

**Example 4:**
```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

**Example 5:**
```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN ($-2^31$) is returned.
```

这道题挺复杂的，在LeetCode上通过率很低，因为需要考虑到的情况很多。
在自测的时候可以用到下面的测试用例。

```
    strs ="  4193 with words"
    strs = " words 3915"
    strs = " +-94"
    strs = "-1"
    strs = "+"
    strs = "-abc"
    strs = "-00000012d121212121212121"
```

我在LintCode提交的前一个版本没有考虑到"+"的情况，但是也通过了，我已经提交了错误。

修改后的代码在LintCode的排名是100%也是很神奇呀

不过LeetCode的大神那么多，我也会给出solution2
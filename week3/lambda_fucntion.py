import re
data = ["abc123" , "hel123 44dfh"]
#extract the digits inside the string using regex and lambda
digits = list(map(lambda s:re.findall(r'\d+',s),data))
print(digits)
#------------------------------------------------------------------------------------------------------------------------
data = ["Hello123","A@B#C","Clean_text","X Y Z"]

cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z0-9]','+',s),data))
print(cleaned)
#------------------------------------------------------------------------------------------------------------------------
emails = ["priyodip1304@gmail.com","priyodip2309@gmail.com","priyodip5986@gmail.com"]

# domains = list(map(lambda s: re.sub(r'@(\w+)\.',s).group(1),emails))

#------------------------------------------------------------------------------------------------------------------------
words = ["apple","banana","mango"]
#capitalize if starts with a vowel
vowel_caps = list(map(lambda w:re.sub(r'^[aeiou]',lambda m: m.group(0).upper(),w),words))
print(vowel_caps)
#Capitalize the whole word if it starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou]',lambda m :w.upper(),w),words))
print(vowel_caps)

vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)',lambda m :w.upper(),w),words))
print(vowel_caps)
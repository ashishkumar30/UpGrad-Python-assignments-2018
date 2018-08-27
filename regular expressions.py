import re 


# Q.2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

'''

a= ("Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.")
a=a.replace("Betty","betty")
a=re.findall(r'b[\w]*',a)
print(a)

'''

# Q.3- Split the following irregular sentence into words sentence = "A, very very; irregular_sentence" desired_output = "A very very irregular sentence"

'''
a=(" \" A, very very; irregular_sentence \" ")
a=a.replace(",","")
a=a.replace(";","")
a=a.replace("_"," ")
print(a)

'''

#Q.4- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

'''

a=(" \' Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today \' http://t.co/lbwej0pxOd cc: @garybernhardt #rstats")
a=a.replace("http://t.co/lbwej0pxOd cc: @garybernhardt #rstats", "")
a=a.replace("! RT @TheNextWeb:","")
print(a)

'''

#Q1  Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')

'''

a= ["zuck26@facebook.com", "page33@google.com", "jeff42@amazon.com"]
z=[]
for e in a:
    z.append(tuple(re.split('[@.]',e)))
print(z)

'''
#END ASSIGNMENT


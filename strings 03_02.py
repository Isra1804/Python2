import re
text =  "almadrasa is your way to learn programming the right way."
text += "almadrasa badges motivate students to do more."
text += "almadrasa quizes help students practice on what they have learned through the course."
text += "almadrasa are one of a kind because they were made by professionals."
text += "almadrasa look and feel is one of a kind. almadrasa wshes you a good learning thanks."
rep = re.sub("almadrasa \w{3,}", "Almadrasa",text,3)
print (rep)

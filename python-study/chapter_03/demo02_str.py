from string import Template
tmp = Template("Hello,$who!")
tmp.substitute(who="liwen")
print(tmp.substitute(who="liwen"))
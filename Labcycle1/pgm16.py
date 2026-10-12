my_dict={'banana':3,'apple':1,'cherry':2,'date':4}
print("Original list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("Ascendig Order:",asorted_dict)
desorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Descendig Order:",desorted_dict)

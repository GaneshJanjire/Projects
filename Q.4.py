import re


def clean_name(name):
    name = re.sub(r'\b[A-Za-z]\d+|\d+[A-Za-z]\b', '', name)

    name = re.sub(r'(S/O|C/O|D/O|S O|C O|D O|SO|CO|DO)', '', name)

    name = re.sub(r'(and \d+ others|and[a-z]{2,7}|and otrs|and anothers)', '', name)

    name = re.sub(r'R/O|R/AT', '', name)

    name = re.sub(r'(alias|urf|urfa|aka)', '', name)

    name = re.sub(r'[^\w\s]', '', name)

    name = re.sub(r'^(Mr|Mrs|Ms|Shri|Dr)', '', name)

    return name.strip()

print(clean_name("A3 KHAJA ZAMEER-UDDIN S O KHAJA ZAHEERUDDIN"))
print(clean_name(" Chiluka Narsing Rao and another"))
print(clean_name("Gopoju-Upendar and 2 others"))
print(clean_name("HEMANTH ALIAS KENCHA ALIAS BOSS"))
print(clean_name("5B Ratnakar Shambhu,Poojari R/o No.764/15A3rd Cross Bhagya Ngr"))
print(clean_name("Parvesh @ Pintu Ramesh Tandel and ors"))
print(clean_name("Venku Urfa Appa Narsu Waghmode and3otrs")) 
print(clean_name("Somnath Ghosh and othrs"))
print(clean_name("Gupta Company and 1 Other"))
print(clean_name("Mr Yangmaso Khariwo and Ors"))
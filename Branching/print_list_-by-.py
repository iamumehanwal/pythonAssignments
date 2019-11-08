product_companies = ['Apple', 'Google', 'Samsung', 'LG', 'Moto', 'Sony']              # List 
no_comp = len(product_companies)                                                      # Count of the list

#product_companies.sort()                                                              # Sorting the list

i=0                                                                                   # Variable used for while loop
while i < no_comp:
    print(str(i+1) + ' : ' + product_companies[i])
    i+=1


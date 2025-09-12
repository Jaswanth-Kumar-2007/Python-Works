def getCostOfCoffee(n,p):
    '''
    Calculate the total cost of coffee orders where
    for every eight coffee you get one additional coffee free
    (i.e., nine coffees in total pyou only pay for eight).
    Return the total cost as a float.
    '''
    r = n//8
    return (n-r)*p
    
#Test Cases:
#print(getCostOfCoffee(10,2.5))
#print(getCostOfCoffee(18, 2.50))
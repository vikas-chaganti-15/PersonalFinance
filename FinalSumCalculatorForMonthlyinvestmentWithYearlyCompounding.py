#We need a 35000 rs monthly investment to reach 2CR fund by then 

ny = 20 #contineous investment period in years
mi = 35000 #monthly investment for kid education
interest_perc = 8 #considering a net 8% yearly compound interest 
yearly_investment = 12 * mi
year = 1
interest = 0
principal = yearly_investment
while(year < ny):
    interest = (principal * interest_perc )/100
    principal = principal + interest + yearly_investment
    year = year + 1
    #print str(year) + " " + str(principal) + "  " + str(interest)

print "Final amount = " + str(principal)

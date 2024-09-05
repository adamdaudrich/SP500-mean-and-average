file = open('SP500.txt','r')
lines = file.readlines()

#initialize eventual lists (mutable and iterable)
SP_500 = []
interest = []

#isolate desired date range (lines 6:18)
for line in lines[6:18]:
    # variable 'columns' is actually the entire row.
    # the index gives you the item
    columns = line.strip().split(',')
    SP_500.append(columns[1])
    interest.append(columns[5])

# make a list called 'float values' which translates
# all numbers in the SP_500 list to a float
float_values = [float(value) for value in SP_500]
SP_sum = sum(float_values)
SP_count = len(float_values)
mean_SP = SP_sum / SP_count
print('The average SP 500 for the date range is: ', mean_SP)

# same thing, translate interest to a new list of floats                  
interest_values = [float(v) for v in interest]
max_interest = max(interest_values)
print('The max interest value for the date range is: ', max_interest)


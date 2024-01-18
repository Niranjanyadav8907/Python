#string are immutable string  ko change nhi kiya ja skta immutable ka mtlb yehi hota hain 

string = "string"
print(string[2])
#print[1] = 'T' # error kyu ki hmm string ko change nhi kr skte hain

string.replace('t', 'T')
print(string.replace('t', 'T')) #replace kr skte hain but wo change new string bn kr ho rha hain

#exaplep
print(string)

new_string = string.replace('t', 'T')
print(new_string)

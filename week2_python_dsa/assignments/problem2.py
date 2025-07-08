request_numbers = int(input("Enter the number of requests :"))
server_requests = [int(request) for request in input().split()]

server1_memory = 0
for i in range (0,request_numbers,2) :
    server1_memory += server_requests[i]

if server1_memory < 0 :
    print("Total memory deallocated by server1 = ",server1_memory, "units")
else :
     print("Total memory allocated by server1 = ",server1_memory, "unit")




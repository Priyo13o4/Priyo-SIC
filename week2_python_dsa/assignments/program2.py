#"meghalaya shillong" "manipur imphal" "mizoram aizal" "tripura agartala" "nagaland kohima"

import sys

states = []
capitals = []
for arg in sys.argv[1:]:
    s, c = arg.split()
    states.append(s.title())
    capitals.append(c.title())

print("State  capital")
print("--------------")
for s, c in zip(states, capitals):
    print(f"{s:<8} {c}") 
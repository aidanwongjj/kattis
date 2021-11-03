
# https://open.kattis.com/problems/upprodun

num_rooms = int(input())
num_teams = int(input())

base_len = num_teams // num_rooms
remainder = num_teams % num_rooms

for i in range(num_rooms):
    print('*' * (base_len+1)) if i < remainder else print('*' * (base_len)) 

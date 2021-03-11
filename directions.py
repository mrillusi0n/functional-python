def get_final_direction(turns):
    return 'ENWS'[sum(map(int, turns.replace('0', '3'))) % 4]

for _ in range(int(input())):
    input()
    print(get_final_direction(input()))


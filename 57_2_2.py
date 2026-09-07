ages = {}
ages['А'], ages['Б'], ages['В'] = map(int, input().split())
print(*[key for key, val in ages.items() if val == max(ages.values())])

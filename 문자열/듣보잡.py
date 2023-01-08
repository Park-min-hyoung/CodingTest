n, m = map(int, input().split())
data = list(input() for _ in range(n + m))
sorted_data = sorted(data)

result = []
for idx in range(1, len(sorted_data)):
    if sorted_data[idx] == sorted_data[idx - 1]:
        result.append(sorted_data[idx])

print(len(result))
print("\n".join(result))
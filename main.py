N = int(input())
hours = (N // 3600) % 24
minutes = (N % 3600) // 60
seconds = N % 60
result = f"{hours}:{minutes:02}:{seconds:02}"
print(result)
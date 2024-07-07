from pathlib import Path

path =Path("ecommerce")
print(path.exists())

print(path.mkdir())
print(path.rmdir())

path = Path()
print(path.glob('*'))

for file in path.glob('*'):
    print(file)

for file in path.glob('*.py'):
    print(file)
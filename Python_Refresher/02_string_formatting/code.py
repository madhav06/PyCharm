# name = "Srinivasan M."

# print(f"Hello, {name}")

# name = "P. Raghurajan"

# print(f"Hello, {name}")

name = "Srinivasan"
greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("P Raghu")

print(with_name)
print(with_name_two)


longer_phrase = "hello, {}. today is {}."
formatted = longer_phrase.format("Krishna Iyyer", "Friday")
print(formatted)


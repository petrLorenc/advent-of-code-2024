with open("input.txt") as f:
    input_data = f.readlines()

input_data = list(map(str.strip, input_data))
input_data = list(map(int, input_data))

out = 0

for number in input_data:
    print(number)
    for i in range(2000):
        number_64 = number * 64
        number_64_mix = number_64 ^ number
        number_64_mix = number_64_mix % 16777216

        number_32 = number_64_mix // 32
        number_32_mix = number_32 ^ number_64_mix
        number_32_mix = number_32_mix % 16777216

        number_2048 = number_32_mix * 2048
        number_2048_mix = number_2048 ^ number_32_mix
        number_2048_mix = number_2048_mix % 16777216

        number = number_2048_mix

    print(number)
    out += number

print(f"{out=}")
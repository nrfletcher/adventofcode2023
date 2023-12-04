file_path = "input.txt"
total = 0
cnt = 1
nums = {'one': 3, 'two': 3, 'three': 5, 'four': 4, 'five': 4, 'six': 3, 'seven': 5, 'eight': 5, 'nine': 4}
convert = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

try:
    with open(file_path, "r") as file:
        
        for line in file:
            cnt += 1
            char1 = ''
            char2 = ''
            current = 0
            seen = 0
            for c in range(len(line)):
                if line[c] in '123456789':
                    if seen == 0:
                        char1 = line[c]
                        seen += 1
                    else:
                        char2 = line[c]
                elif line[c] in 'otfsen':
                        for num in nums:
                            if (nums[num] + c) < len(line):
                                if line[c:c+nums[num]] == num:
                                    if seen == 0:
                                        char1 = convert[num]
                                        seen += 1
                                    else:
                                        char2 = convert[num]
            if char2 == '':
                char2 = char1
            val = char1 + char2
            total += int(val)

        print(total)
                
            
except FileNotFoundError:
    print("no such file")
except IOError:
    print("error reading")

    
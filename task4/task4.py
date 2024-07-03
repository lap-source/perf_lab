#!/usr/bin/env python3

import sys
import os


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 %s <file_numbers>" % os.path.basename(sys.argv[0]))
        sys.exit(0)

    file_numbers = sys.argv[1]

    with open(file_numbers) as f:
        nums = [int(line) for line in f]

    nums.sort()
    element_center = nums[len(nums) // 2]

    count = 0
    for num in nums:
        count += abs(num - element_center)

    print(count)

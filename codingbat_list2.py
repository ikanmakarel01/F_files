def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  terbesar = max(nums)
  terkecil = min(nums)
  perbedaan = terbesar - terkecil
  return perbedaan

def centered_average(nums):
    if len(nums) < 3:  # Pastikan ada cukup angka untuk dihitung
        raise ValueError("List harus memiliki minimal 3 angka")

    nums.sort()  # Urutkan list dari kecil ke besar
    trimmed_nums = nums[1:-1]  # Hapus nilai terkecil dan terbesar

    return sum(trimmed_nums) / len(trimmed_nums)

def sum13(nums):
    total = 0
    i = 0  # Start from index 0
    while i < len(nums):  # Use while loop to manually control `i`
        if nums[i] == 13:
            i += 2  # Skip 13 and the next number
        else:
            total += nums[i]
            i += 1  # Move to the next number
    return total

def sum67(nums):
    total = 0
    skip = False  # Flag to track when to ignore numbers

    for num in nums:
        if num == 6:
            skip = True  # Start ignoring numbers
        elif num == 7 and skip:
            skip = False  # Stop ignoring numbers
        elif not skip:
            total += num  # Add only when not in a skipped section
    return total

def has22(nums):
  for i in range (len(nums)-1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1

        while left <= right:
            
            current_num = numbers[left] + numbers[right]
            
            if current_num == target:
                return [left+1, right+1]
            elif current_num > target:
                right -=1
            else:
                left+=1

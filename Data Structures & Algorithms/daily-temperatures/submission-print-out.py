class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        index = []
        results = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            print(f"Day {i}, temp {t}")

            while len(index) > 0 and t > temperatures[index[-1]]:
                removed = index.pop()
                results[removed] = i - removed
                print(f"   day {removed} found its warmer day: {i - removed} day(s) later")

            index.append(i)
            print(f"   waiting days: {index}")

        return results

Solution().dailyTemperatures([30, 38, 30, 36, 35, 40, 28])
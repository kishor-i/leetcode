class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alitude=0
        highest=0
        for change in gain:
            alitude +=change
            highest=max(highest,alitude)
        return highest
        
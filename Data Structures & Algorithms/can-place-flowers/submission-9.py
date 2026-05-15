class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            prev, succ = flowerbed[i-1] if i > 0 else 0, flowerbed[i+1] if i < len(flowerbed)-1 else 0
            if prev + succ == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
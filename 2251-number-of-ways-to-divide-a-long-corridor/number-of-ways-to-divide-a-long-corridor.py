class Solution:
    def numberOfWays(self, corridor: str) -> int:
        Mod = 10**9 + 7
        seats = corridor.count('S')
        if seats == 0 or seats % 2 == 1 :
            return 0

        ways = 1
        seat_count  = 0
        plant_count = 0

        for c in corridor :
            if c == 'S' :
                seat_count += 1

                if seat_count > 2 and seat_count % 2 == 1 :
                    ways = (ways * (plant_count + 1)) % Mod
                    plant_count = 0

            else:
                if seat_count >= 2 and seat_count % 2 == 0:
                    plant_count += 1

        return ways

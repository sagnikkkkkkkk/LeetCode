class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        import re
        
        offline_until = [0] * numberOfUsers
        result = [0] * numberOfUsers

        def priority(e) :
            if e[0] == "MESSAGE" :
                return 1
            return 0

        events.sort(key=lambda e: (int(e[1]) , priority(e)))

        for event in events :
            if event[0] == "MESSAGE" :
                time = int(event[1])
                text = event[2]

                if text == "ALL" :
                    for i in range(numberOfUsers) :
                        result[i] += 1

                elif text == "HERE" :
                    for i in range(numberOfUsers) :
                        if offline_until[i] <= time :
                            result[i] += 1

                else :
                    ids = re.findall(r'id(\d+)' , text)
                    for uid in ids :
                        u = int(uid)
                        if 0 <= u < numberOfUsers :
                            result[u] += 1

            elif event[0] == "OFFLINE" :
                time = int(event[1])
                user = int(event[2])
                offline_until[user] = time + 60

            elif event[0] == "ONLINE" :
                user = int(event[2])
                offline_until[user] = 0

        return result
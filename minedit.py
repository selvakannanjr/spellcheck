def load_words(path):
    with open(path) as file:
        words = [x.strip() for x in file.readlines()]
    return words

def minDistance(word2: str, word1: str) -> int:
    #dp[i][j] will be the least distance from word1[:i] to word2[:j]
    dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        dp[i][0] = i
        for j in range(1,len(word2)+1):
            if i == 0:
                dp[0][j] = j
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    return (word2,dp[-1][-1])  
                            

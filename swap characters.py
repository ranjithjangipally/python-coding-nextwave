def check_status(word1,word2):
    if word1 == word2:
        return "Yes"
    else:
        return "No"
        
def swap_words_and_check(word1,word2):
    for i in range(len(word1)-1):
        if word1[i] != word2[i]:
            temp = word1[i]
            word1[i] = word1[i+1]
            word1[i+1]=temp 
            break 
    result = check_status(word1,word2)
    return result 
            

def main():
    word1,word2 = list(input()),list(input())
    final_result = swap_words_and_check(word1,word2)
    print(final_result)
main()
def lengthOfLongestSubstring(s):
    res = 0
    l = 0
    charSet = set()

    for r in range(len(s)):
        while s[r] in charSet: # if right of window detects a dupe character
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r]) # extends the window
        res = max(res, r - l + 1) # compares the set longest window to the current size of the window
    return res

def main():
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()
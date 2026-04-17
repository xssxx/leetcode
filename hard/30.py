class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # example case: ["bar","foo","the"]
        word_len = len(words[0]) # 3
        words_len = len(words) # 3 
        window_size = word_len * words_len # 9

        # เก็บจำนวนคำที่ต้องมี 
        # เช่น [bar, foo, the] มีอย่างละ 1
        word_counts = {}
        for w in words:
            word_counts.get(w, 0) + 1

        ans = []

        # step ทีละ 1 window (ขนาด 9 characters) 
        # เพราะ permutation ของ bar, foo, the เอามารวมกันเป็นคำเดียวได้ 9 ตัวอักษร
        for i in range(len(s) - window_size + 1):
            seen_words = {}
            count = 0
            # ไล่ไปทีละ character และตัดคำออกมา ทีละ 3 character ตาม len ของ word ใน words
            while count < words_len:
                start = i + (count * word_len)
                word = s[start : start + word_len] # gap ทีละ 3 character
                if word in word_counts: # ถ้าคำถูก foo, the, bar
                    seen_words[word] = seen_words.get(word, 0) + 1 # เก็บเข้า seen
                    if seen_words[word] > word_counts[word]:
                        break
                else:
                    break
                
                count += 1

            if count == words_len: # ถ้าคำครบเช่นมี foo, the, bar ครบ แสดงว่าเป็น substring
                ans.append(i) # add index นั้นเข้าคำตอบ
        
        return ans

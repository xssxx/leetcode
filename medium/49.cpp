// 2023.04.18

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            groups[sortedWord].push_back(word);
        }
        
        vector<vector<string>> result;
        for (auto& pair : groups) {
            result.push_back(pair.second);
        }
        return result;
    }
};
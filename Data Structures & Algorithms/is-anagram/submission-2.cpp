class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){return false;}
        for (auto i=s.begin();i!=s.end();i++){
            for (auto j=t.begin();j!=t.end();j++){
                if (*i==*j){
                    t.erase(j);
                    break;
                }
            } if (t==""){return true;}
        }
    return false;}
};

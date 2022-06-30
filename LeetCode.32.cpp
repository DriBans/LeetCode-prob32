class  Solution
{
public:
    int longestValid(string s) {
        vector <int> stack = {-1};
        int answer = 0;
        for (int i = 0; i < s.size(); i++)
            if (s[i] == '(') stack.push_back(i);
            else if (stack.size() == 1) stack[0] = i;
            else {
                stack.pop_back();
                answer = max(answer, i - stack.back());
            }
        return answer;  
     }
};
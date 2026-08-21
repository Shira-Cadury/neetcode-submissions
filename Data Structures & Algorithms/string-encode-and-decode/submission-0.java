class Solution {
    public String encode(List<String> strs) {
        StringBuilder w=new StringBuilder();
        for(int i=0; i<strs.size(); i++)
        {
            String word=strs.get(i);
            int len=word.length();          
            w.append(len).append("#").append(word);
        }
        return w.toString();
    }

    public List<String> decode(String str) {
        List<String> ans=new ArrayList<>();
        int i=0;
        while (i < str.length())
        {
            int slash = str.indexOf('#', i);
            int len = Integer.parseInt(str.substring(i, slash));
            ans.add(str.substring(slash+1, slash + 1 + len));
            i=slash + 1 + len;
        }
        return ans;
    }
}

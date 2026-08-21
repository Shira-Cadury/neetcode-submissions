class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map=new HashMap<>();
        
        for(int i=0; i<strs.length; i++)
        {
            String key = help(strs[i]);
            if(!map.containsKey(key))
            {
                map.put(key, new ArrayList<>());
            }          
                map.get(key).add(strs[i]);       
        }
        return new ArrayList<>(map.values());
    }

    private String help(String s)
    {
        int[] temp=new int[26];
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++)
        {
            temp[s.charAt(i) - 'a']++;
        }

        for (int val : temp) {
          sb.append(val);
          sb.append('#');
        }

        return sb.toString();
    }
}

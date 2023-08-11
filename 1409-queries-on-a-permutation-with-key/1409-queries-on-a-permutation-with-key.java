class Solution {
    public int[] processQueries(int[] queries, int m) {
        int[] result = new int[queries.length];
        HashMap<Integer, Integer> P = new HashMap<>();
        for (int i = 1; i <= m; i++) P.put(i,i-1); // key:i~m, value:index
        
        for (int i = 0; i <= queries.length-1; i++){
            int position = P.get(queries[i]); // find the position of queries[i] in the permutation P
            for (int j = 1; j <= m; j++){
                if (P.get(j) == position) P.put(j,0); // move queries[i] at the beginning of the permutation P 
                else if (P.get(j) < position) P.put(j,P.get(j)+1);
            }
            result[i] = position; // position of quries[i] in P
        }
        return result;
    }
}
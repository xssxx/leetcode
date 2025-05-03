// 2023.12.02

class Solution {
    public int finalValueAfterOperations(String[] operations) {
        byte x = 0;
        for (String op : operations) {
            if (op.equals("--X") || op.equals("X--"))
                x--;
            else if (op.equals("++X") || op.equals("X++"))
                x++;
        }

        return x;
    }
}
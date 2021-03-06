# Java코드
import java.lang.Math;
import java.util.Arrays;


class Solution {
    public int solution(int sticker[]) {
    int size = sticker.length;

    if (size <= 3){
        return Arrays.stream(sticker).max().getAsInt();
}

# //각인덱스까지의스티커최대합을저장할배열
#    // 첫번째스티커를떼는경우와두번째스티커를떼는경우로나눠서저장
    int[] dp1 = new int[size];
    int[] dp2 = new int[size];

    dp1[0] = dp1[1] = sticker[0];
    dp2[0] = 0;
    dp2[1] = sticker[1];

    for (int i=2; i < size-1; i++)
    {
// 이전에구한게더크면스티커떼지않고유지
        dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
        dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
}

    int i = size - 1;
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2]);
    dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);

    return Math.max(dp1[i], dp2[i]);
}
}
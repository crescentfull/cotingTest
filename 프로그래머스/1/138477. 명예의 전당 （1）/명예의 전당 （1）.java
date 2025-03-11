import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        PriorityQueue<Integer> hallOfFame = new PriorityQueue<>(); // 최소 힙 사용
        int[] answer = new int[score.length];

        for (int i = 0; i < score.length; i++) {
            hallOfFame.add(score[i]); // 현재 점수를 힙에 추가
            
            if (hallOfFame.size() > k) { // k개를 초과하면 최하위 점수 제거
                hallOfFame.poll();
            }
            
            answer[i] = hallOfFame.peek(); // 현재 명예의 전당 최하위 점수 저장
        }
        
        return answer;
    }
}

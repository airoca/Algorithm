import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        
        Deque<Integer> queue = new ArrayDeque<>();
        int temp = 0;
        
        for (int i = 0; i < n; i++) {
        	st = new StringTokenizer(br.readLine());
        	String inst = st.nextToken();
        	
        	if (inst.equals("push")) {
        		queue.add(Integer.parseInt(st.nextToken()));
        		continue;
        	} else if (inst.equals("pop")) {
        		temp = queue.isEmpty() ? -1 : queue.pop();
        	} else if (inst.equals("size")) {
        		temp = queue.size();
        	} else if (inst.equals("empty")) {
        		temp = queue.isEmpty() ? 1 : 0;
        	} else if (inst.equals("front")) {
        		temp = queue.isEmpty() ? -1 : queue.peekFirst();
        	} else if (inst.equals("back")) {
        		temp =queue.isEmpty() ? -1 :  queue.peekLast();
        	}
        	
        	bw.write(temp + "\n");
        }
        
        bw.flush();
        br.close();
        bw.close();
    }
}
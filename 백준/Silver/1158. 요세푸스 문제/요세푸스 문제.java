import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        List<Integer> stack = new ArrayList<>();
        Queue<Integer> nArray = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            nArray.offer(i);
        }

        int cnt = 0;
        while (!nArray.isEmpty()) {
            cnt++;
            // cnt가 k의 배수인 경우 remove
            if (cnt % k == 0) {
                stack.add(nArray.poll());
                cnt = 0;
            } else {
                nArray.offer(nArray.poll());
            }
        }

        // Print the result
        System.out.print("<");
        for (int i = 0; i < stack.size(); i++) {
            System.out.print(stack.get(i));
            if (i < stack.size() - 1) {
                System.out.print(", ");
            }
        }
        System.out.print(">");
    }
}


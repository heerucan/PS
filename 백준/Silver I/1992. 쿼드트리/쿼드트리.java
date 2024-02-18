import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static StringBuilder compressed = new StringBuilder();

    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(reader.readLine());
            char[][] matrix = new char[n][n];
            for (int i = 0; i < n; i++) {
                String line = reader.readLine();
                matrix[i] = line.toCharArray();
            }

            compress(matrix, 0, 0, n);
            System.out.println(compressed);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void compress(char[][] matrix, int row, int col, int size) {
        if (isSingleColor(matrix, row, col, size)) {
            compressed.append(matrix[row][col]);
            return;
        }

        compressed.append('(');
        int newSize = size / 2;
        compress(matrix, row, col, newSize);
        compress(matrix, row, col + newSize, newSize);
        compress(matrix, row + newSize, col, newSize);
        compress(matrix, row + newSize, col + newSize, newSize);
        compressed.append(')');
    }

    public static boolean isSingleColor(char[][] matrix, int row, int col, int size) {
        char color = matrix[row][col];
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (matrix[i][j] != color) {
                    return false;
                }
            }
        }
        return true;
    }
}

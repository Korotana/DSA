public void toh(int N, int from, int to, int aux) {
        // Your code here

        if (N == 0){
            return;
        }

        toh(N-1, from, aux, to);
        System.out.println("move disk " + N + " from rod "+ from + " to rod "+ to);
        toh(N-1, aux, to, from);

    }
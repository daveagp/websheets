description = r"""
"""

imports = ["java.util.concurrent.RecursiveAction;",
"java.util.concurrent.ForkJoinPool;"]

source_code = r"""
   public static void main(String[] args) {
      int SIZE = 2_000_000;
      int[] list = new int[SIZE];
        
      for (int i = 0; i < SIZE; i++)
         list[i] = (int)(Math.random() * Integer.MAX_VALUE);

      int maxProc = Runtime.getRuntime().availableProcessors();

      // timing[i] : time to sort on i processors
      long[] timing = new long[maxProc+1];

      for (int i=1; i<=maxProc; i++)
        timing[i] = parallelMergeSort((int[])list.clone(), i);
 
      for (int i=2; i<=maxProc; i++)
         if (timing[i] > timing[i-1])
           throw new RuntimeException("More processors should make it faster!");
    }
    
    public static long parallelMergeSort(int[] list, int proc) {
       long startTime = System.currentTimeMillis();

       ForkJoinPool pool = new ForkJoinPool(proc);
       pool.invoke(new SortTask(list));
       pool.shutdown();
       while (!pool.isTerminated()) Thread.yield();

       long time = System.currentTimeMillis() - startTime;
       System.out.println("Time with "+proc+" processors is "+time+" ms");
       return time;
    }  
    
    private static class SortTask extends RecursiveAction {
       private int[] list;
       SortTask(int[] list) { this.list = list; }
        
       @Override
       protected void compute() {
          if (list.length < 2) return; // base case

          // split into halves  
          int[] firstHalf = new int[list.length / 2];
          System.arraycopy(list, 0, firstHalf, 0, list.length / 2);
          int secondHalfLength = list.length - list.length / 2;
          int[] secondHalf = new int[secondHalfLength];
          System.arraycopy(list, list.length / 2, secondHalf, 0, secondHalfLength);
                
          // recursively sort the two halves
\[
          invokeAll(new SortTask(firstHalf),
                    new SortTask(secondHalf));
]\\default[
          new SortTask(firstHalf).invoke();
          new SortTask(secondHalf).invoke();
]\
          // merge halves together
          merge(firstHalf, secondHalf, list);
      }
   }

   public static void merge(int[] list1, int[] list2, int[] merged) {
      int i1 = 0, i2 = 0, i3 = 0; // index in list1, list2, out
        
      while (i1 < list1.length && i2 < list2.length) 
         merged[i3++] = (list1[i1] < list2[i2]) ? list1[i1++] : list2[i2++];
      
      // any trailing ends        
      while (i1 < list1.length) merged[i3++] = list1[i1++];
      while (i2 < list2.length) merged[i3++] = list2[i2++];
   }
"""

tests = r"""
dontRunReference = true;
testMain();
"""

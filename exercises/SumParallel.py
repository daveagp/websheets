description = r"""
Correct the following program so that it correctly adds up
all of the numbers from 1 to <tt>n</tt>, where <tt>n</tt> is its command-line argument. 
E.g., <tt>java Example1 100</tt> should print <tt>5050</tt>.
<p>
You will have to fix two separate problems.
"""

imports = ["java.util.concurrent.*",
           "java.util.concurrent.locks.*"]

source_code = r"""
   // utility function
   static void nap(int ms) {
      try {Thread.sleep(ms);} 
      catch (InterruptedException ie) 
       {System.out.println("!");} 
   }
    
   static int total;

\[
   static Lock lock = new ReentrantLock();
]\\default[   ; // more variables? 
]\

   // a class that adds a number to total
   static class AdderRunnable implements Runnable {
      int increment;
      AdderRunnable(int increment) {this.increment = increment;}
      public void run() {
\[
         // do nothing here
]\\default[
;// maybe do something here?
]\
         // introduce some delays 
         nap(15); 
\[
         lock.lock();
]\\default[
;// maybe do something here?
]\
         total += increment; 
\[
         lock.unlock();
]\\default[
;// maybe do something here?
]\
      }
   };        

   public static void main(String[] args) {
      total = 0;        

      int n = Integer.parseInt(args[0]);
        
      // keep track of all the things we execute
      ExecutorService pool = Executors.newCachedThreadPool();
        
      for (int i=1; i<=n; i++)
         pool.execute(new AdderRunnable(i));

\[
      pool.shutdown();
      while (!pool.isTerminated()) 
         Thread.yield();
]\\default[
         pool.shutdown();
]\
      System.out.println(total);
   }
"""

tests = r"""
testMain(100);
testMain(1000);
"""

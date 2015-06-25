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
public class SumParallel {

   // utility function
   static void nap(int limit_ms) {
      try {Thread.sleep((int)(limit_ms*Math.random()));} 
      catch (InterruptedException ie) 
       {System.out.println("!");} 
   }
    
   static int total;

\[
      static Lock lock = new ReentrantLock();
\show:
   ; // more variables? 
]\

   // a class that adds a number to total
   static class AdderRunnable implements Runnable {
      int increment;
      AdderRunnable(int increment) {this.increment = increment;}
      public void run() {
\[
         // do nothing here
\show:
;// maybe do something here?
]\         
         nap(10); // random delay up to 10ms
\[
         lock.lock();
\show:
;// maybe do something here?
]\
         {
            // increase total by increment
            int oldTotal = total;
            nap(2); // random delay up to 2ms
            total = oldTotal + increment;
         }
\[
         lock.unlock();
\show:
;// maybe do something here?
]\
      }
   };        

   public static void main(String[] args) {
      total = 0;        

      int n = Integer.parseInt(args[0]);
        
      // keep track of all the things we execute
      // & impose limit b/c using many threads at makes memory run out
      ExecutorService pool = Executors.newFixedThreadPool(23);
  
      for (int i=1; i<=n; i++)
         pool.execute(new AdderRunnable(i));

\[
      pool.shutdown();               // ask to shut down
      while (!pool.isTerminated()) 
         Thread.yield();             // wait until shutdown complete
\show:
      pool.shutdown();               // ask to shut down
]\
      System.out.println(total);
   }
}
"""

tests = r"""
testMain(100);
testMain(1000);
"""

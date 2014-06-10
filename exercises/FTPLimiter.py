description = r"""
You would like to download some files from an FTP site. You want to download 100 files called 
<tt>file0.zip</tt>, <tt>file1.zip</tt>, ..., <tt>file99.zip</tt>. Assume that the <tt>static</tt> 
method 
<pre>FTP.get(String filename)</pre>
has been defined for you, and that it tells your FTP client to download that named file from
the server.
<p>
<i>However,</i> because you are downloading so many files, it will take a long time. You
would like to speed this up by downloading multiple files at once. The FTP site allows
<b>up to 5 simultaneous downloads at once</b>. If you try to download more than 5 at once,
your account will be banned.
<p>Use a <tt>Semaphore</tt> to download all of the files as quickly as possible while
never downloading more than 5 at once.
"""

source_code = r"""
public class FTPLimiter {
\hide[
    public static class FTP {
        static int maxload = 0;
        static int connections = 0;
        static int successes = 0;
        static int left = 0;
        static Stopwatch w;
        static int[] counts = new int[100];
        static int totalTime = 0;
        static boolean errored = false;
        static void init() {w = new Stopwatch();}
        static String err = null;
        static synchronized void error(String msg) {
           if (err == null) err = msg;
           errored = true;
        }
        public static void get(String filename) {
            left++;
            if (!(filename.startsWith("file") || filename.endsWith(".zip")))
               error("File not on server: " + filename);
            String c = filename.substring(4, filename.length()-4);
            if (!(c.length()==1 || c.length()==2))
               error("File not on server: " + filename);
            for (char ch:c.toCharArray()) if (ch < '0' || ch > '9')
               error("File not on server: " + filename);
            if (c.charAt(0)=='0' && c.length()==2)
               error("File not on server: " + filename);
            if (errored) return;
            int index = Integer.parseInt(c);
            synchronized (FTP.class) {
                connections++;
                maxload = Math.max(maxload, connections);
                System.out.println("Getting "+filename+"...");
                if (connections > 5) {error("More than 5 connections!"); return;}
                if (counts[index] > 0) {error("Tried to download " + filename + " twice!"); return;}
                counts[index] = 1;
            }
            int i = index;
            int time = 5 + (i*67)%39;
            try {Thread.sleep(time);} catch (InterruptedException e) {error("interrupt!");}
            synchronized (FTP.class) {successes++;
                totalTime += time;
                System.out.println("... finished downloading "+filename+" ("+time+" ms)!");
                connections--;
            }
            if (successes == 100) {
           double elapsed = w.elapsedTime();
           System.out.println("Elapsed real time: " + elapsed + " seconds");
           double load = totalTime/elapsed/1000;
           System.out.printf("Cumulative download time %d ms, average load %.3f\n", totalTime, load);
           if (load <= 4) error("Average load should be greater than 4.");
}
                left--;
        }
        static void done() {
           while (!errored && left > 0) Thread.yield();
           if (successes < 100) error("Did not download all files.");
           if (errored) {throw new framework.GenericTester.FailException(err);}
        }
    }
]\\[
static Semaphore semaphore = new Semaphore(5);
static class GetThread extends Thread {
   String filename;
   GetThread(String filename) {
      this.filename = filename;
   }
   public void run() {
      semaphore.acquireUninterruptibly();
      try {
         FTP.get(filename);
      } finally {
         semaphore.release();
      }
   }
}
]\
\default[;// extra classes, instance variables...?
]\
public static void main(String[] args) {\hide[ FTP.init(); ]\
\[
   for (int i=0; i<100; i++) 
      new GetThread("file"+i+".zip").start();
]\
\hide[ FTP.done(); ]\}
}
"""
tests = r"""
dontRunReference = true;
testMain();
""" 
imports = ["java.util.concurrent.Semaphore" ]


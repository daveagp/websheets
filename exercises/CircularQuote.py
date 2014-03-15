source_code=r"""
public class CircularQuote {

   // the first card in the circular linked list
   private Card start;

   // helper linked-list data type
   private class Card {
      private String word;
      private Card next;

      public Card(String word) {
         this.word = word;
         this.next = null;
      }
   }
   
   // constructor - create an empty quote
   public CircularQuote() {
     \[ start = null; ]\ // no card intitially
   }
   
   // add the word w to the end of the quote
   public void addWord(String w) {
       Card newCard = \[new Card(w);]\

       // degenerate case for empty quote, w is the first word
       if (\[start == null]\) {
         \[start = newCard;]\ // save the card with the new word
          start.next = start; // make it circular
       } 

       // otherwise, traverse list until card points to last word
       else {
          // find the current last word
          Card card = start;
          do {
            \[card = card.next;]\
          } while (\[card.next != start]\);

          // insert new word
\[
          newCard.next = start;
          card.next = newCard;
]\
       } 
   }
   
   // string representation of the entire quote
   public String toString(){
      String result = "";
      if (start == null) // special case
         return result;

      Card card = start;
      do {
         result = result + card.word + " "; // build string
         card = card.next; // traverse list
      } while (card != start);
      return result;

      // note! using a plain while loop would normally require separate
      // logic for the 1-node and the (>1)-node case
   }

   // number of words in the quote
   public int count() {
\[
      // empty quote
      if (start == null) return 0;

      Card card = start;
      int total = 0;
      do {
         total++;
         card = card.next;
      } while (card != start);
      return total;
]\
   }

    // the kth word in the quote (where k = 1 is the first word)
    public String circularGetKth(int k) {
       Card card = start;
       for (int j = 1; j < k; j++) {
          card = card.next;
       }
       return card.word;
    }

   // test client
   public static void main(String[] args) { 
      CircularQuote q = new CircularQuote();
      StdOut.println(q.count() + ": " + q);

      q.addWord("A");
      StdOut.println(q.count() + ": " + q);

      q.addWord("rose");
      StdOut.println(q.count() + ": " + q);
      StdOut.println("Second word: " + q.circularGetKth(2)); // rose

      q.addWord("is");
      StdOut.println(q.count() + ": " + q);
      StdOut.println("Tenth word: " + q.circularGetKth(10)); // A

      q.addWord("a");
      StdOut.println(q.count() + ": " + q);
      StdOut.println("Seventh word: " + q.circularGetKth(7)); // is

      q.addWord("rose.");
      StdOut.println(q.count() + ": " + q);
      StdOut.println("First word: " + q.circularGetKth(1)); // A
   }
}
"""


description = r"""
<i>Booksite web exercise 4.3.2</i> Write a class <tt>CircularQuote</tt> that mimics 
the <tt>Quote</tt> class, but uses a circularly-linked list instead
of a null-terminated linked list. Its API will be:
<pre>
public CircularQuote()              // constructor - create an empty quote
public void addWord(String w)       // add the word w to the end of the quote
public String toString()            // string representation of the quote
public int count()                  // number of words in the quote
public String circularGetKth(int k) // the kth word in the quote (k=1 is first
                                    // word. loops around if needed)
</pre>
This exercise will give you practice with <tt>do {} while ()</tt> loops.
One such example loop, in the <tt>toString()</tt> method, is already completed for you.
Use it again in the constructor and in <tt>count()</tt>.
"""

tests = r"""
testMain();
"""

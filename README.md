# LPTHW3
The exercises in the Learn the Python the Hard Way 3.

These project contains all the exercises from the **“Learn Python the Hard Way 3”**. Before, I start to code in Python. I knew that Python is called **“executable pseudo code”**. 

Python is a such elegant programming language. Compare to the other language like Java and C, it fits the need of fast prototyping and its science libraries are so helpful for machine learning usage.

So if you want to learn Machine Learning, <u>you must learn to code in **Python**</u>.

And this book is the best Python 3 book in my opinion. It emphasis on the basics and  it is different from most of the Python introduction books on the market, the author *Zed Shaw* believes that to learn code you must keep practice.

Study the code example in the books is not equal to type it into the real program. Only when you run the program in your computer, you will begin to learn how to code correctly.

---

I’d like to list some code snippets I implemented to complete the exercises in the book.

1. Check the input string if it contains characters other than digits:

   ```python
   numbers = "0123456789"
   choice = input("> ")
   
   if all(i in numbers for i in choice): # any() and all() take iterables and return True if any and all of the elements are True.
       how_much = int(choice)
   else:
   	dead("Man, learn to type a number.")
   ```

2. The Print function in Python is much more easier to use than Java

   ```python
   number_of_cat = 20
   print(f"The number of cat is: {number of cat}")
   ```

   In Java to print the message to the terminal needs a bit more works:

   ```java
   public class PrintTest{
     public static void main(String[] args){
        int number_of_cat = 20;
        System.out.println("The number of cat is " + number_of_cat);
     }  
   }
   ```

---

Besides, I will post some learning notes in this repository, which will save you a lot of to take notes yourself. 

For example,

>## Switches, Conventions, and Encodings
>
>1. Computer store the data using bits: 0 or 1.
>2. Byte contains a sequence of 8 bits.
>3. Convert the bytes to the text by encoding, which is a kind of mapping from the number to the letters.
>   And the most important one is ASCII.
>4. But the ASCII has one problem is that it only encodes English.
>5. Unicode: you can use the 32 bits number to encode a Unicode character.
>6. But there are lots of white spaces wasted. So we use utf-8 and which make the character represented by the 8 bits and then escaped    out into 16 or 32 bits as needed.
>7. utf-8:  Unicode Transformation Format 8 Bits.
>8. b'' to tell Python this is ”bytes”.
>9. In Python a string is a UTF-8 encoded sequence of characters for displaying or working with text.
>10. Use .decode() to get the string from the raw bytes.
>11. Use .encode() to get the bytes from the string.
>12. "DBES": Decode Bytes Encode String.

So keep practice, if you encounter some problems, you can check the codes in this repository. 

Feel free to contact with me. And let’ s learn Python together. 
import java.io.*;
import java.util.*;
public class NpowK
{
  public static void main(String args[])
  {
 Scanner s=new Scanner(System.in);
  System.out.println("Enter the base and power");
  int n=s.nextInt();
  int k=s.nextInt();
  System.out.println(n^k);
  }
}

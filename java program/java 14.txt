import java.util.*;
public class Fourteen{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
System.out.println("Enter a number to check it is divisible by 3 and 5:");
int a=sc.nextInt();
if(a%5==0 && a%3==0){
System.out.println("divisible by 3 and 5");
}
else if(a%5==0){
System.out.println("Divisible by 5");
}
else if (a%3==0){
System.out.println("Divisible by 3");
}
else{
System.out.println("Not divisible by 3 and 5");
}
}
}
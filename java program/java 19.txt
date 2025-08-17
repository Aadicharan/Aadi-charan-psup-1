import java.util.*;
public class Nineteen{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
System.out.println("enter a number between 1 to 3");
int a=sc.nextInt();
switch(a){
           case 1:
                  System.out.println("petrol");
                  break;
           case 2:
                  System.out.println("Diesel");
                  break;
            case 3:
                  System.out.println("Electric");
                  break;
            default:
                  System.out.println("Invalid");
  }
}
}
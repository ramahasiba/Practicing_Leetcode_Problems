import java.util.Scanner;
import java.util.Stack;
class Solution 
{
    public int calculate(String expression)  { 

        Stack<Integer> numStack = new Stack<>();
    
        expression = expression.replace(" ", ""); 

        int expressionLength = expression.length();
        int curr=0; 
        char operation = '+'; 

        int finalResult = 0;
        
        for (int i=0; i<expressionLength; i++){
            char currChar = expression.charAt(i);  
            if(Character.isDigit(currChar)){
                curr = curr * 10 + ((int)currChar - (int)'0'); //subtract ascii values to convert char to int
            }
            if(!Character.isDigit(currChar) || i == expressionLength - 1){
                switch (operation) {
                    case '+': 
                        numStack.push(curr); 
                        break;
                    case '-':
                        numStack.push(-curr);
                        break;
                    case '*':
                        curr = curr * numStack.pop();
                        numStack.push(curr);
                        break;
                    case '/':
                        curr=numStack.pop()/curr;
                        numStack.push(curr);
                        break;
                    default:
                        System.out.println("Invalid expression, please enter a valid one. e.g: 55 * 6 + 9.");
                        break; 
                }  
                operation = currChar; 
                System.out.println("index: " + i);

                curr = 0;
            } 
        }
         
        while(!numStack.isEmpty()){
            finalResult += numStack.pop();
        }

        return finalResult;
        
    }

}
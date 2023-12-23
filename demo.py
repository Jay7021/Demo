from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


information = """
package javabasics;
import java.util.*;


class CalculatorSimulation{
	private double num1;
    private double num2;

    public double getNum1() {
        return num1;
    }

    public void setNum1(double num1) {
        this.num1 = num1;
    }

    public double getNum2() {
        return num2;
    }

    public void setNum2(double num2) {
        this.num2 = num2;
    }

    public double add() {
        return num1 + num2;
    }

    public double subtract() {
        return num1 - num2;
    }
    
    public double multiply() {
    	return num1*num2;
    }

    public double divide() {
        if (num2 != 0) {
            return num1 / num2;
        } else {
            System.out.println("Error: Cannot divide by zero.");
            return Double.NaN; // Return Not-a-Number for an undefined result
        }
    }



}



public class test {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);

        System.out.println("Simple Calculator Simulation");
        System.out.println("----------------------------");

        CalculatorSimulation calculator = new CalculatorSimulation();

        System.out.print("Enter the first number: ");
        calculator.setNum1(scanner.nextDouble());

        System.out.print("Enter the second number: ");
        calculator.setNum2(scanner.nextDouble());

        System.out.println("Select operation:");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Divide");
        System.out.println("4. Multiply");

        System.out.print("Enter choice (1-4): ");
        int choice = scanner.nextInt();

        double result = 0;

        switch (choice) {
            case 1:
                result = calculator.add();
                break;
            case 2:
                result = calculator.subtract();
                break;
            case 3:
                result = calculator.divide();
                break;
            case 4:
                result = calculator.multiply();
                break;
            default:
                System.out.println("Invalid choice. Please enter a number between 1 and 3.");
                return;
        }

        System.out.println("Result: " + result);
	}

}
"""


if __name__ == '__main__':
    print("Hello LangChain")

    
    
    summary_template = """
    given the information {information} about a java code from I want you to create:
    the documentaion of the code in the code itself
    """

    summary_prompt_templpate = PromptTemplate(
        input_variables = ["information"], template = summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name ="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_templpate)

    print(chain.run(information = information))

    
    

using System;

public class PythonInterop
    {
        public static void Initialize()
        {
            string pythonDll = @"C:\Users\YourUserNameHere\AppData\Local\Programs\Python\Python38\python38.dll";
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
            PythonEngine.Initialize();
        }

        public static void RunPythonCode(string pycode)
        {
            Initialize();
            using (Py.GIL())
            {
                PythonEngine.RunSimpleString(pycode);
            }
        }

        public static void RunPythonCode(string pycode, object parameter, string parameterName) {
            Initialize();
            using (Py.GIL())
            {
                using (PyScope scope = Py.CreateScope())
                {
                    scope.Set(parameterName, parameter.ToPython());
                    scope.Exec(pycode);
                }

            }
        }

        public static object RunPythonCodeAndReturn(string pycode, object parameter, string parameterName, string returnedVariableName) {
            object returnedVariable = new object();
            Initialize();
            using (Py.GIL())
            {
                using (PyScope scope = Py.CreateScope())
                {
                    scope.Set(parameterName, parameter.ToPython());
                    scope.Exec(pycode);
                    returnedVariable=scope.Get<object>(returnedVariableName);
                }
            }
            return returnedVariable;
        }

    }


public class Program
{
    public static void Main()
    {
        // Example Python code to calculate factorial
        string pythonCode = @"
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
";

        // Call RunPythonCodeAndReturn to execute the Python code
        object result = PythonInterop.RunPythonCodeAndReturn(pythonCode, null, null, "result");

        // Print the result
        Console.WriteLine($"Factorial of 5 is: {result}");
    }
}
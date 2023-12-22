using System.Diagnostics;

namespace helper
{
    public static class Funcoes
    {
        public static List<string> CarregaMaterias()
        {
            var list = new List<string>();

            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Biologia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Filosofia");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Física");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("Geografia");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("História");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Inglês");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Língua Portuguesa");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Literatura");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Matemática");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Química");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");
            list.Add("Sociologia");

            return list;
        }
        public static List<string> CarregaGabarito()
        {
            var list = new List<string>();

            list.Add("A");
            list.Add("D");
            list.Add("C");
            list.Add("C");
            list.Add("D");
            list.Add("B");
            list.Add("D");
            list.Add("A");
            list.Add("B");
            list.Add("D");
            list.Add("A");
            list.Add("D");
            list.Add("A");
            list.Add("C");
            list.Add("A");
            list.Add("C");
            list.Add("B");
            list.Add("C");
            list.Add("D");
            list.Add("B");
            list.Add("C");
            list.Add("B");
            list.Add("C");
            list.Add("B");
            list.Add("B");
            list.Add("B");
            list.Add("D");
            list.Add("A");
            list.Add("D");
            list.Add("C");
            list.Add("B");
            list.Add("C");
            list.Add("C");
            list.Add("C");
            list.Add("B");
            list.Add("B");
            list.Add("C");
            list.Add("A");
            list.Add("D");
            list.Add("B");
            list.Add("C");
            list.Add("A");
            list.Add("C");
            list.Add("D");
            list.Add("A");
            list.Add("C");
            list.Add("A");
            list.Add("D");
            list.Add("B");
            list.Add("D");
            list.Add("B");
            list.Add("B");
            list.Add("D");
            list.Add("C");
            list.Add("D");
            list.Add("C");
            list.Add("B");
            list.Add("A");
            list.Add("C");
            list.Add("C");
            list.Add("D");
            list.Add("A");
            list.Add("B");
            list.Add("B");
            list.Add("A");
            list.Add("D");
            list.Add("A");
            list.Add("D");
            list.Add("B");
            list.Add("D");
            list.Add("C");
            list.Add("B");
            list.Add("C");
            list.Add("C");
            list.Add("C");
            list.Add("A");
            list.Add("B");
            list.Add("A");
            list.Add("C");
            list.Add("D");
            list.Add("D");
            list.Add("C");
            list.Add("A");
            list.Add("D");
            list.Add("C");
            list.Add("C");
            list.Add("C");
            list.Add("B");

            return list;
        }
        public static bool Executa(string command, string file)
        {
            bool result = false;

            try
            {
                // Set up the process start information
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = command,
                    Arguments = file,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                // Start the process
                using (Process process = new Process { StartInfo = psi })
                {
                    process.Start();

                    // Read the output and error streams
                    string output = process.StandardOutput.ReadToEnd();
                    string error = process.StandardError.ReadToEnd();

                    process.WaitForExit();

                    // Display output and error
                    Console.WriteLine("Output:");
                    Console.WriteLine(output);

                    // Check the exit code
                    int exitCode = process.ExitCode;
                    Console.WriteLine($"Exit Code: {(exitCode == 0 ? "Success" : exitCode.ToString())}");

                    if (exitCode != 0)
                    {
                        Console.WriteLine("Error: The Python script did not run successfully.");
                        result = false;
                    }
                    else
                    {
                        result = true;
                    }
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            return result;
        }
    }
}

using System;
using System.Diagnostics;

namespace kill
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var process in Process.GetProcessesByName(args[0]))
            {
                Console.WriteLine("killing {0} {1}", process.ProcessName, process.Id);
                process.Kill();
            }
        }
    }
}

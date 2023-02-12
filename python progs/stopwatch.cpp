/* Command given to ChatGPT ChatGPT (chat generative pre-trained transformer)...
write a stopwatch program for a computer 
*/

#include <iostream>
#include <chrono>


int main()
{
    std::cout << "Press any key to start the stopwatch.\n";
    std::cin.get();
    auto startTime = std::chrono::steady_clock::now();

    std::cout << "Press any key to stop the stopwatch.\n";
    std::cin.get();
    auto endTime = std::chrono::steady_clock::now();

    auto elapsedTime = endTime - startTime;
    auto elapsedTimeInSeconds = std::chrono::duration_cast<std::chrono::seconds>(elapsedTime).count();

    std::cout << "Elapsed time: " << elapsedTimeInSeconds << " seconds\n";

    return 0;
}

/*
This is a c++ program use g++ compiler...

$ g++ stopwatch.cpp -o stopwatch

$ ./stopwatch
Press any key to start the stopwatch.

Press any key to stop the stopwatch.

Elapsed time: 4 seconds

*/

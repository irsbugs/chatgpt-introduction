/* write a clock computer program */

#include <iostream>
#include <ctime>
#include <string>

using namespace std;

int main(){
    // Get the current time
    time_t now = time(0);
    tm* ltm = localtime(&now);

    // Output the current time
    cout << "The current time is " << ltm->tm_hour << ":";
    cout << ltm->tm_min << ":" << ltm->tm_sec << endl;

    return 0;
}

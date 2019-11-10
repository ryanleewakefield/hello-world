#include <iostream>
#include <string>
#include <vector>
using namespace std;

void star_tree(int rows)
{
    vector<string> table;

    int index, spaces, stars, og_spaces;
    string star_line;
    index = rows;

    while (rows != 0)
        {
        stars = (rows * 2) - 1;
        star_line = " ";
        if (index != rows)
            {
            spaces = (index - rows) * 2;
            og_spaces = spaces;
            do
                {
                star_line = star_line + " ";
                spaces -= 1;
                }
                while (2 * spaces > og_spaces);
            for (int i = 1; i <= stars; i++)
                star_line = star_line + "*";
            for (int i = 1; i <= spaces; i++)
                star_line = star_line + " ";
            star_line.erase(0,1);
            table.push_back(star_line);
            rows -= 1;
            }
        else
            {
            for(int i = 1; i <= stars; i++)
            star_line = star_line + "*";
            star_line.erase(0,1);
            table.push_back(star_line);
            rows -= 1;
            }
        }
    for (int i = index - 1; i >= 0; i--)
        cout << table.at(i) << endl;





}
int main()
{
    int choice;
    cout <<"*****************\n"
         <<"Make a Star Tree!\n"
         <<"*****************\n\n";
    cout << "How tall should the tree be? (Enter an integer): ";
    cin >> choice;
    while (choice < 0)
    {
        cout << "\n\nError: Please enter a valid number: ";
        cin.ignore();
        cin.clear();
        cin >> choice;

    }
    star_tree(choice);


    return 0;
}

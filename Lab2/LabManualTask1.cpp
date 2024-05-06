#include<bits/stdc++.h>
using namespace std;
string decoder(string cipher,int key)
{
    for(int i = 0; i < cipher.size(); i++)
    {
        cipher[i] = (cipher[i]-'a'-key+26)%26+'a';
    }
    return cipher;
}
int main(){
    string cipher;
    cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo";
    cout << "Cipher Code is: " << cipher << endl;
    for(int i=1; i<26 ;i++){
        cout<<"Key = "<<i<<" Decoded Text - "<<decoder(cipher,i)<<endl;
    }
    // Here key 10 will give the correct plain text
    string plainText = decoder(cipher,10);
    cout<<"Decoded Text - "<<plainText<<endl;
    return 0;
}

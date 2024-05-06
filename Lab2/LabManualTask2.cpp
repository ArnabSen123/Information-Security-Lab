#include<bits/stdc++.h>
using namespace std;

bool cmp(pair<char,double>x,pair<char,double>y){
    return x.second>=y.second;
}

int main(){
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    vector<string>cipherArray;
    string cipher;
    map<char,int>freq;

    vector<int>v;

    int count = 0;
    while(getline(cin,cipher)){
        for(int i = 0; i < cipher.size(); i++){
            char c = cipher[i];
            if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')){
                count++;
                freq[tolower(cipher[i])]++;
            }

        }
        cipherArray.push_back(cipher);
    }
    vector<pair<char,double>>cipherFreq,plainFreq;
    cout<<"cipher letter Frequency----------"<<endl;
    for(auto it : freq){
        cout<<it.first<<"  "<<double((it.second*100.00)/count)<<setprecision(2)<<fixed<<" %"<<endl;
        cipherFreq.push_back({it.first,double((it.second*100.00)/count)});
    }
    map<char, double> freqDist = {
        {'a', 8.05},
        {'b', 1.67},
        {'c', 2.23},
        {'d', 5.1},
        {'e', 12.22},
        {'f', 2.14},
        {'g', 2.3},
        {'h', 6.62},
        {'i', 6.28},
        {'j', 0.19},
        {'k', 0.95},
        {'l', 4.08},
        {'m', 2.33},
        {'n', 6.95},
        {'o', 7.63},
        {'p', 1.66},
        {'q', 0.06},
        {'r', 5.29},
        {'s', 6.02},
        {'t', 9.67},
        {'u', 2.92},
        {'v', 0.82},
        {'w', 2.6},
        {'x', 0.11},
        {'y', 2.04},
        {'z', 0.06}
    };
    cout<<"plain letter Frequency ----------"<<endl;
    for(auto it : freqDist){
        cout<<it.first<<"  "<<it.second<<setprecision(2)<<fixed<<" %"<<endl;
        plainFreq.push_back({it.first,it.second});
    }
    sort(plainFreq.begin(),plainFreq.end(),cmp);
    sort(cipherFreq.begin(),cipherFreq.end(),cmp);

    cout<<"frequency compare ----------"<<endl;

    for(int i = 0; i < 26; i++){
       cout<< cipherFreq[i].first<<" ->  "<<plainFreq[i].first<<endl;
    }
    map<char, char> sub = {
        {cipherFreq[0].first, plainFreq[0].first},
        {cipherFreq[1].first, plainFreq[1].first},
        {cipherFreq[2].first, plainFreq[2].first},
        {cipherFreq[3].first, plainFreq[3].first},
        {cipherFreq[4].first, plainFreq[4].first},
        {cipherFreq[5].first, plainFreq[5].first},
        {cipherFreq[6].first, plainFreq[6].first},
        {cipherFreq[7].first, plainFreq[7].first},
        {cipherFreq[8].first, plainFreq[8].first},
        {cipherFreq[9].first, plainFreq[9].first},
        {cipherFreq[10].first, plainFreq[10].first},
        {cipherFreq[11].first, plainFreq[11].first},
        {cipherFreq[12].first, plainFreq[12].first},
        {cipherFreq[13].first, plainFreq[13].first},
        {cipherFreq[14].first, plainFreq[14].first},
        {cipherFreq[15].first, plainFreq[15].first},
        {cipherFreq[16].first, plainFreq[16].first},
        {cipherFreq[17].first, plainFreq[17].first},
        {cipherFreq[18].first, plainFreq[18].first},
        {cipherFreq[19].first, plainFreq[19].first},
        {cipherFreq[20].first, plainFreq[20].first},
        {cipherFreq[21].first, plainFreq[21].first},
        {cipherFreq[22].first, plainFreq[22].first},
        {cipherFreq[23].first, plainFreq[23].first},
        {cipherFreq[24].first, plainFreq[24].first},
        {cipherFreq[25].first, plainFreq[25].first}
    };
    for(int i = 0; i < 26; i++){
        char c = char('a'+i);
        if(sub.find(c)!=sub.end()){
            cout<<"mapped - "<<char('a'+i)<<" -> "<<sub[char('a'+i)]<<endl;
        }
    }

    cout<<"--------- Decoding ----------"<<endl;
    for(int k = 0 ; k < cipherArray.size() ; k++){
        cipher = cipherArray[k];
        for(int i = 0; i < cipher.size(); i++){
            char c = cipher[i];
            if (sub.find(tolower(c))!=sub.end()){
                cipher[i] = (sub[tolower(c)]);
            }
        }
        cout<<cipher<<endl;
    }

}

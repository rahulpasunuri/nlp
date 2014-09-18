#include<iostream>
#include<fstream>
#include<exception>
#include<cmath>
using namespace std;


int main()
{
	fstream inp;
	try
	{
		inp.open("inp1.txt",ios::in); //open file only for reading purposes.
	}
	catch(...)
	{
		cout<<"Some error happened in opening the file"<<endl;
		return 0;
	}
	
	int charCount[26]={}; //initialize all elements of array to zero.
	float charProb[26]={};
	char c;
	int ascii;
	int totalCount=0;	
	while(inp)
	{
		inp.get(c);
		ascii=(int)c;
		if((ascii>=65&&ascii<=90)||(ascii>=97&&ascii<=122))
		{
			//character must be in english alphabets
			if(ascii>=97)
			{
				ascii=ascii-32;				
			}
			charCount[ascii-65]++;
			totalCount++;
		}
	}
	inp.close();
	if(totalCount==0)
	{
		cout<<"File doesnot have any alphabets\n";
		return 0;
	}
		
	//print counts of every literal
	cout<<"Printing Count for each Alphabet\n";
	for(int i=0;i<26;i++)
	{
		cout<<((char)(i+65))<<" - "<<charCount[i]<<"\n";
	}
	cout<<"---------------------------------\n";
		
	//calculate the probablity of each character now,,,
	for(int i=0;i<26;i++)
	{
		charProb[i]=charCount[i]/(float)totalCount;
	}	
	
	cout<<"Printing probabilities of each character"<<endl;
	//calculate the probablity of each character now,,,
	for(int i=0;i<26;i++)
	{
        cout<<((char)(i+65))<<" - "<<charProb[i]<<"\n";
	}	
		
	//entropy H(X ) = − sum(p(x) log 2 p(x))
	
	float h=0;
		
	for(int i=0;i<26;i++)
	{
		if(charProb[i]!=0)
		{
			h = h-(charProb[i] * log2f(charProb[i]));		
		}
	}
	cout<<"Entropy is "<<h<<"\n";
	cout<<"Number of Bits required is "<<ceil(h)<<"\n";
	cout<<"---------------------------------\n";
	//let A be 1 and Z =26.
	//lets calculate expected value...
	float expectedValue=0;
	for(int i=0;i<26;i++)
	{
		expectedValue+=(charProb[i]*(i+1));		
	}	
	cout<<"Expected value is "<<expectedValue<<"\n";
	//lets calculate variance now...
	float expectedValueSquared=0;
	for(int i=0;i<26;i++)
	{
		expectedValueSquared+=(charProb[i]*(i+1)*(i+1));		
	}		
	cout<<"Variance is "<<(expectedValueSquared-expectedValue)<<"\n";
		
	return 0;
}

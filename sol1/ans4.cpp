#include<iostream>
#include<fstream>
#include<exception>
#include<cmath>
#include<cstring>
using namespace std;


void getProbabilities(const char* fileName, float (&charProb)[26])
{
	fstream inp;
	try
	{
		inp.open(fileName,ios::in); //open file only for reading purposes.
	}
	catch(...)
	{
		cout<<"Some error happened in opening the file"<<endl;
		return;
	}	
	int charCount[26]={}; //initialize all elements of array to zero.
	char c;
	int ascii;
	int totalCount=0;	
	while(inp.eof()==0)
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

	if(totalCount==0)
	{
		cout<<"File with file name \""<<fileName<<"\" doesnot have any alphabets\n";
		return;
	}
	//calculate the probablity of each character now,,,
	for(int i=0;i<26;i++)
	{
		*(charProb+i)=charCount[i]/(float)totalCount;
		if(*(charProb+i)==0)
		{
			*(charProb+i)=0.0001;
		}
	}	
	cout<<"Printing Probabilities of file - "<<fileName<<"\n";
	for(int i=0;i<26;i++)
	{
		cout<< (char(i+65))<<" - "<<*(charProb+i)<<"\n";
	}
}

int main()
{	
	char fileName1[]="inp1.txt";
	char fileName2[]="inp2.txt";
	float prob1[26]={};
	getProbabilities(fileName1,prob1);
	float prob2[26]={};
	getProbabilities(fileName2,prob2);

	float kl_divergence=0;
	for(int i=0;i<26;i++)
	{
		kl_divergence+= prob1[i]*log(prob1[i]/prob2[i]);
	}
	cout<<"KL divergence D(p||q) "<<kl_divergence<<endl;
	
	kl_divergence=0;
	for(int i=0;i<26;i++)
	{
		kl_divergence+= prob2[i]*log(prob2[i]/prob1[i]);
	}
	cout<<"KL divergence D(q||p) "<<kl_divergence<<endl;	
		
	return 0;
}

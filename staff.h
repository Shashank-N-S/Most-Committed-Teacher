#include<iostream>
#include<fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <iterator> //for std::istream_iterator
#include <vector>
#include <iomanip>
using namespace std;



class staff
{
  int id;// for staff id
  char fName[20];//for student first name
  char lName[20];//for student last name
  char qualification[20];//for Registration No number
  char course1[20];//add course1
  char course2[20];//add course2
  long int mNumber;//for class info
  int pay;//Pay of the Teacher


public:
  void show(){
      //  cout<<"\n";

        cout<<id<<setw(15)<<fName<<setw(15)<<lName<<setw(17)<<pay<<setw(15)<<qualification<<setw(19)<<mNumber<<setw(15)<<course1<<setw(15)<<course2<<endl;
  }

  void get(){
    cout<<"enter id"<<endl;
    cin>>id;
    cout<<"enter fName"<<endl;
    cin>>fName;
    cout<<"enter LastName"<<endl;
    cin>>lName;
    cout<<"enter qualification"<<endl;
    cin>>qualification;
    cout<<"enter mNumber"<<endl;
    cin>>mNumber;
    cout<<"enter PAY"<<endl;
    cin>>pay;
    cout<<"enter course 1"<<endl;
    cin>>course1;
    cout<<"enter course 2"<<endl;
    cin>>course2;
  }


void newStaffRegistration()
{
  int sid;
  fstream file;
  staff s;
  file.open("staffi.dat", ios::in|ios::out|ios::app|ios::binary);
  cout<<"\n\nenter id to check whether it exists: ";
  cin>>sid;
  file.seekg(0,ios::beg);
  int found=0;
  while(file.read((char *) &s, sizeof(s))){
     if(s.id==sid){
         found=1;
         cout<<"\n"<<endl;
         cout<<"this id already exists"<<endl;
     }
  }
  file.clear();
  if(found==0)
    {
      cout<<"this id is unique enter it again\n"<<endl;
      s.get();
      file.write((char*)&s,sizeof(s));

    }
      file.close();

}

void updateStaffInform()
{
  staff s;

int nid;
  fstream file;
  cout<<"\n\nEnter id of teacher for which you want to update it : "<<endl;
  cin>>nid;
  file.open("staffi.dat",ios::ate|ios::out|ios::in|ios::binary);

file.seekg(0);
while(file.read((char *) &s, sizeof(s)))
{

   if(nid==s.id)
   {
     file.seekp(-sizeof(s),ios::cur);
     s.get();
     file.write((char*)&s, sizeof(s));

   }
}
//file.clear();
file.close();

}
void deleteStaffInform()
{
staff s;
int flag;
fstream temp1;
fstream file;
int sid;
temp1.open("temp.dat", ios::out|ios::binary|ios::app);
file.open("staffi.dat", ios::in|ios::binary);
cout<<"\n\nEnter the ID You want to Delete : ";
cin>>sid;
file.seekg(0);
while(1){
  flag=0;
  file.read((char *) &s, sizeof(s));
  if(file.eof()) break;
  if(s.id==sid){
    flag++;
  }
  if(!flag)
        temp1.write((char *) &s, sizeof(s));
}
file.close();
temp1.close();
remove("staffi.dat");
rename("temp.dat","staffi.dat");

}

void listOfStaffs()
{
  fstream file;
  staff s;
  file.open("staffi.dat",ios::in|ios::binary);
  file.seekg(0);
  //cout<<"0";
  cout<<"\n";
  cout<<"S.ID"<<setw(15)<<"F.NAME:"<<setw(15)<<"L.NAME"<<setw(15)<<"PAY"<<setw(20)<<"QUALIFICATION"<<setw(15)<<"M.NUMBER"<<setw(15)<<"COURSE1"<<setw(15)<<"COURSE2"<<endl;
  while(file.read((char*)&s,sizeof(s))){

    s.show();
  }
  file.close();
    }
void Searchstaff(){
  int sid;
  fstream file;
  staff s;
  file.open("staffi.dat", ios::in|ios::binary);
  cout<<"\n\nEnter ID to find teacher : ";
  cin>>sid;
  file.seekg(0,ios::beg);
  int found=0;
  while(file.read((char *) &s, sizeof(s))){
     if(s.id==sid){
         found=1;
         cout<<"\n"<<endl;
         cout<<"S.ID"<<setw(15)<<"F.NAME:"<<setw(15)<<"L.NAME"<<setw(15)<<"PAY"<<setw(20)<<"QUALIFICATION"<<setw(15)<<"M.NUMBER"<<setw(15)<<"COURSE1"<<setw(15)<<"COURSE2"<<endl;
         s.show();
     }
  }
  file.clear();
  if(found==0)
     cout<<"\n\tRecord Not found \n\n";
  //getchar();
  file.close();
}



};

// This script is used to analyse the unpacked TRB data.
// A: Jose Cuenca
// D: 26.03.2019
// L: 27.03.2019
// ----------------------------------------------------
#include <iostream>
#include <fstream>
#include <vector>
#include "TH1F.h"
#include "TFile.h"

using namespace std;

// Main function with arguments. The input file is specified at the execution of the binary:
// ./anahld file

int main(int argc, char **argv) {
if(argc != 2) { return 1;}
char *filename;

  // Input data file
  filename =  argv[1];
  cout << "Processing data file: " << filename << endl; // check the name of the file

  // Variables
  int nLines=0;
  int tempValue;
  int cutHistos=10000;
  vector<int> data;
  
  // Histograms
  TH1F **leadHist;  
  leadHist = new TH1F*[128];
    char title1[250];
    for(Int_t i=0;i<128;i++) {
      sprintf(title1,"%s_%i","LeadTime at channel ",i);
      leadHist[i] = new TH1F(title1,title1,50000,-10000,10000);
    }

  TH1F **fallHist;
  fallHist = new TH1F*[128];
    char title2[250];
    for(Int_t i=0;i<128;i++) {
      sprintf(title2,"%s_%i","FallTime at channel ",i);
      fallHist[i] = new TH1F(title2,title2,50000,-10000,10000);
    }
 
  TH1F **difHist;
  difHist = new TH1F*[128];
    char title3[250];
    for(Int_t i=0;i<128;i++) {
      sprintf(title3,"%s_%i","Difference of times at channel ",i);
      difHist[i] = new TH1F(title3,title3,50000,-10000,10000);
    }

  TH1F **leadDifHist;
  leadDifHist = new TH1F*[127];
    char title4[250];
    for(Int_t i=0;i<127;i++) {
      sprintf(title4,"%s_%i","Difference t_{lead, i+1}-t_{lead,i} at channel ",i);
      leadDifHist[i] = new TH1F(title4,title4,50000,-10000,10000);
    }
 
  // I-O files
  fstream inputFile(filename,std::ios_base::in);

  // Open file and store the line in vector
  nLines = count(istreambuf_iterator<char>(inputFile), istreambuf_iterator<char>(), '\n'); // number of lines of the file
  inputFile.clear(); // go back to the top of the file
  inputFile.seekg(0, ios::beg);

  // Loop in lines
  for(Int_t i=0; i<nLines;i++){
    data.clear();
    for(int j=0;j<256;j++){
	  inputFile>> tempValue;
	  data.push_back(tempValue); // lines stored in vector
    }
    
    // Fill histograms using data vector
    for(Int_t k=0; k<128;k++){ if(data[k] !=0)  leadHist[k]->Fill(data[k]);}
    for(Int_t l=128; l<256;l++){ if(data[l] !=0) fallHist[l-128]->Fill(data[l]);}
    for(Int_t m=0; m<128;m++){if((data[m] || data[m+128]) !=0)  difHist[m]->Fill((data[m+128]-data[m]));} // tfall-tlead per channel
    for(Int_t k=0; k<127;k++){ if(data[k] !=0)  leadDifHist[k]->Fill( (data[k+1]-data[k]) );}
    if(data.size() != 256) cout << "Error: the size of the line " << i << " is not 256 " << endl;

  } // end of the loop in lines

  inputFile.close(); // Close data file
  cout << "Data file closed " << endl;


  // Write histograms in outputfile
  TFile *fOut = new TFile(Form("histos_%s.root",filename),"RECREATE");
  
  int cont =0; // counter 
  for(Int_t i=0;i<128;i++){
      if(difHist[i]->GetEntries() > cutHistos){
        difHist[i]->Write();
	cont++;
      }
  }
  for(Int_t i=0;i<127;i++){
    leadDifHist[i]->Write();
  }

fOut->Close(); // Close root file

cout << "Number of relevant histograms " << cont << endl;
cout << "End " << endl;

return 0;

} // end



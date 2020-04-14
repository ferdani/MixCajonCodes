#include "TH1F.h"

void TreePloter_Si_CsI() {
   TFile *f1   = TFile::Open("Silicons_22_run_trial2.root") ;
   TTree *t1   = (TTree*)f1->Get("full_tree");
/*
   TH1F *h0= new TH1F("h0","total",200,0,16000) ;
   TH1F *h1 = new TH1F("h1","total",200,0,16000) ;
   TH1F *h2 = new TH1F("h2","total",200,0,16000) ;
   TH1F *h3 = new TH1F("h3","total",200,0,16000) ;
   TH1F *h4 = new TH1F("h4","total",200,0,16000) ;
   TH1F *h5 = new TH1F("h5","total",200,0,16000) ;
   TH1F *h6 = new TH1F("h6","total",200,0,16000) ;
   TH1F *h7 = new TH1F("h7","total",200,0,16000) ;
   TH1F *h8 = new TH1F("h8","total",200,0,16000) ;
   TH1F *h9 = new TH1F("h9","total",200,0,16000) ;
   TH1F *h10 = new TH1F("h10","total",200,0,16000) ;
   TH1F *h11 = new TH1F("h11","total",200,0,16000) ;
   TH1F *h12= new TH1F("h12","total",200,0,16000) ;
   TH1F *h13 = new TH1F("h1","total",200,0,16000) ;
   TH1F *h14 = new TH1F("h14","total",200,0,16000) ;
   TH1F *h15= new TH1F("h15","total",200,0,16000) ;
   TH1F *h16 = new TH1F("h16","total",200,0,16000) ;
   TH1F *h17= new TH1F("h17","total",200,0,16000) ;
   TH1F *h18= new TH1F("h18","total",200,0,16000) ;
   TH1F *h19= new TH1F("h19","total",200,0,16000) ;
   TH1F *h20= new TH1F("h20","total",200,0,16000) ;
   TH1F *h21= new TH1F("h21","total",200,0,16000) ;
   TH1F *h22 = new TH1F("h22","total",200,0,16000) ;
   TH1F *h23 = new TH1F("h23","total",200,0,16000) ;
  
*/
   
   TH2F *h0d= new TH2F("h0d","total",200,0,16000,200,0,16000 ) ;
   TH2F *h1d = new TH2F("h1d","total",200,0,16000,200,0,16000) ;
   TH2F *h2d = new TH2F("h2d","total",200,0,16000,200,0,16000) ;
   TH2F *h3d = new TH2F("h3d","total",200,0,16000,200,0,16000) ;

   TH2F *h4d = new TH2F("h4d","total",200,0,16000,200,0,16000) ;
   TH2F *h5d = new TH2F("h5d","total",200,0,16000,200,0,16000) ;
   TH2F *h6d = new TH2F("h6d","total",200,0,16000,200,0,16000) ;
   TH2F *h7d = new TH2F("h7d","total",200,0,16000,200,0,16000) ;

   TH2F *h8d = new TH2F("h8d","total",200,0,16000,200,0,16000) ;
   TH2F *h9d = new TH2F("h9d","total",200,0,16000,200,0,16000) ;
   TH2F *h10d = new TH2F("h10d","total",200,0,16000,200,0,16000) ;
   TH2F *h11d= new TH2F("h11d","total",200,0,16000,200,0,16000) ;

   TH2F *h12d= new TH2F("h12d","total",200,0,16000,200,0,16000) ;
   TH2F *h13d= new TH2F("h13d","total",200,0,16000,200,0,16000) ;
   TH2F *h14d = new TH2F("h14d","total",200,0,16000,200,0,16000) ;
   TH2F *h15d= new TH2F("h15d","total",200,0,16000,200,0,16000) ;

   TH2F *h16d = new TH2F("h16d","total",200,0,16000,200,0,16000) ;
   TH2F *h17d= new TH2F("h17d","total",200,0,16000,200,0,16000) ;
   TH2F *h18d= new TH2F("h18d","total",200,0,16000,200,0,16000) ;
   TH2F *h19d= new TH2F("h19d","total",200,0,16000,200,0,16000) ;

   TH2F *h20d= new TH2F("h20d","total",200,0,16000,200,0,16000) ;
   TH2F *h21d= new TH2F("h21d","total",200,0,16000,200,0,16000) ;
   TH2F *h22d = new TH2F("h22d","total",200,0,16000,200,0,16000) ;
   TH2F *h23d = new TH2F("h23d","total",200,0,16000,200,0,16000) ;


   TCanvas *c0 = new TCanvas( "c0", "c0", 1000, 1000 ) ;
   TCanvas *c1 = new TCanvas( "c1", "c1", 1000, 1000 ) ;
   TCanvas *c2 = new TCanvas( "c2", "c2", 1000, 1000 ) ;
   TCanvas *c3 = new TCanvas( "c3", "c3", 1000, 1000 ) ;
   TCanvas *c4 = new TCanvas( "c4", "c4", 1000, 1000 ) ;
   TCanvas *c5 = new TCanvas( "c5", "c5", 1000, 1000 ) ;

   c0->cd() ;
   c0->Divide(2,2) ;
   c0-> cd(1);
   t1-> Draw ("E_Si_H_6_value_b:E_CsI_20_value_b>>h0d","","colz");
   c0-> cd(2);
   t1-> Draw ("E_Si_H_6_value_b:E_CsI_21_value_b>>h1d","","colz");
   c0-> cd(3);
   t1-> Draw ("E_Si_H_6_value_b:E_CsI_22_value_b>>h2d","","colz");
   c0-> cd(4);
   t1-> Draw ("E_Si_H_6_value_b:E_CsI_23_value_b>>h3d","","colz");

   
   c1->cd() ;
   c1->Divide(2,2) ;
   c1-> cd(1);
   t1-> Draw ("E_Si_H_7_value_b:E_CsI_36_value_b>>h4d","","colz");
   c1-> cd(2);
   t1-> Draw ("E_Si_H_7_value_b:E_CsI_37_value_b>>h5d","","colz");
   c1-> cd(3);
   t1-> Draw ("E_Si_H_7_value_b:E_CsI_38_value_b>>h6d","","colz");
   c1-> cd(4);
   t1-> Draw ("E_Si_H_7_value_b:E_CsI_39_value_b>>h7d","","colz");


   c2->cd() ;
   c2->Divide(2,2) ;
   c2-> cd(1);
   t1-> Draw ("E_Si_H_8_value_b:E_CsI_52_value_b>>h8d","","colz");
   c2-> cd(2);
   t1-> Draw ("E_Si_H_8_value_b:E_CsI_53_value_b>>h9d","","colz");
   c2-> cd(3);
   t1-> Draw ("E_Si_H_8_value_b:E_CsI_54_value_b>>h10d","","colz");
   c2-> cd(4);
   t1-> Draw ("E_Si_H_8_value_b:E_CsI_55_value_b>>h11d","","colz");

   c3->cd() ;
   c3->Divide(2,2) ;
   c3-> cd(1);
   t1-> Draw ("E_Si_H_11_value_b:E_CsI_24_value_b>>h12d","","colz");
   c3-> cd(2);
   t1-> Draw ("E_Si_H_11_value_b:E_CsI_25_value_b>>h13d","","colz");
   c3-> cd(3);
   t1-> Draw ("E_Si_H_11_value_b:E_CsI_26_value_b>>h14d","","colz");
   c3-> cd(4);
   t1-> Draw ("E_Si_H_11_value_b:E_CsI_27_value_b>>h15d","","colz");
   
   c4->cd() ;
   c4->Divide(2,2) ;
   c4-> cd(1);
   t1-> Draw ("E_Si_H_12_value_b:E_CsI_40_value_b>>h16d","","colz");
   c4-> cd(2);
   t1-> Draw ("E_Si_H_12_value_b:E_CsI_41_value_b>>h17d","","colz");
   c4-> cd(3);
   t1-> Draw ("E_Si_H_12_value_b:E_CsI_42_value_b>>h18d","","colz");
   c4-> cd(4);
   t1-> Draw ("E_Si_H_12_value_b:E_CsI_43_value_b>>h19d","","colz");

   c5->cd() ;
   c5->Divide(2,2) ;
   c5-> cd(1);
   t1-> Draw ("E_Si_H_13_value_b:E_CsI_56_value_b>>h20d","","colz");
   c5-> cd(2);
   t1-> Draw ("E_Si_H_13_value_b:E_CsI_57_value_b>>h21d","","colz");
   c5-> cd(3);
   t1-> Draw ("E_Si_H_13_value_b:E_CsI_58_value_b>>h22d","","colz");
   c5-> cd(4);
   t1-> Draw ("E_Si_H_13_value_b:E_CsI_59_value_b>>h23d","","colz");

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}

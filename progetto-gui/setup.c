
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 4096

void lanciatore(char* str){
         char* cmdIns = "echo \"[Desktop Entry]\nEncoding=UTF-8\nVersion=1.0\nType=Application\nName=Dutube\nExec=python3 /home/black-jack/05-Script/DuTube/progetto-gui/gui.py\nIcon=/home/black-jack/05-Script/DuTube/ico/Dutube.svg\nTerminal=false\nCategories=GNOME;GTK;Audio;Video;\nComment=By Alessio R\"";

         char* cmdIns2 = " >> ~/.local/share/applications/dutube.desktop";

         //char* copia = "sudo cp ~/Dutube.desktop /usr/share/applications/Dutube.desktop";
 
         char* chmod = "chmod +x ~/.local/share/applications/dutube.desktop";
         char* chmod2 = "chmod +x ~/.local/share/applications/dutube.desktop";
         char* chmod3 = "chmod 664 ~/.local/share/applications/dutube.desktop";
         char* export = "export PATH=$PATH:~/.local/share/applications/dutube.desktop"; 
         char* upd_desk_db = "sudo update-desktop-database";
         //char* upd_desk_db2 = "update-menus"; //non per centos
         /* printf(cmdIns);
         printf(cmdIns2);
         printf(chmod);
         printf(export);
         printf(upd_desk_db); */

         int lenght = strlen(cmdIns) + strlen(cmdIns2);
         char* cmd2 = (char*) malloc(lenght + 1);
         strcpy(cmd2, cmdIns);
         strcat(cmd2, cmdIns2);
         //printf("%s", cmd2);
         system(cmd2);
         system(chmod);
         system(chmod2);
         system(chmod3);
         system(export);
         system(upd_desk_db);
         //system(upd_desk_db2);

         printf("\nLanciatore Installato Con Successo!\n");}



int bashFile(char* bashrcF, char* strCercata){
         //char* bashrcF = "/home/black-jack/.bashrc";
         //char* strCercata = "alias dutube='python3 ~/05-Script/DuTube/progetto-gui/gui.py'";
         char ult_riga[MAX_LINE_LENGTH];
         FILE *fp;
         fp = fopen(bashrcF, "r");
         if(fp == NULL){
            fprintf(stderr, "Errore nell' apertura del file %s\n", bashrcF);
            return -1;}

         while(fgets(ult_riga, MAX_LINE_LENGTH, fp) != NULL){}
         fclose(fp);
         if(strcmp(ult_riga, strCercata) == 0){
            return 1;}
         else{
            return 0;}}


int main(){
   char* str;
   char str1[] = "";
   char* source_upd = "source ~/.bashrc";
   char* bashrc_file = "echo \"alias dutube='python3 ~/05-Script/DuTube/progetto-gui/gui.py'\" >> ~/.bashrc";


   if(bashFile("/home/black-jack/.bashrc", "alias dutube='python3 ~/05-Script/DuTube/progetto-gui/gui.py'\n") == 1){
      printf("\nL' Alias Gia Esiste!\n");}
   else{
      system(bashrc_file);
      system(source_upd);
      printf("\nAlias Aggiunto Con Successo!\n");}
   printf("Verifico se le dipendenze sono gia installate....");

   int status;
   status = system("pip3 --version");
   if(status == 0){
      printf("pip3 è gia installato.\n");
      int res_pathlib = system("pip3 freeze | grep pathlib");
      int res_pytube = system("pip3 freeze | grep pytube");      
      int res_cx_Freeze = system("pip3 freeze | grep cx_Freeze");

      if((res_pathlib != 0) && (res_pytube != 0) && (res_cx_Freeze != 0)){
         system("python3 -m pip install --upgrade pip");
         system("pip3 install pathlib pytube tkinter cx_Freeze");
         system("pip3 install tk");
         system("pip3 install pathlib pytube cx_Freeze");
         system("pip3 install python3-tkinter");
         system("sudo dnf install python3-tk");
         system("sudo dnf install python-tk");
         system("sudo apt-get install python3-tk");
         system("sudo apt-get install python-tk");

         char* str;
         lanciatore(str);

         system("python3 gui.py");}
      else{system("python3 gui.py");}
       }
   else{
      system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py");
      system("python3 get-pip.py");
      char* file = "get-pip.py";
      status = remove(file);
      if(status == 0){
         printf("Il file %s è stato rimosso.\n", file);}
      else{
         printf("Impossibile rimuovere il file %s.\n", file);}

      char* echo = "echo";
      char* alias = " \"alias pip3='~/.pyenv/versions/3.8.6/bin/pip3'\"";
      char* insert = " >> ~/.bashrc && source ~/.bashrc";
      int lenght = strlen(echo) + strlen(alias) + strlen(insert);
      char* cmd = (char*) malloc(lenght + 1);
      strcpy(cmd, echo);
      strcat(cmd, alias);
      strcat(cmd, insert);
      //printf("%s", cmd);
      system(cmd);

      printf("Percorso di pip aggiunto a PATH");
      system("python -m pip install --upgrade pip");
      system("pip install pathlib pytube tkinter cx_Freeze");
      system("pip install tk");
      system("pip install pathlib pytube cx_Freeze");
      system("pip install python3-tkinter");
      system("sudo dnf install python3-tk");
      system("sudo dnf install python-tk");
      system("sudo apt-get install python3-tk");
      system("sudo apt-get install python-tk");

      char* str;
      lanciatore(str);

      system("python3 gui.py");}
   return 0;}
      
      
   

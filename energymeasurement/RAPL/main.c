#include <stdio.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include "rapl.h"
#include <pthread.h> // Include pthread.h for threading support

#define RUNTIME 1

// Global variables to communicate with the thread
int recording_power = 1;
pthread_t power_thread;
//double package_threshold, cpu_threshold, gpu_threshold;
 double package_threshold; 
 //package_threshold = read_config_file();

// Function to stop the power recording thread
void stop_power_recording() {
    recording_power = 0;
    pthread_join(power_thread, NULL); // Wait for the thread to finish
}

// Function to read and record power consumption at regular intervals
void* record_power_data(void* arg) {
    FILE* fp = (FILE*)arg;
    int core = 0;
    int interval_seconds = 10;

    while (recording_power) {
        //package_threshold = read_config_file(); 
        fprintf(fp,"Package , CPU , GPU , DRAM? , Threshold , Actual , Recorded At (timestamp)  \n");
        // Record power data
        rapl_after(fp, core, package_threshold);
        
       // Get the current time with microsecond precision
        struct timeval tv;
        gettimeofday(&tv, NULL);

        // Extract individual time components
        time_t seconds = tv.tv_sec;
        int milliseconds = tv.tv_usec / 1000;
        int microseconds = tv.tv_usec % 1000;
        struct tm* timeinfo = localtime(&seconds);
rec
        // Print the time in the desired format: hour:minutes:seconds.microseconds
       // fprintf(fp, "Power data recorded at: %02d:%02d:%02d.%03d%03d\n",
        //        timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec, milliseconds, microseconds);
        fprintf(fp, "%02d:%02d:%02d.%03d%03d\n",
                timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec, milliseconds, microseconds);        
        fflush(fp); // Flush the buffer to ensure data is written immediately  
        
        // Signal end of one monitoring record
        fprintf(fp,"------------------------------------------------------------------------------------------------------- \n"); 
        fflush(fp); // Flush the buffer to ensure data is written immediately 
        
        // Wait for the specified interval
        sleep(interval_seconds);
    }
    return NULL;
}



int main (int argc, char **argv) 
{ char command[500]="",language[500]="", test[500]="", path[500]="" , powerlogpath[600]="" , logfile[500]="" ;
  int  ntimes = 1;
  int  core = 0 ;
  int  i=0;

#ifdef RUNTIME
  //clock_t begin, end;
  double time_spent;
  struct timeval tvb,tva;
#endif
  
  FILE * fp;
  
  //Run command
//  strcpy(command, "./" );
  strcat(command,argv[1]);
  //Language name
  strcpy(path,"../");
  strcpy(powerlogpath,"../"); 

  strcpy(language,argv[2]);
 
  strcat(language, "_Energy_Consumption");
  
  strcpy(test,argv[3]);
//  strcat(powerlogpath,language);
  strcat(language,".csv");
  strcat(path,language);
  
  strcat(powerlogpath,argv[2]);
  strcat(powerlogpath,"_");
  strcat(powerlogpath,argv[3]);
  strcat(powerlogpath, "_log_");
  strcpy(logfile,powerlogpath);
   
 
   double pt = strtod(argv[4], NULL);
   package_threshold = strtod(argv[4], NULL);

  //ntimes = atoi (argv[2]);

  

  fp = fopen(path,"a");
    if (fp == NULL) {
        perror("Error opening the power consumption data file");
        return 1;
    }  
 
 //time_t currentTime = time(NULL);
 //struct tm *timeInfo = localtime(&currentTime);
 //char timestamp[20];

 //strftime(timestamp, sizeof(timestamp), "%Y%m%d_%H%M%S", timeInfo);
 //strcat(powerlogpath, timestamp); 
 //strcat(powerlogpath, ".csv");
 
 //char csvFileName[100];  // You should choose an appropriate size
 //snprintf(powerlogpath, sizeof(powerlogpath), "%s_%s.csv", powerlogpath , timestamp);
 
 // Open a file to store the power data
  //FILE* power_log_file = fopen(powerlogpath, "w");
  //  if (power_log_file == NULL) {
  //      perror("Error opening the power log file");
  //      return 1;
  //  }   
  
  rapl_init(core);
 
 // Check if the file is empty
 long file_size = ftell(fp);
 bool file_empty = (file_size == 0);
 // Write header if file is empty
 if(file_empty){ 
 fprintf(fp,"Benchmark,Package,CPU,GPU,DRAM?,Threshold,Actual,TotalTime(Sec),RecordedAt(timestamp)\n");
 //fprintf(fp,"------------------------------------------------------------------------------------------------- \n"); 
 fflush(fp); // Flush the buffer to ensure data is written immediately
 }
 // Start the power recording thread
 // int pthread_create_result = pthread_create(&power_thread, NULL, record_power_data, (void*)power_log_file);
 //   if (pthread_create_result != 0) {
 //       perror("Error creating the power recording thread");
 //       fclose(power_log_file);
 //       return 1;
 //   }
     
  for (i = 0 ; i < ntimes ; i++)
    {  
 
       time_t currentTime = time(NULL);
       struct tm *timeInfo = localtime(&currentTime);
       char timestamp[20];
       strcpy(powerlogpath,logfile); 
       strftime(timestamp, sizeof(timestamp), "%Y%m%d_%H%M%S", timeInfo);
       strcat(powerlogpath, timestamp); 
       strcat(powerlogpath, ".csv");
       
       //char csvFileName[100];  // You should choose an appropriate size
       //snprintf(powerlogpath, sizeof(powerlogpath), "%s_%s.csv", powerlogpath , timestamp);
       
       // Open a file to store the power data
        FILE* power_log_file = fopen(powerlogpath, "w");
          if (power_log_file == NULL) {
              perror("Error opening the power log file");
              return 1;
          } 
         // Start the power recording thread
        int pthread_create_result = pthread_create(&power_thread, NULL, record_power_data, (void*)power_log_file);
          if (pthread_create_result != 0) {
              perror("Error creating the power recording thread");
              fclose(power_log_file);
              return 1;
          } 
          
    	fprintf(fp,"%s,",test);
         	      
		#ifdef RUNTIME
		        //begin = clock();
				gettimeofday(&tvb,0);
		#endif
	
	rapl_before(fp,core);
	
        system(command);

	rapl_after(fp,core,package_threshold);

		#ifdef RUNTIME
			//end = clock();
			//time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
			gettimeofday(&tva,0);
			// tv_sec denotes seconds while tv_usec denotes microseconds
			time_spent = (tva.tv_sec-tvb.tv_sec)*1000000 + tva.tv_usec-tvb.tv_usec;
			time_spent = time_spent / 1000000;
		#endif
			

		#ifdef RUNTIME	
			//fprintf(fp," %G \n",time_spent);
			//fprintf(fp,"Total Time to execute (Sec): %.18f ",time_spent);
			fprintf(fp,"%.3f,",time_spent);
			// Get the current time with microsecond precision
                struct timeval tv1;
                gettimeofday(&tv1, NULL);

                // Extract individual time components
                time_t seconds1 = tv1.tv_sec;
                int milliseconds1 = tv1.tv_usec / 1000;
                int microseconds1 = tv1.tv_usec % 1000;
                struct tm* timeinfo1 = localtime(&seconds1);

                // Print the time in the desired format: hour:minutes:seconds.microseconds
                //fprintf(fp, "Power data recorded at: %02d:%02d:%02d.%03d%03d\n",
                //        timeinfo1->tm_hour, timeinfo1->tm_min, timeinfo1->tm_sec, milliseconds1, microseconds1);
                fprintf(fp, "%02d:%02d:%02d.%03d%03d\n",
                        timeinfo1->tm_hour, timeinfo1->tm_min, timeinfo1->tm_sec, milliseconds1, microseconds1);
                fflush(fp); // Flush the buffer to ensure data is written immediately
                // End of single iteration
                //fprintf(fp,"------------------------------------------------------------------------------------------------- \n"); 
                fflush(fp); // Flush the buffer to ensure data is written immediately
	      #endif	

	        // Close the power log file
                fclose(power_log_file);

    }
    
  // Stop the power recording thread
  stop_power_recording();
  fclose(fp);

  // Close the power log file
  // fclose(power_log_file);
  
  fflush(stdout);

  return 0;
}




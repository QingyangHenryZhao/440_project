-Overview:
  This repo contains three folders: Data, Code, and Results. We plan to use this repo to collaborate and analyze 
  a dataset contains serum metabolomics profiling data of 99 metabolites from 170 patients with COVID-19 of different severity 
  (mentioned again below, with link to the dataset). We hope to include pathway information and correlation study to identify
  key changes in different pathways that could potentially lead to Covid progression. We plan to process the data set for 
  further statistical analysis using MetaboAnalyst or python packages. Besides pathway identification, we also want to perform 
  k-means clustering, random forest analysis, as well as PCA to improve on the predictive power of our findings.
  
-Data:
  In the Data folder, there is the origianl raw data 'ST002301_AN003757.csv'
  downloaded from:
  https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=ST002301&StudyType=MS&ResultType=1.
  
  Citation: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9589589/ Saheb Sharif-Askari, Narjes et al. 
  “Saliva metabolomic profile of COVID-19 patients associates with disease severity.” 
  Metabolomics : Official journal of the Metabolomic Society vol. 18,11 81. 22 Oct. 2022, doi:10.1007/s11306-022-01936-1
  
  This dataset contains serum metabolomics profiling data of 99 metabolites from 170 patients with COVID-19 of different severity.
  It is there along with other files, so far mainly data extracted from the raw data, 
  without additional analysis (normalization for example).
  
-Folder Structure:
  This repo contains three folders: Data, Code, and Results. We deposit any raw and processed data in the Data folder. 
  In the Code folder, there are, for now, two code files that allow us to generate the other extracted data files in the Data folder and
  the resulting graphs in the Results folder. In the Results folder, we deposite any graphs that were generated using the code in the 
  Code folder.
  
-Installation:
  The current two python files of code in the Code Folder requires the following:
  matplotlib==3.5.1
  numpy==1.22.2
  pandas==1.4.2

*Context*

*Escherichia coli* is a gram-negative bacteria and one of the most studied organisms in microbiology. While most strains are harmless, pathogenic strains are a leading cause of urinary tract,
gastrointestinal and bloodstream infections worldwide (Flores-Mireles et al., 2015; Bonten et al., 2021).

Ciprofloxacin is a fluoroquinolone antibiotic commonly used to treat *E. coli* infections, and resistance to it is determined by the combination of resistance genes a strain has in its
genome. *E. coli* has a great capacity to accumulate resistance genes mostly through horizontal gene transfer and plasmid-mediated quinolone resistance genes are amongst the most important mechanisms that provide resistance to fluoroquinolones (Poirel et al., 2018).

*Stack*

- Language: Python
- Data: BV-BRC database
- Libraries: pandas, requests, scikit-learn, xgboost, matplotlib, seaborn

*Methods*

1. Data download: Phenotype data and gene annotationsfor *E. coli* genomes tested against ciprofloxacin were downloadedfrom the BV-BRC database keeping only genomes with a Resistant or Susceptible label.

2. Matrix: A matrix was built where each row was a genome and each column a gene. Each cell contains a 1 if that genome has that gene and a 0 if it doesn´t. A column indicating whether each genome is resistant or susceptible was added.

3. Model: Random Forest, XGBoost and SVM classifiers were trained on 80% of the data and evaluated on the remaining 20%. Confusion matrices were plotted for each model. Also, feature importance was extracted to identify which genes contributed
most to the predictions.

*Results*

XGBoost performed best with a test AUC of 0.87 and accuracy of 85%, followed by Random Forest and SVM. Feature importance analysis from XGBoost identified iutA, papH, iucC and iroN
among the top predictive genes.

*References*

Bonten, M. et al. (2021). Epidemiology of Escherichia coli bacteremia: a systematic literature review. Clinical Infectious Diseases, 72(7), 1211–1219. https://doi.org/10.1093/cid/ciaa210

Flores-Mireles, A.L. et al. (2015). Urinary tract infections: epidemiology, mechanisms of infection and treatment options. Nature Reviews Microbiology, 13, 269–284. https://doi.org/10.1038/nrmicro3432

Poirel L.Madec J.Lupo A.Schink A.Kieffer N.Nordmann P.Schwarz S. 2018. Antimicrobial Resistance in Escherichia coli. Microbiol Spectr 6:10.1128/microbiolspec.arba-0026-2017. https://doi.org/10.1128/microbiolspec.arba-0026-2017

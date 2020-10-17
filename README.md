# MTT-Assay-Analyser

The script will analyse and graph data from multiple [MTT assays](https://en.wikipedia.org/wiki/MTT_assay).

The MTT assay measures the viability of a group of cells following treatment by a number of drugs. Metabolically active cells after treatment will convert MTT (yellow) to Formazan (purple) via NADPH oxidoreductase enzymes.

As a result, the efficacy of the drug can be quantified by measuring absorbance at 560nm using a spectrophotometer. In other words, less purple means less living cells, so the drug is more effective at killing cells.

![MTT](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/MTT_reaction.png/1600px-MTT_reaction.png)

The script is capable of analysing data from multiple 96 well plates in sequence from a `.csv` file - see the `HeLa.csv` file as an example. It expects data from the plate to be in this format:

![Plate](https://i.ibb.co/Y867wkv/Picture-1.png)

The equation used for calculating the mean cell viability for each column of dilutions per drug is:
```
Mean cell viability (%) = ((mean absorption - blank absorption) / (control absorption - blank absorption)) * 100
```

## Usage

Download with:
```
git clone https://github.com/Tommrodrigues/MTT-Assay-Analyser.git
pip3 install ~/MTT-Assay-Analyser/requirements.txt
```

Run from same directory with:
```
python3 analyser.py <cell_type> [-o]
```

The `.csv` analysed is defined by changing the cell type called with the script. For HeLa cells, you would run `python3 analyser.py HeLa`.

You can add the argument `-o` when calling the script to output the raw data frames for mean cell viability and standard deviation to separate `.csv` files.

After running the script, you will be presented with an analysis showing the most and least effective drugs for each of the concentrations across the whole assay data:

```
Drug analysis for HeLa cells:
+---------------+----------+-----------+
| Concentration |   Best   |   Worst   |
+---------------+----------+-----------+
|      High     | A (0 %)  | C (136 %) |
|     Medium    | A (5 %)  | C (163 %) |
|      Low      | A (31 %) | C (147 %) |
+---------------+----------+-----------+
```

The script will also plot a clustered bar chart showing the mean percentage viability of the cells for each drug type, along with the standard deviation of each column, multiplied by 100, shown as error bars:

![Plate](https://i.ibb.co/m0X0myS/Figure-1.png)

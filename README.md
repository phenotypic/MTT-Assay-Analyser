# MTT-Assay-Analyser

The script will analyse and graph data from multiple 96 well plates from an MTT assay.

The MTT assay measures the viability of a group of cells following treatment by a number of drugs. Metabolically active cells after treatment will convert MTT (yellow) to Formazan (purple) via NADPH oxidoreductase enzymes, so the efficay of the drug can be quantified by measuring absorbance at 560nm using a spectrophotometer.

![MTT](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/MTT_reaction.png/1600px-MTT_reaction.png)

The script is capable of analysing multiple 96 well plate data in sequence from a `.csv` file - see the `HeLa.csv` file as an example. It expects data from the plate to be in this format:

![Plate](https://i.ibb.co/Y867wkv/Picture-1.png)

The equation used for calculating the mean cell viability for each column of dilutions per drug is:
```
Mean cell viability (%) = ((mean absorbtion - blank absorbtion) / (control absorbtion - blank absorbtion)) * 100
```

## Usage

Download with:
```
git clone https://github.com/Tommrodrigues/MTT-Assay-Analyser.git
pip3 install ~/MTT-Assay-Analyser/requirements.txt
```

Run from same directory with:
```
python3 analyser.py
```

The `.csv` analysed is defined by changing the cell type within the script. E.g. for HeLa cells, the cell type is set to `HeLa`, and it will read the `HeLa.csv` data file.

After running the script, you will be presented with an analysis showing the most and least effective drugs for each of the concentrations across the whole assay data.

The script will also plot a clustered bar chart showing the mean percentage viability of the cells for each drug type, along with the standard deviation of each column shown as error bars:

![Plate](https://i.ibb.co/m0X0myS/Figure-1.png)

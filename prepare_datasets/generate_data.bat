:: Format:
:: labeled split - <datasetname>.<seed>@<percent_of_labeld>
::  unlabeled split - <datasetname>.<seed>@<percent_of_labeld>-unlabeled
rem @echo hello,world
For %%s in (1 2 3 4 5) do (
for %%p in (1 2 5 10 20) do (
@echo %%s %%p
python prepare_coco_data.py --percent %%p --seed %%s))
  rem done
rem done
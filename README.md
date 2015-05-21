Bullshitproject_svm
====
 A tool to extract data to train svm model.
static_analysis.py
----
mark whether a sensitive behaviour is used or not based on smali code.
dynamic_analysis.py
----
mark whether a sensitive behaviour is used or not based on hooklog
get_final.py
----
get final result from both static result and dynamic result.
generate_result.py
----
generate all results 

svm.py
----
pick random data to train and test

How to run
----
simply run generate_result.py
```
python generate_result.py -d /path/to/result
```

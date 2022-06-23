
# Cpe-parser

The cpe-parser libray is a parses for CPE value. This cpe value can be either uri biding cpe or formatted binding value.


###  🔨  Installation ###

```sh
 $ pip install cpe-parser
```


### Guide


```python
from cpeparser import CpeParser
cpe = CpeParser()
result = cpe.parser("cpe:2.3:a:ipython:ipython:*:*:*:*:*:*:*:*")
print(result)
{
    'part': 'a',
    'vendor': 'ipython',
    'product': 'ipython',
    'version': '*',
    'update': '*',
    'edition': '*',
    'language': '*',
    'sw_edition': '*',
    'target_sw': '*',
    'target_hw': '*',
    'other': '*'
}
```
Default values are returned as asterisks '*' that represent ANY.

### NIST Documentation
This library follows the guidelines outline here: 
https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf
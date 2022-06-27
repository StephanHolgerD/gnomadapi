# gnomad selenium API


## rInstalling equirements

* google chrome webbrowser

install via pip:
```
pip install gnomadapi
```

or via conda:
```
gnomad) [stephano@fedora gnomadAPI]$ gnomadAPI -h
ArgumentParser(prog='gnomadAPI', usage=None, description='access to the gnomad database using selenium', formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
usage: gnomadAPI [-h] -g GENE [-v {gnomad_sv_r2_1,gnomad_r3,gnomad_r2_1,exac}]

access to the gnomad database using selenium

options:
  -h, --help            show this help message and exit
  -g GENE, --gene GENE  gene of interest
  -v {gnomad_sv_r2_1,gnomad_r3,gnomad_r2_1,exac}, --version {gnomad_sv_r2_1,gnomad_r3,gnomad_r2_1,exac}
                        gnomad Version

```



Usage example 

```
gnomadAPI -g TP53
```

output 

```
TP53_gnomAD_v2.1.1_17-7565097-7590856_2022_06_27_21_56_11.csv
```

GnomadAPI writes a .csv that you can download from the [gnomad](https://gnomad.broadinstitute.org/) homepage in the your current working dir
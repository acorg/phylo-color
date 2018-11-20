# Phylogenetic tree coloring

The `phylo-color.py` script in this repo can be used to color the nodes of
phylogenetic trees.

Runs on (at least) Python 2.7.15 and 3.6 (and probably all versions of
Python 3).

## Installation

```sh
$ pip install phylo-color
```

## Usage

```
usage: phylo-color.py [-h] [--treeFile FILENAME]
                      [--listColors | --colorFile FILENAME]
                      [--inFormat {newick,nexml,nexus}]
                      [--outFormat {newick,nexml,nexus}]
                      [--defaultColor COLOR] [--taxonColor "TAXON COLOR"]
                      [--preserveOriginalColors] [--regex] [--hex]
                      [--matchCase]

Add color to the taxa of a phylogenetic tree file. Write the new tree to
standard output.

optional arguments:
  -h, --help            show this help message and exit
  --treeFile FILENAME   The tree file to color. If not provided, the tree will
                        be read from standard input. See the --inFormat option
                        for how to specify the tree format if the auto-
                        detection based on filename suffix is not sufficient.
                        (default: None)
  --listColors          If specified, all known color names will be printed,
                        after which the program will exit. (default: False)
  --colorFile FILENAME  Give the name of the color file to use. This is a text
                        file whose lines each have a taxon name, some
                        whitespace, then a color name. Colors are either a
                        named color (see the output of --listColors for the
                        full set) or must have 6 RGB hex values, optionally
                        with a preceeding hash. E.g., DA195 #FF0000. The color
                        name cannot contain whitespace. (default: None)
  --inFormat {newick,nexml,nexus}
                        Specify the input file format. If not specified, this
                        will be auto-detected from the --treeFile suffix. If
                        the tree is supplied on standard input, Newick is
                        assumed. (default: None)
  --outFormat {newick,nexml,nexus}
                        Specify the output file format. If not specified, this
                        will be the same as the input format. (default: None)
  --defaultColor COLOR  Give a default color. If not specified, nodes that are
                        not explicitly colored will be output with no color
                        information. May be specified as a 6-digit hex value
                        (with or without leading #) or as a color name.
                        (default: None)
  --taxonColor "TAXON COLOR", --tc "TAXON COLOR"
                        Specify a color for a taxa. The value must be a taxa
                        name (or regular expression if --regex is used)
                        followed by a space and then a color name (or 6-digit
                        specification). If --colorFile is also used, the
                        values given using --taxonColor will take precedence.
                        (default: None)
  --preserveOriginalColors
                        If specified, taxa that already have a color in the
                        input file, and which are not assigned a new color,
                        will be printed with their original color. (default:
                        False)
  --regex               If specified, taxa names will be treated as regular
                        expressions. (default: False)
  --hex                 If specified, convert color names to 6-digit hex
                        values preceeded by #. (default: False)
  --matchCase           If specified, the regular expressions for taxa names
                        in the color specification file will consider case
                        important in matching in taxa names. (default: False)
```

## Tree formats

[Nexml](http://www.nexml.org/),
[NEXUS](https://en.wikipedia.org/wiki/Nexus_file), and
[Newick](https://en.wikipedia.org/wiki/Newick_format) are supported.  If
you give a filename via `--treeFile`, `phylo-color.py` will guess at its
format based on the filename suffix (if any). If no suffix is found, or if
the suffix is not recognized, or if the tree is given on standard input,
Newick is assumed. To be explicit, use `--inFormat`.  The output format
will be the same as the input, unless `--outFormat` specifies otherwise.

Note that there is no guarantee that the tool you use to read the output
file will respect the colors that are added by `phylo-color.py`!

## Specifying taxon colors

On the command line you can use `--taxonColor 'name color'` (or `--tc 'name
color'`) as many times as you like to specify names of taxa and the color
they should be given. The name and color must be separated by a space (and
the color cannot contain whitespace).

### Specifying taxa names with regular expressions

If `--regex` is used, taxa names will be interpreted as
[regular expressions](https://en.wikipedia.org/wiki/Regular_expression).
Regular expressions matches are not tied to the start of the taxon string,
so remember to use `^` and `$` if you want to tie your regular expression
to one or both ends of the taxon name.

### Conversion to RGB colors

If `--hex` is used, the output color names (where recognized) will be in
`#RRGGBB`
[RGB](https://en.wikipedia.org/wiki/RGB_color_model#Numeric_representations)
hex format.  To see a list of known color names, run with `--listColors`.

### Taxa colors in a file

Taxa colors may also be given in a file with lines like

    # This is a comment.
    taxon-name1 #00FF00
    taxon-name2 #FF00FF
    taxon-name3 antique-fuchsia

Lines are treated as comments if `#` is the first non-blank character on
the line. Empty and whitespace-only lines are ignored. Otherwise, lines
must give a taxon name (or regular expression) followed by a color (as
described for the `taxonColor` option above).

### Coloring precedence

Colors specified on the command line using `--taxonColor` take precedence
over those found in files. If regular expressions are used, the first
matching regex is used (in the order given by `--taxonColor` or as found in
a taxon color file).

### Preserving existing colors

If your input file already has color information and you want to keep it
(in the case where your color specification doesn't indicate otherwise),
you can preserve the original colors with `--preserveOriginalColors`.

The default is that all original colors will be stripped.

### Default color

You can specify a default color for taxa that are not given an explicit
color in the color specification file. E.g., `--defaultColor red`.

### Removing all colors

If you do not provide a color file using `--colorFile` and do not use
`--taxonColor`, all pre-existing colors will be removed (assuming you don't
use `--defaultColor` or `--preserveOriginalColors`).

## Case matching

By default, case will not be considered when matching taxa names against
the first field of your color specification file. To change this, use the
`--matchCase` option.

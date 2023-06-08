[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C2DH/jdh-notebook/HEAD)

Single file via Juypter notebook

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C2DH/jdh-notebook/HEAD?filepath=%2Fexamples%2FD3_JS_example.ipynb)

Single file via Juypter lab

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C2DH/jdh-notebook/HEAD?labpath=%2Fexamples%2FD3_JS_example.ipynb)

# jdh-notebook

Jupyter notebook's contents for the journal of digital history

## To execute the POC_graph

Run the requirements.txt in order to install the librairies

```bash
pip install -r requirements.txt
```

## To execute request_dataverse

Create an .env file based on the .env.example

## DH Nord workshop

Presentation available here: https://docs.google.com/presentation/d/1NQTos1FtiFQZbOuXp7sIsONR_un81V2aR_ug_IY4jpk/edit#slide=id.gfb18a08927_0_16

## Add a notebook as a section of the Author Guidelines

Guidelines are composed by a series of notebooks available in `./examples/Author_Guideline`. Their filename has the `-raw` suffix because they need to be "skimmed" :D with the github action `prepare-guideline-notebooks` to be correctly published on the website.

Please add all the relevant notebook as _single entries_ in the list of this repo actions in `./.github/workflows/prepare-guideline-notebooks.yml`
and follow the full documentation at https://github.com/C2DH/journal-of-digital-history/wiki#how-to-write-the-contents-for-the-guidelines-page

````
  -
    name: Skim introduction
    id: skim
    uses: c2dh/journal-of-digital-history-ipynb-skim-action@master
    with:
      notebook: 'examples/Author_Guideline/introduction-raw.ipynb'
      output_notebook: 'examples/Author_Guideline/introduction.ipynb'

```
````

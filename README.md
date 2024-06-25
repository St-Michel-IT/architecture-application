# Architecture Logicielle

Ce repository contient les cours, les exercices et les sources du module Architecture Logicielle du Bachelor CSI.

Le support de cours est disponible dans le dossier `./doc/build/pdf` au format PDF.

## Programme

Les cours couvrent normalement le programme suivant :

# 1. Les différentes architectures d’une application
# 2. L’architecture REST
## ▪ Architectures Orientées Services
### o Besoins de la SOA
### o Notion de service
### o Introduction aux Architectures Orientées Services
## ▪ Vers les Architectures Orientées Services
### o Les architectures Client-Serveur
### o Les architectures Web
## ▪ Les Web Services
### o Appel de procédure
### o World Wide Web
### o Formats d’échange textuels
### o Vers la notion de Web Service
## ▪ Web Service de type SOAP et REST
## ▪ Guidelines API-REST
### o Gestion des actions et des URL
### o Recherche, Tri, Filtre et Pagination
### o Gestion des erreurs


## Compétences

Ils permettent normalement d'acquérir les compétences suivantes :

* Concevoir une architecture d’applications.

## Installation

Pytest means Python, it's a framework to test Python using Python.
First create a virtual environment.

```bash
python3 -m venv venv
```

Then activate it.

```bash
source venv/bin/activate
```

Then install pytest and other dependencies of that project.

```bash
pip install -r requirements.txt
```


## Build the documentation

This README is just a help, the complete documentation is available in the `doc` folder as a LaTex source.
To build it to a PDF it required `LuaLaTex`.
Dependencies can be installed on Ubuntu with the following command :

```bash
sudo apt install texlive-luatex texlive-latex-base texlive-latex-recommended texlive-pictures texlive-latex-extra ghostscript texlive-fonts-extra
```

Then build the PDF documentation :

```bash
/usr/bin/bash compile-latex.sh
```

To compress the PDF, install `ghostscript` :

 ```bash
 sudo apt install ghostscript
 ```

And run the following command :

```bash
/usr/bin/bash compress-pdf.sh
```

To compress images, install `pngcrush` and `jpegoptim` using the following command :

```bash
sudo apt install pngcrush jpegoptim
```

Then run the following command :

```bash
/usr/bin/bash compress-image.sh
```

Check the LaTex syntax in an active virtual environment :

```bash
/usr/bin/bash checkmytex.sh
```
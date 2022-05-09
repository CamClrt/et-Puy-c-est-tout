# Le blog

[et Puy c'est tout !](https://camclrt.github.io/et-Puy-c-est-tout/ "et Puy c'est tout !")

## CMD utiles

````
# To launch in local

pelican content
pelican --listen
````

```
# To publish on GitHub Pages

pelican content -o output -s pelicanconf.py
ghp-import output
git push origin gh-pages
```
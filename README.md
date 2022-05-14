![](https://github.com/CamClrt/et-Puy-c-est-tout/blob/main/content/assets/images/blog_cover.jpg "Blog cover")

# Le blog

Le lien : [et Puy c'est tout !](https://camclrt.github.io/et-Puy-c-est-tout/ "et Puy c'est tout !")

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
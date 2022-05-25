![](https://github.com/CamClrt/et-Puy-c-est-tout/blob/main/content/assets/images/blog_cover.jpg "Blog cover")

# Le blog

Le lien : [et Puy c'est tout !](https://www.et-puy-c-est-tout.fr "et Puy c'est tout !")

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
git checkout gh-pages
echo www.et-puy-c-est-tout.fr > CNAME && git add CNAME
git push origin gh-pages
```

![](https://github.com/CamClrt/et-Puy-c-est-tout/blob/main/content/assets/images/blog_cover.jpg "Blog cover")

# Le blog

Le lien : [et Puy c'est tout !](https://www.et-puy-c-est-tout.fr "et Puy c'est tout !")

## Tech Stack

* Python 3.9
* Pelican 4.7
* GitHub Pages
* Love 💙

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
git push origin gh-pages
git push origin main
```

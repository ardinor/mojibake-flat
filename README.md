Turn Mojibake into a flat file blog using Flask, Flask-FlatPages and Frozen-Flask. Python 2.7.3.

The Frozen files are in the frozen directory.

Possible moving into DB territory for building the categories and archive....

To create migrations

    python run.py db init

Generate initial migration

    python run.py db migrate

Appliy migration

    python run.py db upgrade

After every database model change run `migrate` and `upgrade` again


Maybe use the editor like in Ghost?
The Editor is http://codemirror.net/ . It then uses https://github.com/coreyti/showdown to convert the markdown to HTML, and jQuery with a simple cross-multiplication of content height (editor & preview) to adjust the the scroll on the other panel.
http://www.reddit.com/r/javascript/comments/1ofhos/nodejsbased_blogging_app_ghost_has_launched_today/ccrnd6i

Using examples from here

http://www.stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/

and

http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/

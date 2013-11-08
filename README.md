Turn Mojibake into a flat file blog using Flask, Flask-FlatPages and Frozen-Flask. Python 2.7.3.

The Frozen files are in the frozen directory.

Possible moving into DB territory for building the categories and archive....

### TO USE: ###

To create migrations

    python run.py db init

Generate initial migration

    python run.py db migrate

Apply migration

    python run.py db upgrade

After every database model change run `migrate` and `upgrade` again

To initiate the DB and make tables for the views

    python run.py manage_db

After new posts are added or existing posts change run the same again


### TO DO: ###

- Maybe use the editor like in Ghost?
The [Editor](http://codemirror.net/) uses [this](https://github.com/coreyti/showdown) to convert the markdown to HTML, and jQuery with a simple cross-multiplication of content height (editor & preview) to adjust the the scroll on the other panel. - [Source](http://www.reddit.com/r/javascript/comments/1ofhos/nodejsbased_blogging_app_ghost_has_launched_today/ccrnd6i)

- Pagination?

- Clean up unused files

### CREDITS: ###

Using examples from [here](http://www.stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/) and [here](http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/)

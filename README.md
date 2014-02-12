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

When making a post, put the date as UTC for the localisation in moment.js to work

    datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


### TO DO: ###

- Maybe use the editor like in Ghost?
The [Editor](http://codemirror.net/) uses [this](https://github.com/coreyti/showdown) to convert the markdown to HTML, and jQuery with a simple cross-multiplication of content height (editor & preview) to adjust the the scroll on the other panel. - [Source](http://www.reddit.com/r/javascript/comments/1ofhos/nodejsbased_blogging_app_ghost_has_launched_today/ccrnd6i)

- ~~Check Pagination works~~ Looks good

- Clean up unused files

- ~~Are the times displayed really localised? Hm..~~ Yep!

- ~~Shadows on the bans page, this page needs a bit of a tidy up~~ Done

- Maybe move the about page and any other similar pages made in the future to .md files and have them generated too?

### CREDITS: ###

Using examples from [here](http://www.stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/) and [here](http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/)

HTML 5 Template from [html5up](http://html5up.net/prologue/)

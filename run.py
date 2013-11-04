import sys

from mojibake import main

#main.app.run(debug=True)
if len(sys.argv) == 1:
    #print dir(main.manager)
    #main.manager.command(run('runserver'))
    #main.manager.run('runserver')
    main.manager.app.run(debug=True)
else:
    main.manager.run()

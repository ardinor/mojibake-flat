from mojibake import main

if __name__ == '__main__':
    #main.freezer.freeze()
    print 'Managing DB...'
    #main.manager.run(commands={'manage_db': ''})
    main.manager.handle('manage.py', ['manage_db'])
    print 'Freezing...'
    main.freezer.run(debug=True)
    print 'Finished.'

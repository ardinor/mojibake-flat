from mojibake import main
from build_gen_files import build_gen_files

if __name__ == '__main__':
    #main.freezer.freeze()
    build_gen_files()
    main.freezer.run(debug=True)
